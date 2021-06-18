import pytest
import requests

data = {
    'id': 12,
    'username': 'test_user',
    'firstName': 'firstName',
    'lastName': 'lastName',
    'email': 'test@email.com',
    'password': 'asdf1234asdf',
    'phone': '123456789',
    'userStatus': 1
}
url = 'https://petstore.swagger.io/v2/user/'


@pytest.mark.parametrize(
    'method, url_, data_, response_message, expected_code',
    [
        ('post', url, data, '12', 200),
        ('put', url+data['username'], data, '12', 200),
        ('get', url+data['username'], None, data, None),
        ('get', url+'some_non_existing_username', None, 'User not found', 1),
        ('delete', url+data['username'], None, data['username'], 200)
    ]
)
def test_user_request(method, url_, data_, response_message, expected_code):
    response = requests.request(method, url_, json=data_).json()
    status_code = response.get('code')
    if status_code is not None:
        assert status_code == expected_code
        assert response.get('message') == response_message
    if status_code is None:
        assert response == response_message
