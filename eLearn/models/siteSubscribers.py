from django.db import models

class SiteSubscribers(object):
	"""docstring for SiteSubscribers, collecting subscribers emails"""
	email = models.Emailfield(max_length = 254)
	status = models.BooleanField(default = True)
