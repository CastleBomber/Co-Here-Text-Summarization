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

def main():

    article = newspaper.Article("https://www.bbc.com/news/world-asia-china-63226230")
    #article.set_html(html)
    article.download()
    article.html
    article.parse()
    article.authors

    print(article.text)

main()
