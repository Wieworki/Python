"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"""

def to_camel_case(text):
    newText = ""
    bandera = False
    for i in text:
        if i == "-" or i == "_":
            bandera = True
            continue
        else:
            if(bandera):
                #El caracter anterior era un separador
                newText += i.upper() 
                bandera = False
            else:
                newText += i
    return newText
