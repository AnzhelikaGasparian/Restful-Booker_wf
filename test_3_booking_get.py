import requests
import pytest
import allure
import test_2_booking_post

@allure.feature('Booking Feature')
@allure.suite('Get Booking Suite')
@allure.title('Get All Bookings')
@allure.description('This test checks the retrieval of all bookings from the Booking Service.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_booking_all():
    with allure.step('Send GET request to /booking endpoint'):
        response = requests.get('https://restful-booker.herokuapp.com/booking')

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'

    with allure.step('Verify the response contains a list of bookings'):
        assert len(response.json()) > 0, 'The list should not be empty'


@allure.feature('Booking Feature')
@allure.suite('Get Booking Suite')
@allure.title('Get Booking by ID')
@allure.description('This test checks the retrieval of a specific booking by ID from the Booking Service.')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_booking_by_id():
    with allure.step('Send GET request to /booking/{id} endpoint'):
        response = requests.get(f'https://restful-booker.herokuapp.com/booking/{test_2_booking_post.my_bookingid}')

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains "firstname"'):
        assert 'firstname' in response_data, "The response does not contain 'firstname'"

    with allure.step('Verify response contains "lastname"'):
        assert 'lastname' in response_data, "The response does not contain 'lastname'"

    with allure.step('Verify response contains "totalprice"'):
        assert 'totalprice' in response_data, "The response does not contain 'totalprice'"

    with allure.step('Verify response contains "depositpaid"'):
        assert 'depositpaid' in response_data, "The response does not contain 'depositpaid'"

    with allure.step('Verify response contains "bookingdates"'):
        assert 'bookingdates' in response_data, "The response does not contain 'bookingdates'"

    with allure.step('Verify "bookingdates" contains "checkin"'):
        assert 'checkin' in response_data['bookingdates'], "The response does not contain 'checkin'"

    with allure.step('Verify "bookingdates" contains "checkout"'):
        assert 'checkout' in response_data['bookingdates'], "The response does not contain 'checkout'"

    with allure.step('Verify response contains "additionalneeds"'):
        assert 'additionalneeds' in response_data, "The response does not contain 'additionalneeds'"

    with allure.step('Verify "depositpaid" is a boolean'):
        assert response_data['depositpaid'] == True or response_data['depositpaid'] == False, "Error depositpaid"

    with allure.step('Verify "totalprice" is a number'):
        assert isinstance(response_data['totalprice'], (int, float)), "The 'totalprice' should be a number"

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)