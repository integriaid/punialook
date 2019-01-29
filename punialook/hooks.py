# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "punialook"
app_title = "Punia Look"
app_publisher = "Punia"
app_description = "Custom look for Punia Online"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "dev@punia.online"
app_license = "MIT"

hide_in_installer = True

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/css/punialook.min.css"
app_include_js = [
	"/assets/punialook/js/punialook.js"
	# "/assets/punialook/js/modules.js"
]

# include js, css files in header of web template
web_include_css = "/assets/css/punialook-web.min.css"
web_include_js = "/assets/punialook/js/punialook.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "desk"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "punialook.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "punialook.install.before_install"
# after_install = "punialook.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "punialook.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"punialook.tasks.all"
# 	],
# 	"daily": [
# 		"punialook.tasks.daily"
# 	],
# 	"hourly": [
# 		"punialook.tasks.hourly"
# 	],
# 	"weekly": [
# 		"punialook.tasks.weekly"
# 	]
# 	"monthly": [
# 		"punialook.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "punialook.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "punialook.event.get_events"
# }

# punia images
website_context = {
	"favicon": "/assets/punialook/img/logo-ico.png",
	"email_brand_image": "assets/punialook/img/punia-logo.png",
	"splash_image": "assets/punialook/img/online-store.png",
	"company_logo": "assets/punialook/img/p-logo.png"
}

update_website_context = "punialook.punia_look.website_context.update_website_context"

default_mail_footer = """
	<span>
		Sent via
		<a class="text-muted" href="https://punia.online?source=via_email_footer" target="_blank">
			Punia Online
		</a>
	</span>
"""
