# Copyright (c) 2019, AiBizzHub, LLC and Contributors
# See license.txt
import unittest

import frappe
from frappe.tests import IntegrationTestCase


class TestIssuePriority(IntegrationTestCase):
	def test_priorities(self):
		make_priorities()
		priorities = frappe.get_list("Issue Priority")

		for priority in priorities:
			self.assertIn(priority.name, ["Low", "Medium", "High"])


def make_priorities():
	insert_priority("Low")
	insert_priority("Medium")
	insert_priority("High")


def insert_priority(name):
	if not frappe.db.exists("Issue Priority", name):
		frappe.get_doc({"doctype": "Issue Priority", "name": name}).insert(ignore_permissions=True)