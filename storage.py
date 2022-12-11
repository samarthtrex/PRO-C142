from flask import Flask, jsonify, request
import csv
 
# All articles list
all_articles = []
 
# Put " encoding="utf-8" " in project as well
# Opening the csv file
with open('articles.csv', encoding="utf-8") as f:
    reader = csv.reader(f) # Reading the file
    data = list(reader) # Storing in data
    all_articles = data[1:] # Taking out the first index
 
# Creating the other lists for liked, and disliked articles
liked_articles = []
disliked_articles = []