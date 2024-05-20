import re
import pandas as pd
import nltk

# Reading text file

sites = ["addiss", "ChengLin", "legge", "lau", "YiWu", "mitchell", "hansen"]

for i in sites:
    with open(f'Scraping/{i}.txt', 'r', encoding='utf8') as rf:
        text = rf.read()    
    text = text[text.find('81'):]   
    print(text[:50]) 

