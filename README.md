<div align="center">

<h1>Hrms Checkin</h1>

Simple and easy-to-use employee dashboard for check-in and check-out.

<br><br>
![image](https://github.com/murtaza-ghadiali/hrms-checkin/blob/develop/hrms-checkin-dashboard.png)

</div>

## Introduction

Hrms Checkin streamlines employee attendance management by offering a user-friendly interface where employees can log their attendance with just a click. The application displays essential details such as the employee's name and the last log detail, ensuring transparency and accuracy in attendance records.

It builds on top of [ERPNext](https://github.com/frappe/erpnext), [hrms](https://github.com/frappe/hrms) and the [Frappe Framework](https://github.com/frappe/frappe) - incredible FOSS projects built and maintained by the incredible folks at Frappe. Go check these out if you haven't already!

## Features

-   Includes role-based access, specifically designed for employees. This ensures that each user has access to the features relevant to their role.
-   A straightforward button interface allows employees to easily check in or check out. This minimizes the time required for attendance logging and reduces errors.
-   Each employee's workspace features a card displaying their name and the last log detail
-   The last log detail provides information on the most recent check-in or check-out activity, ensuring employees are aware of their current status.

## Installation

Once you've set up a [Frappe site](https://frappeframework.com/docs/v14/user/en/installation/), [ERPNext](https://github.com/frappe/erpnext#installation) and [hrms](https://github.com/frappe/hrms#installation),  installing Hrms Checkin is simple:

1.  Download the app using the Bench CLI.

    ```bash
    bench get-app --branch [branch name] https://github.com/murtaza-ghadiali/hrms-checkin.git
    ```

Replace `[branch name]` with the branch that you're using for Frappe Framework, ERPNext and hrms.
If it isn't specified, the `--branch` option will default to **develop**.

2.  Install the app on your site.

    ```bash
    bench --site [site name] install-app hrms_checkin
    ```

## License

Hrms Checkin is released under the [MIT License.](https://github.com/murtaza-ghadiali/hrms-checkin/blob/develop/license.txt)
