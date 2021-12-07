Registering models
==================

You can register your database models in the admin site and Tornadmin will 
auto generate these three pages for your models:

1. A list page which will list all the objects in your model.
2. A create page which will have a form for creating new objects.
3. An edit page which will have a form for editing existing objects.

Available backends
------------------

Tornadmin aims to support multiple database ORMs. Presently, the following
ORMs are supported:

- ``tornadmin.backends.tortoise``: `Tortoise-ORM <https://github.com/tortoise/tortoise-orm/>`_.

To register your models in the admin site, you need to create a subclass of the
``ModelAdmin`` class provided by the db backend.

Basic usage
-----------

Let's assume we've a Tortoise-ORM model called ``User`` which looks like this:

.. code-block:: python

    # models

    from tortoise.models import Model
    from tortoise import fields


    class User(Model):.
        id = fields.IntField(pk=True)
        username = fields.CharField(max_length=150, index=True, unique=True)
        email = fields.CharField(max_length=128, index=True, unique=True)

        first_name = fields.CharField(max_length=32, default='')
        last_name = fields.CharField(max_length=32, default='')

        is_verified = fields.BooleanField(default=False)

        def get_full_name(self):
            return '%s %s' % (self.first_name, self.last_name)

And this is how we'll register this model in the admin site:

.. code-block:: python

    from tornadmin import BaseAdminSite
    from tornadmin.backends.tortoise import ModelAdmin

    from my_models import User


    class AdminSite(BaseAdminSite):
        pass

    admin_site = AdminSite(base_url='/admin')


    class UserAdmin(ModelAdmin):
        pass


    # pass an instance of ModelAdmin
    # to admin site's register method
    admin_site.register(UserAdmin(model=User, app='Auth'))


What's an App?
--------------

The concept of Apps (applications) is inspired by Django. This provides a way
for you to organize similar models under a single app.

Example:

- App: **Blog**

    - ``Articles``
    - ``Authors``
    - ``Comments``

- App: **Shop**

    - ``Products``
    - ``Categories``
    - ``Orders``


Configuration
-------------

See :doc:`ModelAdmin options <modeladmin>` document for details about configuring
the admin pages for a model.