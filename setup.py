from setuptools import setup


setup(
    name="ouihelp_ec2_box_init",
    version="0.0.1",
    entry_points={"console_scripts": ["ec2-box-init=ec2_box_init:ec2_box_init"],},
    py_modules=["ec2_box_init"],
    author="Bastien Gandouet",
    author_email="bastien@ouihelp.fr",
    install_requires=["click==7.0", "requests==2.23.0",],
)
