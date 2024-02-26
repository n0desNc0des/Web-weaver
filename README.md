# How I made a web crawler and modified it to work with onion websites  
* This python tool is a basic web crawler designed to recursively explore and extract hyperlinks and subdomains from a specified target URL. 
* It is implemented using requests library for making HTTP requests and extracting webpage content along with re library for regular expression based parsing and urllib to join links.

* My main aim while building this tool was that the tool crawls without any repetition and redundancy.

---
## Source code explained with each code block:

    #!/usr/bin/env python

    import re
    from urllib.parse import urlparse, urljoin
    import requests

* Important libraries are imported.

        target_url = "https://www.sphoorthyengg.ac.in/"
        target_links = []

* The target_url variable holds the target url which serves as the starting point for web crawling.
* The target_links list stores all the unique links discovered during crawling.

        def extract_links_from(url):
            try:
                response = requests.get(url)
                response.raise_for_status()
                return re.findall('(?:href=")(.*?)"', response.content.decode('utf-8'),)
            except requests.exceptions.ConnectionError as e:
                print(f"Error: {e}")
                return []

* This function sends an HTTP get request from the target URL and  retrieves the web content.
* It then proceeds to extract all the hyperlinks using the  regular expression '(?:href=")(.*?)"'.
* Regualar expression explained:  
    * Suppose href="https://www.sphoorthyengg.ac.in/public/assets/img/favicon.png" is one such hyperlink that we are interested in crawling. But we are only interested in the part which comes between the double quotes.
    * So this regex has ?: known as non capturing group which indicated not to capture href and (.*?) works as capturing group which indicates the part that needs to be captured.
* Alast if a connection error occures with the target url it prints the error message which comes handy for debugging.

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

* This is the main crawling function that takes URL as an input and extracts links using extract_links_from function and iterates through each link.
* It ensures that only unique links within the target URL are processed.
* This function also handles removing fragments such as "<a href='#'> Management</a>" from links and recursively calls itself for each valid link found.
* It also identifies unrelated links such as "https://www.facebook.com/SPHN.Official/" ,"https://www.instagram.com/sphn.official/" and does'nt add them in the list.

        crawl(target_url)

* It initiates the crawling process by calling the crawl function and target_url as the starting point.

### Output : [Here](https://github.com/n0desNc0des/Web-weaver/blob/e2fe2772b714b50e801587182d1f369690e33ab5/Output1.txt)
* We can see that there are no incomplete, repeated or unrelated links in the output.

---

## Now lets understand how I made this code work with .onion websites

I did two main tweaks or changes to make this tool work with .onion sites:  
1. Changed some network configuration settings in kali linux and set up proxy
2. Did some changes in the sourcecode.

### Changes in Network settings of kali linux:

* Installed tor using apt-get install tor before proceeding to change the settings.
* Started tor service using the command "service tor start" and verified the status using "service tor status".
![status](https://i.imgur.com/OVJwXoZ.png)
* Opened the proxychains configuration file using the command  nano /etc/proxychains4.conf
* Uncommented dynamic_chain and commented strict_chain because dynamic proxy chains come handy while connecting to TOR.
* Uncommented proxy DNS requests and enabled it as it helps being anonymous.
* Atlast under proxylist I added internet protocol socks 4 and 5 proxies with the following address and port number.
![socks](https://i.imgur.com/KsWZuj4.png)
* Saved the changes using ctrl+o and exited the file using ctrl+x.
* Restarted the Tor service.

### Changes made to the source code to make the tool work with .onion sites:

        proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }

* Added a section that defines a dictionary named proxies that specifies SOCKS5 protocol should be used for both http and https request.

        def extract_links_from(url):
            try:
                response = requests.get(url, proxies=proxies)
                response.raise_for_status()
                return re.findall('(?:href=")(.*?)"', response.content.decode('utf-8'),)
            except requests.exceptions.ConnectionError as e:
                print(f"Error: {e}")
                return []

* The extract_links_from(url) fuction contains a func called requests.get(url) which now includes a new parameter called 'proxies' passing the configured key value pairs in the dictionary.
* This modification ensures that the HTTP requests made by the script are routed through the specified Tor proxy.

        target_url = "https://www.facebookwkhpilnemxj7asaniu7vnjjbiltxjqhye3mhbshg7kx5tfyd.onion/"

* This time the target URL was set to facebook's onion site.

### Output: [Here]()



## Links to the source code:

* Basic web crawler - [Here](https://github.com/n0desNc0des/Web-weaver/blob/main/Web_weaver.py)
* Crawler that works with .onion sites - [Here](https://github.com/n0desNc0des/Web-weaver/blob/main/Web_weaver_tor.py)
* sourcecode of this markdown file - [Here]()

---
