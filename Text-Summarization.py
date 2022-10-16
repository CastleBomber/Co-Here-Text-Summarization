#!/usr/bin/env python
"""
**************************************************************
    co:here

    Author: [CastleBomber]
    Date:   [15 OCT 2022]

    pip3 install cohere

**************************************************************
"""

import cohere

def main():

    co = cohere.Client("MN0jDAS3JRs46BEZ9ZYm0MyqISSYMlZlATe62XBA")

    response = co.generate(
        model='large',
        prompt="Apple are so damn tasty, they should be illegal.",
        max_tokens=40,
        temperature=0.8,
        stop_sequences=["--"])

    print('Prediction: {}'.format(response.generations[0].text))


main()
