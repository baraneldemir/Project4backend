from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, status
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework_simplejwt.tokens import RefreshToken
from django.forms import BaseModelForm

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatsSerializer
    permission_classes = [permissions.IsAuthenticated]


class LogoutView(APIView):
    def post(self, request):
        print(request.data)
        try :
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class SignupView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            new_user = User.objects.create(username=username, email=email)
            new_user.set_password(password)
            new_user.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        


# class PeopleCreate(CreateView):
#   model = People
#   fields = ['name', 'designation', 'description', 'twitter', 'linkedin', 'image']

#   def form_valid(self, form):
#     # self.request.user is the logged in user
#     form.instance.user = self.request.user
#     #let the createview's from_valid method
#     # do its regular work ( saving the object & redirect)
#     return super().form_valid(form)
  


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request,):
        name = request.data.get('name')
        designation = request.data.get('designation')
        description = request.data.get('description')
        twitter = request.data.get('twitter')
        linkedin = request.data.get('linkedin')
        image = request.data.get('image')
        try:
            profile = People.objects.create(name=name, designation=designation, description=description, twitter=twitter, linkedin=linkedin, image=image)
            profile.save()
            return Response(status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


# class PeopleUpdate(UpdateView):
#   model = People
#   fields = ['name', 'designation', 'description', 'twitter', 'linkedin', 'image']
  
# class PeopleDelete(DeleteView):
#   model = People
#   success_url = '/'
        
        



