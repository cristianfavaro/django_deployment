from django.conf.urls import url
from basic_app import views

#template tagging. preciso dar uma variavel global que ele vai procurar.abs
app_name = 'basic_app' #isso que eu vou referenciar no html do relative

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$',views.other,name='other')
]
