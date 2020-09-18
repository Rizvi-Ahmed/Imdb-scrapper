import re
from imdbproc import imdb_processor as imdbp
import json


FILE_PATH = './downloadlist.txt'
API_KEY = 'e651170a' # 1000 requests per day limit
OUTPUT_PATH = './data.json'

infodict = {}

titles = []

with open(FILE_PATH, "r") as dlfile:
    titles = dlfile.readlines()

titles = [title.strip() for title in titles]

for title in titles:
    searchresult = imdbp.processtitle(API_KEY,title)
    infodict[title] = imdbp.gettitleinfo(searchresult)


with open(OUTPUT_PATH, 'w') as fp:
    json.dump(infodict, fp, indent=4)

