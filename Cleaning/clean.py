import re
import pandas as pd
import nltk

# Reading text file

sites = ["addiss", "ChengLin", "legge", "lau", "YiWu", "mitchell", "hansen"]

i = 6
first_str = "To Guide with"
offset = 7

with open(f'Scraping/{sites[i]}.txt', 'r', encoding='utf8') as rf:
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

