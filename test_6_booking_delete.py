import requests
import pytest
import allure

import test_1_booking_token
import test_2_booking_post


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Booking Delete Suite')
@allure.title('Test Delete Booking by ID')
@allure.description('Test deletes a booking by its ID and verifies the response.')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_booking_by_id():
    headers = {'Content-Type': 'application/json', 'Cookie': f'token={test_1_booking_token.my_token}'}

    with allure.step('Send DELETE request to remove the booking by ID'):
        response = requests.delete(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            headers=headers
        )

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
