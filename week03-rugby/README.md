# Week 3 — Rugby roster

This Django project completes the Week 3 ToDo: teams have players, players can have several positions, positions can be assigned to several players, and the data can be managed in Django admin. Positions marked specialist require an explicit safe-play confirmation when assigning a player. A CSV loader is included.

## Run it

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py makemigrations rugby
python manage.py migrate
python manage.py load_rugby_data
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/admin/`. The sample CSV is `rugby/data/players.csv`.
