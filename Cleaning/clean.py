import re
import pandas as pd
import nltk

# Reading text file

sites = ["addiss", "ChengLin", "legge", "lau", "YiWu", "mitchell", "hansen", "blakney", "tamgibbs", "ludd", "Lin", "Marshall"]

# variables for each different site
# i: choose specific version
i = 11
# first_str: choose first few words of text
first_str = "That which can be perceived"
# offset: subtract a few characters to get first chapter number (1)
offset = 7

with open(f'Scraping/text_files/{sites[i]}.txt', 'r', encoding='utf8') as rf:
    text = rf.read()
new = re.sub(rf'[^a-zA-ZÀ-ÖÙ-öù-ÿĀ-žḀ-ỿ0-9 \']', ' ', text)

new = new[new.find(first_str) - offset:]

# print(new[:100]) 

split = re.split(r"([0-9]+)", new)

chapters = []
text = []

split = list(filter(None, split))

for j in range(len(split)):
    if j % 2 == 0:
        chapters.append(split[j])
    else:
        text.append(split[j])

df = pd.DataFrame({'ch':chapters, 'txt':text})

df['tokens'] = df.apply(lambda row: nltk.word_tokenize(row['txt']), axis=1)
df['ch_len'] = df.apply(lambda row: len(row['tokens']), axis=1)

df.to_csv(f"Cleaning/{sites[i]}.csv", index=False)  

