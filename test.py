
def scramble(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]
        


scramble2 = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))

print(list(scramble2('spam')))
""" 
    def test_create_track_unauthorized(self):
        response = self.client.post(reverse('tracks'), self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED) 
    def test_create_track_authorized(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token_data['access_token'])
        response = self.client.post(reverse('tracks'),self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


"""