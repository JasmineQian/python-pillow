"""
滤镜效果示例脚本
演示 Pillow 的各种滤镜和图像增强功能
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules import basic_operations, filters_effects


def main():
    print("=" * 60)
    print("  滤镜和效果示例")
    print("=" * 60 + "\n")
    
    os.makedirs("output/examples", exist_ok=True)
    
    # 创建测试图像
    test_img = basic_operations.create_gradient_image(400, 300)
    
    # 1. 模糊效果
    print("1. 模糊效果")
    for radius in [2, 5, 10]:
        blurred = filters_effects.apply_blur(test_img, radius=radius)
        basic_operations.save_image(
            blurred, f"output/examples/blur_r{radius}.png"
        )
    
    box_blur = filters_effects.apply_box_blur(test_img, radius=5)
    basic_operations.save_image(box_blur, "output/examples/box_blur.png")
    
    # 2. 锐化和边缘
    print("\n2. 锐化和边缘检测")
    sharpened = filters_effects.apply_sharpen(test_img)
    basic_operations.save_image(sharpened, "output/examples/sharpened.png")
    
    edge_enhance = filters_effects.apply_edge_enhance(test_img)
    basic_operations.save_image(edge_enhance, "output/examples/edge_enhance.png")
    
    edges = filters_effects.apply_find_edges(test_img)
    basic_operations.save_image(edges, "output/examples/find_edges.png")
    
    # 3. 艺术效果
    print("\n3. 艺术效果")
    embossed = filters_effects.apply_emboss(test_img)
    basic_operations.save_image(embossed, "output/examples/emboss.png")
    
    contour = filters_effects.apply_contour(test_img)
    basic_operations.save_image(contour, "output/examples/contour.png")
    
    detail = filters_effects.apply_detail(test_img)
    basic_operations.save_image(detail, "output/examples/detail.png")
    
    # 4. 亮度调整
    print("\n4. 亮度调整")
    for factor in [0.5, 0.75, 1.0, 1.25, 1.5, 2.0]:
        adjusted = filters_effects.adjust_brightness(test_img, factor)
        basic_operations.save_image(
            adjusted, f"output/examples/brightness_{int(factor*100)}.png"
        )
    
    # 5. 对比度调整
    print("\n5. 对比度调整")
    for factor in [0.5, 1.0, 1.5, 2.0]:
        adjusted = filters_effects.adjust_contrast(test_img, factor)
        basic_operations.save_image(
            adjusted, f"output/examples/contrast_{int(factor*100)}.png"
        )
    
    # 6. 饱和度调整
    print("\n6. 饱和度调整")
    for factor in [0.0, 0.5, 1.0, 1.5, 2.0]:
        adjusted = filters_effects.adjust_saturation(test_img, factor)
        basic_operations.save_image(
            adjusted, f"output/examples/saturation_{int(factor*100)}.png"
        )
    
    # 7. 锐度调整
    print("\n7. 锐度调整")
    for factor in [0.0, 0.5, 1.0, 2.0]:
        adjusted = filters_effects.adjust_sharpness(test_img, factor)
        basic_operations.save_image(
            adjusted, f"output/examples/sharpness_{int(factor*100)}.png"
        )
    
    # 8. 平滑效果
    print("\n8. 平滑效果")
    smooth = filters_effects.apply_smooth(test_img)
    basic_operations.save_image(smooth, "output/examples/smooth.png")
    
    smooth_more = filters_effects.apply_smooth_more(test_img)
    basic_operations.save_image(smooth_more, "output/examples/smooth_more.png")
    
    # 9. 滤波器
    print("\n9. 各种滤波器")
    median = filters_effects.apply_median_filter(test_img, size=5)
    basic_operations.save_image(median, "output/examples/median_filter.png")
    
    min_filter = filters_effects.apply_min_filter(test_img, size=3)
    basic_operations.save_image(min_filter, "output/examples/min_filter.png")
    
    max_filter = filters_effects.apply_max_filter(test_img, size=3)
    basic_operations.save_image(max_filter, "output/examples/max_filter.png")
    
    # 10. 反锐化遮罩
    print("\n10. 反锐化遮罩（专业锐化）")
    for percent in [50, 100, 150, 200]:
        unsharp = filters_effects.apply_unsharp_mask(
            test_img, radius=2, percent=percent, threshold=3
        )
        basic_operations.save_image(
            unsharp, f"output/examples/unsharp_{percent}.png"
        )
    
    # 11. 组合效果
    print("\n11. 组合多种效果")
    combined = test_img.copy()
    combined = filters_effects.adjust_brightness(combined, 1.2)
    combined = filters_effects.adjust_contrast(combined, 1.3)
    combined = filters_effects.adjust_saturation(combined, 1.5)
    combined = filters_effects.apply_unsharp_mask(combined, radius=2, percent=120)
    basic_operations.save_image(combined, "output/examples/combined_effects.png")
    
    print("\n" + "=" * 60)
    print("  ✓ 滤镜效果示例完成！")
    print("  查看 output/examples/ 目录")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()

