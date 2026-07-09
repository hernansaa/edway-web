# Edway — Marketing Website

Static marketing site for [Edway](https://edway.io) CRM.

## Quick start

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cd src && python manage.py runserver
```

## Tailwind CSS (no Node required)

Build uses the standalone CLI binary at `src/static/tailwindcss`.

```bash
./src/static/tailwindcss -i tailwind.input.css -o src/static/css/tailwind.css --minify
```

Watch mode:
```bash
./src/static/tailwindcss -i tailwind.input.css -o src/static/css/tailwind.css --watch
```

## Deploy to Railway

Railway auto-detects Django via `manage.py` and `Procfile`. No additional config needed.

Set these environment variables in Railway:

| Variable | Value |
|---|---|
| `SECRET_KEY` | A random string (generate with `openssl rand -hex 32`) |
| `DEBUG` | `0` |
| `ALLOWED_HOSTS` | `.railway.app,yourdomain.com` |
| `CSRF_TRUSTED_ORIGINS` | `https://*.railway.app,https://yourdomain.com` |

Optional for email in production:
| Variable | Value |
|---|---|
| `EMAIL_BACKEND` | `django.core.mail.backends.smtp.EmailBackend` |
| `EMAIL_HOST` + `EMAIL_PORT` + credentials | Your SMTP server |
