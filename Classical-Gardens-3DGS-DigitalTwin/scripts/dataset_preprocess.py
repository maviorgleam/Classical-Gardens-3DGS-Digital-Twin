"""
图像采集与数据集标准化处理
"""

import os
import cv2
import csv
from pathlib import Path

INPUT_FOLDER = "./raw_images"          
OUTPUT_FOLDER = "./processed_images"  
TARGET_RESOLUTION = (1920, 1080)       
SUPPORTED_FORMATS = ('.jpg', '.jpeg', '.png')

def get_image_files(folder_path):
    """获取文件夹内所有支持格式的图像文件"""
    image_list = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(SUPPORTED_FORMATS):
                image_list.append(os.path.join(root, file))
    return sorted(image_list)

def resize_and_save(image_path, output_path, target_size):
    """统一图像分辨率，保持长宽比，填充空白区域"""
    img = cv2.imread(image_path)
    if img is None:
        return False
    
    h, w = img.shape[:2]
    target_w, target_h = target_size
    scale = min(target_w / w, target_h / h)
    new_w, new_h = int(w * scale), int(h * scale)
    
    resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)
    
    # 居中填充
    canvas = np.zeros((target_h, target_w, 3), dtype=np.uint8)
    x_offset = (target_w - new_w) 
    y_offset = (target_h - new_h) 
    canvas[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = resized
    
    cv2.imwrite(output_path, canvas)
    return True

def generate_capture_manifest(image_list, output_csv):
    """生成采集清单，记录每张图像的基本信息，用于3DGS训练输入校验"""
    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["image_id", "file_name", "width", "height", "valid"])
        
        for idx, img_path in enumerate(image_list):
            img = cv2.imread(img_path)
            if img is None:
                valid = False
                h, w = 0, 0
            else:
                valid = True
                h, w = img.shape[:2]
            
            writer.writerow([
                f"img_{idx:04d}",
                os.path.basename(img_path),
                w, h, valid
            ])

if __name__ == "__main__":
    import numpy as np
    
    Path(OUTPUT_FOLDER).mkdir(exist_ok=True)

    # 1. 获取原始图像
    raw_images = get_image_files(INPUT_FOLDER)
    print(f"找到原始图像：{len(raw_images)} 张")
    
    # 2. 批量分辨率统一
    valid_count = 0
    for idx, img_path in enumerate(raw_images):
        file_name = f"scene_{idx:04d}.jpg"
        output_path = os.path.join(OUTPUT_FOLDER, file_name)
        success = resize_and_save(img_path, output_path, TARGET_RESOLUTION)
        if success:
            valid_count += 1
    
    print(f"成功处理图像：{valid_count} 张")
    
    # 3. 生成采集清单
    manifest_path = "./capture_manifest.csv"
    generate_capture_manifest(raw_images, manifest_path)
    print(f"采集清单已生成：{manifest_path}")
