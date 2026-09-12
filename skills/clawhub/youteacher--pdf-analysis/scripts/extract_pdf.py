import argparse
import json
import os
import sys

try:
    import pymupdf
except ImportError:
    try:
        import fitz as pymupdf
    except ImportError:
        sys.exit("缺少 PyMuPDF。请在独立虚拟环境中安装：python3 -m pip install PyMuPDF")


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract page-aware text from a non-scanned PDF.")
    parser.add_argument("pdf_path")
    parser.add_argument("--output")
    parser.add_argument("--max-pages", type=int, default=50)
    parser.add_argument("--max-characters", type=int, default=120000)
    parser.add_argument("--max-bytes", type=int, default=10 * 1024 * 1024)
    args = parser.parse_args()

    if not os.path.isfile(args.pdf_path):
        sys.exit("PDF 文件不存在或无法读取。")
    if os.path.getsize(args.pdf_path) > args.max_bytes:
        sys.exit("PDF 文件超过 10 MB，请先压缩或拆分文档。")

    with open(args.pdf_path, "rb") as stream:
        if stream.read(5) != b"%PDF-":
            sys.exit("文件内容不是有效的 PDF。")

    try:
        document = pymupdf.open(args.pdf_path)
    except Exception as exc:
        sys.exit(f"PDF 无法打开：{exc}")

    try:
        if document.needs_pass:
            sys.exit("PDF 已加密，请解除密码后重试。")
        if document.page_count < 1 or document.page_count > args.max_pages:
            sys.exit(f"PDF 页数必须在 1 至 {args.max_pages} 页之间。")
        pages = []
        total = 0
        for index in range(document.page_count):
            text = (document[index].get_text("text") or "").strip()
            total += len(text)
            if total > args.max_characters:
                sys.exit(f"PDF 文字超过 {args.max_characters} 字符，请先拆分文档。")
            pages.append({"page": index + 1, "text": text})
        if total < 20:
            sys.exit("PDF 没有可读取的文字层；当前版本不支持 OCR。")
        payload = {
            "name": os.path.basename(args.pdf_path)[:180],
            "page_count": document.page_count,
            "total_characters": total,
            "pages": pages,
        }
    finally:
        document.close()

    content = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as stream:
            stream.write(content)
    else:
        print(content)


if __name__ == "__main__":
    main()
