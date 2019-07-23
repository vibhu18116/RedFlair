# RedFlair
A project to predict flairs of reddit posts

data_scrapping.py is used to extract data from reddit.
analyse_data.py plots relevant graphs.
training_ml_models.ipynb is used to train various machine learning models. 

Finally comments, title, body (content), url path have been considered under XGBClassifier for training and prediction purpose.
Accuracy thus obtained is close to 63.7%.

predicting_output.ipynb is used to predit the flairs.

To run the application, clone it from repository and navigate to the RedFlair folder.
Run app.py from command line to initialise flask app and visit https://localhost:5000. 
Give a URL as input and the output will be displayed.
