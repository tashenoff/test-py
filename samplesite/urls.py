# from django.contrib import admin
# from django.urls import path, include
# urlpatterns = [
#     path('bboard/', include('bboards.urls')),
#     path('admin/', admin.site.urls),
   
# ]



from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path('bboard/', include('bboard.urls', namespace = 'bboard')),
path('profiles/', include('profiles.urls', namespace = 'profiles')),
path('admin/', admin.site.urls),
]
