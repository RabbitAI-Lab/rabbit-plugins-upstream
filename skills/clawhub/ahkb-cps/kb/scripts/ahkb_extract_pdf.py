"""
ahkb_extract_pdf.py — PDF 解析器
支持：文字型/幻灯片型(横向)/扫描版 PDF
提取：每页文字、嵌入图片、幻灯片截图
输出：chunks 嵌套结构，资源归属明确
"""
import os, hashlib, json
from pathlib import Path


def extract_pdf(filepath, workspace):
    """Extract text and images from PDF. Returns structured dict with chunks."""
    import pymupdf

    doc = pymupdf.open(filepath)
    base = Path(filepath).stem
    safe_base = "".join(c if c.isalnum() or c in '-_ ' else '_' for c in base)

    # 目录结构
    img_dir = Path(workspace) / "图片及其他资源" / "images"
    img_dir.mkdir(parents=True, exist_ok=True)

    result = {
        "file": str(filepath),
        "type": "pdf",
        "metadata": {"page_count": len(doc)},
        "chunks": [],
        "full_text": "",
        "resources_flat": [],
        "pdf_type": None,
    }

    img_counter = 0

    for page_num in range(len(doc)):
        page = doc[page_num]
        rect = page.rect
        is_landscape = rect.width > rect.height * 1.1
        text = page.get_text().strip()
        has_text = len(text) > 50

        page_images = []

        # ── 幻灯片型（横向）→ 整页截图 ──
        full_slide_fname = None
        if is_landscape:
            slide_fname = f"slide-{safe_base}-{page_num+1:03d}.png"
            pix = page.get_pixmap(dpi=200)
            pix.save(str(img_dir / slide_fname))
            full_slide_fname = slide_fname
            page_images.append({
                "type": "full_slide_capture",
                "filename": slide_fname,
                "ext": "png",
                "source_ref": f"page {page_num+1} - landscape full-slide capture",
                "context_text": text,
            })

        # ── 子图片提取（所有类型）──
        for img_info in page.get_images(full=True):
            xref = img_info[0]
            try:
                base_image = doc.extract_image(xref)
                img_bytes = base_image["image"]
                ext = base_image["ext"]
                img_counter += 1
                fname = f"{safe_base}-p{page_num+1:03d}-img{img_counter:02d}.{ext}"
                with open(img_dir / fname, "wb") as f:
                    f.write(img_bytes)
                page_images.append({
                    "type": "image",
                    "filename": fname,
                    "ext": ext,
                    "source_ref": f"page {page_num+1} - embedded image",
                    "context_text": text,
                })
            except Exception:
                pass

        # ── 构建该页的 chunk ──
        chunk = {
            "id": f"page-{page_num+1:04d}",
            "heading": f"第{page_num+1}页",
            "source_position": f"page {page_num+1}",
            "type": "page",
            "text": text,
            "resources": page_images,
        }
        result["chunks"].append(chunk)
        result["full_text"] += f"\n\n--- 第{page_num+1}页 ---\n\n{text}"

    # ── 判断 PDF 类型 ──
    text_pages = sum(1 for p in result["chunks"] if len(p["text"]) > 50)
    landscape_chunks = [c for c in result["chunks"]
                        if any(r["type"] == "full_slide_capture" for r in c["resources"])]
    landscape_pages = len(landscape_chunks)
    scanned_pages = len(doc) - text_pages

    if landscape_pages > len(doc) * 0.5:
        result["pdf_type"] = "landscape"
    elif scanned_pages > text_pages:
        result["pdf_type"] = "scanned"
    else:
        result["pdf_type"] = "text"

    # ── 构建扁平资源列表 ──
    flat = []
    for chunk in result["chunks"]:
        for r in chunk["resources"]:
            r_copy = dict(r)
            r_copy["belongs_to_chunk"] = chunk["id"]
            r_copy["chunk_heading"] = chunk["heading"]
            r_copy["chunk_text"] = chunk["text"]
            flat.append(r_copy)
    result["resources_flat"] = flat

    doc.close()
    return result
