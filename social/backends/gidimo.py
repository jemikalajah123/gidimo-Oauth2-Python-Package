from urllib.parse import urlencode

from social_core.backends.oauth import BaseOAuth2


class GidimoOAuth2(BaseOAuth2):
    """Gidimo OAuth authentication backend"""
    name = 'gidimo'
    AUTHORIZATION_URL = 'https://oauth2-test.gidimo.com:8443/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://oauth2-test.gidimo.com:8443/oauth/token'
    ACCESS_TOKEN_METHOD = 'POST'
    SCOPE_SEPARATOR = ','
    EXTRA_DATA = [
        ('id', 'id'),
        ('expires', 'expires')
    ]

    def get_user_details(self, response):
        """Return user details from Gidimo account"""
        return {'username': response.get('login'),
                'email': response.get('email') or '',
                'first_name': response.get('name')}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        url = 'https://oauth2-test.gidimo.com:8443/user?' + urlencode({
            'access_token': access_token
        })
        return self.get_json(url)
