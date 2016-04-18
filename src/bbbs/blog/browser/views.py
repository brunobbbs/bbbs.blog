# -*- coding: utf-8 -*-
from datetime import datetime
from Products.Five.browser import BrowserView


class MyFirstView(BrowserView):
    """My first BrowserView"""

    def date(self):
        return datetime.now().strftime('%d/%m/%Y')
