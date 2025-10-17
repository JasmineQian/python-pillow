"""
图像变换示例脚本
演示 Pillow 的各种图像变换功能
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules import basic_operations, transformations


def main():
    print("=" * 60)
    print("  图像变换示例")
    print("=" * 60 + "\n")
    
    os.makedirs("output/examples", exist_ok=True)
    
    # 创建测试图像
    test_img = basic_operations.create_gradient_image(400, 300)
    
    # 1. 大小调整
    print("1. 调整图像大小")
    resized_large = transformations.resize_image(test_img, 800, 600)
    basic_operations.save_image(resized_large, "output/examples/resized_large.png")
    
    resized_small = transformations.resize_image(test_img, 200, 150)
    basic_operations.save_image(resized_small, "output/examples/resized_small.png")
    
    # 按比例缩放
    scaled_50 = transformations.resize_by_ratio(test_img, 0.5)
    basic_operations.save_image(scaled_50, "output/examples/scaled_50.png")
    
    scaled_150 = transformations.resize_by_ratio(test_img, 1.5)
    basic_operations.save_image(scaled_150, "output/examples/scaled_150.png")
    
    # 2. 旋转
    print("\n2. 旋转图像")
    for angle in [30, 60, 90, 120, 180]:
        rotated = transformations.rotate_image(test_img, angle, expand=True)
        basic_operations.save_image(
            rotated, f"output/examples/rotated_{angle}.png"
        )
    
    # 3. 裁剪
    print("\n3. 裁剪图像")
    # 裁剪左上角
    crop_tl = transformations.crop_image(test_img, 0, 0, 200, 150)
    basic_operations.save_image(crop_tl, "output/examples/crop_topleft.png")
    
    # 裁剪中心
    crop_center = transformations.crop_center(test_img, 200, 200)
    basic_operations.save_image(crop_center, "output/examples/crop_center.png")
    
    # 4. 翻转
    print("\n4. 翻转图像")
    h_flip = transformations.flip_horizontal(test_img)
    basic_operations.save_image(h_flip, "output/examples/flip_horizontal.png")
    
    v_flip = transformations.flip_vertical(test_img)
    basic_operations.save_image(v_flip, "output/examples/flip_vertical.png")
    
    # 5. 缩略图
    print("\n5. 创建缩略图")
    for size in [64, 128, 256]:
        thumb = transformations.create_thumbnail(test_img, (size, size))
        basic_operations.save_image(
            thumb, f"output/examples/thumbnail_{size}.png"
        )
    
    # 6. 适配和填充
    print("\n6. 适配和填充")
    fitted = transformations.fit_image(test_img, 300, 300)
    basic_operations.save_image(fitted, "output/examples/fitted_300x300.png")
    
    padded = transformations.pad_image(test_img, 600, 600, (100, 100, 100))
    basic_operations.save_image(padded, "output/examples/padded_600x600.png")
    
    # 7. 转置操作
    print("\n7. 转置操作")
    from PIL import Image
    
    transpose_90 = transformations.transpose_image(test_img, Image.ROTATE_90)
    basic_operations.save_image(transpose_90, "output/examples/transpose_90.png")
    
    transpose_180 = transformations.transpose_image(test_img, Image.ROTATE_180)
    basic_operations.save_image(transpose_180, "output/examples/transpose_180.png")
    
    # 8. 创建变换序列动画
    print("\n8. 创建变换序列")
    frames = []
    for i in range(8):
        angle = i * 45
        frame = transformations.rotate_image(test_img, angle, expand=False)
        frames.append(frame)
        basic_operations.save_image(
            frame, f"output/examples/rotation_seq_{i:02d}.png"
        )
    
    print("\n" + "=" * 60)
    print("  ✓ 图像变换示例完成！")
    print("  查看 output/examples/ 目录")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()

