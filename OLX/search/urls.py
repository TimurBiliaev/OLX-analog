from django.urls import path
from search.views import RenderAdvancedSearch


urlpatterns = [
    path("AdvancedSerarcH", RenderAdvancedSearch, name="advsearch")
]