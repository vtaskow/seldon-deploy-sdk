# coding: utf-8

"""
    Seldon-Deploy API.

    Documentation of Seldon-Deploy API.  # noqa: E501

    OpenAPI spec version: v1alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import seldon_deploy_client
from seldon_deploy_client.api.requests_api import RequestsApi  # noqa: E501
from seldon_deploy_client.rest import ApiException


class TestRequestsApi(unittest.TestCase):
    """RequestsApi unit test stubs"""

    def setUp(self):
        self.api = seldon_deploy_client.api.requests_api.RequestsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_requests(self):
        """Test case for requests

        """
        pass


if __name__ == '__main__':
    unittest.main()