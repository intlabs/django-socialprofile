# You must have virtualenv installed, and the virualenv command in your path for this to work.
# Assuming you have python installed, you can install virtualenv using the command below.
# curl -O https://raw.github.com/pypa/virtualenv/master/virtualenv.py

virtualenv socialprofile-env
. socialprofile-env/bin/activate
pip install -r socialprofile/requirements.txt