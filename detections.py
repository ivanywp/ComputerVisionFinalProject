import cv2

# 讀入訓練好的模型
classifier = cv2.CascadeClassifier('data/cascade.xml')

# 讀入圖片
img = cv2.imread('pos_129.jpg')

# 圖片讀取失敗時顯示錯誤訊息
if img is None:
    print("❌ 圖片讀取失敗，請確認路徑或檔名 pos_129.jpg 是否正確")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 執行偵測
detections = classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f"✅ 偵測到 {len(detections)} 個物件")

# 畫出偵測到的區域
for (x, y, w, h) in detections:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# 顯示圖片
cv2.imshow("Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
