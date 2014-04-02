flask-api-talk
==============

This is a first draft of an introductory talk on implementing APIs with Flask

The talk introduces Flask via a single module application and then discusses common API concerns
and shows how one might go about dealing with those in a larger application.


Get Started with Examples
-------------------------

Setup a new virtualenv with the appropriate dependencies

```bash
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt 
```

Fire up the IPython notebook if you'd like to interact with the APIs using it

```bash
$ ipython notebook
```

Run the single module example with the Flask dev server

```bash
$ cd single-module
$ python happy_birthday.py
```

Run the classy API example using gunicorn via the included Procfile 

```bash
$ cd classy-api
$ honcho start
```
