#!/usr/bin/python

from datetime import datetime 
from PIL import Image
import glob
import os


def getDate(url):
	img = Image.open(url)
	exif = img._getexif()
	try:
		date = datetime.strptime(exif[36867],'%Y:%m:%d  %H:%M:%S').date()
	except KeyError:
		# looking for "date modified"
		try:
			date = datetime.strptime(str(exif[34853][29]),'%Y:%m:%d').date()
		except KeyError:
			raise Exception("No fitting EXIF data found")

	return date


basedir = "../Bilder/"
os.chdir(".")

for ending in ["jpeg","JPG","avi","AVI","mp4","jpg"]:
	for fileName in glob.glob("*."+ending):
		try:
		    date = getDate(fileName)	    
		    print "sorting "+ fileName
		    targetdir = str(basedir+date.strftime("%Y/%m %B")+"/")
		    if not os.path.isdir(targetdir):
		    	os.makedirs(targetdir)
		    os.rename(fileName,targetdir+fileName)
		except Exception as e:
			print " error with "+fileName+ ": "+str(e)
