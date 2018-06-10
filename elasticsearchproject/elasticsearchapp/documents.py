from django_elasticsearch_dsl import DocType, Index
from .models import Post

posts = Index('posts')

posts.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@posts.doc_type
class PostDocument(DocType):
    class Meta:
        model = Post

        fields = [
            'distance',
	    'consume',
	     'speed',
	     'temp_inside',
	      'temp_outside',
	       'specials',
         	'gas_type',
	         'AC',
	          'rain',
	           'sun'

        ]
