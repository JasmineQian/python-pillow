"""
基础操作示例脚本
演示 Pillow 的基础图像操作功能
"""

import os
import sys

# 添加父目录到路径
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules import basic_operations


def main():
    print("=" * 60)
    print("  基础图像操作示例")
    print("=" * 60 + "\n")
    
    # 创建输出目录
    os.makedirs("output/examples", exist_ok=True)
    
    # 1. 创建纯色图像
    print("1. 创建纯色图像")
    red_img = basic_operations.create_new_image(400, 300, (255, 0, 0), 'RGB')
    green_img = basic_operations.create_new_image(400, 300, (0, 255, 0), 'RGB')
    blue_img = basic_operations.create_new_image(400, 300, (0, 0, 255), 'RGB')
    
    basic_operations.save_image(red_img, "output/examples/red.png")
    basic_operations.save_image(green_img, "output/examples/green.png")
    basic_operations.save_image(blue_img, "output/examples/blue.png")
    
    # 2. 创建渐变图像
    print("\n2. 创建渐变图像")
    gradient = basic_operations.create_gradient_image(600, 400)
    basic_operations.save_image(gradient, "output/examples/gradient.png")
    
    # 3. 获取图像信息
    print("\n3. 获取图像信息")
    info = basic_operations.get_image_info(gradient)
    
    # 4. 复制图像
    print("\n4. 复制图像")
    copied = basic_operations.copy_image(gradient)
    basic_operations.save_image(copied, "output/examples/copied.png")
    
    # 5. 模式转换
    print("\n5. 图像模式转换")
    gray = basic_operations.convert_mode(gradient, 'L')
    basic_operations.save_image(gray, "output/examples/grayscale.png")
    
    rgba = basic_operations.convert_mode(gradient, 'RGBA')
    basic_operations.save_image(rgba, "output/examples/rgba.png")
    
    # 6. 像素操作
    print("\n6. 像素级操作")
    pixel_img = basic_operations.create_new_image(400, 300, (255, 255, 255))
    
    # 获取像素值
    pixel_val = basic_operations.get_pixel(pixel_img, 100, 100)
    
    # 设置单个像素
    basic_operations.put_pixel(pixel_img, 200, 150, (255, 0, 0))
    
    # 绘制一条像素线
    for x in range(50, 350):
        basic_operations.put_pixel(pixel_img, x, 150, (0, 0, 255))
    
    basic_operations.save_image(pixel_img, "output/examples/pixel_operations.png")
    
    # 7. 创建彩虹图像
    print("\n7. 创建彩虹效果")
    rainbow = basic_operations.create_new_image(400, 300, (255, 255, 255))
    
    for y in range(300):
        # 计算彩虹颜色
        if y < 50:
            color = (255, 0, 0)  # 红
        elif y < 100:
            color = (255, 127, 0)  # 橙
        elif y < 150:
            color = (255, 255, 0)  # 黄
        elif y < 200:
            color = (0, 255, 0)  # 绿
        elif y < 250:
            color = (0, 0, 255)  # 蓝
        else:
            color = (75, 0, 130)  # 靛
        
        for x in range(400):
            basic_operations.put_pixel(rainbow, x, y, color)
    
    basic_operations.save_image(rainbow, "output/examples/rainbow.png")
    
    print("\n" + "=" * 60)
    print("  ✓ 基础操作示例完成！")
    print("  查看 output/examples/ 目录")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()

