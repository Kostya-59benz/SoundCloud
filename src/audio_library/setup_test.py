from unittest import mock
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile


from src.oauth.models import AuthUser
from src.audio_library.models import Track, License, Genre, Comment, Album, PlayList
from src.oauth.services.base_auth import create_token



def user_with_token_create(user: AuthUser):
     return create_token(user.id)


def user_create():
    user = AuthUser.objects.create(email='detolfero@gmail.com')

    return user
    
        
def user_filter():
    return AuthUser.objects.filter(email='detolfero@gmail.com')

def album_create():
    user = user_create()

    Album.objects.create(
        user = user,
        name='album1',
        description='album1album1album1album1',
        private=True
    )
    Album.objects.create(
        user = user,
        name='album1',
        description='album1album1album1album1'
        )

def license_create():
    user = user_create()

    License.objects.create(
            user = user,
            text = 'licensev2'

        )


def genre_data():
    return {
            'name':'Rap',
        }

def track_data():
    return {
            'title': 'People',
            'license' : 1,
            'genre': 1,
            'file':file_create.get('file_mock')
        }

def file_create():
    file_mock = mock.MagicMock(spec=File)
    file_mock.name = 'cat.jpg'


    with open('media/LoreenTattoo.mp3', 'rb') as f:
        test_mp3_file = SimpleUploadedFile("real_audio.mp3", f.read(), content_type="audio/mpeg")
    
    return {
        'file_mock': file_mock.name,
        'mp3_file': test_mp3_file
    }