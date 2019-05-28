# 砂場
# ちょっとした動作テストとかするよ

with open('../.sushiLog') as log:
    latest_log = log.readlines()[-1].strip()
print(latest_log)
print(type(latest_log))
