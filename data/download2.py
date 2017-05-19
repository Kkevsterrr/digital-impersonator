import argparse
from os.path import join

try:
	import requests as r
except ImportError:
	import pip
	pip.main(["install", "requests"])
	import requests as r



headers = {
	'Pragma': 'no-cache',
	'DNT': '1',
	'Accept-Encoding': 'gzip, deflate, sdch',
	'Accept-Language': 'en-US,en;q=0.8',
	'Upgrade-Insecure-Requests': '1',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Cache-Control': 'no-cache',
	'Connection': 'keep-alive',
	'User-Agent': 'You dont need to know'
}

def download_file(url, path):
    local_filename = url.split('/')[-1]

    req = r.get(url, stream=True, headers=headers)
    with open(join(path, local_filename), 'wb') as f:
        for chunk in req.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename

def iter_download_files(urls, path):
	for url in urls:
		yield download_file(url, path)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Download some files from txt")
	parser.add_argument("-f", "--file", type=str, action="store", required=True, dest="file", help="input file of urls")
	parser.add_argument("-p", "--path", type=str, action="store", required=False, default="", dest="path", help="path to where downloads will be stored")
	parser.add_argument("-n", "--num-files", type=int, action="store", default=-1, dest="num_files", help="number of files you want to download from txt")

	dict_args = vars(parser.parse_args())

	print
	print "Download path: %s" % dict_args["path"]
	print "Number of files: %d" % dict_args["num_files"]
	print "File selected: %s" % dict_args["file"]
	print

	urls = [url.strip() for url in open(dict_args["file"]).readlines()]
	
	for i, filename in enumerate(iter_download_files(urls[:dict_args["num_files"]], dict_args["path"])):
		print "%d Downloading file %s"%(i,filename)
