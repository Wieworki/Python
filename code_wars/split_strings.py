"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']

"""

def solution(s):
    arr = []
    str = ""
    for letter in s:
        str += letter
        if(len(str) > 1):
            arr.append(str) 
            str = ""
    if(len(str) == 1):
        str += "_"
        arr.append(str)
    return arr
