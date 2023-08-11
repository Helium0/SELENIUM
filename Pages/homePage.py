class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_by_XPATH = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span'
        self.logout_link_by_XPATH = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'

    def click_welcome(self):
        self.driver.find_element(self.welcome_link_by_XPATH).click()

    def click_logout(self):
        self.driver.find_element(self.logout_link_by_XPATH).click()
