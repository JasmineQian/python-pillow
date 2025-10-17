"""
绘图功能示例脚本
演示 Pillow 的各种绘图功能
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules import basic_operations, drawing
import math


def main():
    print("=" * 60)
    print("  绘图功能示例")
    print("=" * 60 + "\n")
    
    os.makedirs("output/examples", exist_ok=True)
    
    # 1. 基本形状
    print("1. 绘制基本形状")
    canvas = basic_operations.create_new_image(600, 400, (255, 255, 255))
    
    # 线条
    img_lines = canvas.copy()
    for i in range(10):
        y = 50 + i * 30
        img_lines = drawing.draw_line(
            img_lines, (50, y), (550, y), 
            fill=(255 - i*25, 0, i*25), width=2
        )
    basic_operations.save_image(img_lines, "output/examples/draw_lines.png")
    
    # 矩形
    img_rects = canvas.copy()
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
    for i, color in enumerate(colors):
        x = 50 + i * 130
        img_rects = drawing.draw_rectangle(
            img_rects, [x, 100, x+100, 300],
            fill=None, outline=color, width=3
        )
    basic_operations.save_image(img_rects, "output/examples/draw_rectangles.png")
    
    # 圆形
    img_circles = canvas.copy()
    for i in range(5):
        radius = 30 + i * 10
        img_circles = drawing.draw_circle(
            img_circles, (300, 200), radius,
            fill=None, outline=(i*50, 100, 255-i*50), width=2
        )
    basic_operations.save_image(img_circles, "output/examples/draw_circles.png")
    
    # 2. 多边形
    print("\n2. 绘制多边形")
    img_poly = canvas.copy()
    
    # 三角形
    triangle = [(150, 100), (100, 250), (200, 250)]
    img_poly = drawing.draw_polygon(
        img_poly, triangle,
        fill=(255, 200, 200), outline=(255, 0, 0), width=3
    )
    
    # 五边形
    pentagon = []
    center_x, center_y = 400, 175
    radius = 80
    for i in range(5):
        angle = i * 2 * math.pi / 5 - math.pi / 2
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        pentagon.append((int(x), int(y)))
    
    img_poly = drawing.draw_polygon(
        img_poly, pentagon,
        fill=(200, 255, 200), outline=(0, 255, 0), width=3
    )
    
    basic_operations.save_image(img_poly, "output/examples/draw_polygons.png")
    
    # 3. 文字
    print("\n3. 绘制文字")
    img_text = canvas.copy()
    
    positions = [
        ((100, 50), "Top Left"),
        ((200, 150), "Middle"),
        ((100, 300), "Bottom Left")
    ]
    
    for pos, text in positions:
        img_text = drawing.draw_text(
            img_text, pos, text,
            fill=(0, 0, 0), font_size=30
        )
    
    basic_operations.save_image(img_text, "output/examples/draw_text.png")
    
    # 4. 弧线和扇形
    print("\n4. 绘制弧线和扇形")
    img_arcs = canvas.copy()
    
    # 弧线
    img_arcs = drawing.draw_arc(
        img_arcs, [50, 50, 250, 250],
        0, 180, fill=(255, 0, 0), width=3
    )
    
    # 弦
    img_arcs = drawing.draw_chord(
        img_arcs, [300, 50, 500, 250],
        45, 315, fill=(200, 200, 255), outline=(0, 0, 255), width=3
    )
    
    # 扇形
    colors_pie = [(255, 100, 100), (100, 255, 100), (100, 100, 255)]
    angles = [0, 120, 240, 360]
    
    for i in range(3):
        img_arcs = drawing.draw_pieslice(
            img_arcs, [100, 280, 300, 380],
            angles[i], angles[i+1],
            fill=colors_pie[i], outline=(0, 0, 0), width=2
        )
    
    basic_operations.save_image(img_arcs, "output/examples/draw_arcs.png")
    
    # 5. 复杂图案
    print("\n5. 绘制复杂图案")
    
    # 同心圆
    img_pattern1 = canvas.copy()
    for i in range(10):
        radius = 150 - i * 15
        color = (255 - i*25, i*25, 128)
        img_pattern1 = drawing.draw_circle(
            img_pattern1, (300, 200), radius,
            fill=None, outline=color, width=3
        )
    basic_operations.save_image(img_pattern1, "output/examples/pattern_circles.png")
    
    # 网格
    img_grid = canvas.copy()
    for x in range(0, 600, 50):
        img_grid = drawing.draw_line(
            img_grid, (x, 0), (x, 400),
            fill=(200, 200, 200), width=1
        )
    for y in range(0, 400, 50):
        img_grid = drawing.draw_line(
            img_grid, (0, y), (600, y),
            fill=(200, 200, 200), width=1
        )
    basic_operations.save_image(img_grid, "output/examples/pattern_grid.png")
    
    # 6. 综合绘图 - 简单界面
    print("\n6. 绘制UI界面示例")
    ui = canvas.copy()
    
    # 标题栏
    ui = drawing.draw_rectangle(
        ui, [0, 0, 600, 60],
        fill=(70, 130, 180), outline=None
    )
    ui = drawing.draw_text(
        ui, (20, 15), "Sample UI Design",
        fill=(255, 255, 255), font_size=30
    )
    
    # 按钮
    button_colors = [(52, 152, 219), (46, 204, 113), (231, 76, 60)]
    button_texts = ["Button 1", "Button 2", "Button 3"]
    
    for i, (color, text) in enumerate(zip(button_colors, button_texts)):
        x = 50 + i * 180
        ui = drawing.draw_rectangle(
            ui, [x, 120, x+150, 180],
            fill=color, outline=None
        )
        ui = drawing.draw_text(
            ui, (x+30, 140), text,
            fill=(255, 255, 255), font_size=20
        )
    
    # 内容区域
    ui = drawing.draw_rectangle(
        ui, [50, 220, 550, 350],
        fill=(240, 240, 240), outline=(200, 200, 200), width=2
    )
    ui = drawing.draw_multiline_text(
        ui, (70, 240), "Content Area\nLine 2\nLine 3",
        fill=(80, 80, 80), font_size=18
    )
    
    basic_operations.save_image(ui, "output/examples/ui_design.png")
    
    # 7. 创建图表
    print("\n7. 绘制简单图表")
    chart = canvas.copy()
    
    # 绘制坐标轴
    chart = drawing.draw_line(chart, (50, 350), (550, 350), 
                             fill=(0, 0, 0), width=2)  # X轴
    chart = drawing.draw_line(chart, (50, 50), (50, 350), 
                             fill=(0, 0, 0), width=2)   # Y轴
    
    # 绘制数据点和连线
    data = [100, 150, 120, 200, 180, 250, 220, 280, 300]
    for i in range(len(data)-1):
        x1 = 80 + i * 55
        y1 = 350 - data[i]
        x2 = 80 + (i+1) * 55
        y2 = 350 - data[i+1]
        
        # 连线
        chart = drawing.draw_line(chart, (x1, y1), (x2, y2),
                                 fill=(0, 100, 200), width=2)
        # 数据点
        chart = drawing.draw_circle(chart, (x1, y1), 5,
                                   fill=(255, 0, 0), outline=None)
    
    # 最后一个点
    chart = drawing.draw_circle(
        chart, (80 + (len(data)-1) * 55, 350 - data[-1]), 5,
        fill=(255, 0, 0), outline=None
    )
    
    # 标题
    chart = drawing.draw_text(chart, (220, 20), "Simple Chart",
                             fill=(0, 0, 0), font_size=25)
    
    basic_operations.save_image(chart, "output/examples/simple_chart.png")
    
    print("\n" + "=" * 60)
    print("  ✓ 绘图功能示例完成！")
    print("  查看 output/examples/ 目录")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()

