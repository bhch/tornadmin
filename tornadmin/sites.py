import copy


class AdminSite:
    """The class is responsible for generating the admin site."""
    def __init__(self, base_url, **kwargs):
        self.base_url = base_url
        self.site_name = kwargs.get('site_name', 'Tornadmin')
        self.authenticate = kwargs.get('authenticate')
        self.login = kwargs.get('login')
        self.logout = kwargs.get('logout')

        self._registry = {}

    @classmethod
    def get_registry_key(cls, model_admin):
        """Returns the key used in self._registry dict for the given model"""
        return '.'.join([model_admin.app_slug, model_admin.slug]).strip('.')

    def register(self, model_admin):
        key = self.get_registry_key(model_admin)

        if key in self._registry:
            return

        self._registry[key] = model_admin

    def get_registry(self):
        return copy.deepcopy(self._registry)

    def get_registered(self, app_slug, model_slug):
        key = '.'.join([app_slug, model_slug]).strip('.')
        return self._registry.get(key, (None, None))
