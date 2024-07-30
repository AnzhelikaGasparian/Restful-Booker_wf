import pytest
import requests
import allure

import test_1_booking_token
import test_2_booking_post

@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Booking Update Suite')
@allure.title('Test Update Booking')
@allure.description('Test updates an existing booking in the Booking Service and verifies the response.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.skip
def test_update_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
               'Cookie': f'token={test_1_booking_token.my_token}'}

    with allure.step('Send PUT request to update the booking'):
        response = requests.put(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify updated firstname is correct'):
        assert body['firstname'] == response_data[
            'firstname'], f'Expected firstname to be {body["firstname"]}, but got {response_data["firstname"]}'

    with allure.step('Verify updated lastname is correct'):
        assert body['lastname'] == response_data[
            'lastname'], f'Expected lastname to be {body["lastname"]}, but got {response_data["lastname"]}'

    with allure.step('Verify updated totalprice is correct'):
        assert body['totalprice'] == response_data[
            'totalprice'], f'Expected totalprice to be {body["totalprice"]}, but got {response_data["totalprice"]}'

    with allure.step('Verify updated depositpaid is correct'):
        assert body['depositpaid'] == response_data[
            'depositpaid'], f'Expected depositpaid to be {body["depositpaid"]}, but got {response_data["depositpaid"]}'

    with allure.step('Verify updated checkin date is correct'):
        assert body['bookingdates']['checkin'] == response_data['bookingdates'][
            'checkin'], f'Expected checkin to be {body["bookingdates"]["checkin"]}, but got {response_data["bookingdates"]["checkin"]}'

    with allure.step('Verify updated checkout date is correct'):
        assert body['bookingdates']['checkout'] == response_data['bookingdates'][
            'checkout'], f'Expected checkout to be {body["bookingdates"]["checkout"]}, but got {response_data["bookingdates"]["checkout"]}'

    with allure.step('Verify updated additionalneeds is correct'):
        assert body['additionalneeds'] == response_data[
            'additionalneeds'], f'Expected additionalneeds to be {body["additionalneeds"]}, but got {response_data["additionalneeds"]}'


    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)



@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Update Booking Suite')
@allure.title('Test Negative Update Booking')
@allure.description('Test attempts to update an existing booking with an invalid token and verifies the response.')
@allure.severity(allure.severity_level.CRITICAL)
def test_negative_update_booking(x):
    body = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': 'token=jnfb4561856351bc'}

    with allure.step('Send PUT request to update the booking with an invalid token'):
        response = requests.put(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code is 403'):
        assert response.status_code == 403, f'Expected status code 403, but got {response.status_code}'
