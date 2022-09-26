


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




# Creating different persons
p1 = Personne('Luca', 'Toni')
p2 = Personne('Anne','Bassi')
p3 = Personne('Hamza','Nahari')
p4 = Personne('John', 'lennon')


p1.SePresenter()
p2.SePresenter()
p3.SePresenter()
p4.SePresenter()
