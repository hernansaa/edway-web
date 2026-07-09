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
