[![Build Status](https://travis-ci.com/sendador/w-app.svg?branch=master)](https://travis-ci.com/sendador/w-app)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a9c38df5b8e54a6b93f03826cb6401e5)](https://www.codacy.com/manual/sendador/w-app?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sendador/w-app&amp;utm_campaign=Badge_Grade)
[![codecov](https://codecov.io/gh/sendador/w-app/branch/codecov_setup/graph/badge.svg)](https://codecov.io/gh/sendador/w-app)
# w-app
Weather app using Django. You can follow the weather from as many cities as you like.
Followed cities are assigned to the account.
# Technologies
- Python
- Django
- Unit tests using pytest on models, urls, views
- Coverage and codecov to improve test across the app
- Selenium for functional tests
- Django-environ for environmental variables
- Codacy for automate code reviews and monitors code quality
- Travis CI for continuous integration service used to build and test
- Docker for easy build

# Docker build

Just clone repo
<pre>git clone https://github.com/sendador/w-app.git</pre>
and then use docker-composer
<pre>docker-compose up</pre>
Your app will be on:
<pre>localhost:8000</pre>
# Manual Installation:

You can get repository from git by:

<pre>git clone https://github.com/sendador/w-app.git</pre>

It's good to use code in virtual environment. For that you can use virtualenv:

<pre>pip install virtualenv</pre>
Then you can create your virtualenv

<pre>virtualenv venv</pre>

Next activate virtual environment.
For Windows Powershell:

<pre>*virtualenv dir*\Scripts\activate.ps1</pre>
or Windows command

<pre>*virtualenv dir*\Scripts\activate.bat</pre>

and install other dependency

<pre>pip install -r requirements.txt</pre>

# Usage

First you have to migrate new database:

<pre>python manage.py makemigrations</pre>

and then use:

<pre>python manage.py migrate</pre>

Your database is ready to go! Now you can run the server:

<pre>python manage.py runserver</pre>

Your website will be on:

<pre>http://127.0.0.1:8000/
</pre>

and then create account and add some cities! Have fun!

