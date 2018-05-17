from datetime import datetime, timezone
from mock import MagicMock
from unittest import TestCase
from xplenty import XplentyClient


class TestXplentyApi(TestCase):
    def setUp(self):
        self.client = XplentyClient(account_id='foo', api_key='sekret')

    def test_get_packages(self):
        package_response = {
            u'id': 123,
            u'name': u'my_pkg',
            u'created_at': u'2017-08-09T10:11:12Z'}
        self.client.get = MagicMock(return_value=[package_response])
        packages = self.client.get_packages(10, 1)
        url = 'https://api.xplenty.com/foo/api/packages?offset=10&limit=1'
        self.client.get.assert_called_with(url)
        self.assertEqual(1, len(packages))
        package = packages[0]
        self.assertEqual(123, package.id)
        self.assertEqual(u'my_pkg', package.name)
        created_at = datetime(2017, 8, 9, 10, 11, 12, tzinfo=timezone.utc)
        self.assertEqual(created_at, package.created_at)
