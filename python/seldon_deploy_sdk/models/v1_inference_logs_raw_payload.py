# coding: utf-8

"""
    Seldon Deploy API

    API to interact and manage the lifecycle of your machine learning models deployed through Seldon Deploy.  # noqa: E501

    OpenAPI spec version: v1alpha1
    Contact: hello@seldon.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1InferenceLogsRawPayload(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'request_id': 'str',
        'timestamp': 'datetime',
        'request': 'object',
        'response': 'object'
    }

    attribute_map = {
        'request_id': 'requestId',
        'timestamp': 'timestamp',
        'request': 'request',
        'response': 'response'
    }

    def __init__(self, request_id=None, timestamp=None, request=None, response=None):  # noqa: E501
        """V1InferenceLogsRawPayload - a model defined in Swagger"""  # noqa: E501

        self._request_id = None
        self._timestamp = None
        self._request = None
        self._response = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if timestamp is not None:
            self.timestamp = timestamp
        if request is not None:
            self.request = request
        if response is not None:
            self.response = response

    @property
    def request_id(self):
        """Gets the request_id of this V1InferenceLogsRawPayload.  # noqa: E501


        :return: The request_id of this V1InferenceLogsRawPayload.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this V1InferenceLogsRawPayload.


        :param request_id: The request_id of this V1InferenceLogsRawPayload.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def timestamp(self):
        """Gets the timestamp of this V1InferenceLogsRawPayload.  # noqa: E501


        :return: The timestamp of this V1InferenceLogsRawPayload.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this V1InferenceLogsRawPayload.


        :param timestamp: The timestamp of this V1InferenceLogsRawPayload.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def request(self):
        """Gets the request of this V1InferenceLogsRawPayload.  # noqa: E501


        :return: The request of this V1InferenceLogsRawPayload.  # noqa: E501
        :rtype: object
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this V1InferenceLogsRawPayload.


        :param request: The request of this V1InferenceLogsRawPayload.  # noqa: E501
        :type: object
        """

        self._request = request

    @property
    def response(self):
        """Gets the response of this V1InferenceLogsRawPayload.  # noqa: E501


        :return: The response of this V1InferenceLogsRawPayload.  # noqa: E501
        :rtype: object
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this V1InferenceLogsRawPayload.


        :param response: The response of this V1InferenceLogsRawPayload.  # noqa: E501
        :type: object
        """

        self._response = response

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1InferenceLogsRawPayload, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1InferenceLogsRawPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other