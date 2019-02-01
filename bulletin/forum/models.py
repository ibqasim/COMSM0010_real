from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Thread(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	description = models.TextField()
	time_created = models.DateTimeField(auto_now_add=True)
	time_edited = models.DateTimeField(auto_now=True)

	def last_n_threads(n=10):
		# threads = Thread.objects.order_by('-time_edited')[:n]
		threads = Thread.objects.order_by('-time_edited').all()
		return threads

	def last_n_posts(n=100):
		# posts = self.post_set.order_by('-time_edited')[:n]
		posts = self.post_set.order_by('-time_edited').all()
		return posts

	def __str__(self):
		str_rep = "User: {} \n Title: {} \n Description: {}".format(
			self.user.username,
			self.title,
			self.description,
			)
		return str_rep

class Choice(models.Model):
	thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
	description = models.TextField()
	count = models.IntegerField(default=0)
	time_edited = models.DateTimeField(auto_now=True)

	def increase_count(self):
		self.count += 1
		self.save()

	def __str__(self):
		str_rep = "Thread: {} \n Description: {} \n Count: {}".format(
			self.thread.title,
			self.description,
			self.count,
			)
		return str_rep

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
	choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
	description = models.TextField()
	time_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		str_rep = "User: {} \n Thread: {} \n Vote: {} \n Description: {}".format(
			self.user.username,
			self.thread.title,
			self.vote.description,
			self.description,
			) 
		return str_rep



