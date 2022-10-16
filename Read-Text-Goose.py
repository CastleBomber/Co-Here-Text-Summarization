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
import goose3
from goose3 import Goose
from requests import get

def main():
    response = get(
        'https://www.bbc.com/news/world-asia-china-63226230')
    extractor = Goose()
    article = extractor.extract(raw_html=response.content)
    text = article.cleaned_text

    print(text)

main()
