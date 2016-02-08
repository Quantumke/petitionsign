from django.shortcuts import render_to_response, get_object_or_404
from petition.models import petition
# Create your views here.
def guestbook (request):
	return render_to_response('index.html', {
		'Petition': petition.objects.all()
		})
	