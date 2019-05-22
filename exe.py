from sushi_handler.webauto import Sushidriver

sushi_cheat = Sushidriver()
while True:
    try:
        '''ctrl+cでKeyboadInterruptを拾って終了'''
        sushi_cheat.solve()
    except:
        sushi_cheat.quit()