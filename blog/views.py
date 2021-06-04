from rest_auth.views import LogoutView
from rest_framework import permissions

from blog_api import a
from rest_framework import mixins, viewsets
from blog_api.models import PostImages


class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated, )


class PostImagesViewSet(mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = a.PostImageSerializer
    queryset = PostImages.objects.all()
