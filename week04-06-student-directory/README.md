# Weeks 4–6 — Student directory

One Django project combining the weekly steps: ORM models and relationships, student and module pages, template inheritance, static CSS, pagination, model editing, and GET filters. It is a compact sample dataset rather than the lecture's 1,000-row dataset.

## Run it

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py makemigrations directory
python manage.py migrate
python manage.py load_sample_data
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. The admin is at `/admin/`; create a superuser with `python manage.py createsuperuser` if needed. Student editing includes image uploads under `media/`.
