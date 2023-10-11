# G3D

Site Institucional

## Este projeto foi feito com:

* [Python 3.10.6](https://www.python.org/)
* [Django 4.2.6](https://www.djangoproject.com/)
* [AlpineJS](https://alpinejs.dev/)
* [htmx](https://htmx.org)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/alexlambertini/G3D.git
cd G3D

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python contrib/env_gen.py

python manage.py migrate
python manage.py createsuperuser
```