# OCR识别最佳实践

## Tesseract OCR参数调优

### 基础参数
- `--psm (Page Segmentation Mode)`: 页面分割模式
  - `3`: 自动页面分割（默认）
  - `6`: 假设为统一文本块（适合书籍）
  - `1`: 自动，带OSD（方向和脚本检测）
  
- `-l (Language)`: 语言设置
  - `chi_sim`: 简体中文
  - `chi_tra`: 繁体中文  
  - `eng`: 英文
  - `chi_sim+eng`: 中英混合

### 高级参数
- `--oem (OCR Engine Mode)`: OCR引擎模式
  - `3`: 默认，基于LSTM
  - `1`: 传统神经网络
  - `0`: 传统Tesseract only

- `--dpi`: 指定DPI（当从PDF转换时）

### 针对不同文档类型的推荐配置

#### 书籍文档
```
--psm 6 -l chi_sim+eng --oem 3
```

#### 杂志/报纸
```
--psm 3 -l chi_sim+eng --oem 3
```

#### 表格文档
```
--psm 6 -l chi_sim+eng --oem 3 --tessdata-dir /path/to/tessdata
```

## 图像预处理优化

### 1. 分辨率设置
- 推荐DPI: 300-400
- 最低DPI: 200（会显著影响识别准确率）
- 过高DPI: >500（处理时间长，收益有限）

### 2. 图像增强
```python
from PIL import Image, ImageEnhance, ImageFilter

# 增强对比度
enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(1.5)

# 去噪
image = image.filter(ImageFilter.MedianFilter())

# 二值化（可选）
image = image.convert('L')
threshold = 127
image = image.point(lambda x: 0 if x < threshold else 255, '1')
```

### 3. 倾斜校正
对于扫描倾斜的文档，需要进行倾斜校正：
```python
import cv2
import numpy as np

# 使用OpenCV检测倾斜角度并校正
def correct_skew(image):
    # 转换为OpenCV格式
    img_array = np.array(image)
    
    # 转灰度
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    
    # 边缘检测
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    
    # 霍夫线变换检测直线
    lines = cv2.HoughLines(edges, 1, np.pi/180, 100)
    
    if lines is not None:
        # 计算平均角度
        angles = []
        for rho, theta in lines:
            angle = np.degrees(theta) - 90
            angles.append(angle)
        
        median_angle = np.median(angles)
        
        # 旋转图像
        rotated = rotate_image(image, median_angle)
        return rotated
    
    return image
```

## 置信度分析

### 置信度阈值设置
- **高质量文档**: 80%以上
- **中等质量**: 60-80%
- **低质量**: 40-60%
- **需人工校对**: 40%以下

### 置信度提升策略
1. **预处理优化**: 图像增强、去噪、倾斜校正
2. **参数调整**: 根据文档类型选择合适的PSM模式
3. **语言模型**: 确保安装了正确的语言包
4. **分块处理**: 对复杂页面分区域识别

## 性能优化

### 并行处理
```python
from concurrent.futures import ThreadPoolExecutor
import pytesseract

def process_page(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='chi_sim+eng')
    return text

# 使用线程池并行处理
with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(process_page, image_paths)
```

### 内存管理
对于大文件，避免一次性加载所有页面：
```python
def process_large_pdf(pdf_path, chunk_size=10):
    # 分批处理
    for i in range(0, total_pages, chunk_size):
        chunk_images = convert_pdf_chunk(pdf_path, i, chunk_size)
        for image in chunk_images:
            process_page(image)
        # 释放内存
        del chunk_images
```

## 错误处理

### 常见错误及解决方案

1. **Tesseract not found**
   ```bash
   # 安装Tesseract OCR
   # Ubuntu/Debian
   sudo apt-get install tesseract-ocr tesseract-ocr-chi-sim
   
   # macOS
   brew install tesseract tesseract-lang
   
   # Windows
   # 下载安装包: https://github.com/UB-Mannheim/tesseract/wiki
   ```

2. **Language data not found**
   ```bash
   # 下载中文语言包
   # Ubuntu/Debian
   sudo apt-get install tesseract-ocr-chi-sim
   
   # 手动下载语言包
   wget https://github.com/tesseract-ocr/tessdata/raw/main/chi_sim.traineddata
   sudo mv chi_sim.traineddata /usr/share/tesseract-ocr/4.00/tessdata/
   ```

3. **Memory error**
   - 降低DPI设置
   - 分批处理页面
   - 增加系统交换空间

4. **Poor recognition quality**
   - 检查图像质量
   - 调整PSM参数
   - 尝试图像预处理
   - 考虑使用其他OCR引擎

## 质量评估

### 自动评估指标
1. **平均置信度**: 衡量整体识别质量
2. **空白率**: 识别空白字符的比例
3. **特殊字符率**: OCR产生的乱码字符比例

### 人工检查要点
1. 章节标题是否正确识别
2. 表格格式是否保持
3. 公式和特殊符号是否准确
4. 图片区域的处理是否合理

## 性能基准

### 典型处理时间（基于300 DPI）
| 文档类型 | 页数 | 处理时间 | 内存使用 |
|---------|------|----------|----------|
| 简单文本 | 100页 | 2-3分钟 | 500MB |
| 复杂排版 | 100页 | 5-8分钟 | 1GB |
| 高质量扫描 | 100页 | 3-5分钟 | 600MB |
| 低质量扫描 | 100页 | 8-15分钟 | 1.2GB |

### 硬件建议
- **CPU**: 多核处理器（4核以上）
- **内存**: 最低4GB，推荐8GB
- **存储**: SSD硬盘（显著提升I/O性能）