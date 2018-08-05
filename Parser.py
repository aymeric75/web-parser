import sys
if sys.version_info[0] < 3:
    import urllib2
else:
    from urllib.request import Request, urlopen
    import requests

from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import random



class Parser:

    def return_page_content(self, url):

        proxy_list=self.proxies_list()
        print(proxy_list)
        ua = UserAgent()

        if sys.version_info[0] < 3:
            indic = 1 # 
            while(indic == 1):
                proxy_index = random.randint(0, len(proxy_list) - 1)
                proxy = proxy_list[proxy_index]
                req = urllib2.Request(url)
                req.add_header('User-Agent', ua.random)
                req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')
                try:
                    print("try")
                    page = urllib2.urlopen(req, timeout=4)
                    indic = 0
                    soup = BeautifulSoup(page, 'html.parser')

                    if(page.getcode() == "200"):
                    	indic = 0

                except Exception as e:
                    print("except")
                    del proxy_list[proxy_index]
                    print(len(proxy_list))
                    print(e)
                    pass

            return soup

        else:
            indic = 1
            while(indic == 1):
                proxy_index = random.randint(0, len(proxy_list) - 1)
                proxy = proxy_list[proxy_index]
                # req = Request(url)
                # req.add_header('User-Agent', ua.random)
                # req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')
                try:
                    print("tryy")
                    headers = {'User-Agent': ua.random}
                    page = requests.get(url, headers=headers).content.decode()
                    # page = urlopen(req, timeout=10).read().decode('utf8')
                    indic = 0
                    soup = BeautifulSoup(page, 'html.parser')

                    if(page.getcode() == "200"):
                    	indec=0

                except Exception as e:
                	del proxy_list[proxy_index]
                	print(len(proxy_list))
                	print(e)
                	pass

            return soup

        return 1



    def proxies_list(self):

    	if sys.version_info[0] < 3:
    		ua = UserAgent() 
    		proxies_req = urllib2.Request('https://www.sslproxies.org/')
    		proxies_req.add_header('User-Agent', ua.random)
    		proxies_doc = urllib2.urlopen(proxies_req).read().decode('utf8')

    		soup = BeautifulSoup(proxies_doc, 'html.parser')
    		proxies_table = soup.find(id='proxylisttable')


    		proxies = []

    		for row in proxies_table.tbody.find_all('tr'):

    			proxies.append({'ip':   row.find_all('td')[0].string,'port': row.find_all('td')[1].string})

    		return proxies



    	else:
    		ua = UserAgent()

    		proxies_req = Request('https://www.sslproxies.org/')
    		proxies_req.add_header('User-Agent', ua.random)
    		proxies_doc = urlopen(proxies_req).read().decode('utf8')

    		soup = BeautifulSoup(proxies_doc, 'html.parser')
    		proxies_table = soup.find(id='proxylisttable')


    		proxies = []


    		for row in proxies_table.tbody.find_all('tr'):

    			proxies.append({
    				'ip':   row.find_all('td')[0].string,
    				'port': row.find_all('td')[1].string

    				})

    		return proxies

if __name__ == "__main__":
    # execute only if run as a script

    parse = Parser()

    parse_content = parse.return_page_content("https://openclassrooms.com")

    print(parse_content.find_all('a'))