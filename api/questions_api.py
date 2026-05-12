# Bibliothèque pour effectuer des requêtes HTTP
import requests

# Permet de charger les variables depuis le fichier .env
from dotenv import load_dotenv
import os

# Charge le fichier .env pour rendre les variables d'environnement disponibles
load_dotenv()


class BaseAPI:
    """
    Classe de base contenant la logique commune à toutes les APIs.
    Centralise la requête GET pour éviter la répétition de code.
    Toutes les classes API héritent de cette classe.
    """

    # Récupère l'URL de l'API depuis le fichier .env
    URL_API = os.getenv("API_URL")

    def _get(self, params):
        """
        Méthode générique pour effectuer une requête HTTP GET.
        Le underscore indique que c'est une méthode interne,
        destinée à être utilisée uniquement dans les classes filles.
        """
        response = requests.get(self.URL_API, params=params)
        return response


class QuestionsAPI(BaseAPI):
    """
    Classe dédiée aux questions Stack Overflow.
    Hérite de BaseAPI pour réutiliser la méthode _get().
    """

    def get_latest_questions(self, pagesize=1):
        """
        Récupère les dernières questions triées par date de création.
        Par défaut retourne 1 seule question (pagesize=1).
        """
        params = {
            "order": "desc",        # Tri décroissant (plus récent en premier)
            "sort": "creation",     # Trié par date de création
            "site": "stackoverflow",
            "pagesize": pagesize    
        }

        return self._get(params)

    def get_questions_by_tag(self, python, pagesize=10):
        """
        Récupère les questions filtrées par un tag spécifique.
        Ex : get_questions_by_tag("python") retourne les questions taguées python.
        """
        params = {
            "order": "desc",
            "sort": "creation",
            "site": "stackoverflow",
            "pagesize": pagesize,
            "tagged": python           # Filtre par tag
        }

        return self._get(params)

    def get_invalid_site(self):
        """
        Effectue une requête vers un site inexistant.
        Utilisé pour tester que l'API retourne bien une erreur 400.
        """
        params = {
            "order": "desc",
            "sort": "creation",
            "site": "site_qui_nexiste_pas"  # Site volontairement invalide
        }

        return self._get(params)

    def get_valid_site(self):
        """
        Effectue une requête vers un site valide (stackoverflow).
        Utilisé pour tester que l'API retourne bien un statut 200.
        """
        params = {
            "order": "desc",
            "sort": "creation",
            "site": "stackoverflow"
        }

        return self._get(params)