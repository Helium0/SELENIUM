class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = "username"
        self.password_textbox_name = "password"
        self.login_button_XPATH = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

    def enter_username(self, username):
        self.driver.find_element(self.username_textbox_name).clear()
        self.driver.find_element(self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(self.password_textbox_name).clear()
        self.driver.find_element(self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_XPATH).click()