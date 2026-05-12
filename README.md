# TEST_STID_PHP — Projet de tests automatisés

Projet de tests automatisés pour Stack Overflow, combinant tests API REST et tests UI avec Playwright en python

---


## Fichiers `__init__.py`

Chaque dossier contenant des tests ou des modules Python possède un fichier `__init__.py` vide :

```
pages/__init__.py
tests/api/__init__.py
tests/e2e/__init__.py
tests/ui/__init__.py
```

Ces fichiers ne contiennent aucun code mais sont **indispensables** — ils indiquent à Python que le dossier est un **package**, ce qui permet les imports entre modules :

```python
from pages.questions_page import QuestionsPage
from api.questions_api import QuestionsAPI
```

Sans eux, Python ne saurait pas résoudre ces chemins d'import et lèverait une `ModuleNotFoundError`.


---

## Installation

### 1. Cloner le projet

```bash
git clone <url-du-projet>
cd TEST_STID_PHP
```

### 2. Créer et activer votre propre virtualenv

```bash
python -m venv venv
venv\Scripts\activate
```

Vous devriez voir `(venv)` apparaître au début de la ligne de commande. Pour désactiver :
```bash
deactivate
```

### 3. Installer les dépendances Python

```bash
pip install pytest
pip install pytest-playwright
pip install playwright
pip install allure-pytest
pip install requests
pip install python-dotenv
pip install playwright-stealth
pip install pytest-xdist
```

`python-dotenv` permet de charger les variables du fichier `.env` via `load_dotenv()` dans le code :
```python
from dotenv import load_dotenv
load_dotenv()  # charge automatiquement le fichier .env à la racine
```

`pytest-xdist` est requis pour lancer les tests en parallèle sur plusieurs navigateurs :
```bash
pytest -v --browser chromium --browser firefox --browser webkit -n 3
```

### 4. Installer les navigateurs Playwright

```bash
# Installer tous les navigateurs (Chromium, Firefox, WebKit)
playwright install

# Ou installer un navigateur spécifique
playwright install chromium
playwright install firefox
playwright install webkit
```

### 5. Installer Allure CLI

Téléchargez le zip depuis https://github.com/allure-framework/allure2/releases, décompressez et ajoutez le dossier `bin` au PATH Windows.

Vérifiez l'installation :
```bash
allure --version
```

---

## Configuration

### Fichier `.env`

```dotenv
BASE_URL=https://stackoverflow.com/questions?tab=Newest
API_URL=https://api.stackexchange.com/2.3/questions
```

### Fichier `pytest.ini`

```ini
[pytest]
pythonpath = .
filterwarnings = ignore
addopts = --slowmo 2000 --alluredir=reports/allure-results
markers =
    api: tests liés à l'API
    ui: tests liés à l'interface
    e2e: tests end-to-end
```

---

## Lancer les tests

### Activer le virtualenv

```bash
venv\Scripts\activate
```

### Tous les tests

```bash
pytest -v
```

### Par tag

```bash
# Tests API uniquement
pytest -v -m api

# Tests UI uniquement
pytest -v -m ui

# Tests End-to-End uniquement
pytest -v -m e2e
```

### Par navigateur

```bash
# Chromium (défaut)
pytest -v --browser chromium

# Firefox
pytest -v --browser firefox

# WebKit
pytest -v --browser webkit

# Les 3 navigateurs en même temps
pytest -v --browser chromium --browser firefox --browser webkit
```

### Headless / Headful

```bash
# Headless (défaut)
pytest -v -m ui

# Headful (fenêtre visible)
pytest -v -m ui --headed
```

### Combiner les options

```bash
# Tests UI sur Firefox en headful
pytest -v -m ui --browser firefox --headed

# Tests e2e sur les 3 navigateurs
pytest -v -m e2e --browser chromium --browser firefox --browser webkit
```

---

## Rapport Allure

### Générer et ouvrir le rapport

```bash
allure serve reports/allure-results
```

### Générer sans ouvrir

```bash
allure generate reports/allure-results -o reports/allure-report --clean
```

---

## Description des tests

### Tests API (`tests/api/test_api.py`)

| Test | Description |

| `test_api_retourne_un_titre` | Vérifie que le titre de la première question n'est pas vide |
| `test_tri_questions` | Vérifie que les questions sont triées par date décroissante |
| `test_pagesize` | Vérifie que le paramètre `pagesize` est respecté |
| `test_site_valide` | Vérifie qu'un site valide retourne un statut 200 |
| `test_site_invalide` | Vérifie qu'un site invalide retourne un statut 400 |
| `test_filtre_tag` | Vérifie que le filtre par tag fonctionne correctement |
| `test_structure_question` | Vérifie que chaque question contient les champs obligatoires |
| `test_quota_present` | Vérifie que le quota API est présent dans la réponse |
| `test_titre_est_une_chaine` | Vérifie que le titre est bien de type `str` |
| `test_question_id_est_un_entier` | Vérifie que l'ID de la question est bien un entier positif |
| `test_tag_inexistant_retourne_liste_vide` | Vérifie qu'un tag inexistant retourne une liste vide |

### Tests UI (`tests/ui/test_ui.py`)

| Test | Description |

| `test_premiere_question_visible` | Vérifie que la première question est visible sur la page |

### Tests End-to-End (`tests/e2e/test_ui_api.py`)

| Test | Description |

| `test_api_vs_web` | Compare le titre retourné par l'API avec celui affiché sur la page web |


