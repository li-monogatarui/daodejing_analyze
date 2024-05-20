import requests
import time
from bs4 import BeautifulSoup

sites = ["addiss", "ChengLin", "legge", "lau", "YiWu", "mitchell", "hansen"]

for site in sites:
    # put url in variable
    url = 'https://terebess.hu/english/tao/' + site + '.html' # + 'Kap#' + str(i)

    contents = requests.get(url, verify=False)

    with open(f'{site}.html', 'w', encoding='utf8') as wf:
        wf.write(contents.text)
    
        time.sleep(.5)

    html = contents.text

    soup = BeautifulSoup(html, features="html.parser")
    text = soup.get_text()
    textfile = open(f'{site}.txt', "w", encoding='utf8')
    textfile.write(text)
    textfile.close()

    