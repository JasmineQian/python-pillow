"""
图像合成模块
包含图像混合、粘贴、透明度处理等功能
"""

from PIL import Image, ImageChops


def paste_image(background, foreground, position=(0, 0), mask=None):
    """
    将一个图像粘贴到另一个图像上
    
    参数:
        background: 背景图像
        foreground: 前景图像
        position: 粘贴位置 (x, y)
        mask: 遮罩图像
    
    返回:
        合成后的图像
    """
    print(f"粘贴图像到位置 {position}")
    result = background.copy()
    result.paste(foreground, position, mask)
    return result


def blend_images(img1, img2, alpha=0.5):
    """
    混合两个图像
    
    参数:
        img1: 第一个图像
        img2: 第二个图像
        alpha: 混合系数 (0.0 = 完全是img1, 1.0 = 完全是img2)
    
    返回:
        混合后的图像
    """
    print(f"混合图像: alpha = {alpha}")
    
    # 确保两个图像大小相同
    if img1.size != img2.size:
        img2 = img2.resize(img1.size, Image.LANCZOS)
    
    # 确保两个图像模式相同
    if img1.mode != img2.mode:
        img2 = img2.convert(img1.mode)
    
    return Image.blend(img1, img2, alpha)


def composite_images(img1, img2, mask):
    """
    使用遮罩合成两个图像
    
    参数:
        img1: 第一个图像
        img2: 第二个图像
        mask: 遮罩图像（L模式或1模式）
    
    返回:
        合成后的图像
    """
    print("使用遮罩合成图像")
    
    # 确保图像大小相同
    if img1.size != img2.size:
        img2 = img2.resize(img1.size, Image.LANCZOS)
    if mask.size != img1.size:
        mask = mask.resize(img1.size, Image.LANCZOS)
    
    # 确保模式相同
    if img1.mode != img2.mode:
        img2 = img2.convert(img1.mode)
    if mask.mode != 'L':
        mask = mask.convert('L')
    
    return Image.composite(img1, img2, mask)


def add_images(img1, img2, scale=1.0, offset=0):
    """
    相加两个图像
    
    参数:
        img1: 第一个图像
        img2: 第二个图像
        scale: 缩放因子
        offset: 偏移量
    
    返回:
        相加后的图像
    """
    print(f"相加图像: scale={scale}, offset={offset}")
    
    if img1.size != img2.size:
        img2 = img2.resize(img1.size, Image.LANCZOS)
    if img1.mode != img2.mode:
        img2 = img2.convert(img1.mode)
    
    return ImageChops.add(img1, img2, scale, offset)


def subtract_images(img1, img2, scale=1.0, offset=0):
    """
    相减两个图像
    
    参数:
        img1: 第一个图像
        img2: 第二个图像
        scale: 缩放因子
        offset: 偏移量
    
    返回:
        相减后的图像
    """
    print(f"相减图像: scale={scale}, offset={offset}")
    
    if img1.size != img2.size:
        img2 = img2.resize(img1.size, Image.LANCZOS)
    if img1.mode != img2.mode:
        img2 = img2.convert(img1.mode)
    
    return ImageChops.subtract(img1, img2, scale, offset)


def multiply_images(img1, img2):
    """
    相乘两个图像（混合模式：正片叠底）
    
    参数:
        img1: 第一个图像
        img2: 第二个图像
    
    返回:
        相乘后的图像
    """
    print("相乘图像（正片叠底）")
    
    if img1.size != img2.size:
        img2 = img2.resize(img1.size, Image.LANCZOS)
    if img1.mode != img2.mode:
        img2 = img2.convert(img1.mode)
    
    return ImageChops.multiply(img1, img2)


def screen_images(img1, img2):
    """
    屏幕混合模式
    
    参数:
        img1: 第一个图像
        img2: 第二个图像
    
    返回:
        混合后的图像
    """
    print("屏幕混合模式")
    
    if img1.size != img2.size:
        img2 = img2.resize(img1.size, Image.LANCZOS)
    if img1.mode != img2.mode:
        img2 = img2.convert(img1.mode)
    
    return ImageChops.screen(img1, img2)


def lighter_images(img1, img2):
    """
    取两个图像中较亮的像素
    
    参数:
        img1: 第一个图像
        img2: 第二个图像
    
    返回:
        合成后的图像
    """
    print("取较亮像素")
    
    if img1.size != img2.size:
        img2 = img2.resize(img1.size, Image.LANCZOS)
    if img1.mode != img2.mode:
        img2 = img2.convert(img1.mode)
    
    return ImageChops.lighter(img1, img2)


def darker_images(img1, img2):
    """
    取两个图像中较暗的像素
    
    参数:
        img1: 第一个图像
        img2: 第二个图像
    
    返回:
        合成后的图像
    """
    print("取较暗像素")
    
    if img1.size != img2.size:
        img2 = img2.resize(img1.size, Image.LANCZOS)
    if img1.mode != img2.mode:
        img2 = img2.convert(img1.mode)
    
    return ImageChops.darker(img1, img2)


def difference_images(img1, img2):
    """
    计算两个图像的差异
    
    参数:
        img1: 第一个图像
        img2: 第二个图像
    
    返回:
        差异图像
    """
    print("计算图像差异")
    
    if img1.size != img2.size:
        img2 = img2.resize(img1.size, Image.LANCZOS)
    if img1.mode != img2.mode:
        img2 = img2.convert(img1.mode)
    
    return ImageChops.difference(img1, img2)


def create_alpha_composite(img1, img2):
    """
    Alpha通道合成
    
    参数:
        img1: 第一个图像（RGBA）
        img2: 第二个图像（RGBA）
    
    返回:
        合成后的图像
    """
    print("Alpha通道合成")
    
    img1_rgba = img1.convert('RGBA')
    img2_rgba = img2.convert('RGBA')
    
    if img1_rgba.size != img2_rgba.size:
        img2_rgba = img2_rgba.resize(img1_rgba.size, Image.LANCZOS)
    
    return Image.alpha_composite(img1_rgba, img2_rgba)


def create_gradient_mask(width, height, direction='horizontal'):
    """
    创建渐变遮罩
    
    参数:
        width: 宽度
        height: 高度
        direction: 渐变方向 ('horizontal' 或 'vertical')
    
    返回:
        渐变遮罩图像
    """
    print(f"创建渐变遮罩: {direction}")
    mask = Image.new('L', (width, height))
    
    for y in range(height):
        for x in range(width):
            if direction == 'horizontal':
                value = int(255 * x / width)
            else:  # vertical
                value = int(255 * y / height)
            mask.putpixel((x, y), value)
    
    return mask


def create_circular_mask(width, height, center=None, radius=None):
    """
    创建圆形遮罩
    
    参数:
        width: 宽度
        height: 高度
        center: 圆心位置，默认为图像中心
        radius: 半径，默认为图像最短边的一半
    
    返回:
        圆形遮罩图像
    """
    print("创建圆形遮罩")
    
    if center is None:
        center = (width // 2, height // 2)
    if radius is None:
        radius = min(width, height) // 2
    
    mask = Image.new('L', (width, height), 0)
    
    for y in range(height):
        for x in range(width):
            distance = ((x - center[0]) ** 2 + (y - center[1]) ** 2) ** 0.5
            if distance <= radius:
                # 创建羽化边缘
                if distance > radius - 10:
                    alpha = int(255 * (1 - (distance - (radius - 10)) / 10))
                else:
                    alpha = 255
                mask.putpixel((x, y), alpha)
    
    return mask


# 示例使用
if __name__ == "__main__":
    print("=== Pillow 图像合成示例 ===\n")
    
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from modules.basic_operations import create_new_image, create_gradient_image, save_image
    
    # 创建输出目录
    os.makedirs("output", exist_ok=True)
    
    # 创建测试图像
    img1 = create_gradient_image(400, 300)
    img2 = create_new_image(400, 300, (255, 100, 100))
    
    save_image(img1, "output/comp_img1.png")
    save_image(img2, "output/comp_img2.png")
    
    # 1. 混合图像
    blended_50 = blend_images(img1, img2, alpha=0.5)
    save_image(blended_50, "output/52_blended_50.png")
    
    blended_25 = blend_images(img1, img2, alpha=0.25)
    save_image(blended_25, "output/53_blended_25.png")
    
    # 2. 创建遮罩并合成
    h_mask = create_gradient_mask(400, 300, 'horizontal')
    save_image(h_mask, "output/54_mask_horizontal.png")
    
    composited_h = composite_images(img1, img2, h_mask)
    save_image(composited_h, "output/55_composite_horizontal.png")
    
    v_mask = create_gradient_mask(400, 300, 'vertical')
    composited_v = composite_images(img1, img2, v_mask)
    save_image(composited_v, "output/56_composite_vertical.png")
    
    # 3. 圆形遮罩
    circle_mask = create_circular_mask(400, 300)
    save_image(circle_mask, "output/57_mask_circular.png")
    
    composited_circle = composite_images(img1, img2, circle_mask)
    save_image(composited_circle, "output/58_composite_circular.png")
    
    # 4. 图像运算
    added = add_images(img1, img2, scale=0.5)
    save_image(added, "output/59_added.png")
    
    multiplied = multiply_images(img1, img2)
    save_image(multiplied, "output/60_multiplied.png")
    
    screened = screen_images(img1, img2)
    save_image(screened, "output/61_screened.png")
    
    lighter = lighter_images(img1, img2)
    save_image(lighter, "output/62_lighter.png")
    
    darker = darker_images(img1, img2)
    save_image(darker, "output/63_darker.png")
    
    # 5. 粘贴图像
    small_img = create_new_image(100, 100, (0, 255, 0))
    pasted = paste_image(img1, small_img, position=(150, 100))
    save_image(pasted, "output/64_pasted.png")
    
    print("\n所有合成示例已完成！请查看 output/ 目录")

