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
        discount = IntField


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


``ModelAdmin.order_by``
-----------------------

A list of tuples providing the options for ordering (sorting) the items on list page.

Each tuple looks like this: ``('Display name of option', 'value of the option')``

.. code-block:: python

    class BookAdmin(ModelAdmin):
        order_by = [
            # (<display name>, <value>)
            ('Title (A-Z)', 'title'),
            ('Title (Z-A)', '-title'),
            ('Price (ascending)', 'price'),
            ('Price (descending)', '-price'),
        ]

The ``value`` of the option is passed directly to the datbase ORM's ordering function
(such as Tortoise ORM's ``.order_by()`` method. So, when a user selects an option,
the query will look like this: ``Book.all().order_by('-price')``).

``ModelAdmin.filters``
----------------------

A list of dicts providing the options for filtering the items on the list page.

Each filter is a python dictionary with the following keys:

============ ===========
Key          Description
============ ===========
``name``     Name of the filter (``str``)
``label``    Optional display name of the filter (``str``).

             If not provided, the value of ``name`` key is used.
``type``     Type of the filter. Supports two types: ``'radio'`` and ``'checkbox'``.
``options``  A list of tuples in this format: ``('<display name>', '<value>')``.
============ ===========

A ``checkbox`` filter can have more than one values selected by the user. So, on 
the server, it's values will be inside a list. Whereas a ``radio`` filter can have 
only one value and, so, on the server side it will a standalone value (not inside a list).

You're responsible for writing the filtering logic yourself using a method called
``get_filtered_results()``:

.. code-block:: python

    class BookAdmin(ModelAdmin):
        filters = [
            {
                'name': 'on_sale',
                'type': 'radio',
                'options': [
                    ('Any', ''),
                    ('Yes', True),
                    ('No', False)
                ]
            }
        ]

        def get_filtered_results(self, queryset, filters):
            on_sale = fitlers.get('on_sale')

            if on_sale == True:
                # only show books with discount
                return queryset.filter(discount__gte=0)
            elif on_sale == False:
                # only show books without discount
                return queryset.filter(discount=0)

            return queryset


``ModelAdmin.actions``
----------------------

List specifying the actions for the list page.

By default we provide a **"Delete selected"** action.

Defining a basic action:

.. code-block:: python

    from tornadmin.decorators import action
    from tornadmin.utils.text import pluralize


    class BookAdmin(ModelAdmin):
        action = ['remove_discount']

        @action(label='Remove discount')
        async def remove_discount(self, request_handler, queryset):
            count = await queryset.count()

            if count: # queryset is not empty
                await queryset.update(discount=0) # set discount to zero

                # show a success message to the user
                request_handler.flash(
                    'success', 
                    'Successfully removed discount from %s %s' 
                    % (count, pluralize('book', 'books', count))
                )

The ``@action`` decorator takes these keyword arguments:

``label`` (``str``)
     Optional display name of the action.

``new_tab`` (``bool``)
    If ``True``, the action will run on a new browser tab. Default ``False``.

``require_selection`` (``bool``)
    If ``True``, the action will only run when a user selects items on the list page.
    Set this to ``False`` if you want to run a an action without requiring selection.
    Default ``True``.

``require_confirmation`` (``bool``)
    If ``True``, a confirmation modal will be shown to user before running the action.
    Default ``False``.

``modal_title`` (``str``)
    Optional title for the confirmation modal. Defaults to the value of ``label``.

``modal_body`` (``str``)
    Optional body text for the confirmation modal. Defaults to the value of ``modal_title`` or ``label``.

``modal_button_label`` (``str``)
    Optional label for the confirmation button. Defaults to the value of ``label``.

``modal_button_class`` (``str``)
    Optional CSS class for the confirmation button. You can set this value to any
    button class provided by Bootstrap without the ``btn-`` prefix.
    Default ``primary``.
