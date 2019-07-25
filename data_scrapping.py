import praw
from pymongo import MongoClient
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from urllib.parse import urlparse
import re

def initialising_mongo():
	client = MongoClient()

	redDatabase = client.redditPosts

	redCollection = redDatabase.redditPosts

	return redCollection


def reddit_instance():

	initial_red_instance = praw.Reddit(client_id = '#', \
										client_secret = '#',\
										user_agent = '#',\
										username = '#',\
										password = '#')

	sub_instance = initial_red_instance.subreddit('india')

	return sub_instance



def process_strings(sample):
	sample = word_tokenize(sample)
	stop = stopwords.words('english')

	processed = []

	for word in sample:
		if word.isalpha():
			word = word.lower()
			if word not in stop:
				processed.append(word)

	processed = " ".join(processed)

	return processed

def add_to_dict(dictionary, key_name, value):

	if len(value)!=0:
		dictionary[key_name] = value


def write_in_db(collection, subreddit_inst):

	valid = {"AskIndia", "Business/Finance",\
			"AMA", "Food", "Non-Political", \
			"Photography", "Policy/Economy", \
			"Politics", "Science/Technology", \
			"Sports", "[R]eddiquette"}


	for tag in valid:
		posts = subreddit_inst.search(tag, limit = 500)
		for submission in posts:
			flair = submission.link_flair_text
			if flair is not None and "AMA" in flair:
				flair = "AMA"
			try:
				temporary = dict()
				if flair in valid:
					title_processed = process_strings(str(submission.title))
					content_processed = process_strings(str(submission.selftext))

					comments = ""

					submission.comments.replace_more(limit=0)
					comments = ""
					for comment in submission.comments.list():
						comments = comments + comment.body

					comments = process_strings(comments)

					url = submission.url
					parsed = urlparse(url)

					path = process_strings(" ".join(re.split('/|-|_', str(parsed.path))))
					host = process_strings(" ".join(parsed.hostname.split(".")))



					add_to_dict(temporary, "_id", str(submission.id))
					add_to_dict(temporary, "timestamp", str(submission.created_utc))
					add_to_dict(temporary, "author", str(submission.author))
					add_to_dict(temporary, "title", title_processed)
					add_to_dict(temporary, "content", content_processed)
					add_to_dict(temporary, "flair", flair)
					add_to_dict(temporary, "score", str(submission.score))
					add_to_dict(temporary, "num_comments", str(submission.num_comments))
					add_to_dict(temporary, "url_path", path)
					add_to_dict(temporary, "url_hostname", host)
					add_to_dict(temporary, "comments", comments)


					collection.insert_one(temporary)

			except:
				continue

def extractData():

	ptr_coll = initialising_mongo()

	subreddit_instance = reddit_instance()

	write_in_db(ptr_coll, subreddit_instance)


if __name__ == "__main__":
	extractData()
