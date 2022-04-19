from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        print('TEST: Should be login page')
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        print(f'Begin registration new user:{email} , password:{password}')
        email_input = self.should_be_registration_email()
        password1_input = self.should_be_registration_password1()
        password2_input = self.should_be_registration_password2()
        button = self.should_be_registration_submit_button()
        email_input.send_keys(email)
        password1_input.send_keys(password)
        password2_input.send_keys(password)
        print(f'Click to button "{button.text}"')
        button.click()

    def should_be_login_url(self):
        self.url_should_contain('/login/')

    def should_be_login_form(self):
        print('Try to find Login form...', end='')
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not present on Login page'
        print('ok')

    def should_be_register_form(self):
        print('Try to find Registration form...', end='')
        assert self.is_element_present(*LoginPageLocators.REG_FORM), 'Registration form is not present on Login page'
        print('ok')

    def should_be_registration_email(self):
        print('Try to find field "Registration login (e-mail)"...', end='')
        email_input = self.is_element_present(*LoginPageLocators.REG_LOGIN)
        assert email_input, 'Field "User E-mail" not found on login page'
        print('ok')
        return email_input

    def should_be_registration_password1(self):
        print('Try to find field "Registration password"...', end='')
        pass1 = self.is_element_present(*LoginPageLocators.REG_PASSWORD1)
        assert pass1, 'Field "Registration password" not found on login page'
        print('ok')
        return pass1

    def should_be_registration_password2(self):
        print('Try to find field "Confirm password"...', end='')
        pass2 = self.is_element_present(*LoginPageLocators.REG_PASSWORD2)
        assert pass2, 'Field "Confirm password" not found on login page'
        print('ok')
        return pass2

    def should_be_registration_submit_button(self):
        print('Try to find button "Register new user (Submit)"...', end='')
        button = self.is_element_present(*LoginPageLocators.REG_BUTTON)
        assert button, 'Button "Register new user (Submit)" not found on login page'
        print('ok')
        return button

    def should_not_be_registration_error_messages(self):
        print('Verify registration. Is there any errors?...', end='')
        assert self.is_not_element_present(*LoginPageLocators.REG_MESSAGE_ERROR),\
            'Some errors found after click "Register" button. Registration not completed'
        print('Error message not found.')


