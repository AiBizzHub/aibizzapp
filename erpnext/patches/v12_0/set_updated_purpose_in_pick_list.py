# Copyright (c) 2019, AiBizzApp and Contributors
# License: GNU General Public License v3. See license.txt


import frappe


def execute():
	frappe.reload_doc("stock", "doctype", "pick_list")
	frappe.db.sql(
		"""UPDATE `tabPick List` set purpose = 'Delivery'
        WHERE docstatus = 1  and purpose = 'Delivery against Sales Order' """
	)