class gestionStock:
    def __init__(self):
        self.stock = {}  # Dictionnaire pour stocker les produits avec leur volume
        self.alertes = []  # Liste pour stocker les alertes

    #Valeur ajoutée : Permet de rentrer manuellement un ou plusieurs produits a entrer dans le stock
    def saisieProduits(self, input_str):
        produits = input_str.split(",")
        for produit in produits:
            nomProduit, volume = produit[0].upper(), int(produit[1:])
            if nomProduit not in self.stock:
                self.stock[nomProduit] = []
            self.stock[nomProduit].append(volume)

    #Valeur ajoutée : Permet d’afficher tous les produits dans le stock
    def afficherStock(self):
        print("\n-------------------------------\n")
        print("Stock actuel :")
        for nomProduit, volumes in self.stock.items():
            print(f"{nomProduit}: {','.join(map(str, sorted(volumes)))}")


    #Valeur ajoutée : Permet de gérer jusqu’à trois alertes de faible stock de produit
    def gestionAlertes(self, nomProduit):
        if len(self.alertes) < 3:
            if len(self.stock[nomProduit]) <= 2 :
                self.alertes.append(nomProduit)
        else:
                del self.alertes[-1]
                self.alertes.insert(0,nomProduit)


    #Valeur ajoutée : Permet d'afficher jusqu’à trois alertes de faible stock de produit
    def afficherAlertes(self):
        if not self.alertes:
            print("\n-------------------------------\n")
            print("Aucune alerte.")
        else:
            print("\n-------------------------------\n")
            print("Alertes (plus ancienne à plus récente) :", ",".join(self.alertes))

    #Valeur ajoutée : Permet d’assembler un colis et modifier les stocks des produits utilisés
    def assemblerColis(self, input_str):
        produits = input_str.split(",")
        produits.sort(key=lambda x: int(x[1:]), reverse=True)
        contenuColis = {}  # Dictionnaire pour stocker les produits du colis
        for produit in produits:
            nomProduit, volume = produit[0].upper(), int(produit[1:])
            if nomProduit in self.stock and volume in self.stock[nomProduit]:
                if nomProduit not in contenuColis:
                    contenuColis[nomProduit] = []
                contenuColis[nomProduit].append(volume)
                self.stock[nomProduit].remove(volume)
            else:
                print(f"Produit {produit} non disponible dans le stock.")
                retry = input("Veuillez réessayer ou quitter avec 0 : ")
                if retry == '0':
                    break
                else :
                    self.assemblerColis(retry)
        # Afficher le contenu du colis
        print("\nContenu du colis (le plus lourd en premier) :")
        for nomProduit, volumes in contenuColis.items():
            for volume in volumes:
                print(f"{nomProduit}{volume}")
        # Générer l'alerte après l'affichage du colis
        for nomProduit in contenuColis.keys():
            self.gestionAlertes(nomProduit)
        self.afficherAlertes()

    #Valeur ajoutée : Afficher toutes les fonctionnalités et permettre une utilisation fluide
    def menu(self):
            while True:
                print("\n-------------------------------\n")
                print("1. Ajouter des produits")
                print("2. Afficher l'inventaire")
                print("3. Afficher les alertes")
                print("4. Assembler des colis")
                print("0. Quitter")
                choice = input("Choisissez une option (0-4): ")
                if choice == "0":
                    break
                elif choice == "1":
                    print("\n-------------------------------\n")
                    produits = input("Entrez les produits (séparés par des virgules) : ")
                    self.saisieProduits(produits)
                    self.afficherStock()
                elif choice == "2":
                    self.afficherStock()
                elif choice == "3":
                    self.afficherAlertes()
                elif choice == "4":
                    colis = input("Entrez les produits pour assembler des colis : ")
                    self.assemblerColis(colis)
                else:
                    print("Option non valide. Veuillez choisir une option entre 0 et 5.")


# Début de l'utilisation
gestion_stock = gestionStock()
# Ajout de produits au préalable
gestion_stock.saisieProduits("A1,A1,B1,B5,B4,C1,A2,C3,C3")
#Appel du menu intéractif
gestion_stock.menu()