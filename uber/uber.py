# 讓司機選擇起訖地點和沿途經過的常用地點
start = input("請輸入起點：")
end = input("請輸入目的地：")
waypoints = {}
while True:
    location = input("請輸入經過的常用地點（按Enter跳過）：")
    if location == "":
        break
    time = input("請輸入到達時間（例如13:30）：")
    waypoints[location] = time

# 設定發車時間
departure_time = input("請輸入發車時間（例如14:00）：")

# 輸出司機的行程安排
print("起點：", start)
print("目的地：", end)
print("常用地點：")
for location, time in waypoints.items():
    print("-", location, "（到達時間：", time, "）")
print("發車時間：", departure_time)
