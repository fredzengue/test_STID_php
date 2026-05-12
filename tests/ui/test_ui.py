# Importation du Page Object Model de la page des questions
from pages.questions_page import QuestionsPage
import pytest


# Tag @pytest.mark.ui permet de lancer uniquement ce test avec : pytest -m ui
@pytest.mark.ui
def test_premiere_question_visible(browser_page):
    """
    Test UI — vérifie que la première question est bien visible
    et possède un titre non vide sur la page Stack Overflow.
    """

    # Crée une instance du POM en lui passant la page Playwright
    questions_page = QuestionsPage(browser_page)

    # Navigue vers la page et attend que le contenu soit chargé
    questions_page.navigate()

    # Récupère le titre de la première question affichée
    titre = questions_page.get_titre_premiere_question()

    # Affiche le titre dans la console pour faciliter le débogage
    print(f"\nTitre trouvé : {titre}")

    # Vérifie que le titre n'est pas vide
    assert titre != ""

    # Ferme la page après le test
    browser_page.close()