import connexion
import six

from swagger_server.models.check_token_assignment_output import CheckTokenAssignmentOutput  # noqa: E501
from swagger_server.models.choose_service_mode_input import ChooseServiceModeInput  # noqa: E501
from swagger_server.models.generate_token_input import GenerateTokenInput  # noqa: E501
from swagger_server.models.generate_token_output import GenerateTokenOutput  # noqa: E501
from swagger_server.models.update_counter_status_input import UpdateCounterStatusInput  # noqa: E501
from swagger_server.models.update_system_configuration_input import UpdateSystemConfigurationInput  # noqa: E501
from swagger_server import util


def check_token_assignment_get(counter_id):  # noqa: E501
    """Check the token assignment for a counter

     # noqa: E501

    :param counter_id: ID of the counter to check token assignment
    :type counter_id: str

    :rtype: CheckTokenAssignmentOutput
    """
    return 'do some magic!'


def choose_service_mode_put(body):  # noqa: E501
    """Choose the mode of the service

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ChooseServiceModeInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def generate_token_post(body):  # noqa: E501
    """Generate a queue token for customers

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: GenerateTokenOutput
    """
    if connexion.request.is_json:
        body = GenerateTokenInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_counter_status_put(body):  # noqa: E501
    """Update status of a counter

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UpdateCounterStatusInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_system_configuration_put(body):  # noqa: E501
    """Update system configurations

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UpdateSystemConfigurationInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
