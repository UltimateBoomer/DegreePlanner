# DegreePlanner backend

## Project setup

Create Python virtual environment
```bash
python -m venv .venv
source .venv/bin/activate # note: choose the right activate script for your shell
pip install -r requirements.txt
```

Setup django and run development server
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
