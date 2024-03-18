import requests
from bs4 import BeautifulSoup
import os
import csv
import urllib.request
from urllib.parse import urljoin

url= "http://books.toscrape.com/"
page = requests.get(url)
#rendre le contenu de la page lisible
content = BeautifulSoup(page.content,"html.parser")
a_list = []
tag_elements = []
links = []
books = []
list = []
Titres = []
titles = []
table_elt = []
categories = []
test = 0
books_elements = content.find_all('article',class_= 'content')
nbre_etoiles = 0
upc = 0
categorie = 0
description = 0
liste_liens_categories = []
informations = ['product_page_url',
                'title','universal_ product_code (upc)',
                'price_including_tax',
                'price_excluding_tax',
                'number_available',
                'product_description',
                'category',
                'review_rating',
                'image_url']
#creation du dossier qui contient les fichiers csv
if not os.path.exists("Data") :
   os.mkdir("Data") 

if not os.path.exists("Images") :
   os.mkdir("Images")


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
    #var = url.replace("index.html","")
    if content.find("li",class_ = "next") :
        suivant = content.find("li",class_ ="next")
        next = suivant.find("a")
        next_page = next["href"]
        next_page = urljoin(url , next_page)
        print("next page : ",next_page)
        recuperation_url(next_page)
       

      
#recuperation des informations concernant un livre
def recuperation_info(url):
   page = requests.get(url)
   content = BeautifulSoup(page.content,'html.parser')  
   titre= content.find('ul',class_ = 'breadcrumb')
   titre = content.find("li",class_="active").text
   table_elt = content.find('table', class_= 'table table-striped')
   info = table_elt.find_all("td")
   upc = info[0].text
   price_including_tax = info[4].text
   price_excluding_tax = info[3].text
   number_available =  info[5].text
   test = url
   print(test)
   p_text = content.find_all('p')
   description = p_text[3].text#troisieme balise p
   categories = content.find('ul',class_='breadcrumb').find_all("li")
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
      return nbre_etoiles
   if star == 'three' :
      nbre_etoiles = 3
      return  nbre_etoiles
   if star == 'four' :
      nbre_etoiles = 4
      return nbre_etoiles
   if star == 'five' :
      nbre_etoiles = 5
      return nbre_etoiles
   Image = content.find('img')
   Source = Image["src"]
   Source =  Source.replace("../../",url)
   id = Image["alt"].replace(" ","_")
   
   print(f"voici le source {Source}")
 
  # urllib.request.urlretrieve(Source,"Images/" )
   with open("Images/" + id + ".jpg","wb") as f :
      I = requests.get(Source)
      f.write(I.content)
    
   liste_info = [url,titre, upc,price_including_tax,price_excluding_tax,number_available ,description,categorie,star,source]
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

def save_data() : 
   for link in liste_liens_categories:
       page = requests.get(link)
       content = BeautifulSoup(page.content,"html.parser")
       titre_page = content.find("h1").text.replace(" ","_")
       titre_page = titre_page + ".csv"

       csv_file =open("Data/"+titre_page,"w",encoding='utf-8',newline='')#creation du fichier avec pour nom la categorie
       writer = csv.writer(csv_file)#initialisation 
       writer.writerow(informations)#donner les champs de informations au fichier?
       recuperation_url(link)#recuperation du lien de la page des livres de cette categorie
       for i in list :
          writer.writerow(recuperation_info(i))
       csv_file.close()#terminaison de l'operation de remplissage dans ce fichier
       
save_data()



