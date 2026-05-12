# Importation de la classe QuestionsAPI 
from api.questions_api import QuestionsAPI
import pytest

# Instance unique de l'API réutilisée dans tous les tests
api = QuestionsAPI()


# Tag @pytest.mark.api permet de lancer uniquement ces tests avec : pytest -m api
@pytest.mark.api
def test_api_retourne_un_titre():
    """Vérifie que la première question retournée par l'API possède un titre non vide."""

    response = api.get_latest_questions()

    # Convertit la réponse JSON en dictionnaire Python
    data = response.json()

    # Récupère le titre de la première question
    titre = data["items"][0]["title"]

    # Vérifie que le titre n'est pas une chaîne vide
    assert titre != ""
    # Vérifie que le titre contient au moins un caractère
    assert len(titre) > 0



@pytest.mark.api
def test_pagesize():
    """Vérifie que le paramètre pagesize est bien respecté par l'API."""

    response = api.get_latest_questions(pagesize=5)
    data = response.json()

    # Vérifie qu'on reçoit exactement 5 questions
    assert len(data["items"]) == 5


@pytest.mark.api
def test_site_valide():
    """Vérifie qu'une requête vers un site valide retourne un statut HTTP 200."""

    response = api.get_valid_site()

    assert response.status_code == 200


@pytest.mark.api
def test_site_invalide():
    """Vérifie qu'une requête vers un site inexistant retourne un statut HTTP 400."""

    response = api.get_invalid_site()

    assert response.status_code == 400


@pytest.mark.api
def test_filtre_tag():
    """Vérifie que toutes les questions retournées contiennent bien le tag demandé."""

    response = api.get_questions_by_tag("python")
    data = response.json()

    # Parcourt chaque question et vérifie la présence du tag "python"
    for question in data["items"]:
        assert "python" in question["tags"]


@pytest.mark.api
def test_structure_question():
    """Vérifie que chaque question contient les champs obligatoires attendus."""

    response = api.get_latest_questions(pagesize=3)
    data = response.json()

    for item in data["items"]:
        assert "title" in item           # Titre de la question
        assert "question_id" in item     # Identifiant unique
        assert "creation_date" in item   # Date de création
        assert "owner" in item           # Auteur de la question


@pytest.mark.api
def test_quota_present():
    """Vérifie que la réponse contient le quota d'appels API restant."""

    data = api.get_latest_questions().json()

    # Vérifie que le champ quota_remaining est présent
    assert "quota_remaining" in data
    # Vérifie que le quota est un nombre positif ou nul
    assert data["quota_remaining"] >= 0


@pytest.mark.api
def test_titre_est_une_chaine():
    """Vérifie que le titre de la question est bien de type string."""

    data = api.get_latest_questions().json()
    titre = data["items"][0]["title"]

    # isinstance vérifie le type de la variable
    assert isinstance(titre, str)


@pytest.mark.api
def test_question_id_est_un_entier():
    """Vérifie que l'identifiant de la question est bien un entier positif."""

    data = api.get_latest_questions().json()
    question_id = data["items"][0]["question_id"]

    # Vérifie que c'est bien un entier
    assert isinstance(question_id, int)
    # Vérifie que l'ID est strictement positif
    assert question_id > 0


@pytest.mark.api
def test_tag_inexistant_retourne_liste_vide():
    """Vérifie qu'un tag inexistant retourne une liste vide et non une erreur."""

    response = api.get_questions_by_tag("tag_qui_nexiste_vraiment_pas_xyz123")
    data = response.json()

    # Aucune question ne doit être retournée
    assert len(data["items"]) == 0