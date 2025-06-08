import os
import xml.etree.ElementTree as ET

xml_dir = 'annotations'
img_dir = 'positivesamples_resized'
output_file = 'positive.txt'

with open(output_file, 'w') as f:
    for xml_file in os.listdir(xml_dir):
        if not xml_file.endswith('.xml'):
            continue
        tree = ET.parse(os.path.join(xml_dir, xml_file))
        root = tree.getroot()
        filename = root.find('filename').text
        img_path = os.path.join(img_dir, filename)
        
        objects = root.findall('object')
        line = f"{img_path} {len(objects)}"
        for obj in objects:
            box = obj.find('bndbox')
            xmin = int(box.find('xmin').text)
            ymin = int(box.find('ymin').text)
            xmax = int(box.find('xmax').text)
            ymax = int(box.find('ymax').text)
            w = xmax - xmin
            h = ymax - ymin
            line += f" {xmin} {ymin} {w} {h}"
        f.write(line + '\n')

print("positive.txt generated.")
