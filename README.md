
# OpenCV 物件偵測 Final Project

## 專案說明

本專案利用 OpenCV 的 Haar Cascades 方法進行物件偵測訓練。目標是透過自行標記的影像資料，建立可偵測指定物件的分類器模型。

本專案流程包含資料蒐集、樣本標記、模型訓練與簡單的推論程式。

---

## 專案結構

```
finalproject/
├── positives/             # 正樣本圖像（129張）
├── negatives/             # 負樣本圖像（254張）
├── positives.vec          # 使用 opencv_createsamples 生成的正樣本二進位文件
├── negative.txt           # 負樣本影像的路徑列表
├── data/                  # 模型輸出資料夾
│   └── cascade.xml        # 訓練完成後的偵測模型
├── detections.py          # 測試模型的 Python 偵測程式
└── README.md              # 本文件
```

---

## 工具與版本

- Python 3.13.2
- OpenCV 4.11.0
- 作業系統：Windows 11（PowerShell 環境）

---

## 資料來源

- **正樣本**：手動標記的目標物圖像，共 129 張。
- **負樣本**：無目標物的背景圖像，共 254 張。
- 樣本尺寸統一為 `24x24`。

---

## 訓練流程

### 建立 `.vec` 檔：
```bash
opencv_createsamples -info positives.txt -vec positives.vec -num 129 -w 24 -h 24
```

### 開始訓練：
```bash
opencv_traincascade -data data -vec positives.vec -bg negative.txt -numPos 110 -numNeg 254 -numStages 10 -w 24 -h 24
```

> 實際成功訓練至第 2 stage，並輸出 `cascade.xml` 模型。

---

## 推論與測試程式

```python
import cv2

# 讀入訓練好的模型
classifier = cv2.CascadeClassifier('data/cascade.xml')

# 讀入測試影像
img = cv2.imread('pos_129.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 偵測物件
detections = classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

# 繪製偵測結果
for (x, y, w, h) in detections:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# 顯示影像（如失敗請參見備註）
cv2.imshow("Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## 備註與限制

由於開發環境限制，在 PowerShell 執行 `cv2.imshow()` 時未能成功顯示圖像視窗。但模型訓練與推論邏輯皆已完成並測試無錯誤。

> 可改用 `cv2.imwrite("output.jpg", img)` 將偵測結果存檔查看。

---

## 完成項目摘要

- [x] 正負樣本整理
- [x] `positive.vec` 產生成功
- [x] 模型訓練成功至第 2 stage
- [x] 成功輸出 `cascade.xml`
- [x] 撰寫推論程式並可執行
- [ ] 實時 GUI 展示（因 PowerShell GUI 限制未成功）

---

## 心得與反思

在本次專案中，深刻體會到樣本品質與數量對訓練結果的重要性。OpenCV 的 cascade 訓練工具對新手相對友好，但對資料格式與流程的要求極高。

雖然在時間與環境限制下無法完成所有視覺化呈現，但整體模型流程已成功跑通，對於了解基礎電腦視覺有很大幫助。

