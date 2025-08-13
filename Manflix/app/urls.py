from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register (r'movies',MoviesView)
router.register (r'directors',MoviesView)
router.register (r'plans',MoviesView)

urlpatterns = router.urls

