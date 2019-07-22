from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt


client = MongoClient()

db = client.redditPosts

collection = db.redditAllPosts

data = pd.DataFrame(list(collection.find()))

print(data.describe())

tags = ['Politics', 'AskIndia', 'Food', \
		'[R]eddiquette', 'Policy/Economy',\
		'Photography', 'Science/Technology',\
		'AMA', 'Business/Finance', 'Sports'\
		'Non-Political']
# plt.plot()
plt.figure(figsize = (10,4))

data.flair.value_counts().plot(kind = 'bar')

plt.show()