import data
import helpers

from selenium import webdriver
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            raise Exception("Urban Routes URL is not reachable")

        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}

        cls.driver = webdriver.Chrome()
        cls.driver.get(data.URBAN_ROUTES_URL)

    def test_set_route(self):
        urban_routes_page = UrbanRoutesPage(self.driver)

        urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        assert urban_routes_page.get_from() == data.ADDRESS_FROM
        assert urban_routes_page.get_to() == data.ADDRESS_TO

    def test_select_supportive_plan(self):
        urban_routes_page = UrbanRoutesPage(self.driver)

        urban_routes_page.click_call_taxi()
        urban_routes_page.select_supportive_plan()

        assert urban_routes_page.is_supportive_plan_selected()
        assert "Supportive" in urban_routes_page.get_supportive_plan_text()

    def test_fill_phone_number(self):
        urban_routes_page = UrbanRoutesPage(self.driver)

        urban_routes_page.click_phone_number()
        urban_routes_page.set_phone_number(data.PHONE_NUMBER)
        urban_routes_page.click_phone_number_next()

        code = helpers.retrieve_phone_code(self.driver)

        urban_routes_page.set_sms_code(code)
        urban_routes_page.click_confirm_phone()

        assert data.PHONE_NUMBER in urban_routes_page.get_phone_number()

    def test_add_credit_card(self):
        urban_routes_page = UrbanRoutesPage(self.driver)

        urban_routes_page.click_payment_method()
        urban_routes_page.click_add_card()
        urban_routes_page.set_card_number(data.CARD_NUMBER)
        urban_routes_page.set_card_code(data.CARD_CODE)
        urban_routes_page.click_link_card()

        assert "Card" in urban_routes_page.get_payment_method()

        urban_routes_page.close_payment_method()

    def test_comment_for_driver(self):
        urban_routes_page = UrbanRoutesPage(self.driver)

        urban_routes_page.set_driver_comment(data.MESSAGE_FOR_DRIVER)

        assert urban_routes_page.get_driver_comment() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        urban_routes_page = UrbanRoutesPage(self.driver)

        urban_routes_page.click_blanket_and_handkerchiefs()

        assert urban_routes_page.is_blanket_and_handkerchiefs_selected()

    def test_order_2_ice_creams(self):
        urban_routes_page = UrbanRoutesPage(self.driver)

        urban_routes_page.add_ice_creams(2)

        assert urban_routes_page.get_ice_cream_count() == "2"

    def test_car_search_model_appears(self):
        urban_routes_page = UrbanRoutesPage(self.driver)

        urban_routes_page.click_order_button()

        assert urban_routes_page.is_car_search_modal_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()