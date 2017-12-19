"""Test the add_credential method."""
import pytest
from requests.auth import HTTPBasicAuth


test_creds = {
    'username': 'joe',
    'password': '1234'}

test_creds_2 = {
    'username': '123321',
    'password': 'abcdef'}

test_creds_3 = {
    'bearer_token': '123321'}


def test_username_auth(unauth_client):
    """Test passing in username to authorization."""
    unauth_client.add_credentials(test_creds)
    assert unauth_client.auth.username == 'joe'


def test_username_auth_2(unauth_client):
    """Test passing in username to authorization."""
    unauth_client.add_credentials(test_creds)
    assert unauth_client.auth.password == '1234'


def test_account_id_auth(unauth_client):
    """Test passing in account id to authorization."""
    unauth_client.add_credentials(test_creds_2)
    assert unauth_client.auth.username == '123321'


def test_account_id_auth_2(unauth_client):
    """Test passing in account id to authorization."""
    unauth_client.add_credentials(test_creds_2)
    assert unauth_client.auth.password == 'abcdef'


def test_bearer_token_auth(unauth_client):
    """Test passing in bearer to authorization."""
    unauth_client.add_credentials(test_creds_3)
    assert unauth_client.auth == 'Bearer 123321'


def test_auth_object(unauth_client):
    """Test auth is HTTPBasicAuth object."""
    unauth_client.add_credentials(test_creds)
    assert isinstance(unauth_client.auth, HTTPBasicAuth)


def test_auth_raises_value_error(unauth_client):
    """Test value error is raised with imporper authorization."""
    with pytest.raises(ValueError):
        unauth_client.add_credentials({})


def test_no_auth_if_no_cred_is_added(unauth_client):
    """Test client object auth property is None by default."""
    assert unauth_client.auth is None
