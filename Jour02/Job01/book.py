class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print (self.nom , self.prenom)


    # accesseur et mutateur

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_prenom(self):
        return self.prenom

    def set_prenom(self, prenom):
        self.prenom = prenom


# Auteur
class Auteur(Personne):
  def __init__(self, prenom, nom):
    self.collection = []
    Personne.__init__(self, prenom, nom)

  def listerCollection(self):
    for livre in self.collection :
      print(livre.afficherDetails())

  def ecrireUnLivre(self, titre):
    self.ajouterLivreDansCollection(Livre(titre, self))

  def ajouterLivreDansCollection(self, livre):
    self.collection.append(livre)

# Livre
class Livre:
  def __init__(self, titre, auteur):
    self.titre = titre
    self.auteur = auteur

  def afficherDetails(self):
    return self.titre
# Livre
class Livre:
  def __init__(self, titre, auteur):
    self.titre = titre
    self.auteur = auteur

  def afficherDetails(self):
    return self.titre


Grisham = Auteur('John', 'Grisham')
Grisham.ecrireUnLivre('The Pelican Brief')
Grisham.ecrireUnLivre('The firm')
Grisham.listerCollection()
