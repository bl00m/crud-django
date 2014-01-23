from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from users.models import User
from forms import UserForm

# Create your views here.
def front(request):
	users = User.objects.all()
	return render_to_response('front.html', {'users': users})

def create_user(request):

	if request.method == 'POST':
	 	form = UserForm(request.POST)
	 	if form.is_valid():
	 		form.save()

			return HttpResponseRedirect('/users')
	else:
		form = UserForm()

	return render(request, 'user.html', {'form': form})

def edit_user(request, user_id):

	user = get_object_or_404(User, id = user_id)
	form = UserForm(request.POST or None, instance = user)

	if form.is_valid():
		form.save()

		return HttpResponseRedirect('/users')

	return render(request, 'edit_user.html', {'form': form})

def delete_user(request, user_id):
	cert = {}
	cert.update(csrf(request))

	user = get_object_or_404(User, id = user_id)
	user.delete()
	return HttpResponse(status = 200)