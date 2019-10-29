from setuptools import setup


setup(
    name="ouihelp_ec2_box_init",
    version="0.0.1.dev0",
    entry_points={
        "console_scripts": ["ec2-box-init=ec2_box_init:ec2_box_init"],
    },
    py_modules=["ec2_box_init"],
    author="Bastien Gandouet",
    author_email="bastien@ouihelp.fr",
    install_requires=[
       "click==6.7",
       "requests==2.20.0",
    ],
)
