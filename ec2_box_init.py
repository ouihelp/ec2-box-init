#!/usr/bin/env python

import os
import subprocess
import sys

import click
import requests


if (sys.version_info.major, sys.version_info.minor) != (2, 7):
    click.secho("Sorry, only Python 2.7 is supported")
    sys.exit(1)


@click.command()
@click.argument("USER_FILE_URL")
def ec2_box_init(user_file_url):
    """Simple internal program that put an EC2 box in a "usable
    state" given the URL of the properly formatted user file.

    """
    r = requests.get(user_file_url)
    if r.status_code != 200:
        click.secho("User file request did not answer 200")
        sys.exit(1)

    users = r.json()

    for user in users:
        username, userkey = user

        subprocess.call(["adduser", "--disabled-password", "--gecos", "", username])
        subprocess.call(["adduser", username, "sudo"])

        home_directory = os.path.join("/home", username)
        ssh_directory = os.path.join(home_directory, ".ssh")
        if not os.path.exists(ssh_directory):
            os.makedirs(ssh_directory)

        with open(os.path.join(ssh_directory, "authorized_keys"), "w") as f:
            f.write(userkey)

        sudoers_file = "91-ec2-box-init-{}".format(username)
        with open(os.path.join("/etc/sudoers.d", sudoers_file), "w") as f:
            f.write("{} ALL=(ALL) NOPASSWD:ALL".format(username))


if __name__ == "__main__":
    ec2_box_init()
