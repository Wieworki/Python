"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.

Examples

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""

import re

def to_upper_case(matched):
    return matched.group(0)[1].upper()

def to_lower_case(matched):
    return matched.group(0).lower()

def generate_hashtag(s):
    s = re.sub("\w", to_lower_case, s)     #Removing uppercase letters inside the string
    s = re.sub(" \w", to_upper_case, s)    #Capitalizing first letter in each word
    s = re.sub(" ", "", s)                 #Removing extra spaces
    if (s == '') or (len(s) > 140):
        return False
    else:
        return "#" + s[0].upper() + s[1:]
