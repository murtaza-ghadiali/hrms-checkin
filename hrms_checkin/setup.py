
import frappe
from frappe.core.doctype.doctype.doctype import validate_permissions_for_doctype


def before_install():
    pass

def after_install():
    create_custom_doctype()
    add_permissions_to_employee()

def before_uninstall():
    delete_custom_doctype()

def after_uninstall():
    pass



def create_custom_doctype():
    if not frappe.db.exists("DocType", "Hrms Checkin Custom DocType"):
        doc = frappe.get_doc({
            "doctype": "DocType",
            "name": "Hrms Checkin Custom DocType",
            "module": "Hrms Checkin",
            "custom": 1,
            "fields": [
                {"fieldname": "custom_field", "label": "Custom Field", "fieldtype": "Data"}
            ],
            "permissions": [
                {"role": "Employee", "read": 1, "write": 1, "create": 1, "delete": 1}
            ]
        })
        doc.insert()
        frappe.db.commit()

def add_permissions_to_employee():
    doc = frappe.get_doc("DocType", "Hrms Checkin Custom DocType")
    if not any(perm.role == "Employee" for perm in doc.permissions):
        doc.append("permissions", {
            "role": "Employee",
            "read": 1,
            "write": 1,
            "create": 1,
            "delete": 1
        })
        doc.save()
        validate_permissions_for_doctype("Hrms Checkin Custom DocType")
        frappe.db.commit()



def delete_custom_doctype():
    if frappe.db.exists("DocType", "Hrms Checkin Custom DocType"):
        frappe.delete_doc("DocType", "Hrms Checkin Custom DocType", ignore_permissions=True)
        frappe.db.commit()