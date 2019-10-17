a tiny CMS project 🐭
=====================

A bare minimum example of a CMS project, documenting some core functions of [onespacemedia-cms](https://github.com/onespacemedia/cms) and demonstrating how to be friends with the CMS's helper models and admin classes. This is probably the most absurdly highly-commented code you will ever read; it's intended as a crash-course in building sites with our CMS.

This is operating in tandem with an upcoming total rewrite of the CMS's documentation.

Suggested reading order:

* This list
* `settings/base.py` for CMS-specific settings
* `tiny_project/apps/news/models.py` for how to create page content models & the most useful helper classes
* `tiny_project/apps/news/admin.py` for how to register such things
* `tiny_project/apps/news/views.py` to use RequestPageManager for fun and profit
* `tiny_project/apps/content/models.py` for an example of inline models on page content models
* `tiny_project/apps/content/admin.py` immediately after that, for how to actually register them
* `templates/base.html`
