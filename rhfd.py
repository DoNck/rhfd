#! /usr/bin/env python

#RHFD: Recursive Http Files Downloader

from lxml import html
import requests
import os, errno
import wget
import urllib.parse
import argparse

#def recursive downloader for apache download pages URLs
#dirUrl is encoded
def download(dirUrl, parentPath):
	
	#create dir
	encDirName=dirUrl[:-1].rpartition('/')[2]
	downloadDir=parentPath+urllib.parse.unquote(encDirName)+'/'
	os.makedirs(downloadDir, exist_ok=True)
	print("\nDownloading: "+downloadDir)
	
	#parse page
	response = s.get(dirUrl)
	page = response.text
	tree = html.fromstring(page)
	entries = tree.xpath('//td/a/@href')

	#iterate over entries
	iterLink = iter(entries)
	next(iterLink) #skip first link (parent directory)
	for entry in iterLink: #iterate over file and directories
		
		if(entry[-1])=='/':
			#This is a directory -> Recurse
			download(dirUrl+entry, downloadDir)
		else:
			#This is a file -> Download
			destFile=downloadDir+urllib.parse.unquote(entry)
			fileURL=dirUrl+entry
			print('\nDownloading: '+ urllib.parse.unquote(fileURL))
			#print('Downloading: '+ fileURL+" to: "+destFile)
			wget.download(fileURL, destFile)
	
#run from command line
parser = argparse.ArgumentParser(description='Welcome to RHFD: Recursive Http Files Downloader')
parser = argparse.ArgumentParser(epilog='author: DoNcK')
parser.add_argument('url', type=str, help='URL of the directory to download')

argUrl = parser.parse_args().url
if argUrl[-1] == '/':
	s = requests.Session()
	download(argUrl, './')
	print('\n[DONE]')
else:
	print('Error: this is not a directory')
