#!/usr/bin/env python

import re
from urllib.parse import urlparse, urljoin
import requests

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

target_url = "https://www.facebookwkhpilnemxj7asaniu7vnjjbiltxjqhye3mhbshg7kx5tfyd.onion/"
target_links = []

def extract_links_from(url):
    try:
        response = requests.get(url, proxies=proxies)
        response.raise_for_status()
        return re.findall('(?:href=")(.*?)"', response.content.decode('utf-8'), error = 'replace')
    except requests.exceptions.ConnectionError as e:
        print(f"Error: {e}")
        return []

def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)

crawl(target_url)