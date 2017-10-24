# EC2 Box Init

## A sample user data script

```
#!/bin/bash
apt install -y --no-install-recommends python python-pip
pip install virtualenv
export PATH=/root/.local/bin:$PATH
curl https://raw.githubusercontent.com/mitsuhiko/pipsi/master/get-pipsi.py | python
pipsi install https://github.com/ouihelp/ec2-box-init/archive/master.zip#egg=ouihelp_ec2_box_init
ec2-box-init <URL_TO_THE_FILE>
```
