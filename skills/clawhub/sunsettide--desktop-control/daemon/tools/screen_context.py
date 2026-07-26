"""
Screen context snapshot — generates a text summary of visible screen content.

This is an "AI bridge" capability: it gives the LLM a snapshot of what's
on screen, enabling it to make informed decisions about what to click/type/etc.

Design:
  - Uses image_to_data() from pytesseract for per-word bounding boxes.
  - Classifies words into UI element types (button, label, input, etc.)
    based on common patterns and keywords.
  - Returns a structured summary limited to max_chars.
  - All results are purely local; no data leaves the machine.
"""
import re
import time
import os
import threading

from daemon.handlers.vision_click import _check_pytesseract
from daemon.utils.monitors import resolve_region

# --- pytesseract dependency ---
_pytesseract = None
try:
    import pytesseract as _pt
    _pytesseract = _pt
    tess_path = os.environ.get("TESSERACT_PATH", "")
    if tess_path:
        _pytesseract.pytesseract.tesseract_cmd = tess_path
except Exception:
    pass


# ── UI element type classification ────────────────────────────────────────

# Keywords that suggest button/call-to-action elements
_BUTTON_KEYWORDS = {
    "确定", "取消", "保存", "删除", "编辑", "新建", "添加", "提交",
    "确认", "关闭", "退出", "应用", "重试", "取消", "是", "否",
    "OK", "Cancel", "Save", "Delete", "Edit", "New", "Add", "Submit",
    "Confirm", "Close", "Exit", "Apply", "Retry", "Yes", "No",
    "下一步", "上一步", "完成", "返回",
}

# Keywords that suggest label/header elements
_LABEL_KEYWORDS = {
    "用户名", "密码", "邮箱", "手机号", "地址", "姓名", "标题",
    "Username", "Password", "Email", "Phone", "Address", "Name",
    "搜索", "Search", "查找", "Find",
}

# Element types that are "clickable" (high-priority for the AI)
_CLICKABLE_TYPES = {"button", "link", "menu_item", "tab"}


def _classify_element(text):
    """Classify a text element into a UI type.

    Returns one of: "button", "label", "input", "header", "link", "text"
    """
    t = text.strip()
    if not t:
        return "text"

    if "___" in t or "..." in t or "..." in t:
        return "input"

    if re.match(r"^[\u4e00-\u9fff\w]+[:：]$", t):
        return "label"

    if t in _BUTTON_KEYWORDS:
        return "button"

    if t in _LABEL_KEYWORDS:
        return "label"

    if len(t) <= 8:
        return "button"  # short text often = button

    if re.match(r"^http", t, re.IGNORECASE):
        return "link"

    return "text"


def _merge_nearby_words(words, merge_y_threshold=8):
    """Merge words on the same line (close vertical position) into phrases.

    Args:
        words: List of dicts from image_to_data (text, left, top, width, height).
        merge_y_threshold: Max vertical distance to consider "same line".

    Returns:
        List of merged text blocks.
    """
    if not words:
        return []

    # Sort by top, then left
    sorted_words = sorted(words, key=lambda w: (w.get("top", 0), w.get("left", 0)))

    merged = []
    current_line = [sorted_words[0]]

    for word in sorted_words[1:]:
        prev = current_line[-1]
        prev_bottom = prev.get("top", 0) + prev.get("height", 0)
        curr_top = word.get("top", 0)

        # Same line if vertical overlap or close enough
        if abs(curr_top - prev.get("top", 0)) <= merge_y_threshold:
            current_line.append(word)
        else:
            # Merge current line
            merged.append(_merge_line(current_line))
            current_line = [word]

    if current_line:
        merged.append(_merge_line(current_line))

    return merged


def _merge_line(words):
    """Merge words on one line into a single phrase."""
    words.sort(key=lambda w: w.get("left", 0))
    text = " ".join(w.get("text", "").strip() for w in words if w.get("text", "").strip())
    left = min(w.get("left", 0) for w in words)
    top = min(w.get("top", 0) for w in words)
    right = max(w.get("left", 0) + w.get("width", 0) for w in words)
    bottom = max(w.get("top", 0) + w.get("height", 0) for w in words)
    return {
        "text": text,
        "left": left,
        "top": top,
        "width": right - left,
        "height": bottom - top,
    }


# ── Main handler ──────────────────────────────────────────────────────────

def handle_screen_context(params):
    """Generate a text summary of visible screen content.

    Params:
        region:        Optional dict {left, top, width, height}.
        monitor:       Optional int — anchor region to this monitor.
        lang:          Tesseract language string (default: chi_sim+eng).
        include_layout: Include element layout information (default: true).
        max_chars:     Max characters in the returned text (default: 2000).

    Returns:
        {"text": "...", "summary": "...",
         "elements": [{"text": "...", "type": "...", "bbox": {...}}]}
    """
    if _pytesseract is None:
        raise ValueError(
            "Screen context unavailable: pytesseract not installed. "
            "Install: pip install pytesseract"
        )

    monitor = params.get("monitor", 0)
    region = params.get("region")
    if region is not None:
        region = resolve_region(monitor, region)
    lang = params.get("lang", "chi_sim+eng")
    include_layout = params.get("include_layout", True)
    max_chars = int(params.get("max_chars", 2000))

    # Grab screenshot
    from daemon.handlers.screenshot import _grab_pil
    img = _grab_pil(region)

    # OCR with per-word data
    data = _pytesseract.image_to_data(img, lang=lang, output_type=_pytesseract.Output.DICT)

    # Extract words
    raw_words = []
    n = len(data.get("text", []))
    for i in range(n):
        word = (data.get("text", [])[i] or "").strip()
        if not word:
            continue
        left = int(data.get("left", [0])[i])
        top = int(data.get("top", [0])[i])
        width = int(data.get("width", [0])[i])
        height = int(data.get("height", [0])[i])
        if width <= 0 or height <= 0:
            continue
        raw_words.append({
            "text": word,
            "left": left,
            "top": top,
            "width": width,
            "height": height,
        })

    # Merge into lines
    lines = _merge_nearby_words(raw_words)

    # Build elements list
    elements = []
    all_text_parts = []
    for line in lines:
        etype = _classify_element(line["text"])
        bbox = {
            "left": line["left"],
            "top": line["top"],
            "width": line["width"],
            "height": line["height"],
        }
        elements.append({
            "text": line["text"],
            "type": etype,
            "bbox": bbox,
        })
        all_text_parts.append(line["text"])

    # Build raw text (line-separated)
    raw_text = "\n".join(all_text_parts)

    # Truncate if needed
    if len(raw_text) > max_chars:
        raw_text = raw_text[:max_chars] + "\n...(truncated at " + str(max_chars) + " chars)"

    # Build summary
    clickable = [e for e in elements if e.get("type") in _CLICKABLE_TYPES]
    inputs = [e for e in elements if e.get("type") == "input"]
    labels = [e for e in elements if e.get("type") == "label"]

    summary_parts = []
    summary_parts.append(f"屏幕检测到 {len(elements)} 个文字元素")
    if clickable:
        summary_parts.append(f"可点击元素 ({len(clickable)}个): " +
                             ", ".join(e["text"] for e in clickable[:10]))
        if len(clickable) > 10:
            summary_parts[-1] += f" 等 {len(clickable)} 个"
    if inputs:
        summary_parts.append(f"输入框 ({len(inputs)}个)")
    if labels:
        summary_parts.append(f"标签 ({len(labels)}个): " +
                             ", ".join(e["text"] for e in labels[:5]))
    summary = " | ".join(summary_parts)

    result = {
        "text": raw_text,
        "summary": summary,
        "element_count": len(elements),
    }

    if include_layout:
        result["elements"] = elements

    return result
