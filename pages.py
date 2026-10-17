from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class UrbanRoutesPage:

    # Address locators
    FROM_FIELD = (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')

    # Call taxi button
    CALL_TAXI_BUTTON = (
        By.XPATH,
        '//button[contains(@class, "button") and contains(text(), "Call a taxi")]'
    )

    # Supportive plan
    SUPPORTIVE_PLAN = (
        By.XPATH,
        '//div[contains(@class, "tcard")][.//*[normalize-space()="Supportive"]]'
    )

    SUPPORTIVE_PLAN_CARD = (
        By.XPATH,
        '//div[contains(@class, "tcard")][.//*[normalize-space()="Supportive"]]'
    )

    # Phone number
    PHONE_NUMBER_BUTTON = (
        By.XPATH,
        '//div[contains(@class,"np-button")]'
    )

    PHONE_NUMBER_INPUT = (By.ID, 'phone')

    PHONE_NUMBER_NEXT_BUTTON = (
        By.XPATH,
        '//button[normalize-space()="Next"]'
    )

    SMS_CODE_INPUT = (By.ID, 'code')

    CONFIRM_PHONE_BUTTON = (
        By.XPATH,
        '//button[normalize-space()="Confirm"]'
    )

    # Payment
    PAYMENT_METHOD_BUTTON = (
        By.CLASS_NAME,
        'pp-button'
    )

    ADD_CARD_BUTTON = (
        By.XPATH,
        '//div[@class="pp-title" and text()="Add card"]'
        '/ancestor::div[contains(@class,"pp-row")]'
    )

    CARD_NUMBER_INPUT = (By.ID, 'number')

    CARD_CODE_INPUT = (
        By.CSS_SELECTOR,
        'div.card-code-input input#code.card-input'
    )

    LINK_CARD_BUTTON = (
        By.XPATH,
        '//button[normalize-space()="Link"]'
    )

    PAYMENT_CLOSE_BUTTON = (
        By.CSS_SELECTOR,
        '.payment-picker.open .section.active .close-button'
    )

    # Driver comment
    DRIVER_COMMENT_INPUT = (By.ID, 'comment')

    # Blanket and handkerchiefs
    BLANKET_CHECKBOX = (
        By.XPATH,
        '//div[@class="r-sw-label" and normalize-space()="Blanket and handkerchiefs"]'
        '/following-sibling::div[contains(@class,"r-sw")]'
        '//input[@type="checkbox"]'
    )

    BLANKET_SWITCH = (
        By.XPATH,
        '//div[@class="r-sw-label" and normalize-space()="Blanket and handkerchiefs"]'
        '/following-sibling::div[contains(@class,"r-sw")]'
        '//div[contains(@class,"switch")]'
    )

    # Ice cream
    ICE_CREAM_PLUS_BUTTON = (
        By.XPATH,
        '//div[@class="r-counter-label" and normalize-space()="Ice cream"]'
        '/following-sibling::div[contains(@class,"r-counter")]'
        '//div[contains(@class,"counter-plus")]'
    )

    ICE_CREAM_COUNTER = (
        By.XPATH,
        '//div[@class="r-counter-label" and normalize-space()="Ice cream"]'
        '/following-sibling::div[contains(@class,"r-counter")]'
        '//div[contains(@class,"counter-value")]'
    )

    # Order button
    ORDER_BUTTON = (
        By.CLASS_NAME,
        'smart-button'
    )

    CAR_SEARCH_MODAL = (
        By.CSS_SELECTOR,
        '.order.shown'
    )


    def __init__(self, driver):
        self.driver = driver


    # Address methods
    def set_from(self, address):
        from_field = WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.visibility_of_element_located(
                self.FROM_FIELD
            )
        )

        from_field.clear()
        from_field.send_keys(address)


    def set_to(self, address):
        to_field = WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.visibility_of_element_located(
                self.TO_FIELD
            )
        )

        to_field.clear()
        to_field.send_keys(address)


    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)


    def get_from(self):
        return self.driver.find_element(
            *self.FROM_FIELD
        ).get_attribute('value')


    def get_to(self):
        return self.driver.find_element(
            *self.TO_FIELD
        ).get_attribute('value')


    # Call taxi
    def click_call_taxi(self):
        WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.element_to_be_clickable(
                self.CALL_TAXI_BUTTON
            )
        ).click()


    # Supportive plan
    def select_supportive_plan(self):
        supportive_plan = WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.element_to_be_clickable(
                self.SUPPORTIVE_PLAN
            )
        )

        if 'active' not in supportive_plan.get_attribute('class'):
            supportive_plan.click()


    def is_supportive_plan_selected(self):
        supportive_plan = WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.visibility_of_element_located(
                self.SUPPORTIVE_PLAN_CARD
            )
        )

        return 'active' in supportive_plan.get_attribute('class')


    def get_supportive_plan_text(self):
        return WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.visibility_of_element_located(
                self.SUPPORTIVE_PLAN_CARD
            )
        ).text


    # Phone number methods
    def click_phone_number(self):
        WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.element_to_be_clickable(
                self.PHONE_NUMBER_BUTTON
            )
        ).click()


    def set_phone_number(self, phone_number):
        phone_field = WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.visibility_of_element_located(
                self.PHONE_NUMBER_INPUT
            )
        )

        phone_field.clear()
        phone_field.send_keys(phone_number)


    def click_phone_number_next(self):
        WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.element_to_be_clickable(
                self.PHONE_NUMBER_NEXT_BUTTON
            )
        ).click()


    def set_sms_code(self, code):
        code_field = WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.visibility_of_element_located(
                self.SMS_CODE_INPUT
            )
        )

        code_field.clear()
        code_field.send_keys(code)


    def click_confirm_phone(self):
        WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.element_to_be_clickable(
                self.CONFIRM_PHONE_BUTTON
            )
        ).click()


    def get_phone_number(self):
        return WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.presence_of_element_located(
                self.PHONE_NUMBER_BUTTON
            )
        ).text


    # Payment methods
    def click_payment_method(self):
        WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.element_to_be_clickable(
                self.PAYMENT_METHOD_BUTTON
            )
        ).click()


    def click_add_card(self):
        WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.element_to_be_clickable(
                self.ADD_CARD_BUTTON
            )
        ).click()


    def set_card_number(self, number):
        field = WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.visibility_of_element_located(
                self.CARD_NUMBER_INPUT
            )
        )

        field.clear()
        field.send_keys(number)


    def set_card_code(self, code):
        field = WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.visibility_of_element_located(
                self.CARD_CODE_INPUT
            )
        )

        field.clear()
        field.send_keys(code)

        # Remove focus from CVV field
        field.send_keys(Keys.TAB)


    def click_link_card(self):
        WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.element_to_be_clickable(
                self.LINK_CARD_BUTTON
            )
        ).click()


    def get_payment_method(self):
        return WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.visibility_of_element_located(
                self.PAYMENT_METHOD_BUTTON
            )
        ).text


    def close_payment_method(self):
        close_button = WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.element_to_be_clickable(
                self.PAYMENT_CLOSE_BUTTON
            )
        )

        close_button.click()


    # Driver comment
    def set_driver_comment(self, message):
        comment_field = WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.visibility_of_element_located(
                self.DRIVER_COMMENT_INPUT
            )
        )

        comment_field.clear()
        comment_field.send_keys(message)


    def get_driver_comment(self):
        return self.driver.find_element(
            *self.DRIVER_COMMENT_INPUT
        ).get_attribute('value')


    # Blanket and handkerchiefs
    def click_blanket_and_handkerchiefs(self):
        WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.element_to_be_clickable(
                self.BLANKET_SWITCH
            )
        ).click()


    def is_blanket_and_handkerchiefs_selected(self):
        checkbox = WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.presence_of_element_located(
                self.BLANKET_CHECKBOX
            )
        )

        return checkbox.get_property('checked')


    # Ice cream
    def add_ice_creams(self, amount):
        for _ in range(amount):
            WebDriverWait(
                self.driver,
                10
            ).until(
                expected_conditions.element_to_be_clickable(
                    self.ICE_CREAM_PLUS_BUTTON
                )
            ).click()


    def get_ice_cream_count(self):
        return WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.visibility_of_element_located(
                self.ICE_CREAM_COUNTER
            )
        ).text


    # Order taxi
    def click_order_button(self):
        WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.element_to_be_clickable(
                self.ORDER_BUTTON
            )
        ).click()

    def is_car_search_modal_displayed(self):
        modal = WebDriverWait(
            self.driver,
            10
        ).until(
            expected_conditions.visibility_of_element_located(
                self.CAR_SEARCH_MODAL
            )
        )

        return modal.is_displayed()

