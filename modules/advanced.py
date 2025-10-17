"""
高级功能模块
包含图像直方图、图像增强、批量处理、GIF动画等高级功能
"""

from PIL import Image, ImageStat, ImageSequence
import os


def get_histogram(img):
    """
    获取图像直方图
    
    参数:
        img: Image对象
    
    返回:
        直方图数据列表
    """
    print(f"获取图像直方图: 模式 {img.mode}")
    return img.histogram()


def get_statistics(img):
    """
    获取图像统计信息
    
    参数:
        img: Image对象
    
    返回:
        统计信息字典
    """
    print("获取图像统计信息")
    stat = ImageStat.Stat(img)
    
    info = {
        '平均值': stat.mean,
        '中位数': stat.median,
        '标准差': stat.stddev,
        '极值': stat.extrema,
        '总和': stat.sum,
        '平方和': stat.sum2
    }
    
    print("\n=== 图像统计信息 ===")
    for key, value in info.items():
        print(f"{key}: {value}")
    print("==================\n")
    
    return info


def get_extrema(img):
    """
    获取图像的最小和最大像素值
    
    参数:
        img: Image对象
    
    返回:
        每个通道的 (min, max) 元组列表
    """
    print("获取图像极值")
    return img.getextrema()


def get_bbox(img):
    """
    获取非零区域的边界框
    
    参数:
        img: Image对象
    
    返回:
        (left, top, right, bottom) 或 None
    """
    print("获取非零区域边界框")
    return img.getbbox()


def quantize_colors(img, colors=256, method=None, kmeans=0):
    """
    量化颜色（减少颜色数量）
    
    参数:
        img: Image对象
        colors: 目标颜色数量
        method: 量化方法
        kmeans: k-means迭代次数
    
    返回:
        量化后的图像
    """
    print(f"量化颜色: 目标 {colors} 种颜色")
    return img.quantize(colors=colors, method=method, kmeans=kmeans)


def create_palette_image(colors, width=256, height=100):
    """
    创建调色板图像
    
    参数:
        colors: 颜色列表 [(R,G,B), ...]
        width: 图像宽度
        height: 图像高度
    
    返回:
        调色板图像
    """
    print(f"创建调色板: {len(colors)} 种颜色")
    img = Image.new('RGB', (width, height))
    
    stripe_width = width // len(colors)
    
    for i, color in enumerate(colors):
        for x in range(i * stripe_width, (i + 1) * stripe_width):
            for y in range(height):
                if x < width:  # 防止越界
                    img.putpixel((x, y), color)
    
    return img


def batch_process_images(input_dir, output_dir, operation, **kwargs):
    """
    批量处理图像
    
    参数:
        input_dir: 输入目录
        output_dir: 输出目录
        operation: 要应用的操作函数
        **kwargs: 传递给操作函数的参数
    
    返回:
        处理的文件数量
    """
    print(f"批量处理图像: {input_dir} -> {output_dir}")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    count = 0
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            try:
                img = Image.open(input_path)
                processed = operation(img, **kwargs)
                processed.save(output_path)
                print(f"  处理: {filename}")
                count += 1
            except Exception as e:
                print(f"  错误处理 {filename}: {e}")
    
    print(f"批量处理完成: {count} 个文件")
    return count


def create_animated_gif(images, output_path, duration=500, loop=0):
    """
    创建GIF动画
    
    参数:
        images: Image对象列表或文件路径列表
        output_path: 输出GIF路径
        duration: 每帧持续时间（毫秒）
        loop: 循环次数（0表示无限循环）
    """
    print(f"创建GIF动画: {len(images)} 帧, 每帧 {duration}ms")
    
    # 如果是文件路径，加载图像
    image_objects = []
    for img in images:
        if isinstance(img, str):
            image_objects.append(Image.open(img))
        else:
            image_objects.append(img)
    
    # 保存为GIF
    if image_objects:
        image_objects[0].save(
            output_path,
            save_all=True,
            append_images=image_objects[1:],
            duration=duration,
            loop=loop
        )
        print(f"GIF动画已保存到: {output_path}")


def extract_gif_frames(gif_path, output_dir):
    """
    提取GIF的所有帧
    
    参数:
        gif_path: GIF文件路径
        output_dir: 输出目录
    
    返回:
        提取的帧数
    """
    print(f"提取GIF帧: {gif_path}")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    img = Image.open(gif_path)
    frame_count = 0
    
    for i, frame in enumerate(ImageSequence.Iterator(img)):
        frame_path = os.path.join(output_dir, f"frame_{i:03d}.png")
        frame.save(frame_path)
        frame_count += 1
    
    print(f"提取了 {frame_count} 帧")
    return frame_count


def create_thumbnail_grid(images, grid_size=(3, 3), thumb_size=(150, 150), 
                         spacing=10, bg_color=(255, 255, 255)):
    """
    创建缩略图网格
    
    参数:
        images: Image对象列表
        grid_size: 网格大小 (列, 行)
        thumb_size: 缩略图大小
        spacing: 间距
        bg_color: 背景颜色
    
    返回:
        网格图像
    """
    print(f"创建缩略图网格: {grid_size[0]}x{grid_size[1]}")
    
    cols, rows = grid_size
    
    # 计算总尺寸
    total_width = cols * thumb_size[0] + (cols + 1) * spacing
    total_height = rows * thumb_size[1] + (rows + 1) * spacing
    
    # 创建背景
    grid_img = Image.new('RGB', (total_width, total_height), bg_color)
    
    # 粘贴缩略图
    for i, img in enumerate(images[:cols * rows]):
        row = i // cols
        col = i % cols
        
        # 创建缩略图
        thumb = img.copy()
        thumb.thumbnail(thumb_size, Image.LANCZOS)
        
        # 计算位置
        x = spacing + col * (thumb_size[0] + spacing)
        y = spacing + row * (thumb_size[1] + spacing)
        
        # 粘贴（居中）
        offset_x = (thumb_size[0] - thumb.width) // 2
        offset_y = (thumb_size[1] - thumb.height) // 2
        
        grid_img.paste(thumb, (x + offset_x, y + offset_y))
    
    return grid_img


def create_contact_sheet(image_paths, columns=4, thumb_size=(200, 200)):
    """
    创建联系表（缩略图集合）
    
    参数:
        image_paths: 图像路径列表
        columns: 列数
        thumb_size: 缩略图大小
    
    返回:
        联系表图像
    """
    print(f"创建联系表: {len(image_paths)} 张图片, {columns} 列")
    
    images = [Image.open(path) for path in image_paths]
    rows = (len(images) + columns - 1) // columns
    
    return create_thumbnail_grid(images, (columns, rows), thumb_size)


def apply_noise(img, amount=50):
    """
    添加噪点
    
    参数:
        img: Image对象
        amount: 噪点强度
    
    返回:
        添加噪点后的图像
    """
    import random
    print(f"添加噪点: 强度 {amount}")
    
    img_copy = img.copy()
    pixels = img_copy.load()
    
    for y in range(img.height):
        for x in range(img.width):
            if random.randint(0, 100) < amount:
                # 添加随机噪点
                if img.mode == 'RGB':
                    noise = random.randint(-30, 30)
                    r, g, b = pixels[x, y]
                    pixels[x, y] = (
                        max(0, min(255, r + noise)),
                        max(0, min(255, g + noise)),
                        max(0, min(255, b + noise))
                    )
                elif img.mode == 'L':
                    noise = random.randint(-30, 30)
                    pixels[x, y] = max(0, min(255, pixels[x, y] + noise))
    
    return img_copy


def create_mosaic(img, pixel_size=10):
    """
    创建马赛克效果
    
    参数:
        img: Image对象
        pixel_size: 马赛克像素大小
    
    返回:
        马赛克效果图像
    """
    print(f"创建马赛克效果: 像素大小 {pixel_size}")
    
    # 缩小
    small = img.resize(
        (img.width // pixel_size, img.height // pixel_size),
        Image.NEAREST
    )
    
    # 放大回原尺寸
    return small.resize(img.size, Image.NEAREST)


# 示例使用
if __name__ == "__main__":
    print("=== Pillow 高级功能示例 ===\n")
    
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from modules.basic_operations import create_gradient_image, create_new_image, save_image
    from modules.transformations import resize_image, rotate_image
    
    # 创建输出目录
    os.makedirs("output", exist_ok=True)
    
    # 创建测试图像
    test_img = create_gradient_image(400, 300)
    
    # 1. 获取统计信息
    stats = get_statistics(test_img)
    extrema = get_extrema(test_img)
    print(f"图像极值: {extrema}\n")
    
    # 2. 颜色量化
    quantized = quantize_colors(test_img, colors=16)
    save_image(quantized.convert('RGB'), "output/73_quantized.png")
    
    # 3. 创建调色板
    palette_colors = [
        (255, 0, 0), (0, 255, 0), (0, 0, 255),
        (255, 255, 0), (255, 0, 255), (0, 255, 255),
        (128, 0, 0), (0, 128, 0)
    ]
    palette = create_palette_image(palette_colors, width=400, height=100)
    save_image(palette, "output/74_palette.png")
    
    # 4. 马赛克效果
    mosaic = create_mosaic(test_img, pixel_size=15)
    save_image(mosaic, "output/75_mosaic.png")
    
    # 5. 添加噪点
    noisy = apply_noise(test_img, amount=30)
    save_image(noisy, "output/76_noisy.png")
    
    # 6. 创建GIF动画
    print("\n创建GIF动画示例:")
    frames = []
    base_img = create_new_image(200, 200, (100, 150, 200))
    
    # 创建旋转动画帧
    for angle in range(0, 360, 30):
        rotated = rotate_image(base_img, angle, expand=False)
        frames.append(rotated)
    
    create_animated_gif(frames, "output/77_rotation_animation.gif", 
                       duration=100, loop=0)
    
    # 7. 创建缩小放大动画
    print("\n创建缩放动画:")
    scale_frames = []
    for scale in [1.0, 1.2, 1.4, 1.6, 1.4, 1.2, 1.0, 0.8, 0.6, 0.8]:
        new_size = (int(200 * scale), int(200 * scale))
        scaled = resize_image(base_img, new_size[0], new_size[1])
        # 居中放置在200x200画布上
        canvas = create_new_image(200, 200, (200, 200, 200))
        offset = ((200 - scaled.width) // 2, (200 - scaled.height) // 2)
        canvas.paste(scaled, offset)
        scale_frames.append(canvas)
    
    create_animated_gif(scale_frames, "output/78_scale_animation.gif",
                       duration=100, loop=0)
    
    # 8. 创建缩略图网格
    print("\n创建缩略图网格:")
    grid_images = []
    colors = [
        (255, 100, 100), (100, 255, 100), (100, 100, 255),
        (255, 255, 100), (255, 100, 255), (100, 255, 255),
        (200, 150, 100), (150, 100, 200), (100, 200, 150)
    ]
    
    for color in colors:
        grid_images.append(create_new_image(150, 150, color))
    
    thumbnail_grid = create_thumbnail_grid(grid_images, grid_size=(3, 3),
                                          thumb_size=(120, 120), spacing=10)
    save_image(thumbnail_grid, "output/79_thumbnail_grid.png")
    
    print("\n所有高级功能示例已完成！请查看 output/ 目录")

