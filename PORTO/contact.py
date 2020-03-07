#creation d'une liste de contact

continuer = 'y'   #le y est pour yes et le n sera pour no
liste_de_contact = [] #la lsite est vide au depart 

while continuer == 'y':
    contact_a_ajouter=input('Entrez le contact a ajouter: ')
   
    if contact_a_ajouter.lower() in[contact[0].lower() for contact in liste_de_contact]:
        print('{0} a deja ete ajouter dans votre contact' .format(contact_a_ajouter))
    else:
         telephone=int(input('Entrez le numero du contact: '))
         liste_de_contact.append((contact_a_ajouter, telephone)) #utilisation de turple
    continuer= input('Voulez-vous ajouter un autre contact? y/n: ')
    print('')

liste_de_contact.sort() #pour avoir la liste en ordre alphabetique
print(liste_de_contact)