import os
import sys
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + './sushi_handler/')
from .logger import Logger
from .sushi_ocr import ImgOcr


class Webdriver():
    """
    Sushidriver用API
    実質seleniumのラッパーライブラリ
    """
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
        '''なるべくwait()使った方が時間効率が良い'''
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

    def click_point(self, x, y, element=None, click_mode='right'):
        if not element:
            self.action.move_by_offset(x, y)
            self.action.click()
        else:
            self.action.move_to_element_with_offset(to_element=element,xoffset=x, yoffset=y)
            self.action.click()
        self.action.perform()
        self.log.info('clicked x:{}, y:{}'.format(x, y))

    def push_key(self, key, word=None, delay_mode=False):
        keys_dic = {
            'enter': Keys.ENTER,
            'space': Keys.SPACE,
            'string': str(word),
        }
        self.action.send_keys(keys_dic[key])
        self.action.perform()
        self.log.info('pushed {} key.'.format(key if word==None else word))

    def screen_shot(self, element=None, crop=True, name='__rand_mode'):
        '''
        elementを撮影する.screenshot()がwebdriverのバージョンによって機能しない
        chrome以外にする or ウィンドウ全体を撮るのがベター
        '''
        if name == '__rand_mode':
            name = str(random.random()).replace('.', '')
        temp_shots_folder = os.path.join(os.getcwd(),'sushi_handler', 'temp')
        os.makedirs(temp_shots_folder, exist_ok=True)
        '''
        if element != None:
            element.screenshot(filename=os.path.join(temp_shots_folder, name + '.png'))
            self.log.info('captured screenshot.')
        '''
        fname = os.path.join(temp_shots_folder, name + '.png')
        self.driver.save_screenshot(filename=os.path.join(temp_shots_folder, name + '.png'))
        self.log.info('captured screenshot.')
        return fname

    def suicide(self):
        self.log.info('quit webdriver.')
        self.driver.quit()


class Sushidriver(Webdriver, ImgOcr):
    """
    寿司打実行クラス
    インスタンス化と同時にゲームスタート
    """
    def __init__(self):
        try:
            Webdriver.__init__(self, window_size=(765, 800))
            ImgOcr.__init__(self)
            self.render('http://typingx0.net/sushida/play.html')
            sushida = self.get_element(type='id', query='#canvas')
            self.gomi_kasu_wait(7)
            self.click_point(sushida.location['x'] + 302, sushida.location['y'] + 260)
            self.gomi_kasu_wait(1)
            self.click_point(sushida.location['x'] + 250, sushida.location['y'] + 200, sushida)
            self.gomi_kasu_wait(1)
            self.push_key('enter', sushida)
            self.gomi_kasu_wait(3)
            self.sushida = sushida  #寿司打のelement(canvas)
        except Exception as e:
            sys.stderr.write(str(e))
            sys.exit(0)

    def solve(self):
        fname = self.screen_shot()
        txt = self.ditect(fname)
        self.log.info('get text: {}'.format(txt))
        self.push_key(key='string', word=txt)

    def miss(self):
        pass

    def quit(self):
        import shutil
        shutil.rmtree(os.path.join(os.getcwd(),'sushi_handler', 'temp'))
        self.log.info('quitting sushidriver good bye!')
        sys.exit(0)