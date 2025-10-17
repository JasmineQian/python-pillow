"""
CSV转图像脚本
读取CSV文件并生成美观的表格图像
"""

from PIL import Image, ImageDraw, ImageFont
import csv
import os


def read_csv(file_path):
    """读取CSV文件"""
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data


def get_font(size=12):
    """获取字体"""
    try:
        # 尝试使用系统字体
        return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
    except:
        try:
            return ImageFont.truetype("Arial.ttf", size)
        except:
            return ImageFont.load_default()


def calculate_column_widths(data, font, min_width=80, max_width=400, scale=1):
    """计算每列的最佳宽度"""
    if not data:
        return []
    
    num_cols = len(data[0])
    col_widths = [min_width] * num_cols
    
    # 创建临时图像用于测量文字
    temp_img = Image.new('RGB', (1, 1))
    draw = ImageDraw.Draw(temp_img)
    
    # padding按比例缩放
    cell_padding = int(30 * scale)
    
    for row in data:
        for i, cell in enumerate(row):
            if i < num_cols:
                # 获取文字边界框
                bbox = draw.textbbox((0, 0), str(cell), font=font)
                text_width = bbox[2] - bbox[0] + cell_padding  # 添加更多padding
                col_widths[i] = max(col_widths[i], min(text_width, max_width))
    
    return col_widths


def wrap_text(text, font, max_width, scale=1):
    """文字自动换行"""
    if not text:
        return [""]
    
    temp_img = Image.new('RGB', (1, 1))
    draw = ImageDraw.Draw(temp_img)
    
    # 考虑内边距
    padding = int(20 * scale)
    available_width = max_width - padding
    
    text_str = str(text)
    
    # 先尝试整行
    bbox = draw.textbbox((0, 0), text_str, font=font)
    if bbox[2] - bbox[0] <= available_width:
        return [text_str]
    
    # 需要换行
    words = text_str.split()
    lines = []
    current_line = []
    
    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        width = bbox[2] - bbox[0]
        
        if width <= available_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
                current_line = [word]
            else:
                # 单个词太长，强制换行
                lines.append(word)
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines if lines else [""]


def create_table_image(csv_path, output_path, cell_height=35, header_height=45,
                       padding=10, header_bg=(41, 128, 185), 
                       alt_row_bg=(236, 240, 241), normal_row_bg=(255, 255, 255),
                       text_color=(44, 62, 80), header_text_color=(255, 255, 255),
                       border_color=(189, 195, 199), scale=1, dpi=(96, 96)):
    """
    创建表格图像
    
    参数:
        csv_path: CSV文件路径
        output_path: 输出图像路径
        cell_height: 单元格高度
        header_height: 表头高度
        padding: 内边距
        header_bg: 表头背景色
        alt_row_bg: 交替行背景色
        normal_row_bg: 正常行背景色
        text_color: 文字颜色
        header_text_color: 表头文字颜色
        border_color: 边框颜色
        scale: 缩放倍数（用于高分辨率）
        dpi: 图像DPI设置
    """
    
    print(f"读取CSV文件: {csv_path}")
    data = read_csv(csv_path)
    
    if not data:
        print("CSV文件为空")
        return
    
    print(f"数据行数: {len(data)}")
    
    # 应用缩放到所有尺寸参数
    cell_height = int(cell_height * scale)
    header_height = int(header_height * scale)
    padding = int(padding * scale)
    
    # 获取字体（根据缩放调整大小）
    header_font = get_font(int(14 * scale))
    cell_font = get_font(int(11 * scale))
    
    # 计算列宽（传入scale参数）
    col_widths = calculate_column_widths(data, cell_font, 
                                        min_width=int(80 * scale), 
                                        max_width=int(400 * scale),
                                        scale=scale)
    print(f"列宽: {col_widths}")
    
    # 预计算所有行高（用于确定总高度）
    line_spacing = int(15 * scale)
    min_height = int(25 * scale)
    row_heights = []
    
    for row_idx, row in enumerate(data):
        if row_idx == 0:
            base_height = header_height
            font = header_font
        else:
            base_height = cell_height
            font = cell_font
        
        # 计算这一行的最大行数
        max_lines = 1
        for col_idx, cell in enumerate(row):
            if col_idx < len(col_widths):
                col_width = col_widths[col_idx]
                cell_text = str(cell).strip()
                lines = wrap_text(cell_text, font, col_width, scale=scale)
                max_lines = max(max_lines, len(lines))
        
        row_height = max(base_height, max_lines * line_spacing + min_height)
        row_heights.append(row_height)
    
    # 计算图像尺寸
    table_width = sum(col_widths) + padding * 2
    table_height = sum(row_heights) + padding * 2
    
    print(f"图像尺寸: {table_width}x{table_height}")
    
    # 创建图像
    img = Image.new('RGB', (table_width, table_height), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # 绘制表格
    current_y = padding
    
    for row_idx, row in enumerate(data):
        current_x = padding
        
        # 使用预计算的行高
        row_height = row_heights[row_idx]
        
        # 确定背景色和字体
        if row_idx == 0:
            # 表头
            bg_color = header_bg
            font = header_font
            text_col = header_text_color
        else:
            # 数据行
            # 交替行颜色
            bg_color = alt_row_bg if row_idx % 2 == 0 else normal_row_bg
            font = cell_font
            text_col = text_color
        
        # 绘制行背景
        draw.rectangle(
            [current_x, current_y, table_width - padding, current_y + row_height],
            fill=bg_color
        )
        
        # 绘制单元格
        for col_idx, cell in enumerate(row):
            if col_idx >= len(col_widths):
                break
            
            col_width = col_widths[col_idx]
            
            # 绘制单元格边框
            draw.rectangle(
                [current_x, current_y, current_x + col_width, current_y + row_height],
                outline=border_color,
                width=max(1, int(1 * scale))
            )
            
            # 绘制文字
            cell_text = str(cell).strip()
            
            # 文字换行（传入scale）
            lines = wrap_text(cell_text, font, col_width, scale=scale)
            
            # 计算文字位置
            line_spacing = int(15 * scale)
            text_y = current_y + (row_height - len(lines) * line_spacing) // 2
            left_padding = int(10 * scale)  # 左侧内边距
            
            for line in lines:
                bbox = draw.textbbox((0, 0), line, font=font)
                text_width = bbox[2] - bbox[0]
                
                # 第一列左对齐，其他列居中
                if col_idx == 0:
                    # 左对齐
                    text_x = current_x + left_padding
                else:
                    # 居中
                    text_x = current_x + (col_width - text_width) // 2
                
                # 绘制文字
                draw.text((text_x, text_y), line, fill=text_col, font=font)
                text_y += line_spacing
            
            current_x += col_width
        
        current_y += row_height
    
    # 绘制外边框
    draw.rectangle(
        [padding, padding, table_width - padding, table_height - padding],
        outline=border_color,
        width=max(2, int(2 * scale))
    )
    
    # 保存图像（设置DPI）
    img.save(output_path, quality=95, dpi=dpi)
    print(f"\n✓ 表格图像已保存到: {output_path}")
    print(f"  尺寸: {table_width}x{table_height} 像素")
    print(f"  DPI: {dpi[0]}")
    print(f"  缩放: {scale}x")
    print(f"  行数: {len(data)} (含表头)")


def create_compact_table_image(csv_path, output_path, scale=1, dpi=(96, 96)):
    """创建紧凑版表格图像（较小的尺寸）"""
    print("创建紧凑版表格...")
    create_table_image(
        csv_path, 
        output_path,
        cell_height=30,
        header_height=40,
        padding=8,
        scale=scale,
        dpi=dpi
    )


def create_large_table_image(csv_path, output_path, scale=1, dpi=(96, 96)):
    """创建大尺寸表格图像（更易阅读）"""
    print("创建大尺寸表格...")
    create_table_image(
        csv_path,
        output_path,
        cell_height=45,
        header_height=55,
        padding=15,
        header_bg=(52, 73, 94),
        alt_row_bg=(245, 247, 250),
        border_color=(149, 165, 166),
        scale=scale,
        dpi=dpi
    )


def create_colorful_table_image(csv_path, output_path, scale=1, dpi=(96, 96)):
    """创建彩色主题表格"""
    print("创建彩色主题表格...")
    create_table_image(
        csv_path,
        output_path,
        cell_height=38,
        header_height=48,
        padding=12,
        header_bg=(142, 68, 173),  # 紫色
        alt_row_bg=(250, 219, 216),  # 浅粉
        normal_row_bg=(255, 250, 240),  # 米色
        border_color=(142, 68, 173),
        scale=scale,
        dpi=dpi
    )


def create_professional_table_image(csv_path, output_path, scale=1, dpi=(96, 96)):
    """创建专业风格表格（商务风）"""
    print("创建专业风格表格...")
    create_table_image(
        csv_path,
        output_path,
        cell_height=40,
        header_height=50,
        padding=10,
        header_bg=(34, 49, 63),  # 深蓝灰
        alt_row_bg=(248, 249, 250),  # 极浅灰
        normal_row_bg=(255, 255, 255),  # 白色
        text_color=(33, 37, 41),
        border_color=(206, 212, 218),
        scale=scale,
        dpi=dpi
    )


def main():
    """主函数"""
    print("=" * 70)
    print("  CSV转表格图像工具 - 高清版")
    print("=" * 70 + "\n")
    
    # CSV文件路径
    csv_path = "input/bbm_test_suites.csv"
    
    if not os.path.exists(csv_path):
        print(f"错误: 找不到文件 {csv_path}")
        return
    
    # 创建输出目录
    os.makedirs("output", exist_ok=True)
    
    # 生成标准分辨率的表格图像
    print("\n【标准分辨率版本 - 96 DPI】")
    print("=" * 70)
    
    print("\n1. 生成标准表格...")
    create_table_image(csv_path, "output/table_standard.png")
    
    print("\n2. 生成紧凑版表格...")
    create_compact_table_image(csv_path, "output/table_compact.png")
    
    print("\n3. 生成大尺寸表格...")
    create_large_table_image(csv_path, "output/table_large.png")
    
    print("\n4. 生成彩色主题表格...")
    create_colorful_table_image(csv_path, "output/table_colorful.png")
    
    print("\n5. 生成专业风格表格...")
    create_professional_table_image(csv_path, "output/table_professional.png")
    
    # 生成高分辨率版本（2倍）
    print("\n\n【高分辨率版本 - 2x 缩放, 300 DPI】")
    print("=" * 70)
    
    print("\n6. 生成高清标准表格 (2x)...")
    create_table_image(csv_path, "output/table_standard_2x.png", scale=2, dpi=(300, 300))
    
    print("\n7. 生成高清专业风格表格 (2x)...")
    create_professional_table_image(csv_path, "output/table_professional_2x.png", 
                                   scale=2, dpi=(300, 300))
    
    # 生成超高分辨率版本（3倍）
    print("\n\n【超高分辨率版本 - 3x 缩放, 300 DPI】")
    print("=" * 70)
    
    print("\n8. 生成超高清标准表格 (3x)...")
    create_table_image(csv_path, "output/table_standard_3x.png", scale=3, dpi=(300, 300))
    
    print("\n9. 生成超高清专业风格表格 (3x)...")
    create_professional_table_image(csv_path, "output/table_professional_3x.png", 
                                   scale=3, dpi=(300, 300))
    
    print("\n" + "=" * 70)
    print("  ✓ 所有表格图像已生成完成！")
    print("=" * 70)
    print("\n生成的文件:")
    print("\n【标准分辨率 (96 DPI)】")
    print("  - output/table_standard.png          (标准风格)")
    print("  - output/table_compact.png           (紧凑版)")
    print("  - output/table_large.png             (大尺寸)")
    print("  - output/table_colorful.png          (彩色主题)")
    print("  - output/table_professional.png      (专业商务风)")
    print("\n【高分辨率 (2x, 300 DPI) - 推荐用于打印和放大查看】")
    print("  - output/table_standard_2x.png       (高清标准)")
    print("  - output/table_professional_2x.png   (高清专业)")
    print("\n【超高分辨率 (3x, 300 DPI) - 最清晰，适合大屏展示】")
    print("  - output/table_standard_3x.png       (超高清标准)")
    print("  - output/table_professional_3x.png   (超高清专业)")
    print("\n💡 提示: 高分辨率版本放大后依然清晰，适合打印和演示！")
    print()


if __name__ == "__main__":
    main()

