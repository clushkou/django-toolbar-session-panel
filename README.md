# Session Debug Panel

This panel allow you to query your session after request.

## Install

With pip:

    pip install debug_toolbar_session_panel@git+https://github.com/clushkou/django-toolbar-session-panel.git#egg=debug_toolbar_session_panel

and in settings.py:

    INSTALLED_APPS += (
        'debug_toolbar_session_panel',
    )
    DEBUG_TOOLBAR_PANELS += (
        'debug_toolbar_session_panel.panels.SessionDebugPanel',
    )

