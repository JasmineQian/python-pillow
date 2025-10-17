# Pillow 图像处理学习项目

这是一个全面的Pillow (PIL) 学习项目，包含了各种图像处理功能的示例代码。

## 项目结构

```
1017_pillow/
├── README.md                      # 项目说明文档
├── requirement.txt                # 依赖包列表
├── main.py                        # 主程序入口，演示所有功能
├── examples/                      # 示例脚本
│   ├── run_basic.py              # 运行基础操作示例
│   ├── run_transformations.py    # 运行变换操作示例
│   ├── run_filters.py            # 运行滤镜示例
│   └── run_drawing.py            # 运行绘图示例
├── modules/                       # 功能模块
│   ├── basic_operations.py       # 基础图像操作
│   ├── transformations.py        # 图像变换
│   ├── filters_effects.py        # 滤镜和效果
│   ├── drawing.py                # 绘图功能
│   ├── color_operations.py       # 颜色操作
│   ├── composition.py            # 图像合成
│   ├── text_operations.py        # 文字操作
│   └── advanced.py               # 高级功能
├── input/                         # 输入图片目录
│   └── sample.jpg                # 示例图片
└── output/                        # 输出图片目录
```

## 功能模块说明

### 1. basic_operations.py - 基础操作
- 创建新图像
- 打开和保存图像
- 获取图像信息
- 格式转换
- 复制图像

### 2. transformations.py - 图像变换
- 调整大小 (resize)
- 旋转 (rotate)
- 裁剪 (crop)
- 翻转 (flip)
- 缩略图生成
- 透视变换

### 3. filters_effects.py - 滤镜和效果
- 模糊效果
- 锐化效果
- 边缘检测
- 浮雕效果
- 对比度调整
- 亮度调整
- 颜色增强

### 4. drawing.py - 绘图功能
- 绘制线条
- 绘制矩形
- 绘制圆形
- 绘制多边形
- 绘制文字

### 5. color_operations.py - 颜色操作
- 灰度转换
- 颜色模式转换
- 颜色分离和合并
- 反色效果
- 颜色替换

### 6. composition.py - 图像合成
- 图像混合
- 图像粘贴
- 透明度处理
- 遮罩应用

### 7. text_operations.py - 文字操作
- 添加文字水印
- 多行文字
- 文字居中
- 自定义字体

### 8. advanced.py - 高级功能
- 图像直方图
- 图像增强
- 批量处理
- 动画GIF创建

## 快速开始

### 安装依赖
```bash
source .venv/bin/activate
pip install -r requirement.txt
```

### 运行主程序
```bash
python main.py
```

### 运行单个示例
```bash
python examples/run_basic.py
python examples/run_transformations.py
python examples/run_filters.py
python examples/run_drawing.py
```

## 学习建议

1. **从基础开始**：先运行 `basic_operations.py` 了解图像的基本操作
2. **逐步深入**：按照模块顺序学习，每个模块都有详细注释
3. **动手实践**：修改参数，观察不同效果
4. **查看输出**：所有处理后的图像都会保存在 `output/` 目录
5. **阅读文档**：结合 [Pillow官方文档](https://pillow.readthedocs.io/) 学习

## 常用Pillow概念

### 图像模式
- `RGB`：彩色图像
- `RGBA`：带透明通道的彩色图像
- `L`：灰度图像
- `1`：二值图像
- `CMYK`：印刷色彩模式

### 坐标系统
- 左上角为原点 (0, 0)
- x轴向右，y轴向下

## 参考资源

- [Pillow官方文档](https://pillow.readthedocs.io/)
- [PIL官方教程](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html)
- [图像处理基础知识](https://pillow.readthedocs.io/en/stable/handbook/concepts.html)

## 注意事项

- 确保 `input/` 目录中有示例图片
- 处理后的图片会自动保存到 `output/` 目录
- 某些功能需要额外的字体文件

