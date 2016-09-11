# Eventex

Sistema de eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5.
3. Ative seu virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env.
6. Execute os testes.

```console
git clone git@github.com/josethomazini/eventex.git wttd
cd wttd
mkvirtualenv -p /usr/bin/python3.5 wttd
workon wttd
pip install -r requerements.txt
cp contrib/env-sample .env
./manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no Heroku.
2. Envie as configurações para o Heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False.
5. Configure o serviço de email.
6. Envie o código para o Heroku.

```console
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
heroku login
heroku apps:create minhainstancia
heroku plugins:install heroku-config
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```

## Curso Welcome to the Django deployado em:

https://eventex-josethomazini.herokuapp.com/
