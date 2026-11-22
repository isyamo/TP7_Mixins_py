from abc import ABC, abstractmethod
from datetime import datetime
import json


class Horodatable(ABC):
    @abstractmethod
    def horodatage(self):
        pass


class Validable(ABC):
    @abstractmethod
    def valider(self):
        pass


class Serializable(ABC):
    @abstractmethod
    def to_json(self):
        pass


class Historisable(ABC):
    @abstractmethod
    def ajouter_historique(self, action):
        pass

    @abstractmethod
    def afficher_historique(self):
        pass


class Document(Horodatable, Validable, Serializable, Historisable):
    def __init__(self, titre, contenu):
        self.titre = titre
        self.contenu = contenu
        self.historique = []

    def horodatage(self):
        print(f"[LOG] Action à {datetime.now()}")

    def valider(self):
        if not getattr(self, "titre", None):
            raise ValueError("Titre manquant")
        if not getattr(self, "contenu", None):
            raise ValueError("Contenu manquant")
        print("Validation OK")

    def to_json(self):
        return json.dumps(
            {"titre": self.titre, "contenu": self.contenu},
            ensure_ascii=False,
        )

    def ajouter_historique(self, action):
        self.historique.append(f"{datetime.now()} - {action}")

    def afficher_historique(self):
        print("Historique :", self.historique)

    def sauvegarder(self):
        self.horodatage()
        self.valider()
        print(f"Document '{self.titre}' sauvegardé.")
        self.ajouter_historique(f"Sauvegarde de '{self.titre}'")


doc = Document(" RAPPORT PYTHON ", "resume des exeptions et heritage")
doc.sauvegarder()
print("JSON :", doc.to_json())
doc.afficher_historique()