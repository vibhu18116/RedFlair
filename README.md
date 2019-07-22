# RedFlair
A project to predict flairs of reddit posts

data_scrapping.py is used to extract data from reddit.
analyse_data.py plots relevant graphs.
training_ml_models.ipynb is used to train various machine learning models. 

Finally comments, title, body (content), url path have been considered under XGBClassifier for training and prediction purpose.
Accuracy thus obtained is close to 63.7%.

predicting_output.ipynb is used to predit the flairs. Currently, the file takes a URL as input and returns output (works from command line).

Work is in progress to deploy it as a web app.

