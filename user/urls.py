from django.urls import path
from .views import UserList, UserDetail, like_match, get_by_location
urlpatterns = [
    path('', UserList.as_view()),
    path('detail/<username>', UserDetail.as_view()),
    # path('match/', MatchListing.as_view()),
    path('like/', like_match),
    path('getuser/', get_by_location)

]
