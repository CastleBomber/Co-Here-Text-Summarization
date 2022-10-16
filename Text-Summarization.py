#!/usr/bin/env python
"""
**************************************************************
    Project: Co:here Newspaper Natural Language Processing
    Author: [CastleBomber]
    Date:   [15 OCT 2022]

    Notes:
    pip3 install cohere
    pip3 for python3, pip for python2

**************************************************************
"""

from newspaper import *
import requests
import cohere


def main():

    # newspaper API, webscraper
    article_name = Article("https://www.cnn.com/2022/10/16/us/alaska-snow-crab-harvest-canceled-climate/index.html", language = "en")
    article_name.download()
    article_name.parse()

    # cohere API, natural language processing for summarizing article text
    co = cohere.Client("MN0jDAS3JRs46BEZ9ZYm0MyqISSYMlZlATe62XBA")
    html = requests.get("https://www.bbc.com/news/world-asia-china-63226230").text

    response = co.generate(
        model='xlarge',
        prompt=article_name.text,
        max_tokens=30,
        temperature=0.5)

    #print(article_name.text)
    print('CNN summary: {}'.format(response.generations[0].text))

main()
