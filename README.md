# wttd

Curso Welcome to the Django
---

Deploy em:
---

https://eventex-josethomazini.herokuapp.com/


Heroku
---

wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
heroku login
heroku apps:create eventex-josethomazini
heroku plugins:install heroku-config
heroku config:push
git push heroku master --force
