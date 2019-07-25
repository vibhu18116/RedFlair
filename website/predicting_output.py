#!/usr/bin/env python
# coding: utf-8

import joblib
import praw
from urllib.parse import urlparse
import re
import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
import pickle


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


def get_input(url_to_check):
    
    reddit = praw.Reddit(client_id = 'cqzK0_e-iFTe3Q',
                        client_secret = 'alWsGXWCpkb-SAt72IR98Nh7uSg',
                        user_agent = 'RedFlair',
                        username = 'SmartyVibhu',
                        password = 'vibhu@14')

    post = reddit.submission(url = url_to_check)
    title_c = process_strings(str(post.title))
    content_c = process_strings(str(post.selftext))

    post.comments.replace_more(limit=0)
    comments = ""
    for comment in post.comments.list():
        comments = comments + comment.body

    comments = process_strings(comments)

    comments_c = process_strings(comments)

    url = post.url
    parsed = urlparse(url)
    url_path_c = process_strings(" ".join(re.split('/|-|_', str(parsed.path))))
    
    insert = {
        "title" : [title_c],
        "content" : [content_c],
        "comments" : [comments_c],
        "url_path" : [url_path_c]
    }
    df = pd.DataFrame(insert)
    
    df["merged"] = df["title"] + df["url_path"] + df["comments"] + df["content"]
    
    return df.merged


def fit_to_dict(df_col):
    vec = pickle.load(open("vector.pickle", "rb"))
    trans = vec.transform(df_col)
    return trans


def predict(inp):
    
    frame = get_input(inp)
    changed = fit_to_dict(frame)
    trained_model = joblib.load("flair_predictor.joblib")
    return trained_model.predict(changed)


if __name__ == "__main__":
    i = input()
    print(predict(i))

