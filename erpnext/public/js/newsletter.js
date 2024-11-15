// Copyright (c) 2019, AiBizzHub, LLC and Contributors
// License: GNU General Public License v3. See license.txt

frappe.ui.form.on("Newsletter", {
	refresh() {
		erpnext.toggle_naming_series();
	},
});
