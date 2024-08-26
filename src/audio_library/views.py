import os


from django.shortcuts import get_object_or_404
from django.http import FileResponse, Http404, HttpResponse
from rest_framework import generics, viewsets, parsers, views
from django_filters.rest_framework import DjangoFilterBackend
from . import models, serializers
from ..base.permissions  import IsAuthor
from ..base.services import delete_old_file
from ..base.classes import MixedSerializer, Pagination
from rest_framework.exceptions import PermissionDenied, AuthenticationFailed

from .exceptions import custom_get_object_or_404

class GenreView(generics.ListAPIView):
    """List of genres"""

    queryset = models.Genre.objects.all()

    serializer_class = serializers.GenreSerializer 



class LicenseView(viewsets.ModelViewSet):
    """CRUD licenses of authors"""

    serializer_class = serializers.LicenseSerializer
    permission_class = [IsAuthor]

    def get_queryset(self):
        if not isinstance(self.request.user, models.AuthUser):
            raise AuthenticationFailed("")
        
        return models.License.objects.filter(user=self.request.user)
        
    
        
        

    def perform_create(self, serializer):
        if not isinstance(self.request.user, models.AuthUser):
            raise AuthenticationFailed("")
        serializer.save(user=self.request.user)
    

class AlbumView(viewsets.ModelViewSet):
    """ CRUD author of albums"""

    parser_classes = (parsers.MultiPartParser,)

    serializer_class = serializers.AlbumSerializer
    permission_classes = [IsAuthor]


    def get_queryset(self):
        if not isinstance(self.request.user, models.AuthUser):
            raise AuthenticationFailed("User is not authenticated.")
        return models.Album.objects.filter(user=self.request.user,private=False)
    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def perform_destroy(self, instance):
        delete_old_file(instance.cover.path)
        instance.delete()


class PubliAlbumView(generics.ListAPIView):
    """ List of public authors albums """

    serializer_class = serializers.AlbumSerializer


    def get_queryset(self):
        return models.Album.objects.filter(user__id = self.kwargs.get('pk'), private=False)
    


class TrackView(MixedSerializer, viewsets.ModelViewSet):
    """ Tracks CRUD"""

    parser_classes = (parsers.MultiPartParser,)
    permission_classes = [IsAuthor]

    serializer_class = serializers.CreateAuthorTrackSerializer
    serializer_classes_by_action = {
        'list':  serializers.AuthorTrackSerializer
    }


    def get_queryset(self):
        if not isinstance(self.request.user, models.AuthUser):
            raise AuthenticationFailed("User is not authenticated.")
        return models.Track.objects.filter(user=self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    
    def perform_destroy(self,instance):
        delete_old_file(instance.cover.path)
        delete_old_file(instance.file.path)

        instance.delete()


class PlayListView(MixedSerializer, viewsets.ModelViewSet):
    """CRUD playlists of user"""

    parser_classes = (parsers.MultiPartParser,)
    permission_classes = [IsAuthor]
    serializer_class = serializers.CreatePlayListSerializer
    serializer_classes_by_action = {
        'list': serializers.PlayListSerializer
    }

    def get_queryset(self):
        if not isinstance(self.request.user, models.AuthUser):
            raise AuthenticationFailed("User is not authenticated.")
        return models.PlayList.objects.filter(user=self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
    

    def perform_destroy(self,instance):
        delete_old_file(instance.cover.path)
        instance.delete()


class TrackListView(generics.ListAPIView):
    """ List of all tracks """
    queryset = models.Track.objects.filter(private=False)
    serializer_class = serializers.AuthorTrackSerializer
    #pagination_class = Pagination
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['title', 'user__display_name', 'album__name', 'genre__name']

class AuthorTrackListView(generics.ListAPIView):
    """ List of author tracks """
    
    serializer_class = serializers.AuthorTrackSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'album__name', 'genre__name']

    def get_queryset(self):
        return models.Track.objects.filter(user__id=self.kwargs.get('pk'), album__private=False, private=False)
        
    


class StreamingFileView(views.APIView):
    """File playing"""

    def set_play(self, track):
        self.track.plays_count +=1
        self.track.save()


    def get(self, request, pk):
        self.track  = custom_get_object_or_404(models.Track, id=pk, private=False)
        if os.path.exists(self.track.file.path):
            self.set_play(self.track)
            response = HttpResponse('', content_type="audio/mpeg", status=206)
            response['X-Accel-Redirect'] = f"/mp3/{self.track.file.name}"
            return response
        else:
            return Http404
        

class StreamingFileAuthorView(views.APIView):
    """ Streaming tracks of author """

    permission_classes = [IsAuthor]


    def get(self, request, pk):
        if not request.user.is_authenticated:
            raise PermissionDenied("User is not authenticated")
        self.track = custom_get_object_or_404(models.Track, id=pk, user=request.user, private=False)
        print(self.track)
        if os.path.exists(self.track.file.path):
            response = HttpResponse('', content_type="audio/mpeg", status=206)
            response['X-Accel-Redirect'] = f"/mp3/{self.track.file.name}"
            return response
        else:
            return Http404
        
    


class DownloadTrackView(views.APIView):
    """ File downloading"""

    def set_download(self):
        self.track.download += 1
        self.track.save()


    def get(self,request, pk):
        self.track = custom_get_object_or_404(models.Track, id=pk, private=False)
        if os.path.exists(self.track.file.path):
            self.set_download()
            response = HttpResponse('', content_type="audio/mpeg", status=206)
            response['Content-Disposition'] = f"attachment; filename={self.track.file.name}"
            response['X-Accel-Redirect'] = f"/mp3/{self.track.file.name}"
            return response
        else:
            return Http404

class CommentAuthorView(viewsets.ModelViewSet):

    serializer_class = serializers.CommentAuthorSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        if not isinstance(self.request.user, models.AuthUser):
            raise AuthenticationFailed("User is not authenticated.")
        return models.Comment.objects.filter(user=self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


class CommentView(viewsets.ModelViewSet):

    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        return models.Comment.objects.filter(track_id=self.kwargs.get('pk'))