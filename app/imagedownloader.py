from bs4 import BeautifulSoup

import requests
import urllib.request
import time

file = open("../data/train.txt", "r")

urlprefix = 'http://www.dpchallenge.com/image.php?IMAGE_ID='

headers = {
    'User-Agent': 'Mozilla/5.0'
}
count = 0
try:
    for line in file:

        imageid = line.strip()
        fullurl = urlprefix + imageid

        print(fullurl)

        r  = requests.get(fullurl, headers=headers)

        data = r.text

        soup = BeautifulSoup(data, "html.parser")
        time.sleep(1)
        try:
            for link in soup.find_all(id="img_container"):
                imgurl = link.find_all("img")[1].get("src")
                print(imgurl)
                full_file_name = "../data/train/"+imageid + '.jpg'
                urllib.request.urlretrieve(imgurl, full_file_name)
        except Exception as e:
            print("Error while parsing html", e)

        time.sleep(1)
        count = count +1

except Exception as e:
    print("Error  --> ", e)
print("Count --> ", count)
