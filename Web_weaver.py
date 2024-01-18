#!/usr/bin/python

import requests

def request(url):
	try:
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass

path=[]
def dirdiscover(url):
	with open("common_dir.txt","r") as wordlist_file:
		for line in wordlist_file:
			word = line.strip()
			test_url = url + "/" + word
			response = request(test_url)
			if response :
				print "[+] Discovered URL ----> " + test_url
				path.append(word)

url="192.168.44.101/dvwa"
#edit the url you want to scan
dirdiscover(url)

#recursively gothrough each and every path		
for paths in path:
	dirdiscover(url+"/"+ paths)
