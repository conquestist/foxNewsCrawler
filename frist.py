from bs4 import BeautifulSoup
import requests

def fox_backup():
	#get page
	req = requests.get("https://foxnews.com")
	file = open("backup.txt", "w")
	file.write(str(req.content))
	file.close()

def fox_sort_titles():
	file2 = open("backup.txt", "r")
	rep = file2.read()
	file2.close()
	soup = BeautifulSoup(rep, "html.parser")
	spoon = soup.find_all("h2")
	#get all h2 because title news are there
	soup2 = BeautifulSoup(str(spoon), "html.parser")
	spoon2 = soup2.find_all("a")
	#writing titles
	cont = 0
	file3 = open("titles.txt", "w")
	for i in spoon2:
		file3.write(str(spoon2[cont])+"*")
		cont += 1
	cont = 0
	file3.close()

def struct_fox_news():
	file4 = open("titles.txt", "r")
	fox_hrefs = file4.read().split("*")
	file4.close()
	try:
			for i in fox_hrefs:
				file5 = open("foxhrefs.txt", "w")
				soup3 = BeautifulSoup(i, "html.parser")
				spoon3 = soup3.find("a")
				file5.write(str(spoon3["href"])+"*")
	except:
		pass

def sort_fox_href_file():
	file6 = open("foxhrefs.txt", "r")
	reading = file6.read().split("*")
	frist_read_list = []
	final_good_list = []
	for i in reading:
		frist_read_list.append(i)
	for i in frist_read_list:
		if "video" not in i:
			final_good_list.append(i)
	file7 = open("good_fox_hrefs.txt", "w")
	for i in final_good_list:
		file7.write(i+"*")
	file7.close()

def get_main_fox_news():
	try:
		file8 = open("good_fox_hrefs.txt", "r")
		read = file8.read().split("*")
		for i in read:
			req = requests.get(i)
			soup4 = BeautifulSoup(req.content, "html.parser")
			spoon4 = soup4.find_all("p")
			for i in spoon4:
				file9 = open("mainfox.txt", "w")
				file9.write(str(spoon4)+"*")
				file9.close()
	except:
		pass

def read_fox_main():
	file10 = open("mainfox.txt", "r")
	print(file10.read().split("*"))


#get_main_fox_news()
read_fox_main()	





