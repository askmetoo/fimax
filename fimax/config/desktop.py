# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	from fimax.install import update_erpnext_icons
	
	# update the icons for erpnext on every migration
	update_erpnext_icons()

	icons = [
		{
			"module_name": "Control Panel",
			"_doctype": "Control Panel",
			"color": "#009688",
			"icon": "fa fa-cog",
			"type": "link",
			"link": "Form/Control Panel"
		}, 
		{
			"module_name": "Loan Application",
			"_doctype": "Loan Application",
			"color": "#009688",
			"icon": "fa fa-check-square-o",
			"type": "link",
			"link": "List/Loan Application/List"
		}, 
		{
			"module_name": "Loan",
			"_doctype": "Loan",
			"color": "#ffc107",
			"icon": "fa fa-credit-card" ,
			"type": "link",
			"link": "List/Loan/List"
		}, 
		{
			"module_name": "Amortization Tool",
			"_doctype": "Amortization Tool",
			"color": "#ff5722",
			"icon": "fa fa-fire" ,
			"type": "link",
			"link": "Form/Amortization Tool"
		}, 
		{
			"module_name": "Insurance Card",
			"_doctype": "Insurance Card",
			"color": "#607d8b",
			"icon": "fa fa-id-card-o" ,
			"type": "link",
			"link": "List/Insurance Card/List"
		},
		{
			"module_name": "Loan Charges",
			"_doctype": "Loan Charges",
			"color": "#9e9e9e",
			"icon": "fa fa-list-alt" ,
			"type": "link",
			"link": "List/Loan Charges/List"
		}, 
		{
			"module_name": "GPS Installation",
			"_doctype": "GPS Installation",
			"color": "#607d8b",
			"icon": "fa fa-globe" ,
			"type": "link",
			"link": "List/GPS Installation/List"
		}, 
		{
			"module_name": "Car",
			"_doctype": "Car",
			"color": "#3f51b5",
			"icon": "fa fa-car" ,
			"type": "link",
			"link": "List/Car/List"
		}, 
		{
			"module_name": "Property",
			"_doctype": "Property",
			"color": "#4caf50",
			"icon": "fa fa-home" ,
			"type": "link",
			"link": "List/Property/List"
		}, 
		{
			"module_name": "Income Receipt Express",
			"label": "Payment Express",
			"_doctype": "Income Receipt Express",
			"color": "#4caf50",
			"icon": "fa fa-paper-plane" ,
			"type": "link",
			"link": "List/Income Receipt Express/List"
		}, 
		{
			"module_name": "Income Receipt",
			"_doctype": "Income Receipt",
			"color": "#9e9e9e",
			"icon": "fa fa-money" ,
			"type": "link",
			"link": "List/Income Receipt/List"
		},
	]

	return icons