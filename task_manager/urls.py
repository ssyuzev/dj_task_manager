from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from tasks import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^login/$',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'
    ),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    url(r'^new/$', views.new_task, name='new'),
    
    url(r'^aj/check_task/$', views.check_task_title, name='check_task_title'),
    url(r'^$', views.task_list, name='home'),

]
