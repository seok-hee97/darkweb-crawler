from bs4 import BeautifulSoup
import requests
def getLinksFromUrl(url, depth):
    headers = {
        "User-Agent" : "Android"
    }
    print(depth, url)
    naver_response = requests.get(url, headers=headers)
    naver_response.close()
    
    soup = BeautifulSoup(naver_response.content, "html.parser")
    links = []
    for a in soup.findAll("a"):
        try:
            href = a["href"]
        except:
            continue
        if href in links:
            continue
        if href.startswith("#") or href.startswith("/"):
            continue
        links.append(href)
        
    return links
depth = 0
referer = ""
links = getLinksFromUrl("https://www.naver.com", depth)    
while True:
    depth += 1
    for link in links:
        links_ = getLinksFromUrl(link, depth)    
    links = links_
    if depth >= 5:
        break    
    
    
    
    