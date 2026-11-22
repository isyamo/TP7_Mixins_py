from datetime import datetime
import json


class Horodatable:
    def horodatage(self):
        return str(datetime.now())


class Serializable:
    def to_json(self):
        donnees = {k: v for k, v in self.__dict__.items() if k != "historique"}
        return json.dumps(donnees, ensure_ascii=False)


class ExportableCSV:
    def to_csv(self):
        valeurs = [str(v) for k, v in self.__dict__.items() if k != "historique"]
        return ";".join(valeurs)


class Historisable:
    def sauver_etat(self):
        etat = {k: v for k, v in self.__dict__.items() if k != "historique"}
        self.historique.append({"date": self.horodatage(), **etat})


class Journalisable:
    def log(self, texte):
        print(f"\n {self.horodatage()} --> {texte} \n ")


class Contrat(Horodatable, Serializable, ExportableCSV, Historisable, Journalisable):
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.historique = []
        self.sauver_etat()
        self.log(" Contrat créé ")


class Commande(Horodatable, Serializable, ExportableCSV, Historisable, Journalisable):
    def __init__(self, id, produit):
        self.id = id
        self.produit = produit
        self.historique = []
        self.sauver_etat()
        self.log(" Commande créée ")


class Client(Horodatable, Serializable, ExportableCSV, Journalisable):
    def __init__(self, id, nom):
        self.id = id
        self.nom = nom
        self.log(" Client créé ")


ct = Contrat(1, " Gestion ")
print(ct.to_json())
print(ct.to_csv())
print(ct.historique)

c = Commande(2, " PC ")
print(c.to_json())
print(c.to_csv())

cl = Client(3, " Moaad ")
print(cl.to_json())
print(cl.to_csv())