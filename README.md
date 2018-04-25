# django-variable-settings

A simple django application to manage dynamic settings saved in database using namespaced keys and json string values.

## Demo

To try it now, download this repo and use docker-compose to run it

    git clone git@github.com:jperelli/django-variable-settings.git
    cd django-variable-settings
    docker-compose up

Then go to http://localhost:8080/admin and login with user `admin` and password `admin`, you should see the Settings. If you add a settings, it should be a json object. So a string should be saved with double quotes around it.

It can be tested from django shell also easily. Go to another console while `docker-compose up` is running and type

    docker-compose exec django ./manage.py shell
    >>> import variable_settings
    >>> variable_settings.set('evergreenstreet', 123)
    >>> variable_settings.set('address.evergreenstreet', 123)
    >>> variable_settings.set('address.evergreenavenue', 'first')
    >>> variable_settings.get('evergreenstreet')
    123
    >>> variable_settings.get('address.evergreenavenue')
    u'first'
    >>> variable_settings.get('address.*')
    {u'address.evergreenavenue': u'first', u'address.evergreenstreet': 123}
    >>> variable_settings.all()
    {u'address.evergreenavenue': u'first', u'evergreenstreet': 123, u'address.evergreenstreet': 123}

## Installation

    pip install django-variable-settings

In settings.py add

    variable_settings

Then run migrations

    manage.py migrate variable_settings

Then use it as in the Demo

## Settings and custom command

If you want to add some default settings to the database then you can add something like this to `settings.py`

    # default django_variable_settings
    # use ./manage.py variable_settings_initialize
    # If overwrite=False(default) they are not applied if already exist in database
    VARIABLE_SETTINGS = [
        #[ key , value (, overwrite) ]
        ['alerting.connection', '127.0.0.1', False],
        ['alerting.warning', 123, False],
        ['wrong_permissions.enabled', True, True],
    ]

Use custom command `./manage.py variable_settings_initialize` to save those in database. The command only overwrites the variable value if the last parameter is set to true

## Caching

WIP

# Authors

 - Julian Perelli
 - Maxi Padulo

# LICENSE

MIT
