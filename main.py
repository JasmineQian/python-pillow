"""
Pillow 学习项目 - 主程序
运行所有模块的示例代码，展示Pillow的各种功能
"""

import os
import sys

# 添加模块路径
sys.path.append(os.path.dirname(__file__))

from modules import (
    basic_operations,
    transformations,
    filters_effects,
    drawing,
    color_operations,
    composition,
    text_operations,
    advanced
)


def create_directories():
    """创建必要的目录"""
    dirs = ['input', 'output', 'output/examples']
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
    print("✓ 已创建必要的目录\n")


def print_section(title):
    """打印章节标题"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60 + "\n")


def run_basic_operations():
    """运行基础操作示例"""
    print_section("1. 基础图像操作")
    
    # 创建新图像
    red_img = basic_operations.create_new_image(400, 300, (255, 0, 0))
    basic_operations.save_image(red_img, "output/01_red_image.png")
    
    # 创建渐变图像
    gradient = basic_operations.create_gradient_image(400, 300)
    basic_operations.save_image(gradient, "output/02_gradient.png")
    
    # 获取图像信息
    basic_operations.get_image_info(red_img)
    
    print("✓ 基础操作完成")
    return gradient  # 返回用于后续测试


def run_transformations(img):
    """运行图像变换示例"""
    print_section("2. 图像变换")
    
    # 调整大小
    resized = transformations.resize_image(img, 200, 150)
    basic_operations.save_image(resized, "output/03_resized.png")
    
    # 旋转
    rotated = transformations.rotate_image(img, 45, expand=True)
    basic_operations.save_image(rotated, "output/04_rotated.png")
    
    # 裁剪
    cropped = transformations.crop_center(img, 200, 200)
    basic_operations.save_image(cropped, "output/05_cropped.png")
    
    # 翻转
    flipped = transformations.flip_horizontal(img)
    basic_operations.save_image(flipped, "output/06_flipped.png")
    
    # 缩略图
    thumbnail = transformations.create_thumbnail(img, (128, 128))
    basic_operations.save_image(thumbnail, "output/07_thumbnail.png")
    
    print("✓ 图像变换完成")


def run_filters(img):
    """运行滤镜效果示例"""
    print_section("3. 滤镜和效果")
    
    # 模糊
    blurred = filters_effects.apply_blur(img, radius=5)
    basic_operations.save_image(blurred, "output/08_blurred.png")
    
    # 锐化
    sharpened = filters_effects.apply_sharpen(img)
    basic_operations.save_image(sharpened, "output/09_sharpened.png")
    
    # 边缘检测
    edges = filters_effects.apply_find_edges(img)
    basic_operations.save_image(edges, "output/10_edges.png")
    
    # 浮雕
    embossed = filters_effects.apply_emboss(img)
    basic_operations.save_image(embossed, "output/11_embossed.png")
    
    # 亮度调整
    brighter = filters_effects.adjust_brightness(img, 1.5)
    basic_operations.save_image(brighter, "output/12_brighter.png")
    
    # 对比度调整
    high_contrast = filters_effects.adjust_contrast(img, 2.0)
    basic_operations.save_image(high_contrast, "output/13_high_contrast.png")
    
    print("✓ 滤镜效果完成")


def run_drawing():
    """运行绘图功能示例"""
    print_section("4. 绘图功能")
    
    canvas = basic_operations.create_new_image(600, 400, (255, 255, 255))
    
    # 绘制矩形
    img_rect = drawing.draw_rectangle(canvas, [100, 100, 300, 200], 
                                     fill=(200, 200, 255), outline=(0, 0, 255), width=3)
    basic_operations.save_image(img_rect, "output/14_rectangle.png")
    
    # 绘制圆形
    img_circle = drawing.draw_circle(canvas, (300, 200), 80, 
                                    fill=(255, 200, 200), outline=(255, 0, 0), width=3)
    basic_operations.save_image(img_circle, "output/15_circle.png")
    
    # 绘制多边形
    triangle = [(300, 100), (200, 300), (400, 300)]
    img_poly = drawing.draw_polygon(canvas, triangle, 
                                   fill=(200, 255, 200), outline=(0, 255, 0), width=3)
    basic_operations.save_image(img_poly, "output/16_polygon.png")
    
    # 绘制文字
    img_text = drawing.draw_text(canvas, (200, 180), "Hello Pillow!", 
                                fill=(0, 0, 0), font_size=40)
    basic_operations.save_image(img_text, "output/17_text.png")
    
    # 组合绘图
    combined = canvas.copy()
    combined = drawing.draw_circle(combined, (150, 150), 50, 
                                  fill=(255, 100, 100), outline=(200, 0, 0), width=2)
    combined = drawing.draw_circle(combined, (450, 150), 50, 
                                  fill=(100, 255, 100), outline=(0, 200, 0), width=2)
    combined = drawing.draw_text(combined, (200, 320), "Combined Drawing", 
                                fill=(0, 0, 0), font_size=30)
    basic_operations.save_image(combined, "output/18_combined_drawing.png")
    
    print("✓ 绘图功能完成")


def run_color_operations(img):
    """运行颜色操作示例"""
    print_section("5. 颜色操作")
    
    # 灰度转换
    gray = color_operations.convert_to_grayscale(img)
    basic_operations.save_image(gray, "output/19_grayscale.png")
    
    # 反转颜色
    inverted = color_operations.invert_colors(img)
    basic_operations.save_image(inverted, "output/20_inverted.png")
    
    # 色调分离
    posterized = color_operations.posterize(img, bits=3)
    basic_operations.save_image(posterized, "output/21_posterized.png")
    
    # 曝光效果
    solarized = color_operations.solarize(img, threshold=128)
    basic_operations.save_image(solarized, "output/22_solarized.png")
    
    # 分离通道
    r, g, b = color_operations.split_channels(img)
    basic_operations.save_image(r, "output/23_channel_red.png")
    basic_operations.save_image(g, "output/24_channel_green.png")
    basic_operations.save_image(b, "output/25_channel_blue.png")
    
    # 棕褐色效果
    sepia = color_operations.apply_sepia(img)
    basic_operations.save_image(sepia, "output/26_sepia.png")
    
    print("✓ 颜色操作完成")


def run_composition(img):
    """运行图像合成示例"""
    print_section("6. 图像合成")
    
    img2 = basic_operations.create_new_image(400, 300, (255, 100, 100))
    
    # 混合图像
    blended = composition.blend_images(img, img2, alpha=0.5)
    basic_operations.save_image(blended, "output/27_blended.png")
    
    # 创建渐变遮罩并合成
    mask = composition.create_gradient_mask(400, 300, 'horizontal')
    composited = composition.composite_images(img, img2, mask)
    basic_operations.save_image(composited, "output/28_composite_gradient.png")
    
    # 圆形遮罩
    circle_mask = composition.create_circular_mask(400, 300)
    circle_comp = composition.composite_images(img, img2, circle_mask)
    basic_operations.save_image(circle_comp, "output/29_composite_circle.png")
    
    # 图像运算
    multiplied = composition.multiply_images(img, img2)
    basic_operations.save_image(multiplied, "output/30_multiplied.png")
    
    print("✓ 图像合成完成")


def run_text_operations(img):
    """运行文字操作示例"""
    print_section("7. 文字操作")
    
    # 添加水印
    watermarked = text_operations.add_text_watermark(
        img, "© 2024", position='bottom-right', font_size=20
    )
    basic_operations.save_image(watermarked, "output/31_watermarked.png")
    
    # 居中文字
    centered = text_operations.add_centered_text(
        img, "CENTERED", font_size=60, color=(255, 255, 255)
    )
    basic_operations.save_image(centered, "output/32_centered_text.png")
    
    # 多行文字
    multiline = text_operations.add_multiline_text(
        img, "Line 1\nLine 2\nLine 3", 
        position=(50, 50), font_size=30, color=(255, 255, 255)
    )
    basic_operations.save_image(multiline, "output/33_multiline_text.png")
    
    # 带背景的文字
    text_bg = text_operations.add_text_with_background(
        img, "Text with BG", position=(150, 130), font_size=35,
        text_color=(255, 255, 255), bg_color=(255, 0, 0), padding=15
    )
    basic_operations.save_image(text_bg, "output/34_text_with_bg.png")
    
    # 纯文字图像
    text_img = text_operations.create_text_image(
        "Hello Pillow!", width=400, height=200, font_size=40
    )
    basic_operations.save_image(text_img, "output/35_text_image.png")
    
    print("✓ 文字操作完成")


def run_advanced(img):
    """运行高级功能示例"""
    print_section("8. 高级功能")
    
    # 获取统计信息
    stats = advanced.get_statistics(img)
    
    # 颜色量化
    quantized = advanced.quantize_colors(img, colors=16)
    basic_operations.save_image(quantized.convert('RGB'), "output/36_quantized.png")
    
    # 马赛克效果
    mosaic = advanced.create_mosaic(img, pixel_size=15)
    basic_operations.save_image(mosaic, "output/37_mosaic.png")
    
    # 创建调色板
    colors = [
        (255, 0, 0), (0, 255, 0), (0, 0, 255),
        (255, 255, 0), (255, 0, 255), (0, 255, 255)
    ]
    palette = advanced.create_palette_image(colors, 400, 100)
    basic_operations.save_image(palette, "output/38_palette.png")
    
    # 创建GIF动画
    frames = []
    base_img = basic_operations.create_new_image(200, 200, (100, 150, 200))
    for angle in range(0, 360, 45):
        rotated = transformations.rotate_image(base_img, angle, expand=False)
        frames.append(rotated)
    
    advanced.create_animated_gif(
        frames, "output/39_animation.gif", duration=200, loop=0
    )
    
    # 创建缩略图网格
    grid_images = []
    test_colors = [
        (255, 100, 100), (100, 255, 100), (100, 100, 255),
        (255, 255, 100), (255, 100, 255), (100, 255, 255)
    ]
    for color in test_colors:
        grid_images.append(basic_operations.create_new_image(150, 150, color))
    
    grid = advanced.create_thumbnail_grid(
        grid_images, grid_size=(3, 2), thumb_size=(120, 120)
    )
    basic_operations.save_image(grid, "output/40_thumbnail_grid.png")
    
    print("✓ 高级功能完成")


def create_comprehensive_demo():
    """创建综合演示"""
    print_section("综合演示 - 组合多种效果")
    
    # 创建基础图像
    img = basic_operations.create_gradient_image(800, 600)
    
    # 应用多种效果
    img = filters_effects.adjust_brightness(img, 1.2)
    img = filters_effects.adjust_contrast(img, 1.3)
    img = filters_effects.adjust_saturation(img, 1.5)
    
    # 添加形状
    img = drawing.draw_circle(img, (200, 150), 80, 
                             fill=(255, 200, 200), outline=(255, 0, 0), width=4)
    img = drawing.draw_rectangle(img, [500, 100, 700, 300], 
                                fill=(200, 200, 255), outline=(0, 0, 255), width=4)
    
    # 添加文字
    img = text_operations.add_text_with_background(
        img, "PILLOW DEMO", position=(250, 50), font_size=50,
        text_color=(255, 255, 255), bg_color=(0, 0, 0), padding=20
    )
    
    img = text_operations.add_text_watermark(
        img, "© Pillow Learning Project", 
        position='bottom-right', font_size=18
    )
    
    basic_operations.save_image(img, "output/00_comprehensive_demo.png")
    print("✓ 综合演示完成")


def print_summary():
    """打印总结"""
    print("\n" + "=" * 60)
    print("  🎉 所有示例运行完成！")
    print("=" * 60)
    print("\n📁 输出文件位置: output/ 目录")
    print("\n📚 学习建议:")
    print("  1. 查看 output/ 目录中生成的图像")
    print("  2. 阅读 modules/ 目录中各模块的源代码")
    print("  3. 尝试修改参数，观察不同效果")
    print("  4. 运行单独的示例脚本: python examples/run_basic.py")
    print("\n💡 提示:")
    print("  - 每个模块都可以单独运行: python -m modules.basic_operations")
    print("  - 查看 README.md 了解更多信息")
    print("\n" + "=" * 60 + "\n")


def main():
    """主函数"""
    print("\n" + "=" * 60)
    print("  🎨 Pillow 图像处理学习项目")
    print("  欢迎使用！这个程序将演示 Pillow 的各种功能")
    print("=" * 60)
    
    # 创建目录
    create_directories()
    
    try:
        # 运行各模块示例
        test_img = run_basic_operations()
        run_transformations(test_img)
        run_filters(test_img)
        run_drawing()
        run_color_operations(test_img)
        run_composition(test_img)
        run_text_operations(test_img)
        run_advanced(test_img)
        
        # 综合演示
        create_comprehensive_demo()
        
        # 打印总结
        print_summary()
        
        return 0
        
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())

