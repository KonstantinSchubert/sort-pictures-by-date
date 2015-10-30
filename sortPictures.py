#!/usr/bin/python

from datetime import datetime
from PIL import Image
import glob
import os


def getDate(url):
	try:
		img = Image.open(url)
		exif = img._getexif()
		if 36867 in exif:
			return  datetime.strptime(exif[36867],'%Y:%m:%d  %H:%M:%S').date()
		if 34853 in exif:
			print ' looking for "date modified" '
			return  datetime.strptime(str(exif[34853][29]),'%Y:%m:%d').date()
	except Exception:
		pass
	print "Problem with exif data"
	print "Now using file creation time"
	return datetime.fromtimestamp(os.stat(url).st_mtime)




basedir = "../Bilder/"
os.chdir(".")

for ending in ["jpeg","JPG","avi","AVI","mp4","jpg", "JPG", "MOV", "PNG"]:
	for fileName in glob.glob("*."+ending):
		print "sorting "+ fileName
		try:
		    date = getDate(fileName)
		    targetdir = str(basedir+date.strftime("%Y/%m %B")+"/")
		    if not os.path.isdir(targetdir):
		    	os.makedirs(targetdir)
		    os.rename(fileName,targetdir+fileName)
		except Exception as e:
			print " error with "+fileName+ ": "+str(e)
