#!/usr/bin/env python3
"""
证据OCR识别脚本
对图片或PDF格式的证据材料进行文字识别，输出结构化文本。

依赖：
  pip install pytesseract Pillow pdf2image
  系统需安装 tesseract-ocr（支持中文：tesseract-ocr-chi-sim）

用法：
  python3 ocr_evidence.py <文件路径> [--output <输出路径>] [--lang <语言>]

示例：
  python3 ocr_evidence.py /path/to/evidence.jpg
  python3 ocr_evidence.py /path/to/contract.pdf --output /path/to/output.txt
  python3 ocr_evidence.py /path/to/evidence.png --lang chi_sim+eng
"""

import sys
import os
import argparse
from pathlib import Path


def check_dependencies():
    """检查依赖是否安装"""
    missing = []
    try:
        import pytesseract
    except ImportError:
        missing.append("pytesseract")
    try:
        from PIL import Image
    except ImportError:
        missing.append("Pillow")
    try:
        from pdf2image import convert_from_path
    except ImportError:
        missing.append("pdf2image")

    if missing:
        print("缺少依赖包，请安装：")
        print(f"  pip install {' '.join(missing)}")
        print("系统还需安装 tesseract-ocr：")
        print("  Ubuntu/Debian: sudo apt install tesseract-ocr tesseract-ocr-chi-sim")
        print("  macOS: brew install tesseract tesseract-lang")
        print("  Windows: 从 https://github.com/UB-Mannheim/tesseract/wiki 下载安装")
        return False
    return True


def ocr_image(image_path, lang="chi_sim+eng"):
    """对图片进行OCR识别"""
    try:
        from PIL import Image
        import pytesseract
    except ImportError:
        print("错误：缺少依赖包，请先安装。")
        return None

    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang=lang)
        return text
    except Exception as e:
        print(f"OCR识别失败：{e}")
        return None


def ocr_pdf(pdf_path, lang="chi_sim+eng"):
    """对PDF进行OCR识别（逐页）"""
    try:
        from pdf2image import convert_from_path
        import pytesseract
    except ImportError:
        print("错误：缺少依赖包，请先安装。")
        return None

    try:
        pages = convert_from_path(pdf_path, dpi=300)
        all_text = []
        for i, page in enumerate(pages, 1):
            text = pytesseract.image_to_string(page, lang=lang)
            all_text.append(f"=== 第{i}页 ===\n{text}\n")
        return "\n".join(all_text)
    except Exception as e:
        print(f"PDF OCR识别失败：{e}")
        return None


def extract_key_info(text):
    """从识别文本中提取关键信息"""
    import re

    info = {
        "日期": [],
        "金额": [],
        "身份证号": [],
        "电话号码": [],
        "合同编号": [],
        "银行账号": [],
    }

    # 日期
    dates = re.findall(
        r'\d{4}年\d{1,2}月\d{1,2}日|\d{4}[-/]\d{1,2}[-/]\d{1,2}', text
    )
    info["日期"] = list(set(dates))

    # 金额
    amounts = re.findall(
        r'(?:人民币)?[￥¥]?\s*[\d,]+\.?\d*\s*(?:元|万元|万)', text
    )
    info["金额"] = list(set(amounts))

    # 身份证号
    id_numbers = re.findall(r'\d{17}[\dXx]|\d{15}', text)
    info["身份证号"] = list(set(id_numbers))

    # 电话号码
    phones = re.findall(r'1[3-9]\d{9}|0\d{2,3}-\d{7,8}', text)
    info["电话号码"] = list(set(phones))

    # 合同编号
    contracts = re.findall(r'(?:合同|协议)\s*编号[：:\s]*([A-Za-z0-9\-]+)', text)
    info["合同编号"] = list(set(contracts))

    # 银行账号
    bank_accounts = re.findall(r'\d{16,19}', text)
    info["银行账号"] = list(set(bank_accounts))

    return info


def main():
    parser = argparse.ArgumentParser(description='证据OCR识别工具')
    parser.add_argument('file', help='待识别的图片或PDF文件路径')
    parser.add_argument('--output', '-o', help='输出文件路径（可选，默认打印到控制台）')
    parser.add_argument(
        '--lang', '-l', default='chi_sim+eng',
        help='OCR语言（默认：chi_sim+eng，中文简体+英文）'
    )
    parser.add_argument(
        '--extract', '-e', action='store_true',
        help='提取关键信息（日期、金额、身份证号等）'
    )

    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"错误：文件不存在 - {file_path}")
        sys.exit(1)

    if not check_dependencies():
        sys.exit(1)

    suffix = file_path.suffix.lower()
    print(f"正在识别：{file_path}")
    print(f"语言：{args.lang}")
    print("-" * 60)

    if suffix in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif', '.gif']:
        text = ocr_image(str(file_path), lang=args.lang)
    elif suffix == '.pdf':
        text = ocr_pdf(str(file_path), lang=args.lang)
    else:
        print(f"错误：不支持的文件格式 - {suffix}")
        print("支持的格式：jpg, jpeg, png, bmp, tiff, gif, pdf")
        sys.exit(1)

    if text is None:
        print("OCR识别失败。")
        sys.exit(1)

    # 清理文本
    text = text.strip()

    # 提取关键信息
    key_info = ""
    if args.extract:
        info = extract_key_info(text)
        key_info = "\n\n" + "=" * 60 + "\n关键信息提取\n" + "=" * 60 + "\n"
        for k, v in info.items():
            if v:
                key_info += f"\n【{k}】"
                for item in v:
                    key_info += f"\n  - {item}"

    # 输出结果
    result = text + key_info

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"\n识别结果已保存至：{args.output}")
    else:
        print("\n识别结果：")
        print("-" * 60)
        print(result)
        print("-" * 60)

    # 输出置信度提示
    print("\n⚠️ OCR识别结果仅供参考，请与原始证据材料核对。")
    print("如有关键信息（金额、日期、签名等），请务必人工核实。")


if __name__ == '__main__':
    main()
