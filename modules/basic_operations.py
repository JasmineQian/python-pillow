"""
基础图像操作模块
包含图像的创建、打开、保存、信息获取等基础功能
"""

from PIL import Image
import os


def create_new_image(width=400, height=300, color=(255, 0, 0), mode='RGB'):
    """
    创建一个新的空白图像
    
    参数:
        width: 图像宽度
        height: 图像高度
        color: 背景颜色 (R, G, B) 元组
        mode: 图像模式 ('RGB', 'RGBA', 'L' 等)
    
    返回:
        Image对象
    """
    print(f"创建新图像: {width}x{height}, 颜色: {color}, 模式: {mode}")
    img = Image.new(mode, (width, height), color)
    return img


def open_image(file_path):
    """
    打开一个图像文件
    
    参数:
        file_path: 图像文件路径
    
    返回:
        Image对象
    """
    try:
        print(f"打开图像: {file_path}")
        img = Image.open(file_path)
        return img
    except FileNotFoundError:
        print(f"错误: 找不到文件 {file_path}")
        return None
    except Exception as e:
        print(f"错误: {e}")
        return None


def save_image(img, output_path, format=None, quality=95):
    """
    保存图像到文件
    
    参数:
        img: Image对象
        output_path: 输出文件路径
        format: 图像格式 ('JPEG', 'PNG', 'GIF' 等)
        quality: JPEG图像质量 (1-95)
    """
    try:
        # 确保输出目录存在
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        if format:
            img.save(output_path, format=format, quality=quality)
        else:
            img.save(output_path, quality=quality)
        print(f"图像已保存到: {output_path}")
    except Exception as e:
        print(f"保存图像失败: {e}")


def get_image_info(img):
    """
    获取图像的详细信息
    
    参数:
        img: Image对象
    
    返回:
        包含图像信息的字典
    """
    info = {
        '格式': img.format,
        '模式': img.mode,
        '尺寸': img.size,
        '宽度': img.width,
        '高度': img.height,
        '信息': img.info
    }
    
    print("\n=== 图像信息 ===")
    for key, value in info.items():
        print(f"{key}: {value}")
    print("================\n")
    
    return info


def copy_image(img):
    """
    复制图像
    
    参数:
        img: Image对象
    
    返回:
        新的Image对象
    """
    print("复制图像")
    return img.copy()


def convert_mode(img, mode):
    """
    转换图像模式
    
    参数:
        img: Image对象
        mode: 目标模式 ('RGB', 'L', 'RGBA' 等)
    
    返回:
        转换后的Image对象
    """
    print(f"转换图像模式: {img.mode} -> {mode}")
    return img.convert(mode)


def format_conversion(input_path, output_path, output_format):
    """
    图像格式转换
    
    参数:
        input_path: 输入图像路径
        output_path: 输出图像路径
        output_format: 输出格式 ('JPEG', 'PNG', 'GIF' 等)
    """
    img = open_image(input_path)
    if img:
        save_image(img, output_path, format=output_format)
        print(f"格式转换完成: {output_format}")


def get_pixel(img, x, y):
    """
    获取指定位置的像素值
    
    参数:
        img: Image对象
        x, y: 像素坐标
    
    返回:
        像素值 (根据图像模式不同，可能是整数或元组)
    """
    pixel = img.getpixel((x, y))
    print(f"位置 ({x}, {y}) 的像素值: {pixel}")
    return pixel


def put_pixel(img, x, y, value):
    """
    设置指定位置的像素值
    
    参数:
        img: Image对象
        x, y: 像素坐标
        value: 新的像素值
    """
    img.putpixel((x, y), value)
    print(f"设置位置 ({x}, {y}) 的像素值为: {value}")


def create_gradient_image(width=400, height=300):
    """
    创建一个渐变色图像
    
    参数:
        width: 图像宽度
        height: 图像高度
    
    返回:
        Image对象
    """
    print(f"创建渐变图像: {width}x{height}")
    img = Image.new('RGB', (width, height))
    
    for y in range(height):
        for x in range(width):
            # 创建从左到右的红色渐变
            r = int(255 * x / width)
            # 创建从上到下的绿色渐变
            g = int(255 * y / height)
            b = 128
            img.putpixel((x, y), (r, g, b))
    
    return img


# 示例使用
if __name__ == "__main__":
    print("=== Pillow 基础操作示例 ===\n")
    
    # 创建输出目录
    os.makedirs("output", exist_ok=True)
    
    # 1. 创建新图像
    red_img = create_new_image(400, 300, (255, 0, 0))
    save_image(red_img, "output/01_red_image.png")
    
    # 2. 创建不同颜色的图像
    blue_img = create_new_image(400, 300, (0, 0, 255))
    save_image(blue_img, "output/02_blue_image.png")
    
    # 3. 创建渐变图像
    gradient_img = create_gradient_image(400, 300)
    save_image(gradient_img, "output/03_gradient_image.png")
    
    # 4. 获取图像信息
    get_image_info(red_img)
    
    # 5. 像素操作示例
    print("\n像素操作示例:")
    pixel_value = get_pixel(red_img, 100, 100)
    put_pixel(red_img, 200, 150, (0, 255, 0))  # 设置一个绿色像素
    
    print("\n所有示例已完成！请查看 output/ 目录")

