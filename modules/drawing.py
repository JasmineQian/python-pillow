"""
绘图功能模块
包含在图像上绘制线条、矩形、圆形、文字等功能
"""

from PIL import Image, ImageDraw, ImageFont


def draw_line(img, start, end, fill=(255, 0, 0), width=1):
    """
    在图像上绘制线条
    
    参数:
        img: Image对象
        start: 起点坐标 (x, y)
        end: 终点坐标 (x, y)
        fill: 线条颜色
        width: 线条宽度
    
    返回:
        绘制后的Image对象
    """
    print(f"绘制线条: {start} -> {end}, 颜色: {fill}, 宽度: {width}")
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    draw.line([start, end], fill=fill, width=width)
    return img_copy


def draw_rectangle(img, xy, fill=None, outline=(255, 0, 0), width=1):
    """
    在图像上绘制矩形
    
    参数:
        img: Image对象
        xy: 矩形坐标 [(x1, y1), (x2, y2)] 或 [x1, y1, x2, y2]
        fill: 填充颜色
        outline: 边框颜色
        width: 边框宽度
    
    返回:
        绘制后的Image对象
    """
    print(f"绘制矩形: {xy}, 填充: {fill}, 边框: {outline}, 宽度: {width}")
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    draw.rectangle(xy, fill=fill, outline=outline, width=width)
    return img_copy


def draw_circle(img, center, radius, fill=None, outline=(255, 0, 0), width=1):
    """
    在图像上绘制圆形
    
    参数:
        img: Image对象
        center: 圆心坐标 (x, y)
        radius: 半径
        fill: 填充颜色
        outline: 边框颜色
        width: 边框宽度
    
    返回:
        绘制后的Image对象
    """
    print(f"绘制圆形: 中心 {center}, 半径 {radius}, 填充: {fill}, 边框: {outline}")
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    
    # 计算圆形的边界框
    x, y = center
    bbox = [x - radius, y - radius, x + radius, y + radius]
    draw.ellipse(bbox, fill=fill, outline=outline, width=width)
    return img_copy


def draw_ellipse(img, bbox, fill=None, outline=(255, 0, 0), width=1):
    """
    在图像上绘制椭圆
    
    参数:
        img: Image对象
        bbox: 边界框 [x1, y1, x2, y2]
        fill: 填充颜色
        outline: 边框颜色
        width: 边框宽度
    
    返回:
        绘制后的Image对象
    """
    print(f"绘制椭圆: {bbox}, 填充: {fill}, 边框: {outline}")
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    draw.ellipse(bbox, fill=fill, outline=outline, width=width)
    return img_copy


def draw_polygon(img, points, fill=None, outline=(255, 0, 0), width=1):
    """
    在图像上绘制多边形
    
    参数:
        img: Image对象
        points: 顶点坐标列表 [(x1, y1), (x2, y2), ...]
        fill: 填充颜色
        outline: 边框颜色
        width: 边框宽度
    
    返回:
        绘制后的Image对象
    """
    print(f"绘制多边形: {len(points)}个顶点, 填充: {fill}, 边框: {outline}")
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    draw.polygon(points, fill=fill, outline=outline)
    return img_copy


def draw_text(img, position, text, fill=(0, 0, 0), font=None, font_size=20):
    """
    在图像上绘制文字
    
    参数:
        img: Image对象
        position: 文字位置 (x, y)
        text: 文字内容
        fill: 文字颜色
        font: 字体对象
        font_size: 字体大小（当font为None时使用）
    
    返回:
        绘制后的Image对象
    """
    print(f"绘制文字: '{text}' 在位置 {position}, 颜色: {fill}")
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    
    if font is None:
        try:
            # 尝试使用系统字体
            font = ImageFont.truetype("Arial.ttf", font_size)
        except:
            # 如果失败，使用默认字体
            font = ImageFont.load_default()
    
    draw.text(position, text, fill=fill, font=font)
    return img_copy


def draw_multiline_text(img, position, text, fill=(0, 0, 0), font=None, font_size=20, spacing=4):
    """
    在图像上绘制多行文字
    
    参数:
        img: Image对象
        position: 文字位置 (x, y)
        text: 文字内容（使用\n分隔多行）
        fill: 文字颜色
        font: 字体对象
        font_size: 字体大小
        spacing: 行间距
    
    返回:
        绘制后的Image对象
    """
    print(f"绘制多行文字在位置 {position}, 颜色: {fill}")
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    
    if font is None:
        try:
            font = ImageFont.truetype("Arial.ttf", font_size)
        except:
            font = ImageFont.load_default()
    
    draw.multiline_text(position, text, fill=fill, font=font, spacing=spacing)
    return img_copy


def draw_arc(img, bbox, start, end, fill=(255, 0, 0), width=1):
    """
    在图像上绘制弧线
    
    参数:
        img: Image对象
        bbox: 边界框 [x1, y1, x2, y2]
        start: 起始角度（度）
        end: 结束角度（度）
        fill: 线条颜色
        width: 线条宽度
    
    返回:
        绘制后的Image对象
    """
    print(f"绘制弧线: {bbox}, 角度 {start}° - {end}°, 颜色: {fill}")
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    draw.arc(bbox, start, end, fill=fill, width=width)
    return img_copy


def draw_chord(img, bbox, start, end, fill=None, outline=(255, 0, 0), width=1):
    """
    在图像上绘制弦（弧线加闭合线）
    
    参数:
        img: Image对象
        bbox: 边界框 [x1, y1, x2, y2]
        start: 起始角度（度）
        end: 结束角度（度）
        fill: 填充颜色
        outline: 边框颜色
        width: 边框宽度
    
    返回:
        绘制后的Image对象
    """
    print(f"绘制弦: {bbox}, 角度 {start}° - {end}°")
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    draw.chord(bbox, start, end, fill=fill, outline=outline, width=width)
    return img_copy


def draw_pieslice(img, bbox, start, end, fill=None, outline=(255, 0, 0), width=1):
    """
    在图像上绘制扇形
    
    参数:
        img: Image对象
        bbox: 边界框 [x1, y1, x2, y2]
        start: 起始角度（度）
        end: 结束角度（度）
        fill: 填充颜色
        outline: 边框颜色
        width: 边框宽度
    
    返回:
        绘制后的Image对象
    """
    print(f"绘制扇形: {bbox}, 角度 {start}° - {end}°")
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    draw.pieslice(bbox, start, end, fill=fill, outline=outline, width=width)
    return img_copy


def draw_points(img, points, fill=(255, 0, 0)):
    """
    在图像上绘制点
    
    参数:
        img: Image对象
        points: 点坐标列表 [(x1, y1), (x2, y2), ...]
        fill: 点的颜色
    
    返回:
        绘制后的Image对象
    """
    print(f"绘制 {len(points)} 个点, 颜色: {fill}")
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    draw.point(points, fill=fill)
    return img_copy


# 示例使用
if __name__ == "__main__":
    print("=== Pillow 绘图功能示例 ===\n")
    
    import os
    from basic_operations import create_new_image, save_image
    
    # 创建输出目录
    os.makedirs("output", exist_ok=True)
    
    # 创建一个白色背景
    canvas = create_new_image(600, 400, (255, 255, 255))
    
    # 1. 绘制线条
    img_line = draw_line(canvas, (50, 50), (550, 50), fill=(255, 0, 0), width=3)
    save_image(img_line, "output/28_line.png")
    
    # 2. 绘制矩形
    img_rect = draw_rectangle(canvas, [100, 100, 300, 200], fill=(200, 200, 255), 
                              outline=(0, 0, 255), width=3)
    save_image(img_rect, "output/29_rectangle.png")
    
    # 3. 绘制圆形
    img_circle = draw_circle(canvas, (300, 200), 80, fill=(255, 200, 200), 
                            outline=(255, 0, 0), width=3)
    save_image(img_circle, "output/30_circle.png")
    
    # 4. 绘制椭圆
    img_ellipse = draw_ellipse(canvas, [150, 150, 450, 250], fill=(200, 255, 200),
                               outline=(0, 255, 0), width=3)
    save_image(img_ellipse, "output/31_ellipse.png")
    
    # 5. 绘制多边形（三角形）
    triangle_points = [(300, 100), (200, 300), (400, 300)]
    img_polygon = draw_polygon(canvas, triangle_points, fill=(255, 255, 200),
                              outline=(255, 165, 0), width=3)
    save_image(img_polygon, "output/32_polygon.png")
    
    # 6. 绘制文字
    img_text = draw_text(canvas, (200, 180), "Hello, Pillow!", 
                        fill=(0, 0, 0), font_size=30)
    save_image(img_text, "output/33_text.png")
    
    # 7. 绘制弧线
    img_arc = draw_arc(canvas, [150, 150, 450, 350], 0, 180, 
                      fill=(255, 0, 255), width=3)
    save_image(img_arc, "output/34_arc.png")
    
    # 8. 绘制扇形
    img_pie = draw_pieslice(canvas, [200, 150, 400, 350], 0, 120,
                           fill=(255, 200, 100), outline=(255, 0, 0), width=2)
    save_image(img_pie, "output/35_pieslice.png")
    
    # 9. 组合绘图
    img_combined = canvas.copy()
    img_combined = draw_rectangle(img_combined, [50, 50, 550, 350], 
                                 outline=(0, 0, 0), width=2)
    img_combined = draw_circle(img_combined, (150, 150), 50, 
                              fill=(255, 100, 100), outline=(200, 0, 0), width=2)
    img_combined = draw_circle(img_combined, (450, 150), 50,
                              fill=(100, 255, 100), outline=(0, 200, 0), width=2)
    img_combined = draw_circle(img_combined, (300, 250), 50,
                              fill=(100, 100, 255), outline=(0, 0, 200), width=2)
    img_combined = draw_text(img_combined, (220, 320), "Combined Drawing",
                            fill=(0, 0, 0), font_size=25)
    save_image(img_combined, "output/36_combined_drawing.png")
    
    print("\n所有绘图示例已完成！请查看 output/ 目录")

