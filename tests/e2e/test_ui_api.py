# Importation de la classe QuestionsAPI 
from api.questions_api import QuestionsAPI

# Importation du Page Object Model de la page des questions
from pages.questions_page import QuestionsPage
import pytest

# Instance unique de l'API réutilisée dans le test
api = QuestionsAPI()


# Tag @pytest.mark.e2e permet de lancer uniquement ce test avec : pytest -m e2e
@pytest.mark.e2e
def test_api_vs_web(browser_page):
    """
    Test End-to-End — compare le titre de la première question
    retournée par l'API avec celui affiché sur la page web.
    Les deux doivent être identiques.
    """

    # --- PARTIE API ---
    # Récupère la dernière question via l'API Stack Exchange
    response = api.get_latest_questions()
    data = response.json()

    # Extrait et nettoie le titre de la première question
    titre_api = data["items"][0]["title"].strip()

    # --- PARTIE UI ---
    # Crée une instance du POM en lui passant la page Playwright
    questions_page = QuestionsPage(browser_page)

    # Navigue vers la page et attend que le contenu soit chargé
    questions_page.navigate()

    # Récupère le titre de la première question affichée sur la page
    titre_ui = questions_page.get_titre_premiere_question()

    # Affiche les deux titres dans la console pour faciliter le débogage
    print(f"\nTitre API : {titre_api}")
    print(f"Titre UI  : {titre_ui}")

    # --- ASSERTION ---
    # Vérifie que le titre affiché sur le web correspond à celui retourné par l'API
    assert titre_api == titre_ui