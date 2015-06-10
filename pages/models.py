from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from autoslug import AutoSlugField
from django.core.exceptions import NON_FIELD_ERRORS


class newlist(models.Model):
	user = models.ForeignKey(User)
	list_name = models.CharField(max_length = 100,)#Create a unique field int he database to get rid of teh duplicate entries for the users
	picture = models.ImageField(upload_to='profiles/', default = "/media/profiles/default.jpg")
	slug = AutoSlugField(populate_from='list_name', default = '')
	class Meta:
		unique_together=('user','list_name')
<<<<<<< HEAD

=======
		error_messages = {
			NON_FIELD_ERRORS: {
				'unique_together': "s's are not unique.",
			}
		}
>>>>>>> ed78a14ef7596ba3f0ade075f760d5b486bdc2f8

	def __str__(self):
		return self.list_name


class newlistitem(models.Model):
	user = models.ForeignKey(User)
	list_name = models.ForeignKey(newlist)
	list_item = models.CharField(max_length = 200)
	slugitem = AutoSlugField(populate_from='list_item', default = '')


	def __str__(self):
		return self.list_item

