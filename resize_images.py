from PIL import Image
import os

def resize_images(input_folder, output_folder, size=(640, 480)):
    os.makedirs(output_folder, exist_ok=True)
    for file in os.listdir(input_folder):
        if file.lower().endswith(('.jpg', '.png', '.jpeg')):
            img_path = os.path.join(input_folder, file)
            img = Image.open(img_path)
            img = img.resize(size)
            img.save(os.path.join(output_folder, file))
    print(f"Images resized to {size} and saved in {output_folder}.")

# 用法（依你的情況修改路徑與大小）：
resize_images('positivesamples', 'positivesamples_resized', size=(640, 480))
