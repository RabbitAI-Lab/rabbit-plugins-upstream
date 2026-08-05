"""
ahkb_extract_md.py — MD/HTML/TXT 解析器
提取：文字内容、章节划分、图片引用、音视频引用
输出：chunks 嵌套结构，资源归属明确
"""
import re
from pathlib import Path

# ─── 媒体扩展名 ───

IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.svg', '.webp'}
VIDEO_EXTS = {'.mp4', '.avi', '.mov', '.wmv', '.m4v', '.mpg', '.mpeg', '.flv', '.webm'}
AUDIO_EXTS = {'.mp3', '.wav', '.wma', '.aac', '.ogg', '.flac', '.m4a'}
MEDIA_EXTS = IMAGE_EXTS | VIDEO_EXTS | AUDIO_EXTS


def _get_media_type(ext):
    ext = ext.lower()
    if ext in IMAGE_EXTS:
        return "image"
    elif ext in VIDEO_EXTS:
        return "video"
    elif ext in AUDIO_EXTS:
        return "audio"
    return "other"


def extract_md(filepath, workspace):
    """Extract text from MD/HTML/TXT. Returns structured dict with chunks."""
    base = Path(filepath).stem
    safe_base = "".join(c if c.isalnum() or c in '-_ ' else '_' for c in base)
    ext = Path(filepath).suffix.lower()

    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        raw = f.read()

    if ext == ".html":
        return _extract_html(filepath, raw, safe_base, workspace)
    elif ext == ".md":
        return _extract_from_markdown(filepath, raw, safe_base, workspace)
    else:  # .txt 及其他纯文本
        return _extract_from_text(filepath, raw, safe_base, workspace)


def _extract_from_markdown(filepath, raw, safe_base, workspace):
    """Extract from Markdown with chunks + resources."""
    # 目录结构
    img_dir = Path(workspace) / "图片及其他资源" / "images"
    video_dir = Path(workspace) / "图片及其他资源" / "videos"
    audio_dir = Path(workspace) / "图片及其他资源" / "audios"
    other_dir = Path(workspace) / "图片及其他资源" / "others"
    for d in [img_dir, video_dir, audio_dir, other_dir]:
        d.mkdir(parents=True, exist_ok=True)

    # 提取 frontmatter
    frontmatter = {}
    body = raw
    if raw.startswith("---"):
        parts = raw.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            body = parts[2]
            for line in fm_text.strip().split("\n"):
                if ":" in line:
                    k, v = line.split(":", 1)
                    frontmatter[k.strip()] = v.strip()

    # ── 按标题分割章节 ──
    sections = []
    lines = body.split("\n")
    current_heading = "(前言)"
    current_content = []
    current_level = 0

    for line in lines:
        heading_match = re.match(r'^(#{1,6})\s*(.+)$', line)
        if heading_match:
            if current_content:
                sections.append({
                    "level": current_level,
                    "heading": current_heading,
                    "text": "\n".join(current_content).strip(),
                    "start_pos": body.find("\n".join(current_content)) if current_content else 0,
                })
            current_level = len(heading_match.group(1))
            current_heading = heading_match.group(2).strip()
            current_content = []
        else:
            current_content.append(line)

    if current_content:
        sections.append({
            "level": current_level,
            "heading": current_heading,
            "text": "\n".join(current_content).strip(),
        })

    if not sections:
        sections.append({"level": 0, "heading": "(正文)", "text": body.strip()})

    # ── 提取所有媒体引用及其位置 ──
    # 包括 ![]() 语法、<img>、<video>、<audio>、<source> 标签
    media_refs = []

    # Markdown 图片/视频/音频引用 ![](url)
    for match in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', body):
        url = match.group(1) or match.group(2)
        alt = match.group(1)
        media_refs.append({
            "alt": alt,
            "url": match.group(2),
            "syntax": "markdown",
            "pos": match.start(),
        })

    # HTML <img> 标签
    for match in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', body):
        media_refs.append({
            "alt": "",
            "url": match.group(1),
            "syntax": "html_img",
            "pos": match.start(),
        })

    # HTML <video> 标签（含 <source> 子标签）
    for match in re.finditer(r'<video[^>]*>(.*?)</video>', body, re.DOTALL):
        inner = match.group(1)
        src_match = re.search(r'<source[^>]+src=["\']([^"\']+)["\']', inner)
        src_direct = re.search(r'src=["\']([^"\']+)["\']', match.group(0))
        url = src_match.group(1) if src_match else (src_direct.group(1) if src_direct else "")
        if url:
            media_refs.append({
                "alt": "video",
                "url": url,
                "syntax": "html_video",
                "pos": match.start(),
            })

    # HTML <audio> 标签
    for match in re.finditer(r'<audio[^>]*>(.*?)</audio>', body, re.DOTALL):
        inner = match.group(1)
        src_match = re.search(r'<source[^>]+src=["\']([^"\']+)["\']', inner)
        src_direct = re.search(r'src=["\']([^"\']+)["\']', match.group(0))
        url = src_match.group(1) if src_match else (src_direct.group(1) if src_direct else "")
        if url:
            media_refs.append({
                "alt": "audio",
                "url": url,
                "syntax": "html_audio",
                "pos": match.start(),
            })

    # ── 构建位置 → 章节索引映射 ──
    def _build_pos_map():
        pos_map = {}
        running_pos = 0
        sec_idx = 0
        for line in body.split("\n"):
            if re.match(r'^#{1,6}\s*', line):
                if sec_idx < len(sections) - 1:
                    sec_idx += 1
            pos_map[running_pos] = min(sec_idx, len(sections) - 1)
            running_pos += len(line) + 1
        return pos_map

    pos_to_section = _build_pos_map()

    def _find_section(pos):
        best = 0
        for lp, si in sorted(pos_to_section.items()):
            if lp <= pos:
                best = si
            else:
                break
        return min(best, len(sections) - 1) if sections else 0

    # ── 处理每个媒体引用 —— 保存或记录 ──
    result = {
        "file": str(filepath),
        "type": "markdown",
        "metadata": {"frontmatter": frontmatter},
        "chunks": [],
        "full_text": body,
        "resources_flat": [],
    }

    # 为每个章节收集资源
    resources_by_section = {}
    for sec_idx, sec in enumerate(sections):
        resources_by_section[sec_idx] = []

    for ref in media_refs:
        url = ref["url"]
        sec_i = _find_section(ref.get("pos", 0))
        ctx_text = sections[sec_i].get("text", "") if sections else ""

        if url.startswith("http://") or url.startswith("https://"):
            # 远程资源 — 记录但不下载
            ext = Path(url).suffix.lower()
            mtype = _get_media_type(ext) if ext else "other"
            resources_by_section[sec_i].append({
                "type": mtype,
                "url": url,
                "ext": ext[1:] if ext else "",
                "source_ref": "remote URL",
                "context_text": ctx_text,
                "alt": ref["alt"],
            })
        else:
            # 本地路径
            resource_path = Path(filepath).parent / url
            if resource_path.exists():
                ext = resource_path.suffix.lower()
                mtype = _get_media_type(ext)
                target_dir = {"image": img_dir, "video": video_dir, "audio": audio_dir, "other": other_dir}[mtype]

                # 复制文件到资源目录
                count = len(resources_by_section[sec_i]) + 1
                fname = f"{safe_base}-{mtype}{count:02d}{ext}"
                import shutil
                shutil.copy2(resource_path, target_dir / fname)

                resources_by_section[sec_i].append({
                    "type": mtype,
                    "filename": fname,
                    "ext": ext[1:],
                    "source_ref": f"local file: {url}",
                    "context_text": ctx_text,
                    "alt": ref["alt"],
                })

    # ── 构建 chunks ──
    for sec_idx, sec in enumerate(sections):
        chunk_resources = resources_by_section.get(sec_idx, [])
        clean_resources = []
        for r in chunk_resources:
            entry = {"type": r["type"], "context_text": r["context_text"], "source_ref": r["source_ref"]}
            if "filename" in r:
                entry["filename"] = r["filename"]
                entry["ext"] = r["ext"]
            if "url" in r:
                entry["url"] = r["url"]
            if "alt" in r:
                entry["alt"] = r["alt"]
            clean_resources.append(entry)

        chunk = {
            "id": f"sec-{sec_idx+1:03d}",
            "heading": sec["heading"],
            "source_position": sec["heading"],
            "type": "section",
            "text": sec["text"],
            "resources": clean_resources,
        }
        result["chunks"].append(chunk)

    # ── 扁平资源列表 ──
    flat = []
    for chunk in result["chunks"]:
        for r in chunk["resources"]:
            r_copy = dict(r)
            r_copy["belongs_to_chunk"] = chunk["id"]
            r_copy["chunk_heading"] = chunk["heading"]
            r_copy["chunk_text"] = chunk["text"]
            flat.append(r_copy)
    result["resources_flat"] = flat

    return result


def _extract_html(filepath, raw, safe_base, workspace):
    """Extract from HTML with full media handling (img, video, audio, embed)."""
    from html.parser import HTMLParser

    # 目录结构
    img_dir = Path(workspace) / "图片及其他资源" / "images"
    video_dir = Path(workspace) / "图片及其他资源" / "videos"
    audio_dir = Path(workspace) / "图片及其他资源" / "audios"
    other_dir = Path(workspace) / "图片及其他资源" / "others"
    for d in [img_dir, video_dir, audio_dir, other_dir]:
        d.mkdir(parents=True, exist_ok=True)

    # ── 提取纯文本并按标题分节 ──
    class TextExtractor(HTMLParser):
        def __init__(self):
            super().__init__()
            self.text_parts = []
            self.skip = False
            self._current_tag = None
        def handle_starttag(self, tag, attrs):
            self._current_tag = tag
            if tag in ('script', 'style'):
                self.skip = True
            if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
                self.text_parts.append('\n### ')
        def handle_endtag(self, tag):
            if tag in ('script', 'style'):
                self.skip = False
            if tag in ('p', 'br', 'div', 'li'):
                self.text_parts.append('\n')
            if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
                self.text_parts.append('\n')
        def handle_data(self, data):
            if not self.skip:
                self.text_parts.append(data)

    extractor = TextExtractor()
    extractor.feed(raw)
    text = "".join(extractor.text_parts)

    # ── 按标题拆分为章节 ──
    sections = []
    lines = text.strip().split('\n')
    current_heading = "(正文)"
    current_content = []
    for line in lines:
        if line.startswith("### "):
            if current_content:
                sections.append({
                    "level": 1,
                    "heading": current_heading,
                    "text": "\n".join(current_content).strip(),
                    "start_pos": text.find("\n".join(current_content)) if current_content else 0,
                })
            current_heading = line.replace("### ", "").strip()
            current_content = []
        else:
            current_content.append(line)
    if current_content:
        sections.append({
            "level": 1 if current_heading != "(正文)" else 0,
            "heading": current_heading,
            "text": "\n".join(current_content).strip(),
        })
    if not sections:
        sections.append({"level": 0, "heading": "(正文)", "text": text.strip()})

    # ── 提取所有媒体引用，带周围上下文 ──
    # 策略：找到每个媒体标签，提取附近文本作为上下文
    media_entries = []
    seen_urls = set()

    # 所有需要提取的媒体标签和属性
    media_patterns = [
        # (标签正則, url属性, 类型标签)
        (r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', 'img', 'image'),
        (r'<video[^>]+src=["\']([^"\']+)["\'][^>]*>', 'video', 'video'),
        (r'<audio[^>]+src=["\']([^"\']+)["\'][^>]*>', 'audio', 'audio'),
        (r'<source[^>]+src=["\']([^"\']+)["\'][^>]*>', 'source', 'other'),
        (r'<embed[^>]+src=["\']([^"\']+)["\'][^>]*>', 'embed', 'other'),
        (r'<object[^>]+data=["\']([^"\']+)["\'][^>]*>', 'object', 'other'),
    ]

    # 同时处理 <video>/<audio> 内含 <source> 的情况
    for tag_match in re.finditer(r'<(video|audio)[^>]*>(.*?)</\1>', raw, re.DOTALL):
        tag_type = tag_match.group(1)
        outer = tag_match.group(0)
        inner = tag_match.group(2)

        # 检查外层标签有没有直接 src
        src_direct = re.search(r'src=["\']([^"\']+)["\']', outer)
        if src_direct:
            url = src_direct.group(1)
        else:
            # 检查内层 <source> 标签
            src_source = re.search(r'<source[^>]+src=["\']([^"\']+)["\']', inner)
            url = src_source.group(1) if src_source else ""

        if url and url not in seen_urls:
            seen_urls.add(url)
            media_pos = tag_match.start()
            mtype = "video" if tag_type == "video" else "audio"
            _extract_html_media_context(raw, media_pos, url, mtype, media_entries, sections)

    # 独立的 <img> 标签（不在 video/audio 内的）
    for match in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', raw):
        url = match.group(1)
        if url in seen_urls:
            continue
        seen_urls.add(url)
        _extract_html_media_context(raw, match.start(), url, "image", media_entries, sections)

    # 独立的 <source> / <embed> / <object>（不在 video/audio 内的）
    for pattern, tag, mtype in media_patterns:
        if tag in ('source', 'embed', 'object'):
            for match in re.finditer(pattern, raw):
                url = match.group(1)
                if url in seen_urls:
                    continue
                seen_urls.add(url)
                _extract_html_media_context(raw, match.start(), url, mtype, media_entries, sections)

    # ── 按章节组织资源 ──
    resources_by_section = {}
    for sec_idx, sec in enumerate(sections):
        resources_by_section[sec_idx] = []

    for entry in media_entries:
        sec_i = entry["section_idx"]
        if sec_i not in resources_by_section:
            resources_by_section[sec_i] = []
        resources_by_section[sec_i].append(entry)

    # ── 构建 chunks ──
    result = {
        "file": str(filepath),
        "type": "html",
        "metadata": {},
        "chunks": [],
        "full_text": text.strip(),
        "resources_flat": [],
    }

    for sec_idx, sec in enumerate(sections):
        chunk_resources = []
        for r in resources_by_section.get(sec_idx, []):
            entry = {
                "type": r["type"],
                "context_text": r["context_text"],
                "source_ref": r.get("source_ref", "HTML tag"),
            }
            if r.get("url", "").startswith("http"):
                entry["url"] = r["url"]
            elif r.get("local_path"):
                entry["filename"] = r["local_filename"]
                entry["ext"] = r["ext"]
            elif r.get("url"):
                entry["url"] = r["url"]
            chunk_resources.append(entry)

        chunk = {
            "id": f"sec-{sec_idx+1:03d}",
            "heading": sec["heading"],
            "source_position": sec["heading"],
            "type": "section",
            "text": sec["text"],
            "resources": chunk_resources,
        }
        result["chunks"].append(chunk)

    # ── 扁平资源列表 ──
    flat = []
    for chunk in result["chunks"]:
        for r in chunk["resources"]:
            r_copy = dict(r)
            r_copy["belongs_to_chunk"] = chunk["id"]
            r_copy["chunk_heading"] = chunk["heading"]
            r_copy["chunk_text"] = chunk["text"]
            flat.append(r_copy)
    result["resources_flat"] = flat

    return result


def _extract_html_media_context(raw, media_pos, url, mtype, media_entries, sections):
    """提取 HTML 中媒体标签的上下文文本，并决定保存还是记录。"""
    # 提取周围文本
    before = raw[max(0, media_pos - 300):media_pos]
    after = raw[media_pos:media_pos + 300]

    # 从 before 中提取最后一个段落/标题的文本
    ctx_before = ""
    for tag in ['<p>', '<div>', '<h1>', '<h2>', '<h3>', '<li>', '<br>', '<section>', '<article>']:
        idx = before.rfind(tag)
        if idx >= 0:
            tag_end = before.find('>', idx)
            if tag_end >= 0:
                rest = before[tag_end + 1:]
                rest = re.sub(r'<[^>]+>', '', rest)
                ctx_before = rest.strip()
            break

    # 从 after 中提取文本
    ctx_after = ""
    for tag in ['</p>', '</div>', '</h1>', '</h2>', '</h3>', '</li>', '<p>', '<br>',
                '</section>', '</article>']:
        idx = after.find(tag, 1)
        if idx >= 0:
            content = after[:idx]
            content = re.sub(r'<[^>]+>', '', content)
            ctx_after = content.strip()
            break

    context = (ctx_before + " " + ctx_after).strip()
    if not context:
        # 找最近的标题
        headings = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', raw[:media_pos])
        if headings:
            context = headings[-1]

    # 找到所属章节
    sec_i = 0
    running_text = ""
    for idx, sec in enumerate(sections):
        running_text += sec.get("text", "")
        if len(running_text) >= media_pos * 0.8:  # 大致定位
            sec_i = idx
            break

    # 判断是远程还是本地
    if url.startswith("http://") or url.startswith("https://"):
        # 远程资源
        entry = {
            "type": mtype,
            "url": url,
            "context_text": context,
            "source_ref": "remote URL",
            "section_idx": sec_i,
        }
        media_entries.append(entry)
    else:
        # 本地路径 — 保存
        base = Path(url).stem
        ext = Path(url).suffix.lower()
        entry = {
            "type": mtype,
            "url": url,
            "context_text": context,
            "source_ref": f"local file: {url}",
            "section_idx": sec_i,
            "local_path": url,
            "local_filename": f"html_{base}{ext}",
            "ext": ext[1:] if ext else "",
        }
        media_entries.append(entry)


def _extract_from_text(filepath, raw, safe_base, workspace):
    """Extract from plain text."""
    lines = raw.strip().split("\n")
    sections = []
    current_block = []
    current_heading = "(正文)"

    for line in lines:
        if line.strip() == "":
            if current_block:
                sections.append({
                    "level": 0,
                    "heading": current_heading,
                    "text": "\n".join(current_block),
                })
                current_block = []
                current_heading = "(续)"
            continue
        current_block.append(line)

    if current_block:
        sections.append({
            "level": 0,
            "heading": current_heading,
            "text": "\n".join(current_block),
        })

    if not sections:
        sections.append({"level": 0, "heading": "(正文)", "text": raw.strip()})

    result = {
        "file": str(filepath),
        "type": "text",
        "metadata": {},
        "chunks": [],
        "full_text": raw.strip(),
        "resources_flat": [],
    }

    for sec_idx, sec in enumerate(sections):
        chunk = {
            "id": f"sec-{sec_idx+1:03d}",
            "heading": sec["heading"],
            "source_position": sec["heading"],
            "type": "paragraph",
            "text": sec["text"],
            "resources": [],
        }
        result["chunks"].append(chunk)

    return result
