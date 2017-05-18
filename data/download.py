import os
speeches = open("obama_speeches.txt").readlines()

for s in speeches:
    s= s.strip()
    name = s.split("/")[-1]
    
    os.system("curl '"+s+"' -H 'Pragma: no-cache' -H 'DNT: 1' -H 'Accept-Encoding: gzip, deflate, sdch' -H 'Accept-Language: en-US,en;q=0.8' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Cache-Control: no-cache' -H 'Connection: keep-alive' --compressed -o "+name)

