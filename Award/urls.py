from django.urls import path, include, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import home, project_view, signup, upload, index




urlpatterns = [
    path('', home, name='home'),
    path('project/<int:project_id>', project_view, name='project'),
    path('signup/', signup, name='signup'),
    path('upload/', upload, name='upload'),
    # path('profile/<username>/', profile, name='profile'),
    # path('profile/<username>/settings', edit_profile, name='edit'),
    path('account/', include('django.contrib.auth.urls')),
]
# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
