# EC2 Box Init

## A sample user data script

This scripts works on Ubuntu 18.04 LTS.

```
#!/bin/bash
apt-get update --yes && apt-get --yes install python3-pip python3-venv
python3 -m pip install --user pipx virtualenv
export PATH=/root/.local/bin:$PATH
pipx install https://github.com/ouihelp/ec2-box-init/archive/master.zip
ec2-box-init <URL_TO_THE_FILE>
```
