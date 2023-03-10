from django.urls import path
from .views.attendee_views import Attendees, AttendeeDetail, AttendeesAll
from .views.user_views import SignUp, SignIn, SignOut

urlpatterns = [
    path('attendeesall/', AttendeesAll.as_view()),
    path('attendees/', Attendees.as_view(), name='attendees'),
    path('attendees/<int:pk>/', AttendeeDetail.as_view()),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
]