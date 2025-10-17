"""
创建示例图像
这个脚本会在 input/ 目录中创建一个示例图像
"""

from PIL import Image, ImageDraw
import os


def create_sample_image():
    """创建一个彩色示例图像"""
    # 创建一个 600x400 的图像
    img = Image.new('RGB', (600, 400), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # 绘制渐变背景
    for y in range(400):
        r = int(100 + 155 * y / 400)
        g = int(150 + 105 * y / 400)
        b = int(200 + 55 * y / 400)
        draw.line([(0, y), (600, y)], fill=(r, g, b))
    
    # 绘制一些形状
    # 圆形
    draw.ellipse([100, 100, 200, 200], fill=(255, 100, 100), outline=(200, 0, 0), width=3)
    # 矩形
    draw.rectangle([250, 100, 400, 200], fill=(100, 255, 100), outline=(0, 200, 0), width=3)
    # 另一个圆
    draw.ellipse([450, 100, 550, 200], fill=(100, 100, 255), outline=(0, 0, 200), width=3)
    
    # 绘制一些文字
    try:
        from PIL import ImageFont
        font = ImageFont.truetype("Arial.ttf", 40)
    except:
        font = None
    
    draw.text((180, 250), "Sample Image", fill=(255, 255, 255), font=font)
    draw.text((200, 300), "for Pillow", fill=(255, 255, 255), font=font)
    
    return img


if __name__ == "__main__":
    # 创建 input 目录
    os.makedirs("input", exist_ok=True)
    
    # 创建并保存示例图像
    sample = create_sample_image()
    sample.save("input/sample.jpg", quality=95)
    print("✓ 示例图像已创建: input/sample.jpg")
    
    # 创建一张纯色图像
    red_img = Image.new('RGB', (400, 300), (255, 100, 100))
    red_img.save("input/red.png")
    print("✓ 示例图像已创建: input/red.png")
    
    # 创建一张带图案的图像
    pattern = Image.new('RGB', (400, 300))
    for y in range(300):
        for x in range(400):
            r = (x * 255) // 400
            g = (y * 255) // 300
            b = 128
            pattern.putpixel((x, y), (r, g, b))
    pattern.save("input/pattern.png")
    print("✓ 示例图像已创建: input/pattern.png")
    
    print("\n所有示例图像创建完成！")

