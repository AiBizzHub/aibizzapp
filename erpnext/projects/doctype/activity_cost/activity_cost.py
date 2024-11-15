# Copyright (c) 2015, AiBizzHub, LLC and Contributors and contributors
# For license information, please see license.txt


import frappe
from frappe import _
from frappe.model.document import Document


class DuplicationError(frappe.ValidationError):
	pass


class ActivityCost(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		activity_type: DF.Link
		billing_rate: DF.Currency
		costing_rate: DF.Currency
		department: DF.Link | None
		employee: DF.Link | None
		employee_name: DF.Data | None
		title: DF.Data | None
	# end: auto-generated types

	def validate(self):
		self.set_title()
		self.check_unique()

	def set_title(self):
		if self.employee:
			if not self.employee_name:
				self.employee_name = frappe.db.get_value("Employee", self.employee, "employee_name")
			self.title = _("{0} for {1}").format(self.employee_name, self.activity_type)
		else:
			self.title = self.activity_type

	def check_unique(self):
		if self.employee:
			if frappe.db.sql(
				"""select name from `tabActivity Cost` where employee_name= %s and activity_type= %s and name != %s""",
				(self.employee_name, self.activity_type, self.name),
			):
				frappe.throw(
					_("Activity Cost exists for Employee {0} against Activity Type - {1}").format(
						self.employee, self.activity_type
					),
					DuplicationError,
				)
		else:
			if frappe.db.sql(
				"""select name from `tabActivity Cost` where ifnull(employee, '')='' and activity_type= %s and name != %s""",
				(self.activity_type, self.name),
			):
				frappe.throw(
					_("Default Activity Cost exists for Activity Type - {0}").format(self.activity_type),
					DuplicationError,
				)