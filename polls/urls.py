from django.urls import path

from . import views
from .views import RainbowSixSiegeStatsView


app_name = "polls"
urlpatterns = [
    path("api/r6s/stats/", RainbowSixSiegeStatsView.as_view(), name="r6s-stats"),
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
