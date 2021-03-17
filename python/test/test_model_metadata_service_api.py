# coding: utf-8

"""
    Seldon Deploy API

    API to interact and manage the lifecycle of your machine learning models deployed through Seldon Deploy.  # noqa: E501

    OpenAPI spec version: v1alpha1
    Contact: hello@seldon.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import seldon_deploy_sdk
from seldon_deploy_sdk.api.model_metadata_service_api import ModelMetadataServiceApi  # noqa: E501
from seldon_deploy_sdk.rest import ApiException


class TestModelMetadataServiceApi(unittest.TestCase):
    """ModelMetadataServiceApi unit test stubs"""

    def setUp(self):
        self.api = seldon_deploy_sdk.api.model_metadata_service_api.ModelMetadataServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_model_metadata_service_create_model_metadata(self):
        """Test case for model_metadata_service_create_model_metadata

        Create a Model Metadata entry.  # noqa: E501
        """
        pass

    def test_model_metadata_service_delete_model_metadata(self):
        """Test case for model_metadata_service_delete_model_metadata

        Delete a Model Metadata entry.  # noqa: E501
        """
        pass

    def test_model_metadata_service_list_model_metadata(self):
        """Test case for model_metadata_service_list_model_metadata

        List Model Metadata entries.  # noqa: E501
        """
        pass

    def test_model_metadata_service_list_runtime_metadata_for_model(self):
        """Test case for model_metadata_service_list_runtime_metadata_for_model

        List Runtime Metadata for all deployments associated with a model.  # noqa: E501
        """
        pass

    def test_model_metadata_service_update_model_metadata(self):
        """Test case for model_metadata_service_update_model_metadata

        Update a Model Metadata entry.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
