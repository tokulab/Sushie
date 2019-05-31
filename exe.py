from sushi_handler.webauto import Sushidriver

sushi_cheat = Sushidriver()
while True:
    try:
        """
        ゲーム終了のオート検知 or
        KeyboardIntterpt拾って終了
        """
        sushi_cheat.solve()
    except:
        sushi_cheat.quit()
