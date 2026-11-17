# Week 7 — HashThat

A Django app based on the worksheet's expected behaviour: enter text, submit it, calculate its SHA-256 digest, store the text and digest, show a result page, and preview the digest while typing.

## Run it

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py makemigrations hashing
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. The live preview uses the same Python SHA-256 function via a small JSON endpoint.
