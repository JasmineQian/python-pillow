"""
颜色操作模块
包含灰度转换、颜色模式转换、颜色分离合并等功能
"""

from PIL import Image, ImageOps


def convert_to_grayscale(img):
    """
    转换为灰度图像
    
    参数:
        img: Image对象
    
    返回:
        灰度图像
    """
    print("转换为灰度图像")
    return img.convert('L')


def convert_to_black_and_white(img, threshold=128):
    """
    转换为黑白图像（二值化）
    
    参数:
        img: Image对象
        threshold: 阈值 (0-255)
    
    返回:
        黑白图像
    """
    print(f"转换为黑白图像: 阈值 {threshold}")
    gray = img.convert('L')
    return gray.point(lambda x: 255 if x > threshold else 0, mode='1')


def invert_colors(img):
    """
    反转颜色
    
    参数:
        img: Image对象
    
    返回:
        反转后的图像
    """
    print("反转颜色")
    return ImageOps.invert(img.convert('RGB'))


def posterize(img, bits=4):
    """
    色调分离（减少颜色数量）
    
    参数:
        img: Image对象
        bits: 保留的位数 (1-8)
    
    返回:
        色调分离后的图像
    """
    print(f"色调分离: 保留 {bits} 位")
    return ImageOps.posterize(img, bits)


def solarize(img, threshold=128):
    """
    曝光过度效果
    
    参数:
        img: Image对象
        threshold: 阈值 (0-255)
    
    返回:
        曝光效果后的图像
    """
    print(f"曝光过度效果: 阈值 {threshold}")
    return ImageOps.solarize(img, threshold)


def equalize_histogram(img):
    """
    直方图均衡化（增强对比度）
    
    参数:
        img: Image对象
    
    返回:
        均衡化后的图像
    """
    print("直方图均衡化")
    return ImageOps.equalize(img)


def autocontrast(img, cutoff=0):
    """
    自动对比度调整
    
    参数:
        img: Image对象
        cutoff: 裁剪百分比
    
    返回:
        调整后的图像
    """
    print(f"自动对比度调整: 裁剪 {cutoff}%")
    return ImageOps.autocontrast(img, cutoff=cutoff)


def split_channels(img):
    """
    分离颜色通道
    
    参数:
        img: Image对象
    
    返回:
        通道列表 [R, G, B] 或 [R, G, B, A]
    """
    print(f"分离颜色通道: {img.mode}")
    if img.mode == 'RGB':
        return img.split()  # Returns (R, G, B)
    elif img.mode == 'RGBA':
        return img.split()  # Returns (R, G, B, A)
    else:
        rgb_img = img.convert('RGB')
        return rgb_img.split()


def merge_channels(mode, bands):
    """
    合并颜色通道
    
    参数:
        mode: 图像模式 ('RGB' or 'RGBA')
        bands: 通道列表
    
    返回:
        合并后的图像
    """
    print(f"合并颜色通道: {mode}")
    return Image.merge(mode, bands)


def adjust_gamma(img, gamma=1.0):
    """
    伽马校正
    
    参数:
        img: Image对象
        gamma: 伽马值 (< 1.0 变亮, > 1.0 变暗)
    
    返回:
        校正后的图像
    """
    print(f"伽马校正: gamma = {gamma}")
    inv_gamma = 1.0 / gamma
    lut = [int(pow(i / 255.0, inv_gamma) * 255) for i in range(256)]
    
    if img.mode == 'RGB':
        return img.point(lambda i: lut[i])
    elif img.mode == 'L':
        return img.point(lut)
    else:
        rgb_img = img.convert('RGB')
        return rgb_img.point(lambda i: lut[i])


def replace_color(img, target_color, replacement_color, tolerance=0):
    """
    替换指定颜色
    
    参数:
        img: Image对象
        target_color: 要替换的颜色 (R, G, B)
        replacement_color: 替换成的颜色 (R, G, B)
        tolerance: 容差值
    
    返回:
        替换颜色后的图像
    """
    print(f"替换颜色: {target_color} -> {replacement_color}, 容差: {tolerance}")
    img_rgb = img.convert('RGB')
    pixels = img_rgb.load()
    
    for y in range(img_rgb.height):
        for x in range(img_rgb.width):
            r, g, b = pixels[x, y]
            
            # 检查颜色是否在容差范围内
            if (abs(r - target_color[0]) <= tolerance and
                abs(g - target_color[1]) <= tolerance and
                abs(b - target_color[2]) <= tolerance):
                pixels[x, y] = replacement_color
    
    return img_rgb


def apply_sepia(img):
    """
    应用复古棕褐色效果
    
    参数:
        img: Image对象
    
    返回:
        棕褐色效果的图像
    """
    print("应用复古棕褐色效果")
    img_rgb = img.convert('RGB')
    width, height = img_rgb.size
    pixels = img_rgb.load()
    
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            
            # 棕褐色转换公式
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)
            
            # 确保值在 0-255 范围内
            pixels[x, y] = (min(255, tr), min(255, tg), min(255, tb))
    
    return img_rgb


def create_color_mask(img, color, tolerance=10):
    """
    创建颜色遮罩
    
    参数:
        img: Image对象
        color: 目标颜色 (R, G, B)
        tolerance: 容差值
    
    返回:
        遮罩图像（L模式）
    """
    print(f"创建颜色遮罩: 颜色 {color}, 容差 {tolerance}")
    img_rgb = img.convert('RGB')
    mask = Image.new('L', img_rgb.size, 0)
    pixels = img_rgb.load()
    mask_pixels = mask.load()
    
    for y in range(img_rgb.height):
        for x in range(img_rgb.width):
            r, g, b = pixels[x, y]
            
            if (abs(r - color[0]) <= tolerance and
                abs(g - color[1]) <= tolerance and
                abs(b - color[2]) <= tolerance):
                mask_pixels[x, y] = 255
    
    return mask


def colorize_grayscale(img, black_color=(0, 0, 0), white_color=(255, 255, 255)):
    """
    给灰度图像着色
    
    参数:
        img: Image对象（灰度图）
        black_color: 黑色映射的颜色
        white_color: 白色映射的颜色
    
    返回:
        着色后的图像
    """
    print(f"灰度图着色: 黑色->{black_color}, 白色->{white_color}")
    gray = img.convert('L')
    return ImageOps.colorize(gray, black_color, white_color)


# 示例使用
if __name__ == "__main__":
    print("=== Pillow 颜色操作示例 ===\n")
    
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from modules.basic_operations import create_gradient_image, save_image
    
    # 创建输出目录
    os.makedirs("output", exist_ok=True)
    
    # 创建一个测试图像
    test_img = create_gradient_image(400, 300)
    save_image(test_img, "output/color_original.png")
    
    # 1. 灰度转换
    gray = convert_to_grayscale(test_img)
    save_image(gray, "output/37_grayscale.png")
    
    # 2. 黑白转换
    bw = convert_to_black_and_white(test_img, threshold=128)
    save_image(bw, "output/38_black_white.png")
    
    # 3. 反转颜色
    inverted = invert_colors(test_img)
    save_image(inverted, "output/39_inverted.png")
    
    # 4. 色调分离
    poster = posterize(test_img, bits=3)
    save_image(poster, "output/40_posterized.png")
    
    # 5. 曝光效果
    solar = solarize(test_img, threshold=128)
    save_image(solar, "output/41_solarized.png")
    
    # 6. 直方图均衡化
    equalized = equalize_histogram(test_img)
    save_image(equalized, "output/42_equalized.png")
    
    # 7. 自动对比度
    auto_contrast = autocontrast(test_img)
    save_image(auto_contrast, "output/43_autocontrast.png")
    
    # 8. 分离和合并通道
    r, g, b = split_channels(test_img)
    save_image(r, "output/44_channel_red.png")
    save_image(g, "output/45_channel_green.png")
    save_image(b, "output/46_channel_blue.png")
    
    # 交换通道
    swapped = merge_channels('RGB', (b, r, g))  # BGR -> RGB
    save_image(swapped, "output/47_channels_swapped.png")
    
    # 9. 伽马校正
    gamma_light = adjust_gamma(test_img, gamma=0.5)
    save_image(gamma_light, "output/48_gamma_light.png")
    
    gamma_dark = adjust_gamma(test_img, gamma=2.0)
    save_image(gamma_dark, "output/49_gamma_dark.png")
    
    # 10. 棕褐色效果
    sepia = apply_sepia(test_img)
    save_image(sepia, "output/50_sepia.png")
    
    # 11. 灰度着色
    colorized = colorize_grayscale(gray, (0, 0, 100), (255, 255, 150))
    save_image(colorized, "output/51_colorized.png")
    
    print("\n所有颜色操作示例已完成！请查看 output/ 目录")

