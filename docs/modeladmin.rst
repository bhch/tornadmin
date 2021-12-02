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

.. code-block:: python

    from tornadmin import BaseAdminSite
    from tornadmin.backends.tortoise import ModelAdmin


    class AdminSite(BaseAdminSite):
        pass

    admin_site = AdminSite(base_url='/admin')


    class UserAdmin(ModelAdmin):
        pass


    # pass an instance of ModelAdmin
    # to admin site's register method
    admin_site.register(UserAdmin(model=User, app='Auth'))

