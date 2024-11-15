# Copyright (c) 2015, AiBizzHub, LLC and Contributors and contributors
# For license information, please see license.txt


from frappe.model.document import Document


class ItemVariant(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		item_attribute: DF.Link
		item_attribute_value: DF.Data
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
	# end: auto-generated types

	pass
