import requests
from bs4 import BeautifulSoup
import os

#agent utilisateur
headers = {
   'User-Agent':
   'Mozilla/5.0 (Windows NT 10.0; WIN64; X64) AppleWebkit/537.36 (KHTML,like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

url= "http://books.toscrape.com/"
page = requests.get(url,headers=headers)
#rendre le contenu de la page lisible
content = BeautifulSoup(page.content,"html.parser")
a_list = []
tag_elements = []
links = []
books = []
list = []
Titres = []
titles = []
info = []
categories = []
test = 0
books_elements = content.find_all('article',class_= 'content')
nbre_etoiles = 0
categorie = 0
description = 0
liste_liens_categories = []
informations = ['product_page_url',
                'title','product_description',
                'category',
                'review_rating',
                'image_url']
"""
recuperation/extraction des elements demandés dans le cahier des exigences
for book_element in books_elements:
   price_including_tax= book_element.find('p',class_ = 'price_including_tax')
   title = book_element.find('h3',class_='title')
   review_rating= book_element.find('p',class_ ='review_rating')

#for book_element in books_elements :
#  print(book_element)

#classement de ces éléments dans la liste books ligne par ligne
books.append ({
   
      'price_including_tax' : price_including_tax,
      'title' : title,
      'review_rating' :  review_rating
})

#logique crawling
#url of the home page
base_url = 'http://books.toscrape.com/'
#extraction de la page te initialisation du content
#recuperation de la balise indiquant la prochaine page
 
next_li_element = content.find('li',class_='next')
while next_li_element is not None :
   next_page_relative_url = next_li_element.find('a',href = True)['href']
   page = requests.get(base_url + next_page_relative_url,headers=headers)
   content = BeautifulSoup(page.content,'html.parser')
   #chercher le prochain element dans la page suivante
   next_li_element=content.find('li',class_='next')

"""

#recuperation des liens de tous les livres
def recuperation_url(url):
    page = requests.get(url)
    content = BeautifulSoup(page.content,'html.parser')    
    tag_elements = content.find_all('h3')
    for tag_element in tag_elements :
       a_list = tag_element.find("a")
       links = a_list["href"]
       links = links.replace("../../../","http://books.toscrape.com/catalogue/")#remplacemment des points par l'adresse de la page
       list.append(links)


#recuperation des informations concernant un livre
def recuperation_info(url):
   page = requests.get(url)
   content = BeautifulSoup(page.content,'html.parser')  
   Titres= content.find_all('ul',class_ = 'breadcumb')
   for Titre in Titres :
      titre = Titres.find('li',class_ = 'active')

   infos = content.find('table', class_= 'table table-striped') 
   test = url
   print(test)
   p_text = content.find_all('p')
   description = p_text[3]#troisieme balise p
   categories = content.find('ul',class_='breadcumb')
   print(f"{categories} est la categorie")
   categorie = categories[2].text
   
   
   image = content.find('img')
   source = image["src"]
   source =  source.replace("../../",url)
   star = content.find("p",class_ = 'star-rating')["class"]
   star = star[1]#second element de la liste
   if star == 'one' :
      nbre_etoiles = 1
      return nbre_etoiles
   if star == 'two' :
      nbre_etoiles = 2
   
   if star == 'three' :
      nbre_etoiles = 3
      return  nbre_etoiles
   if star == 'four' :
      nbre_etoiles = 4
      return nbre_etoiles
   if star == 'five' :
      nbre_etoiles = 5
      return nbre_etoiles
   
   liste_info = [url,titre,description,categorie,star,source]
   return liste_info

def url_categorie():
   #url de la page principale
   page = requests.get(url)
   content = BeautifulSoup(page.content,"html.parser")
   liste_categories = content.find('ul',class_ = 'nav').find_all('a')
   liste_lien_categorie = liste_categories
   
   for i in liste_lien_categorie :
      i = i["href"]
      i = url + i 
      liste_liens_categories.append(i)
   liste_liens_categories.pop(0)
      

url_categorie()
#for i in liste_liens_categories :
 # print(i)
#creation du dossier qui contient les fichiers csv
if not os.path.exists("Data") :
   os.mkdir("Data") 


for i in liste_liens_categories :
   print(i)
   page = requests.get(i)
   content = BeautifulSoup(page.content,"html.parser")
   recuperation_url(i)
   for j in list:
      print (recuperation_info(j))

