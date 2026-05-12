# Importation de pytest pour utiliser le décorateur @pytest.fixture
import pytest

# Définition du fixture "browser_page" utilisé dans tous les tests UI et e2e
# scope="function" signifie qu'un nouveau navigateur est créé pour chaque test
@pytest.fixture(scope="function")
def browser_page(browser):
    """
    Fixture Playwright personnalisée.
    Le paramètre 'browser' est fourni automatiquement par pytest-playwright
    selon le --browser passé en ligne de commande (chromium, firefox, webkit).
    """

    # Crée un nouveau contexte de navigation avec des paramètres personnalisés
    context = browser.new_context(

        # Simule un vrai navigateur Chrome pour éviter la détection bot
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),

        # Résolution de la fenêtre du navigateur
        viewport={"width": 1280, "height": 720},

        # Langue du navigateur en français
        locale="fr-FR"
    )

    # Ouvre une nouvelle page dans ce contexte
    page = context.new_page()

    # Fournit la page au test — tout ce qui est avant yield est le "setup"
    yield page

    # Ferme le contexte après le test — tout ce qui est après yield est le "teardown"
    context.close()