from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Thread, Choice, Post

# Create your views here.

def index(request):
	threads = Thread.last_n_threads()
	context = {
		'latest_threads': threads,
	}
	return render(request, 'index.html', context)

def thread(request, thread_id):
	thread = get_object_or_404(Thread, pk=thread_id)
	context = {
		'thread': thread,
	}
	return render(request, 'thread.html', context)



