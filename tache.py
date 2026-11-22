from datetime import datetime


class ValidationMixin:
    def verifier_titre(self, titre):
        if not titre or not titre.strip():
            raise ValueError("Le titre est obligatoire !")
        return titre.strip()


class HistoriqueMixin:
    def __init__(self):
        self.historique = []

    def ajouter_historique(self, ancienne_description):
        self.historique.append(ancienne_description)

    def afficher_historique(self):
        print(f"Historique de '{self.titre}' :")
        for i, desc in enumerate(self.historique, 1):
            print(f"  {i}. {desc}")


class JournalisationMixin:
    def log(self, message):
        print(f"[LOG] {message}")


class Tache(ValidationMixin, HistoriqueMixin, JournalisationMixin):
    def __init__(self, titre, description="", date_creation=None):
        HistoriqueMixin.__init__(self)
        self.titre = self.verifier_titre(titre)
        self.description = description
        self.date_creation = date_creation or datetime.now()
        self.log(f"Création de la tâche '{self.titre}'")

    def mettre_a_jour(self, nouvelle_description):
        self.ajouter_historique(self.description)
        self.description = nouvelle_description
        self.log(f"Mise à jour de la tâche '{self.titre}'")



t = Tache(" Rapport de tache ", " La version 1")
t.mettre_a_jour(" La version 2")
t.mettre_a_jour(" La version finale")
t.mettre_a_jour(" La version finale definitive ")
t.afficher_historique()