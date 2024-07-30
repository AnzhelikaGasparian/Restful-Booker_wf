import pytest
import requests
import allure


@pytest.mark.smoke
@pytest.mark.regression

@allure.feature('Booking Service')
@allure.suite('Ping Tests')
@allure.title('Health Check Test')
@allure.description('This test checks the health status of the Booking Service to ensure it is up and running.')
@allure.severity('BLOCKER')
def test_health_check():
    with allure.step('Send request to health check endpoint'):
        response = requests.get('https://restful-booker.herokuapp.com/ping')

    with allure.step('Verify response status code is 201'):
        assert response.status_code == 201, f"expected status code 201, but got {response.status_code}"