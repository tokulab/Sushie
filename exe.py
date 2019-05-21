import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '..')
from sushi_handler.webauto import Sushidriver

sushi_cheat = Sushidriver()
sushi_cheat.solve()