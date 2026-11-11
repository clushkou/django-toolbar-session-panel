from collections import OrderedDict
from debug_toolbar.panels import Panel
from django.utils.translation import gettext_lazy as _

class SessionDebugPanel(Panel):
    """
    Panel that displays session content
    """
    name = 'Session'
    template = 'debug_toolbar_session_panel/panel.html'
    has_content = True

    def nav_title(self):
        return _('Session')

    def title(self):
        return self.nav_title()

    def process_request(self, request):
        data = {'session':{
            'info': OrderedDict([
                ('session_key',request.session.session_key),
                ('modified', request.session.modified),
                ('accessed', request.session.accessed)
                ]),
            'data': dict(request.session.items())
        }}
        self.record_stats(data)
        return self.get_response(request)
