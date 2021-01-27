# Anmie-Recommender-System

This project uses Angular, FLask Python and SQLite to create a user friendly anime website.

## Run Angular frontend
cd anime-app
npm install
ng serve

## Run flask backend
cd flask_backend

### Create environment
python -m venv anime_env

### Activate Environment
Windows: anime_env\Scripts\activate 
Mac/Linux: source anime_env_linux/bin/activate

### Install Packages
pipenv install -r requirements.txt

### Run flask backend
python run.py
