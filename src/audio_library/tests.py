from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .setup_test import user_with_token_create, album_create, license_create, file_create, user_filter, genre_data, track_data
class AudioLibraryTests(APITestCase):

    def setUp(self):

                
        album_create()
        license_create()

        self.token_data = user_with_token_create()

        self.file_create = file_create()
        
        license = {
            'text' : 'licensev2',
        }
        self.genre = genre_data()
        self.create_track = track_data()
    
    """  Test of User Creation   """ 

    def test_user_creation(self):
        self.assertIsNotNone(user_filter())


    """  Test of genres   """  

    def test_list_genres(self):
        response = self.client.get(reverse('genres'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

       
        
    """  Test of licenses """  

    def test_list_licenses(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token_data['access_token'])
        response = self.client.get(reverse('license'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_list_licenses(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token_data['access_token'])
        response = self.client.get(reverse('license'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0].get('text'), 'licensev2')
        self.assertEqual(len(response.json()), 1)



    def test_create_license_post(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token_data['access_token'])
        response = self.client.post(reverse('license'), self.license, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_fail_license_unauthorized(self):
        response = self.client.get(reverse('license'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_fail_license_put(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token_data['access_token'])
        url = reverse('license_change', kwargs={'pk': 99})

        response = self.client.put(url, self.license, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    
    def test_success_license_put(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token_data['access_token'])
        url = reverse('license_change', kwargs={'pk': 1})

        response = self.client.put(url, self.license, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_success_license_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token_data['access_token'])
        url = reverse('license_change', kwargs={'pk': 1})

        response = self.client.delete(url, self.license, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    
    
    """  Test of albums   """  
    def test_success_license_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token_data['access_token'])

        response = self.client.get(reverse('album'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

