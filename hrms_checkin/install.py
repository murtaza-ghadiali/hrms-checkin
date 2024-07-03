from hrms_checkin.setup import after_install as setup
import click

def after_install():
	try:
		print("Setting up Hrms Checkin...")
		setup()

		click.secho("Thank you for installing Hrms Checkin!", fg="green")

	except Exception as e:
		BUG_REPORT_EMAIL = "info@fusionsofttech.co.in"
		click.secho(
			"Installation for Hrms Checkin app failed due to an error."
			" Please try re-installing the app or"
			f" report the issue on {BUG_REPORT_EMAIL} if not resolved.",
			fg="bright_red",
		)
		raise e