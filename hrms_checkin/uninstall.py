from hrms_checkin.setup import before_uninstall as remove_custom_fields
import click

def before_uninstall():
	try:
		print("Removing customizations created by the Hrms Checkin...")
		remove_custom_fields()

	except Exception as e:
		BUG_REPORT_EMAIL = "info@fusionsofttech.co.in"
		click.secho(
			"Removing Customizations for Hrms Checkin failed due to an error."
			" Please try again or"
			f" report the issue on {BUG_REPORT_EMAIL} if not resolved.",
			fg="bright_red",
		)
		raise e
	
	click.secho("Hrms Checkin app customizations have been removed successfully...", fg="green")
    
    