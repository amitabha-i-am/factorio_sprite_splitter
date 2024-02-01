import os
from PIL import Image
folder_name = 'running_gun_shadow'
folder = r"C:\tmp"
folder_path = os.path.join(folder, folder_name)

folder_names = [str(i+1) for i in range(len(os.listdir(folder_path))-1)]

image_paths = []
for fold in folder_names:
    temp_path = os.path.join(folder_path, fold)
    temp_folder = os.listdir(temp_path)
    for image in temp_folder:
        image_path = os.path.join(temp_path, image)
        image_paths.append(image_path)

print(image_paths)

offset_h = 160
offset_w = 150
size_h = offset_h * len(folder_names)
size_w = int(len(image_paths) / len(folder_names) * offset_w)

background = Image.new('RGBA', (size_w, size_h), (255, 255, 255, 0))
tmp_size_h = 0
tmp_size_w = 0
for i in range(len(image_paths)):
    img = Image.open(image_paths[i])
    background.paste(img, [tmp_size_w, tmp_size_h])
    tmp_size_w += offset_w
    if tmp_size_w == size_w:
        tmp_size_w = 0
        tmp_size_h += offset_h

background.save(os.path.join(folder_path, folder_name) + '.png')
