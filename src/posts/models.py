from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.conf import settings
from django.core.urlresolvers import reverse
User = settings.AUTH_USER_MODEL

class Post(models.Model):	

	category    = models.CharField(max_length=120)
	owner		= models.ForeignKey(User)
	name		= models.CharField(max_length=120)
	slug 		= models.SlugField(unique=True)
	content 	= models.TextField()
	timestamp	= models.DateTimeField(auto_now=True, auto_now_add=False)
	updated		= models.DateTimeField(auto_now=False, auto_now_add=True)
	readtime	= models.IntegerField(default=0)
	image		= models.FileField(null=True, blank=True, default='/placeholder.png')
	logo		= models.CharField(max_length=120)
	ticker		= models.CharField(max_length=120)
	draft 		= models.BooleanField(default=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('posts:detail', kwargs={'slug': self.slug})

	@property
	def title(self):
		return self.name

	@property
	def image_url(self):
		if self.image and hasattr(self.image, 'url'):
			return self.image.url
			
	class Meta:
		ordering = ["-timestamp", "-updated"]

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

	instance.category = instance.category.lower()
	instance.readtime = int(round(len(instance.content.split()) / 200.0))


pre_save.connect(pre_save_post_receiver, sender=Post)

