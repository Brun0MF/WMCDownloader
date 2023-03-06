import os
import requests
from bs4 import BeautifulSoup
import urllib.request
import time



def download_images(title, max_images=None):

    # Create URL
    searchtitle = title.replace(' ','+')
    url = 'https://commons.wikimedia.org/w/index.php?search='+searchtitle+'&title=Special:MediaSearch&type=image'

    # Create Folder Name
    folder_name = "WMD/"+title.replace(' ','_')

    # Request the Web Page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Create a Folder with the Title
    os.makedirs(folder_name, exist_ok=True)
    
    img_tags = soup.find_all('img', class_='sd-image')
    
    # Download the Images and place them in the Folder
    count = 0
    for img_tag in img_tags:
        
        img_url = img_tag.get('src')
        img_name =folder_name+"/"+img_tag.get('alt')
        if img_url:
            print("Downloading: ("+img_name+") "+img_url)
            try:
                urllib.request.urlretrieve(img_url, img_name)
                count += 1   
            except Exception as e:
                print("Download Failed! /n("+str(e)+")")
                pass
            time.sleep(1)
            
        if(count >= int(max_images)):
            break

    print(f'{count} images have been transferred to {folder_name}.')


# Example of Use:
#    download_images("Cats", max_images=10)
