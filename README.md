on va écrire un module pour récupérer le fichier depuis : "https://community-engineering-artifacts.s3.us-west-2.amazonaws.com/dagster-university/data/taxi_zones.csv"
l'enregistrer dans data/ en csv
le charger ensuite avec pandas, faire quelques opérations et l'enregistrer en format parquet,
calculer ensuite 2-3 métriques et enregister ca dans une db, duckdb
puis enfin créer un petit graphique .
On va intégrer tout ce dont on a parlé : gestion d'erreur, fichier, idempotence, atomicité, structuration de code, typing, logging et tout.


Donne moi d'aboard une structure / arboresence pour mon module : __init__, get_data, save_data, transform_data, plot_data..... A toii de voir la structure adaptée On va intégrer tout ce dont on a parlé : gestion d'erreur, fichier, idempotence, atomicité, structuration de code, typing, logging et tout. Pour l'instant l'arboressence c'est : # File Tree: training-atut Generated on: 8/14/2025, 2:20:53 PM Root path: /Users/abraham/Desktop/Perso/training-atut
├── 📁 .git/ 🚫 (auto-hidden)
├── 📁 .venv/ 🚫 (auto-hidden)
├── 📁 data/
│   └── 📄 tmp_example.txt
├── 📁 docs/
├── 📁 logs/
├── 📁 notebooks/
│   ├── 📁 logs/
│   │   ├── 📋 dictconfig_pipeline.log 🚫 (auto-hidden)
│   │   └── 📋 pipeline.log 🚫 (auto-hidden)
│   ├── 📓 01-Syntaxe et Variables.ipynb
│   ├── 📓 02-Logging en Python.ipynb
│   ├── 📓 03-Organisation projet.ipynb
│   └── 📓 04-Atomicité-et-Idempotence.ipynb
├── 📁 scripts/
├── 📁 src/
│   └── 📁 taxi_pipeline/
├── 🚫 .gitignore
├── 📄 .python-version 🚫 (auto-hidden)
├── 📖 README.md
├── 🐍 main.py
├── ⚙️ pyproject.toml
└── 🔒 uv.lock