Scraping de données de livres - Guide d'installation et d'utilisation
Ce guide explique comment créer et activer un environnement virtuel pour exécuter le code de scraping de données de livres à partir du site "http://books.toscrape.com/". L'environnement virtuel garantit que les dépendances requises sont isolées et facilite la gestion du code.

#Étapes d'installation
Suivez ces étapes pour créer et activer un environnement virtuel :

-Assurez-vous d'avoir Python installé sur votre système. Vous pouvez vérifier cela en exécutant la commande suivante dans votre terminal :
>>>python --version
Si Python n'est pas installé, téléchargez et installez la dernière version compatible avec votre système d'exploitation à partir du site officiel : https://www.python.org/downloads/

-Ouvrez un terminal et accédez au répertoire où vous souhaitez enregistrer le code de scraping.

-Créez un nouvel environnement virtuel en exécutant la commande suivante :
>>>python -m venv env

-Activez l'environnement virtuel en exécutant la commande appropriée selon votre système d'exploitation :

Sur Windows :
>>>env\Scripts\activate
Sur macOS et Linux :
>>>source env/bin/activate
Lorsque l'environnement virtuel est activé, vous verrez le préfixe (env) dans votre terminal.

-Installez les dépendances requises en exécutant la commande suivante :
>>>pip install requests bs4
Cela installera les bibliothèques requests et beautifulsoup4 nécessaires pour exécuter le code de scraping.

-Téléchargez le code de scraping précédent et placez-le dans le répertoire où vous avez créé l'environnement virtuel.

#Exécution du code de scraping
Après avoir configuré l'environnement virtuel, vous pouvez exécuter le code de scraping en suivant ces étapes :

-Assurez-vous que votre environnement virtuel est activé. Si ce n'est pas le cas, suivez l'étape 4 des instructions d'installation pour l'activer.

-Dans le terminal, accédez au répertoire où vous avez placé le code de scraping.

-Exécutez le script Python à l'aide de la commande suivante :
>>>python scraper.py
Le script commencera à scraper les données de livres à partir du site "http://books.toscrape.com/" et les enregistrera dans des fichiers CSV.

Attendez que le script se termine. Une fois terminé, vous trouverez les fichiers CSV contenant les données de livres dans le répertoire où vous avez exécuté le script.

