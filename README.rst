weather
=======

CLI for getting the temperature of cities in the world

Preparing for Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone repository: ``git clone git@github.com:edwardpius/weather``
3. ``cd`` into the repository.
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``


Usage
-----

Pass in a city name and optionally a country code (defaults to US)

US City example:

::

    $ weather seattle


International City example:

::

    $ weather munich --country germany


Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn't active then use:

::

    $ pipenv run make
