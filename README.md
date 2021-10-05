# :dart: Recommendations Systems
The goal of this projet is to recommend books / articles to customers, integrate in a Node.js Mobile App.

## Different types of recommendation systems

<img src='/pictures\recommendation_systems_categorization.png'>

# :card_index_dividers: Dataset
[News Portal provided by Globo.com](https://www.kaggle.com/gspmoreira/news-portal-user-interactions-by-globocom#clicks_sample.csv), one of the most popular media company in Brazil.

**More information** available on [Gabriel Moreira's Github/paper](https://github.com/gabrielspmoreira/chameleon_recsys)

# :scroll: Tasks
- :heavy_check_mark: Perform Exploratory Data Analysis (EDA);
- :heavy_check_mark: Try different RecSys model (by popularity, Content-Based, Collaborative Filtering);
- :heavy_check_mark: Select the architecture to meet the business need;
- :heavy_check_mark: Integrate in a Node.js Mobile App;
- :heavy_check_mark: Deploy Content-based RecSys on Azure (Azure Functions, Azure Blob Storage).

# :computer: Dependencies
Pandas, sklearn, implicit library, Azure Functions, Azure Blob Storage, Github, VS Code

## Targeted Serverless Architecture

<img src='/pictures\targeted_serverless_architecture.png'>

# :hammer_and_wrench: Tools (prerequisites)
- Fork of [Bookshelf App](https://github.com/OpenClassrooms-Student-Center/bookshelf) on Github;
- [Node.js](https://nodejs.org/en/), including npm (Node package manager);
- [Azure Functions Core Tools](https://docs.microsoft.com/fr-fr/azure/azure-functions/functions-run-local?tabs=windows%2Ccsharp%2Cportal%2Cbash%2Ckeda#install-the-azure-functions-core-tools);
- [Android Studio](https://developer.android.com/studio?hl=fr);

# :pushpin: References
- Recommendations systems: [Categories of RecSys](https://interstices.info/les-systemes-de-recommandation-categorisation/)
- Implicit / Explicit data : 
- Cosine similarity : [Sklearn pairwise metrics](https://scikit-learn.org/stable/modules/metrics.html); 
- [Implicit library](https://implicit.readthedocs.io/en/latest/quickstart.html);
- [Create Azure Functions with Visual Studio Code](https://docs.microsoft.com/fr-fr/azure/azure-functions/create-first-function-vs-code-python);
- Serverless : [What is Serverless?](https://serverless-stack.com/chapters/fr/what-is-serverless.html).
