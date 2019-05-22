import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + './sushi_handler/')
from .logger import Logger
from PIL import Image
import pyocr
import pyocr.builders as b

class ImgOcr():

    def __init__(self):
        self.temp_shots_folder = os.path.join(os.getcwd(),'sushi_handler', 'temp')
        self.log = Logger()
        self.tools = pyocr.get_available_tools()
        if len(self.tools) == 0:
            self.log.error('cant get ocr tools plz check your tesseract programs.')
            sys.exit(0)
        else:
            self.tool = self.tools[0]
            self.log.info('init ocr tool. {}'.format(self.tool.get_name()))

    def ditect(self, fname):
        try:
            croped_img = self.__crop_img(fname)
            inference_txt = self.tool.image_to_string(
                croped_img,
                lang='eng',
                builder=b.TextBuilder(tesseract_layout=6)
            )
        except Exception as e:
            sys.stderr.write(str(e))
            sys.exit(0)
        return inference_txt

    def __crop_img(self, fname):
        img = Image.open(fname)
        croped_img = img.crop((439, 709, 1072, 770))
        return croped_img