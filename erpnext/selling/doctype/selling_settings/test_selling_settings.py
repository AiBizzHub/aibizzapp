# Copyright (c) 2019, AiBizzHub, LLC and Contributors
# See license.txt
import unittest

import frappe
from frappe.tests import IntegrationTestCase


class TestSellingSettings(IntegrationTestCase):
	def test_defaults_populated(self):
		# Setup default values are not populated on migrate, this test checks
		# if setup was completed correctly
		default = frappe.db.get_single_value("Selling Settings", "maintain_same_rate_action")
		self.assertEqual("Stop", default)
