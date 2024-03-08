# Exercise 4: Select the first element from your dictionary.

# Dictionary
languages = {
        "fr": "french",
        "es": "spanish",
        "la": "latin",
        "en": "english",
        "eu": "euskera",
        }

# Obs. No sabía si el término 'element' se refería a 'items' o 'values', por lo que preferí colocar ambos. 

print(list(languages.values())[0])

print(list(languages.items())[0])
