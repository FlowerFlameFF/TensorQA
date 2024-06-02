class base_page():
    url = ''

    def __init__(self, browser):
        self.browser = browser

    def checkUrl(self):
        try:
            index = self.browser.current_url.index(self.url)
            return index == 0
        except:
            return False

    def open(self):
        self.browser.get(self.url)

    def find_element(self, locator):
        return self.browser.find_element(*locator)

    def find_elements(self, locator):
        return self.browser.find_elements(*locator)

    def select_last_page(self):
        window_handles = self.browser.window_handles
        self.browser.switch_to.window(window_handles[len(window_handles) - 1])

    def click(self, element):
        self.browser.execute_script('arguments[0].click()', element)

    def wait(self, sec=5):
        self.browser.implicitly_wait(sec)