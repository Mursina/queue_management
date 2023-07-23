# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.check_token_assignment_output import CheckTokenAssignmentOutput  # noqa: E501
from swagger_server.models.choose_service_mode_input import ChooseServiceModeInput  # noqa: E501
from swagger_server.models.generate_token_input import GenerateTokenInput  # noqa: E501
from swagger_server.models.generate_token_output import GenerateTokenOutput  # noqa: E501
from swagger_server.models.update_counter_status_input import UpdateCounterStatusInput  # noqa: E501
from swagger_server.models.update_system_configuration_input import UpdateSystemConfigurationInput  # noqa: E501
from swagger_server.test import BaseTestCase


class TestQueueManagementController(BaseTestCase):
    """QueueManagementController integration test stubs"""

    def test_check_token_assignment_get(self):
        """Test case for check_token_assignment_get

        Check the token assignment for a counter
        """
        query_string = [('counter_id', 'counter_id_example')]
        response = self.client.open(
            '/check_token_assignment',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_choose_service_mode_put(self):
        """Test case for choose_service_mode_put

        Choose the mode of the service
        """
        body = ChooseServiceModeInput()
        response = self.client.open(
            '/choose_service_mode',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_generate_token_post(self):
        """Test case for generate_token_post

        Generate a queue token for customers
        """
        body = GenerateTokenInput()
        response = self.client.open(
            '/generate_token',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_counter_status_put(self):
        """Test case for update_counter_status_put

        Update status of a counter
        """
        body = UpdateCounterStatusInput()
        response = self.client.open(
            '/update_counter_status',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_system_configuration_put(self):
        """Test case for update_system_configuration_put

        Update system configurations
        """
        body = UpdateSystemConfigurationInput()
        response = self.client.open(
            '/update_system_configuration',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
