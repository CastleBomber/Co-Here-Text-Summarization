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
import cohere

def main():

    co = cohere.Client("MN0jDAS3JRs46BEZ9ZYm0MyqISSYMlZlATe62XBA")
    html = requests.get("https://www.bbc.com/news/world-asia-china-63226230").text
    article_text = fulltext(html)

    response = co.generate(
        model='xlarge',
        prompt=article_text,
        max_tokens=40,
        temperature=0.8,
        stop_sequences=["--"])

    print(article_text)
    print('\n')
    print('Prediction: {}'.format(response.generations[0].text))


main()
