from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Thread, Choice, Post

# Create your views here.

@login_required
def index(request):
	# return HttpResponse('Listing threads')
	threads = Thread.last_n_threads()
	context = {
		'latest_threads': threads,
	}
	return render(request, 'index.html', context)

@login_required
def create(request):
	# return HttpResponse('Create thread')
	context = {

	}
	return render(request, 'create.html', context)

@login_required
def create_thread(request):
	# return HttpResponse('Creating thread')
	thread = Thread(user=request.user, title=request.POST['title'], description=request.POST['description'])
	thread.save()
	thread.choice_set.create(description=request.POST['choice1'])
	thread.choice_set.create(description=request.POST['choice2'])
	return HttpResponseRedirect(reverse('forum:thread', args=(thread.id,)))

@login_required
def thread(request, thread_id):
	# return HttpResponse('Viewing in {}'.format(thread_id))
	thread = get_object_or_404(Thread, pk=thread_id)
	context = {
		'thread': thread,
	}
	return render(request, 'thread.html', context)

@login_required
def post(request, thread_id):
	# return HttpResponse('Posting in {}'.format(thread_id))
	thread = get_object_or_404(Thread, pk=thread_id)
	choice = thread.choice_set.get(pk=request.POST['choice'])
	# choice = thread.choice_set.get(pk=request.POST.get('choice', 0))
	choice.increase_count()
	post = Post(user=request.user, thread=thread, choice=choice, description=request.POST['description'])
	post.save()
	return HttpResponseRedirect(reverse('forum:thread', args=(thread.id,)))




