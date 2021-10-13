class BaseModelAdmin:
    list_headers = []
    items_per_page = 20
    fields = []
    exclude = []
    prefetch_fields = []
    readonly_fields = []

    def __init__(self, *args, **kwargs):
        raise NotImplementedError('Implement in subclass')

    def get_list_headers(self):
        raise NotImplementedError('Implement in subclass')

    async def get_list(self, request_handler, page_num, per_page):
        raise NotImplementedError('Implement in subclass')

    async def get_object(self, request, id):
        raise NotImplementedError('Implement in subclass')

    async def get_form_data(self, obj):
        raise NotImplementedError('Implement in subclass')

    def get_form(self, request_handler):
        raise NotImplementedError('Implement in subclass')

    async def save_model(self, request_handler, form, obj=None):
        raise NotImplementedError('Implement in subclass')

    def get_absolute_url(self, request_handler, obj):
        return None
