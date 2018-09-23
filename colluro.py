import os
import eyed3
import re
import datetime

EmptyString = {"",None}
MusicFiles = {".mp3",".ogg"}
tags = {"title","album","artist"}

def saveMaj(mp3):
	mem = {}
	oldMmp3 = eye3d.load(mp3.path)
	mem["date"] = datetime.datetime.now()
	for tag in tags:
		if oldMmp3.get(tag) != mp3.get(tag):
			mem[tag] = oldMmp3.get(tag)
	

def check_album(mp3, album):
	global EmptyString
	if mp3.tag.album in EmptyString:
		mp3.tag.album = album
		mp3.tag.save()

def check_artist(mp3, album):
	global EmptyString
	if mp3.tag.artist in EmptyString:
		mp3.tag.artist = artist
		mp3.tag.save()	
		
def check_title(mp3, title):
	global EmptyString
	if mp3.tag.title in EmptyString:
		mp3.tag.title = title
		mp3.tag.save()

def epurateRegex(string, rgx):
	m = re.search(rgx,string)
	if m == None:
		# print("fail")
		return string
	return string[:m.start()] + string[m.end():]

def rekt_rgx_from_title(dir, rgx):
	for file in os.listdir(dir):
		mp3.tag.title = epurateRegex(mp3.tag.title, rgx)
		mp3.tag.save();

print("sapar")
for artist in os.listdir("."):
	print("voilà ./"+artist)
	if os.path.isdir("./"+artist):
		print("j'entre dans./"+artist)
		for album in os.listdir("./"+artist):
			if os.path.isdir("./"+artist+"/"+album):
				print("j'entre dans./"+artist+"/"+album)
				for file in os.listdir("./"+artist+"/"+album):
					print("fichier : "+file)
					if file[-4:]==".mp3":
						print("c'est un mp3 !")
						mp3 = eyed3.load("./"+artist+"/"+album+"/"+file)
						check_album(mp3, album)
						check_artist(mp3, artist)
						check_title(mp3, file[:-4])
						
