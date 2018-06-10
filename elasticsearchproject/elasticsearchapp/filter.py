#from django.contrib.auth.models import User
from elasticsearchapp.models import Post
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['speed', 'temp_inside', 'temp_outside', ]
