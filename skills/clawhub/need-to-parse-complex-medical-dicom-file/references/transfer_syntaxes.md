# Transfer Syntax 速查表（供参考 · 定性）

> 依据：DICOM PS3.5 2026c 附录 A（注册 UID）；2026-09-06 经 3 个独立来源交叉核对
> （meddream conformance statement 2020-08-19 · Gdcm 3.0 ConformanceSummary · postdicom 综述）。
> **供参考：以 PS3.5 官方附录为准。**

## 未压缩（本工具可解析元数据+像素）

| UID | 名称 | 本工具 |
|---|---|---|
| 1.2.840.10008.1.2 | Implicit VR Little Endian | ✓ 完整（默认语法，任何合规实现必须支持） |
| 1.2.840.10008.1.2.1 | Explicit VR Little Endian | ✓ 完整 |
| 1.2.840.10008.1.2.1.99 | Deflated Explicit VR Little Endian | △ 仅 file meta（zlib 流未解，警告） |
| 1.2.840.10008.1.2.2 | Explicit VR Big Endian（已退役） | △ 尽力解析，提示 pydicom 复核 |

## 封装/压缩（encapsulated；像素 = 0xFFFFFFFF 未定义长度 + FFFE,E000 片段 + FFFE,E0DD）

| UID | 名称 | 备注 |
|---|---|---|
| 1.2.840.10008.1.2.4.50 | JPEG Baseline (Process 1, 8-bit) | **仅 8 位**；16 位 CT/MR 用它即违规（常见损坏/误配信号） |
| 1.2.840.10008.1.2.4.51 | JPEG Baseline (Process 2, 12-bit) | |
| 1.2.840.10008.1.2.4.57 | JPEG Lossless (Process 14) | |
| 1.2.840.10008.1.2.4.70 | JPEG Lossless, First-Order Prediction（默认无损） | |
| 1.2.840.10008.1.2.4.80 | JPEG-LS Lossless | |
| 1.2.840.10008.1.2.4.81 | JPEG-LS Near-Lossless | |
| 1.2.840.10008.1.2.4.90 | JPEG 2000 Part 1 (lossless) | |
| 1.2.840.10008.1.2.4.91 | JPEG 2000 Part 1 | |
| 1.2.840.10008.1.2.4.100/101/102 | MPEG2 / MPEG-4 AVC 视频 | 动态序列 |
| 1.2.840.10008.1.2.5 | RLE Lossless | pydicom ≥2.2 内置 numpy RLE 处理器 |

**本工具对以上全部：检测 → 报告 transfer_syntax.name/class + fragment 数 → 给出精确解码命令 → exit 2（像素相关命令）。绝不猜测像素值。**

## 解码外部依赖（诚实指向）

```bash
pip install 'pydicom' 'pylibjpeg[all]'
python3 -c "from pydicom import dcmread; ds = dcmread('FILE'); print(ds.pixel_array.shape, ds.file_meta.TransferSyntaxUID.name)"
```
- pylibjpeg 插件分工（pylibjpeg 2.1.0 README/PyPI, 2026-09-06 核对）：
  - libjpeg → JPEG baseline/lossless/LS
  - openjpeg → JPEG 2000 / HTJ2K
  - pylibjpeg-rle → RLE
- RLE：pydicom ≥2.2 默认 numpy 处理器；`ds.decompress("pylibjpeg")` 可强制插件。

## 快速判读（check 命令的判定逻辑）

1. (0002,0003) 不在已知表 → `unknown_transfer_syntax`（error；本工具识别表为常见子集）。
2. 未压缩：PixelData 字节数 < Rows×Cols×SamplesPerPixel×BitsAllocated/8 → `pixel_too_short`（error）。
3. 未压缩：PixelData 字节数非单帧整数倍 → `pixel_length_odd`（warn，可能是多帧）。
4. 封装：`encapsulated_pixel_data`（info，属正常结构，不是错误）。
5. 1.2.840.10008.1.2.4.50 + BitsAllocated=16 → 提示 8-bit-only 约束冲突（warn）。
