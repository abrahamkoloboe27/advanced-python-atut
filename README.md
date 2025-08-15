# Python Avancé — Africa Tech Up Tour 2025 🚀

Ce dépôt a pour objectif d'enseigner des **concepts avancés de Python** utiles en data engineering / data science.
Les notions sont d'abord expliquées dans des notebooks pédagogiques, puis mises en pratique via un **mini-pipeline** d'exemple pour montrer comment organiser un projet data.

# Notebooks (contenu pédagogique)

Les notebooks se trouvent dans `notebooks/` et couvrent les notions suivantes :

* **01-Syntaxe et Variables.ipynb**
  Rappels et approfondissement : types, objets en Python, annotations, f-strings, compréhensions, fonctions, bonnes pratiques.

* **02-Logging en Python.ipynb**
  Pourquoi logger (vs `print`), configuration (handlers, formatters), rotation, logging structuré, `logger.exception`, bonnes pratiques en production.

* **03-Organisation projet.ipynb**
  Arborescence recommandée (`src/`, `data/`, `notebooks/`, `tests/`), séparation I/O ↔ logique, gestion des dépendances, README/CI, et exemples concrets.

* **04-Atomicité-et-Idempotence.ipynb**
  Concepts, motifs pratiques (tmp → `os.replace`, upsert DB, manifest/ready), tests d’idempotence, exemples simples en Python.

* **05-Secrets et Variables d'environnement.ipynb**
  Gestion sécurisée des secrets, `python-dotenv`, `.env.example`, bonnes pratiques pour dev vs prod, intégration avec vault/kubernetes secrets.

* **06-Packaging-avec-uv.ipynb**
  Utiliser `uv` pour gérer l'environnement et les dépendances, commandes usuelles (`uv install`, `uv run`), lockfile et reproducibility.


# Mini-projet d’exemple — organisation & rôle pédagogique

Ce mini-projet sert d’illustration pratique : il rassemble plusieurs bonnes pratiques vues dans les notebooks (typing, logging, atomicité, idempotence, `.env`, tests simples).

Arborescence (extrait) :

```
├── notebooks/
│   ├── 01-Syntaxe et Variables.ipynb
│   ├── 02-Logging en Python.ipynb
│   └── ...
├── scripts/
│   └── taxi_pipeline.py
├── src/
│   └── taxi_pipeline/
│       ├── __init__.py
│       ├── duckdb_utils.py     # helpers DuckDB (création tables, import csv/parquet)
│       ├── get_data.py         # téléchargement atomique / idempotent
│       ├── loggins.py         # configuration du logging (console + fichier)
│       ├── save_data.py        # lecture CSV, sauvegarde parquet atomique
│       └── transform_data.py   # fonctions pures de transformation (typées)
├── .env                      # (local) paramètres (ne pas committer)
├── main.py                   # script d'orchestration simple
├── pyproject.toml
└── uv.lock
```

**Objectif du mini-pipeline (exemple)**

* Télécharger un CSV (atomique) → `data/`
* Charger avec `pandas` et transformer (noms colonnes, dedup)
* Sauvegarder en Parquet (écriture atomique)
* Enregistrer quelques métriques dans DuckDB
* Générer un graphique HTML (Plotly)

> Remarque : le mini-projet est un *exemple* pour appliquer les patterns avancés — l’essentiel du TP reste l’apprentissage des concepts Python avancés.


# Installation & exécution (rapide)

## Prérequis

* Python ≥ 3.10
* `uv` (recommandé) ou `venv` + `pip`

## Avec `uv`

```bash
# depuis la racine du repo
uv install            # installe les dépendances à partir du lockfile
uv run python main.py # lance l'orchestrateur (exemple)
```

## Alternative (venv + pip)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt   # si fourni
python main.py
```

## Variables d’environnement

Copier `.env.example` → `.env` et compléter si nécessaire. Exemple minimal :

```
DUCKDB_DATABASE=data/nyc.duckdb
CSV_URL=https://.../taxi_zones.csv
LOG_DIR=logs
```

Le code lit automatiquement ces variables via `python-dotenv`.