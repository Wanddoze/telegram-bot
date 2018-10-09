# -*- coding: utf-8 -*-
#!/usr/bin/python3 
from bs4 import BeautifulSoup
from urllib import request
from urllib.error import HTTPError 
import time 

def get_site_table(html):
    page_soup = BeautifulSoup(html,"html.parser")
    page = page_soup.findAll("div",{"id":"siteTable"})[0]
    return page

def get_results_by_site(site):
    results = []
    divs = site.select("div[class*=thing]")
    for item in divs:
        data_score = int(item["data-score"])
        if(data_score >= 5000):
            thread = {}
            thread["subreddit"] = item["data-subreddit-prefixed"]
            thread["upvotes"] = item["data-score"]
            thread["title"] = item.select("p[class*=title]")[0].a.contents[0]   
            thread["comments"] = item["data-permalink"]   
            thread["link"] = item["data-url"]   
            results.append(thread)
    return results

def get_data(url):  
    try:
        req = request.Request(url)
        req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)')
        resp = request.urlopen(req)
        page_html = resp.read()
        # print(page_html)
        site = get_site_table(page_html)
        results = get_results_by_site(site)

        return results
    except HTTPError as e: 
        print(e)
        if e.code == 429:
            time.sleep(1)
            return get_data(url)
        return 
    # Se pegar a pagina errada
    except IndexError as e: 
        time.sleep(1)
        return  get_data(url)
    # Abort in case of wrong page
    except KeyError as e: 
        return