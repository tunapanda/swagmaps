# Swagmap Viewer

## What is it?
A [Django](http://django.readthedocs.org/en/latest/) app to host Tunapanda's [swag](https://github.com/tunapanda/swag/blob/master/Readme.md) system (tracked separately in the  [swagmap](https://github.com/tunapanda/swagmap) repo and incorporated as a submodule-- be sure to follow the setup instructions below!).

## How do I use it?
1. Clone this repo
1. `cd $clone_dir`
1. Get its submodules:
  1. `git submodule update --init`
1. Install prerequisites:
  1. `sudo pip install -r requirements.txt`  *# or set up a [virtualenv](https://virtualenv.pypa.io/en/latest/) and you won't need to use `sudo`*

Now you have a few options for how to deploy Swag:

1. **Standalone Django test server** *(recommended for testing)*
  1. *(optional)* `./manage.py syncdb`
  1. `./manage.py runserver`
  1. Open the url provided by the last command in a browser
1. **WSGI application in Apache httpd** *(recommended for production)*
  1. `Use swag_devsite/wsgi.py` with [Django's wsgi setup instructions](https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/modwsgi/)
    * See [here](https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/) for other deployment options
1. **App in an existing Django site**
  1. `cd $clone_dir`
  1. `sudo pip install .` (or `sudo pip install -e .` if you plan on editing any code)
  1. Add Swag to your site like any other app:
    1. Add "swag" to `INSTALLED_APPS` in your site's `settings.py`
    1. `./manage.py syncdb`
    1. `./manage.py collectstatic`
    1. ...etc.
1. **Standalone HTML**
  1. You'll lose all the Django stuff, but for a simple test/demo of the node.js component, simply copy `$clone_dir/swag/static/swag` into the documentroot of a webserve and open it in a browser (opening it without a webserver currently does not work). 
  
## How can I help?
  * Take a look at the open issues: [server](https://github.com/tunapanda/swagmap/issues),  [curricula](https://github.com/tunapanda/swagmaps/issues), [general/higher-level](https://github.com/tunapanda/swag/issues)
  * Introduce yourself on the Tunapanda [Discourse forum](discourse.tunapanda.org) and/or [Google group](https://groups.google.com/forum/#!forum/tunapanda) 
  * If you find a problem or have a suggestion, please don't hesitate to use the tools above to start a discussion!
