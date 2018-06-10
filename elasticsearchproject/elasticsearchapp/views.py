# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings
#from elasticsearchapp.documents import PostDocument
from elasticsearchapp.models import Post
#from django.contrib.auth.models import Post
#from commpy.filters import *

"""
def search(request):

    q = request.GET.get('q')

    if q:
        posts = PostDocument.search().query("match", temp_outside=q)
    else:
        posts = ''
"""

def display(request):

  
    all_entries = Post.objects.all()
    print(all_entries)
    return render(request, 'search/search.html', {'all_entries':all_entries})	
   
	


	#return render(request, 'search/search.html', {'posts':posts})
	
def user1(request):
	user1result = Post.objects.filter(temp_outside__gte=5,temp_outside__lte=10)
	return render(request, 'search/search.html',{'user1result':user1result})

def user2(request):
	user2result = Post.objects.filter(speed__gte=30,speed__lte=50)
	return render(request, 'search/search.html',{'user2result':user2result})
	
	
