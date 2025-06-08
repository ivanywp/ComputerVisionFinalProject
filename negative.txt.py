import os

neg_img_dir = 'negativesamples'  # 你的負樣本圖片資料夾
output_file = 'negative.txt'     # 輸出負樣本txt檔名

with open(output_file, 'w') as f:
    for img_file in os.listdir(neg_img_dir):
        if img_file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            img_path = os.path.join(neg_img_dir, img_file)
            f.write(img_path + '\n')

print(f"{output_file} 生成完成。")

#opencv_traincascade -data data -vec positives.vec -bg negative.txt -numPos 120 -numNeg 254 -numStages 10 -w 24 -h 24 