# Importation du type Page de Playwright pour le typage
from playwright.sync_api import Page

# Permet de charger les variables depuis le fichier .env
from dotenv import load_dotenv
import os

# Charge le fichier .env pour rendre les variables d'environnement disponibles
load_dotenv()

# Page Object Model (POM) — représente la page des questions de Stack Overflow
# Le POM permet de centraliser les sélecteurs et actions liés à une page
class QuestionsPage:

    # Récupère l'URL de la page depuis le fichier .env
    URL = os.getenv("BASE_URL")

    def __init__(self, page: Page):
        """
        Constructeur — reçoit la page Playwright injectée par le fixture.
        Ne fait aucune action sur le DOM, stocke uniquement la page.
        """
        self.page = page

    def navigate(self):
        """
        Navigue vers la page des questions et attend que le contenu soit chargé.
        Gère également la bannière de cookies si elle apparaît.
        """
        # Navigue vers l'URL avec un timeout de 60 secondes
        self.page.goto(self.URL, timeout=60000)

        # Tente de cliquer sur le bouton d'acceptation des cookies
        # Si la bannière n'apparaît pas, on continue sans erreur
        try:
            self.page.click("#onetrust-accept-btn-handler", timeout=5000)
        except:
            pass  # pas de bannière, on continue

        # Attend que les questions soient visibles sur la page (max 60 secondes)
        self.page.wait_for_selector(".s-post-summary--content-title", timeout=60000)

    def get_titre_premiere_question(self):
        """
        Récupère le titre de la première question affichée sur la page.
        Retourne le texte nettoyé (sans espaces superflus).
        """
        return (
            self.page
            .locator(".s-post-summary--content-title a")  # Sélecteur CSS du titre
            .first                                         # Prend uniquement le premier résultat
            .inner_text()                                  # Extrait le texte visible
            .strip()                                       # Supprime les espaces en début/fin
        )