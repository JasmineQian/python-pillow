"""
文字操作模块
包含添加文字水印、多行文字、文字居中等功能
"""

from PIL import Image, ImageDraw, ImageFont


def add_text_watermark(img, text, position='bottom-right', font_size=20, 
                       color=(255, 255, 255), opacity=128):
    """
    添加文字水印
    
    参数:
        img: Image对象
        text: 水印文字
        position: 位置 ('top-left', 'top-right', 'bottom-left', 'bottom-right', 'center')
        font_size: 字体大小
        color: 文字颜色
        opacity: 不透明度 (0-255)
    
    返回:
        添加水印后的图像
    """
    print(f"添加文字水印: '{text}' 在 {position}")
    
    # 创建RGBA图像用于透明度
    if img.mode != 'RGBA':
        img_rgba = img.convert('RGBA')
    else:
        img_rgba = img.copy()
    
    # 创建透明图层
    txt_layer = Image.new('RGBA', img_rgba.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)
    
    # 获取字体
    try:
        font = ImageFont.truetype("Arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    # 获取文字大小
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # 计算位置
    margin = 10
    if position == 'top-left':
        xy = (margin, margin)
    elif position == 'top-right':
        xy = (img_rgba.width - text_width - margin, margin)
    elif position == 'bottom-left':
        xy = (margin, img_rgba.height - text_height - margin)
    elif position == 'bottom-right':
        xy = (img_rgba.width - text_width - margin, 
              img_rgba.height - text_height - margin)
    elif position == 'center':
        xy = ((img_rgba.width - text_width) // 2,
              (img_rgba.height - text_height) // 2)
    else:
        xy = position  # 直接使用元组坐标
    
    # 绘制文字（带透明度）
    color_with_alpha = (*color[:3], opacity)
    draw.text(xy, text, font=font, fill=color_with_alpha)
    
    # 合成图层
    result = Image.alpha_composite(img_rgba, txt_layer)
    
    # 如果原图不是RGBA，转回RGB
    if img.mode == 'RGB':
        result = result.convert('RGB')
    
    return result


def add_centered_text(img, text, font_size=40, color=(0, 0, 0)):
    """
    在图像中心添加文字
    
    参数:
        img: Image对象
        text: 文字内容
        font_size: 字体大小
        color: 文字颜色
    
    返回:
        添加文字后的图像
    """
    print(f"在中心添加文字: '{text}'")
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    
    try:
        font = ImageFont.truetype("Arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    # 获取文字大小
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # 计算居中位置
    x = (img.width - text_width) // 2
    y = (img.height - text_height) // 2
    
    # 绘制文字
    draw.text((x, y), text, font=font, fill=color)
    
    return img_copy


def add_multiline_text(img, text, position=(10, 10), font_size=20, 
                       color=(0, 0, 0), spacing=4, align='left'):
    """
    添加多行文字
    
    参数:
        img: Image对象
        text: 多行文字（使用\n分隔）
        position: 起始位置
        font_size: 字体大小
        color: 文字颜色
        spacing: 行间距
        align: 对齐方式 ('left', 'center', 'right')
    
    返回:
        添加文字后的图像
    """
    print(f"添加多行文字在位置 {position}")
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    
    try:
        font = ImageFont.truetype("Arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    draw.multiline_text(position, text, font=font, fill=color, 
                       spacing=spacing, align=align)
    
    return img_copy


def add_text_with_background(img, text, position, font_size=20, 
                             text_color=(255, 255, 255), bg_color=(0, 0, 0),
                             padding=5, bg_opacity=200):
    """
    添加带背景的文字
    
    参数:
        img: Image对象
        text: 文字内容
        position: 位置
        font_size: 字体大小
        text_color: 文字颜色
        bg_color: 背景颜色
        padding: 内边距
        bg_opacity: 背景不透明度
    
    返回:
        添加文字后的图像
    """
    print(f"添加带背景的文字: '{text}'")
    
    if img.mode != 'RGBA':
        img_rgba = img.convert('RGBA')
    else:
        img_rgba = img.copy()
    
    # 创建透明图层
    txt_layer = Image.new('RGBA', img_rgba.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)
    
    try:
        font = ImageFont.truetype("Arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    # 获取文字大小
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # 绘制背景矩形
    bg_bbox = [
        position[0] - padding,
        position[1] - padding,
        position[0] + text_width + padding,
        position[1] + text_height + padding
    ]
    bg_color_with_alpha = (*bg_color[:3], bg_opacity)
    draw.rectangle(bg_bbox, fill=bg_color_with_alpha)
    
    # 绘制文字
    draw.text(position, text, font=font, fill=text_color)
    
    # 合成图层
    result = Image.alpha_composite(img_rgba, txt_layer)
    
    if img.mode == 'RGB':
        result = result.convert('RGB')
    
    return result


def add_outlined_text(img, text, position, font_size=40, 
                     text_color=(255, 255, 255), outline_color=(0, 0, 0),
                     outline_width=2):
    """
    添加带轮廓的文字
    
    参数:
        img: Image对象
        text: 文字内容
        position: 位置
        font_size: 字体大小
        text_color: 文字颜色
        outline_color: 轮廓颜色
        outline_width: 轮廓宽度
    
    返回:
        添加文字后的图像
    """
    print(f"添加带轮廓的文字: '{text}'")
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    
    try:
        font = ImageFont.truetype("Arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    # 绘制轮廓（在多个位置绘制轮廓颜色）
    for adj_x in range(-outline_width, outline_width + 1):
        for adj_y in range(-outline_width, outline_width + 1):
            draw.text((position[0] + adj_x, position[1] + adj_y), 
                     text, font=font, fill=outline_color)
    
    # 绘制主文字
    draw.text(position, text, font=font, fill=text_color)
    
    return img_copy


def create_text_image(text, width=400, height=200, font_size=30,
                     text_color=(0, 0, 0), bg_color=(255, 255, 255)):
    """
    创建纯文字图像
    
    参数:
        text: 文字内容
        width: 图像宽度
        height: 图像高度
        font_size: 字体大小
        text_color: 文字颜色
        bg_color: 背景颜色
    
    返回:
        文字图像
    """
    print(f"创建文字图像: '{text}'")
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("Arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    # 获取文字大小并居中
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    draw.text((x, y), text, font=font, fill=text_color)
    
    return img


def get_text_size(text, font_size=20):
    """
    获取文字尺寸
    
    参数:
        text: 文字内容
        font_size: 字体大小
    
    返回:
        (width, height) 元组
    """
    # 创建临时图像来测量文字
    temp_img = Image.new('RGB', (1, 1))
    draw = ImageDraw.Draw(temp_img)
    
    try:
        font = ImageFont.truetype("Arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), text, font=font)
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    
    print(f"文字 '{text}' 的尺寸: {width}x{height}")
    return (width, height)


# 示例使用
if __name__ == "__main__":
    print("=== Pillow 文字操作示例 ===\n")
    
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from modules.basic_operations import create_gradient_image, save_image
    
    # 创建输出目录
    os.makedirs("output", exist_ok=True)
    
    # 创建测试图像
    test_img = create_gradient_image(600, 400)
    
    # 1. 添加水印（不同位置）
    watermark_br = add_text_watermark(test_img, "Watermark", 
                                     position='bottom-right', font_size=20)
    save_image(watermark_br, "output/65_watermark_br.png")
    
    watermark_tl = add_text_watermark(test_img, "© 2024", 
                                     position='top-left', font_size=15)
    save_image(watermark_tl, "output/66_watermark_tl.png")
    
    # 2. 居中文字
    centered = add_centered_text(test_img, "CENTERED TEXT", 
                                font_size=50, color=(255, 255, 255))
    save_image(centered, "output/67_centered_text.png")
    
    # 3. 多行文字
    multiline_text = "Line 1\nLine 2\nLine 3"
    multiline = add_multiline_text(test_img, multiline_text, 
                                  position=(50, 50), font_size=30,
                                  color=(255, 255, 255), spacing=10)
    save_image(multiline, "output/68_multiline_text.png")
    
    # 4. 带背景的文字
    text_bg = add_text_with_background(test_img, "Text with BG", 
                                      position=(200, 180), font_size=30,
                                      text_color=(255, 255, 255),
                                      bg_color=(0, 0, 0), padding=10)
    save_image(text_bg, "output/69_text_with_bg.png")
    
    # 5. 带轮廓的文字
    outlined = add_outlined_text(test_img, "OUTLINED", 
                                position=(150, 150), font_size=60,
                                text_color=(255, 255, 0),
                                outline_color=(0, 0, 0), outline_width=3)
    save_image(outlined, "output/70_outlined_text.png")
    
    # 6. 纯文字图像
    text_img = create_text_image("Hello Pillow!", width=400, height=200,
                                font_size=40, text_color=(0, 0, 128),
                                bg_color=(255, 255, 200))
    save_image(text_img, "output/71_text_image.png")
    
    # 7. 组合多个文字效果
    combined = test_img.copy()
    combined = add_text_watermark(combined, "© 2024", position='bottom-right',
                                 font_size=15, opacity=150)
    combined = add_text_with_background(combined, "TITLE", position=(230, 50),
                                       font_size=40, text_color=(255, 255, 255),
                                       bg_color=(255, 0, 0), padding=15)
    combined = add_multiline_text(combined, "Description\nLine 2\nLine 3",
                                 position=(50, 250), font_size=20,
                                 color=(255, 255, 255))
    save_image(combined, "output/72_combined_text.png")
    
    print("\n所有文字操作示例已完成！请查看 output/ 目录")

