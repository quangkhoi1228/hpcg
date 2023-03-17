
from django.urls import include, path
from django.contrib import admin

from rest_framework import routers
from hpcg_backend.quickstart import views as quickstart_views
from hpcg_backend.review_search import views as review_search_views

router = routers.DefaultRouter()
router.register(r'users', quickstart_views.UserViewSet)
router.register(r'groups', quickstart_views.GroupViewSet)
# router.register(r'review-search',
#                 review_search_views.ReviewSearchViewSet, basename='review-search')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('review_search/',  review_search_views.ReviewSearchViewSet.as_view(),
         name='review-search'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
