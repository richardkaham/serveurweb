def install_apache2():
    os.system("sudo apt-get update")
    os.system("sudo apt-get install apache2")
    os.system("clear")
    config_site()

def config_site():
    vhost=["<VirtualHost *:80>",
            "ServerAdmin ",
            "ServerName ",
            "ServerAlias ",
            "DocumentRoot ",
            "ErrorLog ${APACHE_LOG_DIR}/error.log",
            "CustomLog ${APACHE_LOG_DIR}/access.log combined",
            "</VirtualHost>"
             ]
    nomsite = input("entrez le nom du site (ex. www.monsite.com): ")
    mailadmin = input("Entrez adresse mail de l'administrateur :")

    docroot = "/var/www/html/"+nomsite
    siteconf = "001-"+nomsite+".conf"
    cheminsite= "/etc/apache2/sites-available/"+siteconf
    alias = nomsite.replace("www","*") # construire l'alias du site
    vhost[1] = vhost[1]+mailadmin # mail administrateur
    vhost[2] = vhost[2]+nomsite   # nom de domaine
    vhost[3] = vhost[3]+alias     # alias
    vhost[4] = vhost[4]+docroot   # /var/www/html/www.gotam.com
    os.system('clear')
    print("création du fichier de configuration du site")
    print(cheminsite)
    input("une touche ....")
    with open("virtual","w") as flux:
         for ligne in vhost:
            print(ligne)
            flux.write("%s\n" %ligne)

    dossier = "sudo mkdir /var/www/html/"+nomsite
    os.system(dossier)   # créer le dossier du site
    copiehtml = "sudo cp photopays/*.html /var/www/html/"+nomsite+"/"
    copiejpeg = "sudo cp photopays/*.jpeg /var/www/html/"+nomsite+"/"
    os.system(copiehtml)
    os.system(copiejpeg)
#  print("creation du line symbolique")
    lien = "sudo a2ensite "+"001-"+nomsite
    os.system("sudo cp virtual /etc/apache2/sites-available/"+siteconf)
    os.system(lien) 
# input("lien ok, tapez une touhce pour recharger apache2")
    os.system("systemctl reload apache2.service")
#  input("tout est ok, tapez une touhce pour continuer")

def desinst_apache2():
# Arrêt apache2.
    os.system("sudo service apache2 stop")
# autoremove pour se débarrasser des autres dépendances.
    os.system("sudo apt-get autoremove apache2")


import os
import csv
lchoix = ["i = Installer et configurer Apache","d = désinstaller apache","q = Quiter"]
ch = ""
os.system("clear")
while ch.upper() != 'Q':
    for choix in lchoix:
        print(choix)
    ch = input("votre choix SVP ") 
    if ch.upper() == 'I': 
        os.system("clear")
        print ("intallation")
        install_apache2()
    if ch.upper() == 'D':
        os.system("clear") 
        print("désinstallation")
        desinst_apache2()
    os.system("clear")
print("aurevoir")

# config_site()

