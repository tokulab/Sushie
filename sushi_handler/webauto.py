import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from logger import Logger

class Webdriver():
    def __init__(self, window_size):
        self.log = Logger(self.__class__.__name__)
        try:
            self.driver = webdriver.Chrome()
            self.driver.set_window_size(window_size[0], window_size[1])
            self.log.info('init webdriver.')
            self.action = ActionChains(self.driver)
            self.log.info('init action.')
        except Exception as e:
            self.log.error('cant read chromedriver.', e)
            sys.exit(0)

    def render(self, url):
        self.driver.get(url=url)

    def wait(self, sec):
        self.driver.implicitly_wait(sec)

    def gomi_kasu_wait(self, sec):
        '''クソゴミ　悪手　カスコード　最終手段'''
        from time import sleep
        sleep(sec)


    def get_element(self, type, query):
        type_dic = {
            'id': By.ID,
            'class': By.CLASS_NAME,
            'css': By.CSS_SELECTOR,
            'name': By.NAME,
        }
        element = self.driver.find_element(type_dic[type], query)
        return element

    def click_point(self, x, y, click_mode='right'):
        self.action.move_by_offset(x, y)
        print(x, y)
        self.action.click()
        self.action.perform()

    def suicide(self):
        self.log.info('quit webdriver.')
        self.driver.quit()

class Sushidriver(Webdriver):
    def __init__(self):
        try:
            super().__init__(window_size=(765, 800))
            self.render('http://typingx0.net/sushida/play.html?soundless')
            sushida = self.get_element(type='id', query='#canvas')

            # self.wait(5)
            self.gomi_kasu_wait(9)
            self.click_point(sushida.location['x'] + 302, sushida.location['y'] + 260)
            self.gomi_kasu_wait(5)
        finally:
            self.suicide()




if __name__ == '__main__':
    w = Sushidriver()