import pytest
import requests
import allure

import test_1_booking_token
import test_2_booking_post


@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Partial Update Booking Suite')
@allure.title('Test Partial Update Booking')
@allure.description('Test partially updates an existing booking in the Booking Service and verifies the response.')
@allure.severity(allure.severity_level.CRITICAL)
def test_partial_update_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown"
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={test_1_booking_token.my_token}'
    }

    with allure.step('Send PATCH request to partially update the booking'):
        response = requests.patch(
           f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected StatusCode 200, But Got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify updated firstname is correct'):
        assert body['firstname'] == response_data[
            'firstname'], f"Expected firstname to be {body['firstname']}, but got {response_data['firstname']}"

    with allure.step('Verify updated lastname is correct'):
        assert body['lastname'] == response_data[
            'lastname'], f"Expected lastname to be {body['lastname']}, but got {response_data['lastname']}"

    with allure.step('Verify totalprice is present in the response'):
        assert 'totalprice' in response_data, "Expected totalprice to be in the response, but it's missing"

    with allure.step('Verify depositpaid is present in the response'):
        assert 'depositpaid' in response_data, "Expected depositpaid to be in the response, but it's missing"

    with allure.step('Verify bookingdates is present in the response'):
        assert 'bookingdates' in response_data, "Expected bookingdates to be in the response, but it's missing"

    with allure.step('Verify checkin date is present in the response'):
        assert 'checkin' in response_data[
            'bookingdates'], f"Expected bookingdates checkin to be in the response, but it's missing"

    with allure.step('Verify checkout date is present in the response'):
        assert 'checkout' in response_data[
            'bookingdates'], f"Expected bookingdates checkout to be in the response, but it's missing"

    with allure.step('Verify additionalneeds is present in the response'):
        assert 'additionalneeds' in response_data, "Expected additionalneeds to be in the response, but it's missing"

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)


@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Partial Update Booking Suite')
@allure.title('Negative Partial Update Booking Test with Invalid Token')
@allure.description('Test attempts to partially update an existing booking with an invalid token and verifies the response.')
@allure.severity(allure.severity_level.CRITICAL)
def test_negative_partial_update_with_invalid_token_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown"
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': 'token=sfg662sr11651654'}

    with allure.step('Send PATCH request to partially update the booking with an invalid token'):
        response = requests.patch(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code is 403'):
        assert response.status_code == 403, f'Expected status code 403, but got {response.status_code}'


@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Partial Update Booking Suite')
@allure.title('Negative Partial Update Booking Test without Token')
@allure.description('This test attempts to partially update an existing booking without token and verifies the response.')
@allure.severity(allure.severity_level.CRITICAL)
def test_negative_partial_update_without_token_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown"
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    with allure.step('Send PATCH request to partially update the booking without a token'):
        response = requests.patch(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code is 403'):
        assert response.status_code == 403, f'Expected status code 403, but got {response.status_code}'
