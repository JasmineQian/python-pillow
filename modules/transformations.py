"""
图像变换模块
包含调整大小、旋转、裁剪、翻转等变换操作
"""

from PIL import Image


def resize_image(img, new_width, new_height, resample=Image.LANCZOS):
    """
    调整图像大小
    
    参数:
        img: Image对象
        new_width: 新宽度
        new_height: 新高度
        resample: 重采样方法 (LANCZOS, BILINEAR, BICUBIC, NEAREST)
    
    返回:
        调整大小后的Image对象
    """
    print(f"调整图像大小: {img.size} -> ({new_width}, {new_height})")
    return img.resize((new_width, new_height), resample)


def resize_by_ratio(img, ratio):
    """
    按比例调整图像大小
    
    参数:
        img: Image对象
        ratio: 缩放比例 (如 0.5 表示缩小到原来的50%)
    
    返回:
        调整大小后的Image对象
    """
    new_width = int(img.width * ratio)
    new_height = int(img.height * ratio)
    print(f"按比例 {ratio} 调整图像大小: {img.size} -> ({new_width}, {new_height})")
    return img.resize((new_width, new_height), Image.LANCZOS)


def rotate_image(img, angle, expand=False, fillcolor=None):
    """
    旋转图像
    
    参数:
        img: Image对象
        angle: 旋转角度 (逆时针)
        expand: 是否扩展画布以适应旋转后的图像
        fillcolor: 填充颜色
    
    返回:
        旋转后的Image对象
    """
    print(f"旋转图像: {angle}度, 扩展画布: {expand}")
    return img.rotate(angle, expand=expand, fillcolor=fillcolor)


def crop_image(img, left, top, right, bottom):
    """
    裁剪图像
    
    参数:
        img: Image对象
        left, top, right, bottom: 裁剪区域的坐标
    
    返回:
        裁剪后的Image对象
    """
    print(f"裁剪图像: ({left}, {top}, {right}, {bottom})")
    return img.crop((left, top, right, bottom))


def crop_center(img, crop_width, crop_height):
    """
    从中心裁剪图像
    
    参数:
        img: Image对象
        crop_width: 裁剪宽度
        crop_height: 裁剪高度
    
    返回:
        裁剪后的Image对象
    """
    center_x = img.width / 2
    center_y = img.height / 2
    
    left = int(center_x - crop_width / 2)
    top = int(center_y - crop_height / 2)
    right = int(center_x + crop_width / 2)
    bottom = int(center_y + crop_height / 2)
    
    print(f"从中心裁剪图像: {crop_width}x{crop_height}")
    return img.crop((left, top, right, bottom))


def flip_horizontal(img):
    """
    水平翻转图像
    
    参数:
        img: Image对象
    
    返回:
        翻转后的Image对象
    """
    print("水平翻转图像")
    return img.transpose(Image.FLIP_LEFT_RIGHT)


def flip_vertical(img):
    """
    垂直翻转图像
    
    参数:
        img: Image对象
    
    返回:
        翻转后的Image对象
    """
    print("垂直翻转图像")
    return img.transpose(Image.FLIP_TOP_BOTTOM)


def create_thumbnail(img, max_size=(128, 128)):
    """
    创建缩略图 (保持宽高比)
    
    参数:
        img: Image对象
        max_size: 最大尺寸 (宽, 高)
    
    返回:
        缩略图Image对象
    """
    print(f"创建缩略图: 最大尺寸 {max_size}")
    img_copy = img.copy()
    img_copy.thumbnail(max_size, Image.LANCZOS)
    return img_copy


def transpose_image(img, method):
    """
    转置图像
    
    参数:
        img: Image对象
        method: 转置方法
            - Image.FLIP_LEFT_RIGHT: 水平翻转
            - Image.FLIP_TOP_BOTTOM: 垂直翻转
            - Image.ROTATE_90: 旋转90度
            - Image.ROTATE_180: 旋转180度
            - Image.ROTATE_270: 旋转270度
            - Image.TRANSPOSE: 对角线翻转
            - Image.TRANSVERSE: 反对角线翻转
    
    返回:
        转置后的Image对象
    """
    print(f"转置图像: {method}")
    return img.transpose(method)


def fit_image(img, target_width, target_height, method=Image.LANCZOS, centering=(0.5, 0.5)):
    """
    将图像适配到指定尺寸 (会裁剪)
    
    参数:
        img: Image对象
        target_width: 目标宽度
        target_height: 目标高度
        method: 重采样方法
        centering: 居中方式 (0.5, 0.5) 表示中心
    
    返回:
        适配后的Image对象
    """
    from PIL import ImageOps
    print(f"适配图像到: {target_width}x{target_height}")
    return ImageOps.fit(img, (target_width, target_height), method, centering=centering)


def pad_image(img, target_width, target_height, color=(255, 255, 255)):
    """
    填充图像到指定尺寸 (不会裁剪)
    
    参数:
        img: Image对象
        target_width: 目标宽度
        target_height: 目标高度
        color: 填充颜色
    
    返回:
        填充后的Image对象
    """
    from PIL import ImageOps
    print(f"填充图像到: {target_width}x{target_height}")
    return ImageOps.pad(img, (target_width, target_height), color=color)


# 示例使用
if __name__ == "__main__":
    print("=== Pillow 图像变换示例 ===\n")
    
    import os
    from basic_operations import create_gradient_image, save_image
    
    # 创建输出目录
    os.makedirs("output", exist_ok=True)
    
    # 创建一个测试图像
    test_img = create_gradient_image(400, 300)
    save_image(test_img, "output/transform_original.png")
    
    # 1. 调整大小
    resized = resize_image(test_img, 200, 150)
    save_image(resized, "output/04_resized.png")
    
    # 2. 按比例缩放
    scaled = resize_by_ratio(test_img, 0.5)
    save_image(scaled, "output/05_scaled_50percent.png")
    
    # 3. 旋转
    rotated_45 = rotate_image(test_img, 45, expand=True, fillcolor=(0, 0, 0))
    save_image(rotated_45, "output/06_rotated_45.png")
    
    rotated_90 = rotate_image(test_img, 90)
    save_image(rotated_90, "output/07_rotated_90.png")
    
    # 4. 裁剪
    cropped = crop_image(test_img, 50, 50, 350, 250)
    save_image(cropped, "output/08_cropped.png")
    
    # 5. 中心裁剪
    center_cropped = crop_center(test_img, 200, 200)
    save_image(center_cropped, "output/09_center_cropped.png")
    
    # 6. 翻转
    h_flipped = flip_horizontal(test_img)
    save_image(h_flipped, "output/10_flipped_horizontal.png")
    
    v_flipped = flip_vertical(test_img)
    save_image(v_flipped, "output/11_flipped_vertical.png")
    
    # 7. 创建缩略图
    thumbnail = create_thumbnail(test_img, (128, 128))
    save_image(thumbnail, "output/12_thumbnail.png")
    
    # 8. 适配和填充
    fitted = fit_image(test_img, 300, 300)
    save_image(fitted, "output/13_fitted.png")
    
    padded = pad_image(test_img, 500, 500, (100, 100, 100))
    save_image(padded, "output/14_padded.png")
    
    print("\n所有变换示例已完成！请查看 output/ 目录")

