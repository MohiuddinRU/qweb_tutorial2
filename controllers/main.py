# -*- coding: utf-8 -*-

from odoo import http
from odoo.tools import html_escape, html_sanitize
from markupsafe import Markup


class QwebTutorials(http.Controller):
    @http.route('/test', type='http', auth='public', website=True)
    def qweb_tutorials(self):
        return http.request.render("qweb_tutorial.somePythonTemplate")
