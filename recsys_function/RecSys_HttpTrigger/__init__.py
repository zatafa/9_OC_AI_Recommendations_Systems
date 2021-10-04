import logging
import azure.functions as func
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from io import BytesIO


def get_ContentBased_Reco(userID, small_clicks, small_embeddings, n_reco=5):
    '''Return 5 recommended articles ID to user'''

    # Get the list of articles viewed by the user
    var = small_clicks.loc[small_clicks.user_id == userID]['article_id'].to_list()

    # Get the list of unique article_ID in small_clicks
    list_articleID = sorted(list(small_clicks.article_id.unique()))

    # Retrieve the corresponding index of the articles viewed by userID in var
    idx_var = []
    for i in range(0, len(var)):
        for idx, item in enumerate(list(list_articleID)):
            if item == var[i]:
                idx_var.append(idx)

    # Select the last element of the list
    value = idx_var[-1]
    # print(value)

    # Compute the cosine similarity
    emb = small_embeddings
    distances = cosine_similarity([emb[value]], emb)[0]

    # Save the result in Pandas DataFrame
    df_reco = pd.DataFrame(list(zip(list_articleID, distances)),
                           columns=(["reco_article_id", "similarity"]))
    
    # Sort the DF by similarity
    df_reco.sort_values(by='similarity', ascending=False, inplace=True)

    # Exclude already viewed articles
    top_reco = df_reco[~df_reco.reco_article_id.isin(var)]

    # Give the list of recommended articles
    result = list(top_reco["reco_article_id"].iloc[:(n_reco)].values)

    return result


# Use Azure main function to get the recommendations
def main(
    req: func.HttpRequest, 
    clicksBlob: func.InputStream, 
    embeddingsBlob: func.InputStream) -> func.HttpResponse:
    
    logging.info('Python HTTP trigger function processed a request.')

    # Load the data from AzureBlobStorage
    clicks = pd.read_csv(BytesIO(clicksBlob.read()), index_col=None, header=0)
    print('click: ', clicks.shape)
    embeddings = pd.read_pickle(BytesIO(embeddingsBlob.read()))
    print('emb ', embeddings.shape)

    # Put the mobile app userId param in a variable
    userID = req.params.get('userId')
    
    if not userID:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            userID = req_body.get('userId')

    if userID:
        # Get the 5 articles' recommendations
        userID = int(userID)
        reco5 = get_ContentBased_Reco(int(userID), clicks, embeddings, n_reco=5)

        # Convert the list in string
        str_result = ' '.join(str(elem)+"," for elem in reco5)

        # Delete the last comma
        result = str_result.rstrip(str_result[-1])

        # Template example is to return a sentence with the user_id
        return func.HttpResponse(result)

    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Please enter a userID.", 
             status_code=200)