a tiny CMS project 🐭
=====================

This is a tiny CMS project which documents some core functions of [onespacemedia-cms](https://github.com/onespacemedia/cms) and demonstrating how to make friends with the CMS's helper models and admin classes. This is probably the most absurdly highly-commented code you will ever read; it's intended as a crash-course in building sites with our CMS.

This is a companion repository for an upcoming total rewrite of the CMS's documentation.

Suggested reading order:

* This list
* `settings/base.py` for CMS-specific settings
* `tiny_project/apps/news/models.py` for how to create page content models & the most useful helper classes
* `tiny_project/apps/news/admin.py` for how to register such things
* `tiny_project/apps/news/views.py` to use RequestPageManager for fun and profit
* `tiny_project/apps/content/models.py` for an example of inline models on page content models
* `tiny_project/apps/content/admin.py` immediately after that, for how to actually register them
* `templates/base.html`

Quickstart:

```
# add your SECRET_KEY herein :)
nano tiny_project/settings/local.py
createdb tiny_project
# A minimum of 3.6 is required. Later versions should work fine, but this is
# what the Ubuntu box this is being written from ships with by default. :)
virtualenv -p python3.6 .venv
. .venv/bin/activate
pip install -r requirements.txt
./manage.py runserver
```
