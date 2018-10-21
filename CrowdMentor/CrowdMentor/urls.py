"""CrowdMentor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import url, include
#from django.contrib import admin
from django.contrib.auth import views as auth_views
from CrowdMentor.controllers import signup as register
from django.conf.urls import include, url
from django.contrib import admin
from CrowdMentor.controllers import user

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Login and Registration
    url(r'^$', user.view, name='view'),
    url(r'^home/$', user.view, name='view'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', register.signup, name='signup'),
    url(r'^change_roles/$', user.change_roles, name='change_roles'),
    # url(r'^account_activation_sent/$', register.account_activation_sent, name='account_activation_sent'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     register.activate, name='activate'),

    #For the tasks
    url(r'^tasks/', include('tasks.urls')),
]
