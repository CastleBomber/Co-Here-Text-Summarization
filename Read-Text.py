#!/usr/bin/env python
"""
**************************************************************
    co:here

    Author: [CastleBomber]
    Date:   [15 OCT 2022]

    pip3 install cohere

**************************************************************
"""

import newspaper
from newspaper import fulltext
import requests

def main():

    #article = newspaper.Article("https://www.bbc.com/news/world-asia-china-63226230")
    #article.download()
    #article.html
    #article.parse()
    #article.authors
    #text = fulltext(article)
    #print(text)

    html = requests.get("https://www.bbc.com/news/world-asia-china-63226230").text
    text = fulltext(html)
    print(text)

main()
