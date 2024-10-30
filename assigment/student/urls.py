from django.urls import path
from .views import student
from django.conf import settings
from django .conf.urls.static import static


urlpatterns = [
    path('student/', student, name='student'),
    # path('index', index, name = 'indexmain')
 
]
    #  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
   
if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)