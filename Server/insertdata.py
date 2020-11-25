from bs4 import BeautifulSoup

soup = BeautifulSoup(open('index.html'), 'html.parser')
tag = soup.new_tag("p")
title = soup.new_tag("h1")

list = []
with open("../Virtual-Ambient/infos.txt","r") as file:
    data = file.read()
    list = data.split(":")

f = open("index.html","a")
for i in range(0,len(list)):
    infos = list[i].split("-")
    title.string = infos[0]
    tag.string = infos[1]
    f.write(str(title) + "\n")
    f.write(str(tag)+"\n")

    