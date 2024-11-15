# Copyright (c) 2015, AiBizzHub, LLC and Contributors
# See license.txt
import unittest

import frappe
from frappe.tests import IntegrationTestCase


class TestOperation(IntegrationTestCase):
	pass


def make_operation(*args, **kwargs):
	args = args if args else kwargs
	if isinstance(args, tuple):
		args = args[0]

	args = frappe._dict(args)

	if not frappe.db.exists("Operation", args.operation):
		doc = frappe.get_doc(
			{"doctype": "Operation", "name": args.operation, "workstation": args.workstation}
		)
		doc.insert()
		return doc

	return frappe.get_doc("Operation", args.operation)
