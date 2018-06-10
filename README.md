# everuselasticsearchdjangoassingment

The below Steps has been done,

Installed elasticsearch through 

curl -L -O https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.6.8.tar.gz

Django Integration

pip install django-elasticsearch-dsl

Created django project using 

django-admin startproject elasticsearchproject
cd elasticsearchproject
python manage.py startapp elasticsearchapp

Added  settings file and add your app, and the django_elasticsearch_dsl to the INSTALLED_APPS list:

'django_elasticsearch_dsl',
'search',

Specified the search engine host with this code:

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
    },
}

Cretated models.py
Created documents.py
Inserted the data from sample using insert.csv program

Note : Multiple views created for different filteration

I am not aware of django how to add user authorisation for particular view 
