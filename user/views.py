from django.shortcuts import render
from .models import User
from .serializers import UserSerializers, UserEditSerializers
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    lookup_url_kwarg = 'username'
    lookup_field = 'username'

    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     context["request"] = self.request
    #     return context


# class MatchListing(generics.ListCreateAPIView):
#     queryset = MatchList.objects.all()
#     serializer_class = MatchSerializers


@api_view(['POST'])
def like_match(request):
    username = request.data.get('username')
    myprofile = request.user
    obj = User.objects.get(username=username)

    if obj in myprofile.like.all():
        myprofile.match.add(obj)
        return Response("match added")
        # notification object will be created after matching - pending
    else:
        obj.like.add(myprofile)
        return Response("Like added")
        # notification after like - pending


@api_view(['GET'])
def get_by_location(request):
    user = User.objects.filter(city="dhaka")
    serializer = UserSerializers(user, many=True)
    return Response(serializer.data)