# Portfolio Website

A Django portfolio website with database-managed projects, admin controls, and a responsive frontend.

## Local Setup

From this directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open the website at `http://127.0.0.1:8000/`.

Open the admin panel at `http://127.0.0.1:8000/admin/`.

## Admin Access

Create or reset an administrator account with:

```powershell
python manage.py createsuperuser
python manage.py changepassword <username>
```

Projects can be managed from **Admin > Portfolios**. Published projects appear on the homepage.

## Production Configuration

Set these environment variables before deployment:

```text
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=<strong-random-secret>
DJANGO_ALLOWED_HOSTS=your-domain.com
DJANGO_SECURE_SSL_REDIRECT=True
DJANGO_SESSION_COOKIE_SECURE=True
DJANGO_CSRF_COOKIE_SECURE=True
```

Then collect static files:

```powershell
python manage.py collectstatic
```

Do not commit `.env`, `db.sqlite3`, `media/`, or `staticfiles/`.
