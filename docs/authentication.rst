Authentication
==============

Tornadmin allows you to use your own authentication system.

To implement authentication, you're required to create the following three methods
in your ``AdminSite``:

1. ``login`` (*coroutine*) - For logging in a user.
2. ``authenticate`` (*coroutine*) - For authenticating a user.
3. ``logout`` (*coroutine*) - For logging out a user.


Here's a sample code for implementing authentication using cookies:

.. code-block:: python

    from tornadmin import BaseAdminSite


    class AdminSite(BaseAdminSite):
        async def login(self, handler):
            """This method is responsible for logging a user in.

            You are free to set cookie, create session, issue JWT, or anything
            else in this method.
            """

            username = handler.get_body_argument('username', '')
            password = handler.get_body_argument('password', '')

            # You can put any kind of complex logic in here
            # such as querying database etc.

            # For this example,
            # we will just check hardcoded values
            if username == 'john' and password == 'password':
                handler.set_secure_cookie('user', 'john')
                return True

            return False

        async def authenticate(self, handler):
            """This method is responsible for authenticating the current request.

            If the request is sent by a logged-out user, this method MUST return
            False.

            If the request is send by a logged-in user, this method MUST return
            a dict containing the username of the user. This username will be
            displayed on the admin site.
            """

            # We'll check the 'user' cookie for identifying the current user

            user = handler.get_secure_cookie('user')

            if user:
                return {'username': user}

            return False

        async def logout(self, handler):
            """Method for logging a user out"""

            # We'll delete the 'user' cookie to log the user out

            handler.clear_cookie('user')
            return True
