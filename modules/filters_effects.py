"""
滤镜和效果模块
包含模糊、锐化、边缘检测、对比度调整等效果
"""

from PIL import Image, ImageFilter, ImageEnhance


def apply_blur(img, radius=2):
    """
    应用模糊效果
    
    参数:
        img: Image对象
        radius: 模糊半径
    
    返回:
        模糊后的Image对象
    """
    print(f"应用模糊效果: 半径 {radius}")
    return img.filter(ImageFilter.GaussianBlur(radius))


def apply_box_blur(img, radius=2):
    """
    应用方框模糊
    
    参数:
        img: Image对象
        radius: 模糊半径
    
    返回:
        模糊后的Image对象
    """
    print(f"应用方框模糊: 半径 {radius}")
    return img.filter(ImageFilter.BoxBlur(radius))


def apply_sharpen(img):
    """
    应用锐化效果
    
    参数:
        img: Image对象
    
    返回:
        锐化后的Image对象
    """
    print("应用锐化效果")
    return img.filter(ImageFilter.SHARPEN)


def apply_edge_enhance(img):
    """
    应用边缘增强
    
    参数:
        img: Image对象
    
    返回:
        边缘增强后的Image对象
    """
    print("应用边缘增强")
    return img.filter(ImageFilter.EDGE_ENHANCE)


def apply_find_edges(img):
    """
    边缘检测
    
    参数:
        img: Image对象
    
    返回:
        边缘检测后的Image对象
    """
    print("应用边缘检测")
    return img.filter(ImageFilter.FIND_EDGES)


def apply_contour(img):
    """
    应用轮廓效果
    
    参数:
        img: Image对象
    
    返回:
        轮廓效果后的Image对象
    """
    print("应用轮廓效果")
    return img.filter(ImageFilter.CONTOUR)


def apply_emboss(img):
    """
    应用浮雕效果
    
    参数:
        img: Image对象
    
    返回:
        浮雕效果后的Image对象
    """
    print("应用浮雕效果")
    return img.filter(ImageFilter.EMBOSS)


def apply_detail(img):
    """
    应用细节增强
    
    参数:
        img: Image对象
    
    返回:
        细节增强后的Image对象
    """
    print("应用细节增强")
    return img.filter(ImageFilter.DETAIL)


def adjust_brightness(img, factor):
    """
    调整亮度
    
    参数:
        img: Image对象
        factor: 亮度因子 (1.0 = 原始, < 1.0 = 变暗, > 1.0 = 变亮)
    
    返回:
        调整后的Image对象
    """
    print(f"调整亮度: 因子 {factor}")
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(factor)


def adjust_contrast(img, factor):
    """
    调整对比度
    
    参数:
        img: Image对象
        factor: 对比度因子 (1.0 = 原始, < 1.0 = 降低, > 1.0 = 增强)
    
    返回:
        调整后的Image对象
    """
    print(f"调整对比度: 因子 {factor}")
    enhancer = ImageEnhance.Contrast(img)
    return enhancer.enhance(factor)


def adjust_saturation(img, factor):
    """
    调整饱和度
    
    参数:
        img: Image对象
        factor: 饱和度因子 (0.0 = 灰度, 1.0 = 原始, > 1.0 = 增强)
    
    返回:
        调整后的Image对象
    """
    print(f"调整饱和度: 因子 {factor}")
    enhancer = ImageEnhance.Color(img)
    return enhancer.enhance(factor)


def adjust_sharpness(img, factor):
    """
    调整锐度
    
    参数:
        img: Image对象
        factor: 锐度因子 (0.0 = 模糊, 1.0 = 原始, 2.0 = 锐化)
    
    返回:
        调整后的Image对象
    """
    print(f"调整锐度: 因子 {factor}")
    enhancer = ImageEnhance.Sharpness(img)
    return enhancer.enhance(factor)


def apply_smooth(img):
    """
    应用平滑效果
    
    参数:
        img: Image对象
    
    返回:
        平滑后的Image对象
    """
    print("应用平滑效果")
    return img.filter(ImageFilter.SMOOTH)


def apply_smooth_more(img):
    """
    应用更强的平滑效果
    
    参数:
        img: Image对象
    
    返回:
        平滑后的Image对象
    """
    print("应用更强的平滑效果")
    return img.filter(ImageFilter.SMOOTH_MORE)


def apply_median_filter(img, size=3):
    """
    应用中值滤波（去噪）
    
    参数:
        img: Image对象
        size: 滤波器大小
    
    返回:
        滤波后的Image对象
    """
    print(f"应用中值滤波: 大小 {size}")
    return img.filter(ImageFilter.MedianFilter(size))


def apply_min_filter(img, size=3):
    """
    应用最小值滤波（腐蚀效果）
    
    参数:
        img: Image对象
        size: 滤波器大小
    
    返回:
        滤波后的Image对象
    """
    print(f"应用最小值滤波: 大小 {size}")
    return img.filter(ImageFilter.MinFilter(size))


def apply_max_filter(img, size=3):
    """
    应用最大值滤波（膨胀效果）
    
    参数:
        img: Image对象
        size: 滤波器大小
    
    返回:
        滤波后的Image对象
    """
    print(f"应用最大值滤波: 大小 {size}")
    return img.filter(ImageFilter.MaxFilter(size))


def apply_unsharp_mask(img, radius=2, percent=150, threshold=3):
    """
    应用反锐化遮罩（专业锐化）
    
    参数:
        img: Image对象
        radius: 模糊半径
        percent: 锐化强度百分比
        threshold: 阈值
    
    返回:
        锐化后的Image对象
    """
    print(f"应用反锐化遮罩: 半径={radius}, 强度={percent}%, 阈值={threshold}")
    return img.filter(ImageFilter.UnsharpMask(radius, percent, threshold))


# 示例使用
if __name__ == "__main__":
    print("=== Pillow 滤镜和效果示例 ===\n")
    
    import os
    from basic_operations import create_gradient_image, save_image
    
    # 创建输出目录
    os.makedirs("output", exist_ok=True)
    
    # 创建一个测试图像
    test_img = create_gradient_image(400, 300)
    save_image(test_img, "output/filter_original.png")
    
    # 1. 模糊效果
    blurred = apply_blur(test_img, radius=5)
    save_image(blurred, "output/15_blurred.png")
    
    # 2. 锐化效果
    sharpened = apply_sharpen(test_img)
    save_image(sharpened, "output/16_sharpened.png")
    
    # 3. 边缘检测
    edges = apply_find_edges(test_img)
    save_image(edges, "output/17_edges.png")
    
    # 4. 浮雕效果
    embossed = apply_emboss(test_img)
    save_image(embossed, "output/18_embossed.png")
    
    # 5. 轮廓效果
    contour = apply_contour(test_img)
    save_image(contour, "output/19_contour.png")
    
    # 6. 亮度调整
    brighter = adjust_brightness(test_img, 1.5)
    save_image(brighter, "output/20_brighter.png")
    
    darker = adjust_brightness(test_img, 0.5)
    save_image(darker, "output/21_darker.png")
    
    # 7. 对比度调整
    high_contrast = adjust_contrast(test_img, 2.0)
    save_image(high_contrast, "output/22_high_contrast.png")
    
    low_contrast = adjust_contrast(test_img, 0.5)
    save_image(low_contrast, "output/23_low_contrast.png")
    
    # 8. 饱和度调整
    saturated = adjust_saturation(test_img, 2.0)
    save_image(saturated, "output/24_saturated.png")
    
    desaturated = adjust_saturation(test_img, 0.3)
    save_image(desaturated, "output/25_desaturated.png")
    
    # 9. 平滑效果
    smoothed = apply_smooth_more(test_img)
    save_image(smoothed, "output/26_smoothed.png")
    
    # 10. 反锐化遮罩
    unsharp = apply_unsharp_mask(test_img, radius=2, percent=150)
    save_image(unsharp, "output/27_unsharp_mask.png")
    
    print("\n所有滤镜示例已完成！请查看 output/ 目录")

