ModelAdmin options
==================

This document enlists all configuration options available for ``ModelAdmin`` class.

Sample models
-------------

Let's define some sample models which we'll use in code examples throughout this
document.

These models are pseudo-code.

.. code-block:: python
    
    # sample models

    class Author(Model):
        name = CharField


    class Book(Model):
        title = CharField
        authors = ManyToManyField(to=Author)
        price = IntField


``ModelAdmin.exclude``
----------------------

A list of fields to exclude from the admin form page.

.. code-block:: python

    class BookAdmin(ModelAdmin):
        exclude = ['price']

``ModelAdmin.prefetch_fields``
------------------------------

Most async database ORMs don't fetch relations of a given object unless explicitly
asked. This can be undesirable in certain cases such as when you want to display
the values from a related field.

For those cases, you can set ``prefetch_fields`` attribute on your admin class.
It is list of names of the related fields (foreignkey, many2many, etc) which you
want to load along with the main object.

.. code-block:: python

    class BookAdmin(ModelAdmin):
        prefetch_fields = ['authors']


``ModelAdmin.list_headers``
---------------------------

A list specifying the columns to display in the table on the list page.

The values in the list can be one of the following:

- Name of a database field in the model
- Name of a method on the model class
- Name of a method on the admin class
- A callable object

**Example 1**: Name of a database field in the model:

.. code-block:: python

    class BookAdmin(ModelAdmin):
        list_headers = ['title', 'price']


You can change the display name of the columns:

.. code-block:: python

    class BookAdmin(ModelAdmin):
        list_headers = [('title', 'Book title'), 'price']


**Example 2**: Name of a method on the model class:

.. code-block:: python

    class Author(Model):
        name = CharField
        age = IntegerField

        def is_older_than_50(self):
            return self.age > 50


    class AuthorAdmin(ModelAdmin):
        list_display = ['name', 'is_older_than_50']


**Example 3**: Name of a method on the admin class:

.. code-block:: python

    class AuthorAdmin(ModelAdmin):
        list_headers = ['uppercase_name']

        def is_older_than_50(self, obj):
            """The 'obj' parameter will be an instance of the model class"""
            return obj.age > 50


**Example 4**: A callable object:

.. code-block:: python

    def is_older_than_50(obj):
        return obj.age > 50


    class AuthorAdmin(ModelAdmin):
        list_headers = [is_older_than_50] # Pass the function object directly
