from django.conf.urls import url
# from django.contrib import admin
# import blog.views as bv

from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^index/', bv.index)
    url(r'^$', views.index)
]
