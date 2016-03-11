Issues?
-------

Issues with the opencivicdata.org API should be filed at the [api.opencivicdata.org issue tracker](https://sunlight.atlassian.net/browse/OCD/component/10001)

All Open Civic Data issues can be browsed and filed at [the Open Civic Data JIRA instance](https://sunlight.atlassian.net/browse/OCD/).

Usage
-----

Instructions assumes that you already have a database populated with scraped
data.

```
mkvirtualenv ocdapi --python=`which python3`
workon ocdapi
export DATABASE_URL=postgis://my-user:@localhost/my-pupa-database
python manage.py migrate
python manage.py runserver
```

Heroku
------

* Requires `make` command. (Run without arguments for task help)
* Requires the [Heroku Toolbelt](https://toolbelt.heroku.com/).
* Assumes the opencivicdata database is [populated][ocd-getting-started] and named `pupa`
  (relates to `Makefile`).

```
workon ocdapi
heroku create myocdapi
heroku buildpacks:set https://github.com/ddollar/heroku-buildpack-multi.git
make heroku-deploy
make heroku-pg-push
```

What is this?
-------------

This repo is essentially just a Django project for deployment- actual API code is a part of several other projects:

* [boundaries](https://github.com/rhymeswithcycle/represent-boundaries) - backs GIS portion
* [imago](https://github.com/opencivicdata/imago) - people, bills, events, etc.

[ocd-getting-started]: http://docs.opencivicdata.org/en/latest/scrape/basics.html#getting-started
