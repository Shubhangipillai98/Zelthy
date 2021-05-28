import requests
import json
import sys


word = input("Word: ")
# Getting json response from the api url according to given word
response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en_US/"+word)

# converting above json response to python dictionary
result = response.json()

# Getting the value with key 'word' from the dictionary's first list
word = result[0]["word"]
# Getting the value with key 'definition' from nested list of meanings in the 2nd list of json dictionary
definition = result[0]["meanings"][1]["definitions"][0]["definition"]

# Getting the partOfSpeech key's value from the meanings dictionary in the response's 2nd list
partOfSpeech = result[0]["meanings"][1]["partOfSpeech"]
# printing above extracted details
print(word+"."+partOfSpeech+"."+definition)