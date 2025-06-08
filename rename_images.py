import os

def rename_images(folder, prefix):
    files = sorted(os.listdir(folder))
    count = 1
    for file in files:
        if file.lower().endswith(('.jpg', '.png', '.jpeg')):
            ext = os.path.splitext(file)[1]
            new_name = f"{prefix}_{count:03d}{ext}"
            os.rename(os.path.join(folder, file), os.path.join(folder, new_name))
            count += 1
    print(f"Renamed {count-1} files in {folder}.")

# 用法：
rename_images('positivesamples', 'pos')
rename_images('negativesamples', 'neg')
