ITHACA website
=======================

This website is based on Wagtail CMS.

### Documentation

[docs.wagtail.io](http://docs.wagtail.io/) is the full reference for Wagtail, and includes guides for developers, designers and editors, alongside release notes and the product roadmap.

# Installation
You can install this website in an isolated python environment. For instance:
```
virtualenv -p /usr/bin/python3 wagtail
cd wagtail
. bin/activate
```
Then run the following commands:
```
git clone https://github.com/ITHACA-org/wagtail-ithaca.git
cd wagtail-ithaca
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 
```
