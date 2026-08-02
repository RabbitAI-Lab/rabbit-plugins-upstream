#!/usr/bin/env python3
"""
kb2slides.py — 知识库数据提取器

为 AI 生成幻灯片提供结构化的知识元数据。只提取，不生成。

用法：
    # 列出所有知识元（按标签分组）
    python scripts/kb2slides.py list-units --workspace <vault路径>

    # 按标签过滤
    python scripts/kb2slides.py list-units --workspace <vault路径> --tag "大系统观"

    # 读取指定知识元的完整内容
    python scripts/kb2slides.py get-content --workspace <vault路径> --units "大系统观,七色光方法,王权"

输出（list-units）：
    {
      "ok": true,
      "total": 30,
      "tag_groups": {
        "概念": [{"name": "...", "summary": "...", "tags": [...]}, ...],
        "方法论": [...],
        ...
      }
    }

输出（get-content）：
    {
      "ok": true,
      "units": [
        {
          "name": "大系统观",
          "title": "大系统观",
          "summary": "...",
          "tags": [...],
          "source": "原始文件/...",
          "body": "正文内容...",
          "related_units": ["..."],
          "resources": [{"type": "image", "file": "...", "ctx": "..."}],
          "source_files": ["..."]
        },
        ...
      ]
    }
"""

import os
import re
import json
import sys
import argparse

# ── 导入 kb 模块的提取脚本（复用文档抽取功能）──
_ahkb_scripts = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                             'kb', 'scripts')
if os.path.isdir(_ahkb_scripts) and _ahkb_scripts not in sys.path:
    sys.path.insert(0, _ahkb_scripts)


def parse_frontmatter(text):
    """解析 Markdown 文件的 YAML frontmatter

    返回 (frontmatter_dict, body_text)。
    使用简单的手动解析，避免依赖 PyYAML。
    """
    text = text.strip()
    if not text.startswith('---'):
        return {}, text

    # 找到第二个 ---
    end_idx = text.find('---', 3)
    if end_idx == -1:
        return {}, text

    fm_text = text[3:end_idx].strip()
    body = text[end_idx + 3:].strip()

    fm = {}
    current_key = None
    current_list = None

    for line in fm_text.split('\n'):
        stripped = line.strip()

        # 跳过空行
        if not stripped:
            continue

        # 列表项（缩进后以 - 开头）
        if stripped.startswith('- ') and current_key:
            item_value = stripped[2:].strip()
            # 处理嵌套对象 { key: value, ... }
            if item_value.startswith('{') and item_value.endswith('}'):
                item = {}
                # 简单解析 {key: value, key: value}
                inner = item_value[1:-1]
                for pair in inner.split(','):
                    pair = pair.strip()
                    if ':' in pair:
                        k, v = pair.split(':', 1)
                        k = k.strip().strip('"').strip("'")
                        v = v.strip().strip('"').strip("'")
                        item[k] = v
                current_list.append(item)
            else:
                current_list.append(item_value.strip('"').strip("'"))
            continue

        # 键值对
        if ':' in stripped:
            key, _, value = stripped.partition(':')
            key = key.strip()
            value = value.strip()

            if value == '':
                # 可能是列表的开始
                current_key = key
                current_list = []
                fm[key] = current_list
            elif value.startswith('[') and value.endswith(']'):
                # 内联数组 [item1, item2, ...]
                inner = value[1:-1]
                items = []
                for item in inner.split(','):
                    item = item.strip().strip('"').strip("'")
                    if item:
                        items.append(item)
                fm[key] = items
                current_key = None
                current_list = None
            else:
                # 普通标量值
                fm[key] = value.strip('"').strip("'")
                current_key = None
                current_list = None

    return fm, body


def extract_wikilinks(text):
    """从文本中提取 [[知识元名称]] 链接"""
    pattern = r'\[\[([^\]]+)\]\]'
    matches = re.findall(pattern, text)
    # 处理含别名的链接 [[目标|显示名]]
    result = []
    for m in matches:
        if '|' in m:
            target = m.split('|')[0].strip()
        else:
            target = m.strip()
        result.append(target)
    return result


def extract_resource_embeds(text):
    """从文本中提取 ![[资源文件名]] 嵌入"""
    pattern = r'!\[\[([^\]]+)\]\]'
    matches = re.findall(pattern, text)
    return [m.strip() for m in matches]


def extract_resource_sections(text):
    """从正文中提取 ## 关联资源 部分的资源引用"""
    # 找到 "## 关联资源" 部分
    pattern = r'##\s*关联资源\s*\n(.*?)(?=\n##|\Z)'
    match = re.search(pattern, text, re.DOTALL)
    if not match:
        return []
    section = match.group(1)
    return extract_resource_embeds(section)


def extract_related_units_sections(text):
    """从正文中提取 ## 关联知识元 部分的知识元引用"""
    pattern = r'##\s*关联知识元\s*\n(.*?)(?=\n##|\Z)'
    match = re.search(pattern, text, re.DOTALL)
    if not match:
        return []
    section = match.group(1)
    return extract_wikilinks(section)


def load_concept_index(workspace):
    """加载 concept_index.json"""
    idx_path = os.path.join(workspace, '临时工作文件', 'concept_index.json')
    if os.path.isfile(idx_path):
        with open(idx_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None


def scan_knowledge_units(workspace):
    """直接扫描 知识元/ 目录获取知识元列表"""
    units_dir = os.path.join(workspace, '知识元')
    if not os.path.isdir(units_dir):
        return []

    units = []
    for fname in sorted(os.listdir(units_dir)):
        if not fname.endswith('.md'):
            continue
        fpath = os.path.join(units_dir, fname)
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            fm, _ = parse_frontmatter(content)
            name = fname[:-3]  # 去掉 .md
            units.append({
                'name': name,
                'summary': fm.get('summary', ''),
                'tags': fm.get('tags', []),
            })
        except Exception:
            continue

    return units


def group_by_tag(units):
    """按最后一个标签（类型标签）分组"""
    groups = {}
    for u in units:
        tags = u.get('tags', [])
        if not tags:
            group_key = '未分类'
        else:
            group_key = tags[-1]  # 最后一个标签
        if group_key not in groups:
            groups[group_key] = []
        groups[group_key].append(u)
    return groups


def cmd_list_units(args):
    """list-units 子命令"""
    workspace = args.workspace
    if not os.path.isdir(workspace):
        print(json.dumps({'ok': False, 'error': f'workspace not found: {workspace}'}, ensure_ascii=False))
        sys.exit(1)

    # 优先从 concept_index.json 读取
    idx = load_concept_index(workspace)
    if idx and 'concepts' in idx:
        units = idx['concepts']
    else:
        units = scan_knowledge_units(workspace)

    # 按标签过滤
    if args.tag:
        tag_filter = args.tag
        units = [u for u in units if tag_filter in u.get('tags', [])]

    groups = group_by_tag(units)

    result = {
        'ok': True,
        'total': len(units),
        'tag_groups': groups,
        'updated': idx.get('updated', '') if idx else '',
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_get_content(args):
    """get-content 子命令"""
    workspace = args.workspace
    if not os.path.isdir(workspace):
        print(json.dumps({'ok': False, 'error': f'workspace not found: {workspace}'}, ensure_ascii=False))
        sys.exit(1)

    unit_names = [n.strip() for n in args.units.split(',') if n.strip()]
    if not unit_names:
        print(json.dumps({'ok': False, 'error': 'no unit names provided'}, ensure_ascii=False))
        sys.exit(1)

    units_dir = os.path.join(workspace, '知识元')
    result_units = []

    for name in unit_names:
        fpath = os.path.join(units_dir, f'{name}.md')
        if not os.path.isfile(fpath):
            result_units.append({
                'name': name,
                'error': 'file not found',
            })
            continue

        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()

            fm, body = parse_frontmatter(content)

            # 提取关联知识元（frontmatter 中的关联 + 正文中的关联）
            related_from_body = extract_related_units_sections(body)
            # 从正文中移除已提取的关联章节，避免重复
            body_clean = re.sub(r'##\s*关联知识元\s*\n.*?(?=\n##|\Z)', '', body, flags=re.DOTALL).strip()
            body_clean = re.sub(r'##\s*关联资源\s*\n.*?(?=\n##|\Z)', '', body_clean, flags=re.DOTALL).strip()
            body_clean = re.sub(r'##\s*关联原始文件\s*\n.*?(?=\n##|\Z)', '', body_clean, flags=re.DOTALL).strip()
            body_clean = re.sub(r'##\s*标签\s*\n.*?(?=\n##|\Z)', '', body_clean, flags=re.DOTALL).strip()

            # 提取资源
            resources = []
            fm_resources = fm.get('resources', [])
            if isinstance(fm_resources, list):
                for r in fm_resources:
                    if isinstance(r, dict):
                        resources.append({
                            'type': r.get('type', ''),
                            'file': '',
                            'ctx': r.get('ctx', ''),
                        })
                    elif isinstance(r, str):
                        resources.append({'type': '', 'file': r, 'ctx': ''})
            resource_embeds = extract_resource_sections(content)

            # 提取 source_files
            source_files = []
            related_files = fm.get('related_files', [])
            if isinstance(related_files, list):
                for rf in related_files:
                    if isinstance(rf, dict):
                        source_files.append(rf.get('file', ''))
                    elif isinstance(rf, str):
                        # 清理 "file: \"...\"" 格式 → 纯净路径
                        cleaned = rf.strip()
                        if cleaned.startswith('file:'):
                            cleaned = cleaned[5:].strip()
                        source_files.append(cleaned.strip('"').strip("'"))

            # 自动匹配图片（即使 frontmatter resources 为空，也通过内容检索图片）
            matched_images = match_images_for_unit(name, fm.get('summary', ''), body_clean, workspace, top_n=5)

            unit = {
                'name': name,
                'title': fm.get('title', name),
                'summary': fm.get('summary', ''),
                'tags': fm.get('tags', []) if isinstance(fm.get('tags'), list) else [],
                'source': fm.get('source', ''),
                'unit_id': fm.get('unit_id', ''),
                'body': body_clean,
                'related_units': related_from_body,
                'resources': resources,
                'resource_embeds': resource_embeds,
                'source_files': source_files,
                'matched_images': matched_images,
            }
            result_units.append(unit)

        except Exception as e:
            result_units.append({
                'name': name,
                'error': str(e),
            })

    result = {
        'ok': True,
        'units': result_units,
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))


def tokenize(text):
    """简单中文/英文分词：提取所有中文词（2-4字）和英文单词"""
    tokens = []
    # 英文单词
    eng_words = re.findall(r'[a-zA-Z]{2,}', text.lower())
    tokens.extend(eng_words)
    # 中文2-4字词组（滑动窗口）
    chinese_chars = re.findall(r'[一-鿿]', text)
    for n in [4, 3, 2]:
        for i in range(len(chinese_chars) - n + 1):
            tokens.append(''.join(chinese_chars[i:i+n]))
    return tokens


def search_units(query, workspace, top_n=15):
    """全文检索知识元：名称(×5) + summary(×3) + 正文(×1)"""
    query_tokens = tokenize(query)
    if not query_tokens:
        return []

    units = scan_knowledge_units(workspace)
    if not units:
        idx = load_concept_index(workspace)
        if idx and 'concepts' in idx:
            units = idx['concepts']

    scored = []
    units_dir = os.path.join(workspace, '知识元')

    for u in units:
        name = u.get('name', '')
        summary = u.get('summary', '')

        # 读取正文
        body = ''
        fpath = os.path.join(units_dir, f'{name}.md')
        if os.path.isfile(fpath):
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    content = f.read()
                _, body = parse_frontmatter(content)
            except Exception:
                pass

        # 评分
        score = 0.0
        name_lower = name.lower()
        summary_lower = summary.lower()
        body_lower = body.lower()

        for token in query_tokens:
            token_lower = token.lower()
            # 名称匹配（×5）
            if token_lower in name_lower:
                score += 5
            # summary 匹配（×3）
            if token_lower in summary_lower:
                score += 3
            # 正文匹配（×1）
            count = body_lower.count(token_lower)
            score += min(count, 10) * 1

        if score > 0:
            # 生成摘要片段
            snippet = ''
            for qt in query_tokens[:3]:
                qt_lower = qt.lower()
                idx_pos = body_lower.find(qt_lower)
                if idx_pos >= 0:
                    start = max(0, idx_pos - 30)
                    end = min(len(body), idx_pos + 80)
                    snippet = body[start:end].replace('\n', ' ').strip()
                    if start > 0:
                        snippet = '…' + snippet
                    if end < len(body):
                        snippet = snippet + '…'
                    break
            if not snippet and summary:
                snippet = summary
            elif not snippet:
                snippet = body[:150].replace('\n', ' ').strip()

            scored.append({
                'name': name,
                'summary': summary,
                'tags': u.get('tags', []),
                'score': round(score, 1),
                'snippet': snippet,
            })

    scored.sort(key=lambda x: x['score'], reverse=True)
    return scored[:top_n]


def search_chunks(query, workspace, top_n=10):
    """检索 chunks 原文：heading(×3) + text(×1)"""
    query_tokens = tokenize(query)
    if not query_tokens:
        return []

    chunks_dir = os.path.join(workspace, 'chunks')
    if not os.path.isdir(chunks_dir):
        return []

    # 读取所有 chunks 文件
    all_chunks = []
    for fname in os.listdir(chunks_dir):
        if fname == 'index.json' or not fname.endswith('.json'):
            continue
        fpath = os.path.join(chunks_dir, fname)
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            all_chunks.extend(data.get('chunks', []))
        except Exception:
            continue

    scored = []
    for c in all_chunks:
        heading = c.get('heading', '')
        text = c.get('text', '')[:2000]  # 只取前2000字
        heading_lower = heading.lower()
        text_lower = text.lower()

        score = 0.0
        for token in query_tokens:
            token_lower = token.lower()
            if token_lower in heading_lower:
                score += 3
            count = text_lower.count(token_lower)
            score += min(count, 10) * 1

        if score > 0:
            snippet = text[:200].replace('\n', ' ').strip()
            scored.append({
                'chunk_id': c.get('chunk_id', ''),
                'source_file': c.get('source_file', ''),
                'heading': heading,
                'position': c.get('position', heading),
                'word_count': c.get('word_count', 0),
                'score': round(score, 1),
                'snippet': snippet,
            })

    scored.sort(key=lambda x: x['score'], reverse=True)
    return scored[:top_n]


def search_images(query, workspace, top_n=15):
    """检索 .ctx 文件匹配图片：tags(×3) + heading(×3) + description(×1)"""
    query_tokens = tokenize(query)
    if not query_tokens:
        return []

    images_dir = os.path.join(workspace, '图片及其他资源', 'images')
    if not os.path.isdir(images_dir):
        return []

    scored = []
    for fname in os.listdir(images_dir):
        if not fname.endswith('.ctx'):
            continue
        ctx_path = os.path.join(images_dir, fname)
        try:
            with open(ctx_path, 'r', encoding='utf-8') as f:
                ctx_content = f.read()
        except Exception:
            continue

        fm, body = parse_frontmatter(ctx_content)
        resource_file = fm.get('resource_file', '')
        if not resource_file:
            # .ctx文件名去掉.ctx后缀通常就是资源文件名
            resource_file = fname[:-4]

        # 确认图片文件存在
        img_path = os.path.join(images_dir, resource_file)
        if not os.path.isfile(img_path):
            continue

        tags = fm.get('tags', [])
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.strip('[]').split(',')]
        chunk_heading = fm.get('chunk_heading', '')
        description = body.strip() if body else ''

        # 评分
        score = 0.0
        tags_text = ' '.join(tags).lower() if isinstance(tags, list) else str(tags).lower()
        heading_lower = chunk_heading.lower()
        desc_lower = description.lower()

        for token in query_tokens:
            token_lower = token.lower()
            # 标签匹配（×3）
            if token_lower in tags_text:
                score += 3
            # heading 匹配（×3）
            if token_lower in heading_lower:
                score += 3
            # 描述匹配（×1）
            count = desc_lower.count(token_lower)
            score += min(count, 5) * 1

        if score > 0:
            scored.append({
                'resource_file': resource_file,
                'img_path': img_path,
                'chunk_heading': chunk_heading,
                'tags': tags if isinstance(tags, list) else [],
                'description': description[:200].replace('\n', ' ').strip(),
                'importance': fm.get('importance', 3),
                'score': round(score, 1),
            })

    scored.sort(key=lambda x: x['score'], reverse=True)
    return scored[:top_n]


def match_images_for_unit(unit_name, unit_summary, unit_body, workspace, top_n=5):
    """为特定知识元匹配相关图片（使用知识元名称+summary+正文检索.ctx）"""
    query = unit_name + ' ' + unit_summary + ' ' + unit_body[:500]
    return search_images(query, workspace, top_n=top_n)


def cmd_search(args):
    """search 子命令 — 全文检索知识元 + chunks + 图片"""
    workspace = args.workspace
    if not os.path.isdir(workspace):
        print(json.dumps({'ok': False, 'error': f'workspace not found: {workspace}'}, ensure_ascii=False))
        sys.exit(1)

    query = args.query
    if not query or len(query.strip()) < 2:
        print(json.dumps({'ok': False, 'error': 'query too short (min 2 chars)'}, ensure_ascii=False))
        sys.exit(1)

    top_n = args.top or 15

    units = search_units(query, workspace, top_n=top_n)
    chunks = search_chunks(query, workspace, top_n=top_n)
    images = search_images(query, workspace, top_n=top_n)

    result = {
        'ok': True,
        'query': query,
        'units': units,
        'chunks': chunks,
        'images': images,
        'total_units': len(units),
        'total_chunks': len(chunks),
        'total_images': len(images),
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_list_docs(args):
    """list-docs 子命令 — 列出知识库中已入库的文档

    仅扫描 chunks/index.json 和 _processed_docs.json 中记录的已入库文档。
    不再扫描原始文件目录下的未处理文档（新文档需先通过知识库构建模块入库）。
    """
    workspace = args.workspace
    if not os.path.isdir(workspace):
        print(json.dumps({'ok': False, 'error': f'workspace not found: {workspace}'}, ensure_ascii=False))
        sys.exit(1)

    docs = []
    seen_paths = set()

    # ── 1. 从 chunks/index.json 读取已有 chunk 的文档 ──
    chunks_dir = os.path.join(workspace, 'chunks')
    idx_path = os.path.join(chunks_dir, 'index.json')
    if os.path.isfile(idx_path):
        try:
            with open(idx_path, 'r', encoding='utf-8') as f:
                idx = json.load(f)
            for source_file in idx.get('files', []):
                if not source_file:
                    continue
                seen_paths.add(source_file)
                # file_chunk_map 的 key 可能使用反斜杠（Windows），而 files 数组使用正斜杠
                # 先尝试直接匹配，失败则尝试反斜杠变体
                fcm = idx.get('file_chunk_map', {})
                chunk_ids = fcm.get(source_file)
                if chunk_ids is None:
                    chunk_ids = fcm.get(source_file.replace('/', '\\'), [])
                chunk_count = len(chunk_ids)
                file_path = os.path.join(workspace, source_file)
                file_size = os.path.getsize(file_path) if os.path.isfile(file_path) else 0
                ext = os.path.splitext(source_file)[1].lower().lstrip('.')
                docs.append({
                    'name': os.path.basename(source_file),
                    'path': source_file,
                    'format': ext,
                    'size': file_size,
                    'chunk_count': chunk_count,
                    'status': 'ready',
                })
        except Exception:
            pass

    # ── 2. 从 _processed_docs.json 读取可能没有 chunk 的文档 ──
    manifest_path = os.path.join(workspace, '原始文件', '_processed_docs.json')
    if os.path.isfile(manifest_path):
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                manifest = json.load(f)
            for p in manifest.get('processed', []):
                sp = p.get('source_path', '')
                sp = sp.replace('\\', '/')
                if not sp or sp in seen_paths:
                    continue
                file_path = os.path.join(workspace, sp.replace('/', os.sep))
                file_size = os.path.getsize(file_path) if os.path.isfile(file_path) else 0
                ext = os.path.splitext(sp)[1].lower().lstrip('.')
                docs.append({
                    'name': os.path.basename(sp),
                    'path': sp,
                    'format': ext,
                    'size': file_size,
                    'chunk_count': 0,
                    'status': 'raw',
                    'processed_date': p.get('processed_date', ''),
                })
                seen_paths.add(sp)
        except Exception:
            pass

    # ── 3. 不再扫描 原始文件/ 下未处理的文档 ──
    # 菜单 2/3 仅支持 _processed_docs.json 中已入库的文档
    # 新文档需先通过知识库构建模块入库

    result = {
        'ok': True,
        'total': len(docs),
        'docs': docs,
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_read_doc(args):
    """read-doc 子命令 — 读取指定文档的内容（优先从已有 chunks 读取，否则现场提取）

    支持的文档格式：pptx/ppt, docx/doc, xlsx/xls, pdf, md, html/htm, txt, csv

    输出：{ ok, doc: { name, path, format, full_text, total_word_count,
            chunk_count, chunks: [{chunk_id, heading, position, word_count, text}],
            images: [{resource_file, chunk_heading, description, score}],
            source } }
    """
    workspace = args.workspace
    if not os.path.isdir(workspace):
        print(json.dumps({'ok': False, 'error': f'workspace not found: {workspace}'}, ensure_ascii=False))
        sys.exit(1)

    doc_ref = args.doc  # 文档名称、相对路径或绝对路径
    force_extract = getattr(args, 'force_extract', False)

    # ── 0. 解析文档路径 ──
    doc_path = None
    # 先尝试作为相对路径解析
    candidate = os.path.join(workspace, doc_ref.replace('/', os.sep))
    if os.path.isfile(candidate):
        doc_path = os.path.relpath(candidate, workspace).replace('\\', '/')
    else:
        # 尝试在 原始文件/ 下搜索
        source_dir = os.path.join(workspace, '原始文件')
        if os.path.isdir(source_dir):
            for root, dirs, files in os.walk(source_dir):
                for fname in files:
                    if fname == doc_ref:
                        fpath = os.path.join(root, fname)
                        doc_path = os.path.relpath(fpath, workspace).replace('\\', '/')
                        break
                if doc_path:
                    break
        # 尝试绝对路径
        if not doc_path and os.path.isfile(doc_ref):
            doc_path = doc_ref
        # 在 chunks/index.json 中按名称搜索
        if not doc_path:
            idx_path = os.path.join(workspace, 'chunks', 'index.json')
            if os.path.isfile(idx_path):
                try:
                    with open(idx_path, 'r', encoding='utf-8') as f:
                        idx = json.load(f)
                    for sf in idx.get('files', []):
                        if os.path.basename(sf) == doc_ref:
                            doc_path = sf
                            break
                except Exception:
                    pass

    if not doc_path:
        print(json.dumps({'ok': False, 'error': f'Document not found: {doc_ref}. '
                          'Provide a name, relative path, or absolute path.'}, ensure_ascii=False))
        sys.exit(1)

    # ── 1. 尝试从 chunks 读取（除非强制提取）──
    if not force_extract:
        try:
            from ahkb_chunks import load_chunks_for_file
            chunk_data = load_chunks_for_file(doc_path, workspace)
            if chunk_data and chunk_data.get('chunks'):
                chunks_out = []
                for c in chunk_data.get('chunks', []):
                    chunks_out.append({
                        'chunk_id': c.get('chunk_id', ''),
                        'heading': c.get('heading', ''),
                        'position': c.get('position', ''),
                        'word_count': c.get('word_count', 0),
                        'text': c.get('text', ''),
                    })

                # 匹配图片
                images_out = _match_images_for_doc(doc_path, workspace)

                result = {
                    'ok': True,
                    'doc': {
                        'name': os.path.basename(doc_path),
                        'path': doc_path,
                        'format': chunk_data.get('format', 'unknown'),
                        'full_text': chunk_data.get('full_text', ''),
                        'total_word_count': chunk_data.get('total_word_count', 0),
                        'chunk_count': len(chunks_out),
                        'chunks': chunks_out,
                        'images': images_out,
                        'source': 'chunks',
                    }
                }
                print(json.dumps(result, ensure_ascii=False, indent=2))
                return
        except ImportError:
            pass
        except Exception:
            pass

    # ── 2. 现场提取文档 ──
    abs_path = os.path.join(workspace, doc_path.replace('/', os.sep))
    if not os.path.isfile(abs_path):
        abs_path = doc_path
    if not os.path.isfile(abs_path):
        print(json.dumps({'ok': False, 'error': f'File not found on disk: {doc_path}'}, ensure_ascii=False))
        sys.exit(1)

    ext = os.path.splitext(abs_path)[1].lower()

    # 为资源目录做准备
    for d in ['images', 'videos', 'audios', 'others']:
        os.makedirs(os.path.join(workspace, '图片及其他资源', d), exist_ok=True)

    extracted = None
    try:
        if ext in ('.pptx', '.ppt'):
            from ahkb_extract_pptx import extract_pptx
            extracted = extract_pptx(str(abs_path), workspace)
        elif ext in ('.docx', '.doc'):
            from ahkb_extract_docx import extract_docx
            extracted = extract_docx(str(abs_path), workspace)
        elif ext in ('.pdf',):
            from ahkb_extract_pdf import extract_pdf
            extracted = extract_pdf(str(abs_path), workspace)
        elif ext in ('.xlsx', '.xls'):
            from ahkb_extract_xlsx import extract_xlsx
            extracted = extract_xlsx(str(abs_path), workspace)
        elif ext in ('.md', '.html', '.htm', '.txt', '.csv'):
            from ahkb_extract_md import extract_md
            extracted = extract_md(str(abs_path), workspace)
        else:
            print(json.dumps({'ok': False, 'error': f'Unsupported format: {ext}'}, ensure_ascii=False))
            sys.exit(1)
    except ImportError as e:
        print(json.dumps({'ok': False, 'error': f'Import error: {e}. '
                          'Ensure AHKB-CPS skill is installed and Python dependencies are met.'}, ensure_ascii=False))
        sys.exit(1)
    except Exception as e:
        print(json.dumps({'ok': False, 'error': f'Extraction failed: {e}'}, ensure_ascii=False))
        sys.exit(1)

    if not extracted:
        print(json.dumps({'ok': False, 'error': 'Extraction returned no data'}, ensure_ascii=False))
        sys.exit(1)

    # ── 3. 格式化输出 ──
    chunks_out = []
    for i, c in enumerate(extracted.get('chunks', [])):
        chunks_out.append({
            'chunk_id': c.get('id', f'chunk-{i+1:03d}'),
            'heading': c.get('heading', ''),
            'position': c.get('source_position', c.get('heading', '')),
            'word_count': len(c.get('text', '').replace('\n', '').replace(' ', '')),
            'text': c.get('text', ''),
        })

    # 提取图片信息
    images_out = []
    images_dir = os.path.join(workspace, '图片及其他资源', 'images')
    for r in extracted.get('resources_flat', []):
        if r.get('type') in ('image', 'full_slide_capture'):
            res_file = r.get('filename', '')
            file_size = 0
            img_path = os.path.join(images_dir, res_file)
            if os.path.isfile(img_path):
                file_size = os.path.getsize(img_path)
            images_out.append({
                'resource_file': res_file,
                'chunk_heading': r.get('chunk_heading', ''),
                'description': r.get('context_text', '')[:200],
                'file_size': file_size,
            })
    if not images_out:
        images_out = _match_images_for_doc(doc_path, workspace)

    result = {
        'ok': True,
        'doc': {
            'name': os.path.basename(doc_path),
            'path': doc_path,
            'format': ext.lstrip('.'),
            'full_text': extracted.get('full_text', ''),
            'total_word_count': sum(c['word_count'] for c in chunks_out),
            'chunk_count': len(chunks_out),
            'chunks': chunks_out,
            'images': images_out,
            'source': 'extracted',
        }
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))


def _match_images_for_doc(doc_path, workspace):
    """为指定文档匹配关联图片（扫描 .ctx 文件中 source 匹配的图片）"""
    images_dir = os.path.join(workspace, '图片及其他资源', 'images')
    if not os.path.isdir(images_dir):
        return []

    doc_name = os.path.basename(doc_path)
    matched = []
    for fname in os.listdir(images_dir):
        if not fname.endswith('.ctx'):
            continue
        ctx_path = os.path.join(images_dir, fname)
        try:
            with open(ctx_path, 'r', encoding='utf-8') as f:
                ctx_content = f.read()
            fm, body = parse_frontmatter(ctx_content)
            source = fm.get('source', '')
            if doc_name in source or doc_path in source or source.endswith(doc_name):
                res_file = fm.get('resource_file', fname[:-4])
                # 获取实际图片文件大小
                file_size = 0
                img_path = os.path.join(images_dir, res_file)
                if os.path.isfile(img_path):
                    file_size = os.path.getsize(img_path)
                matched.append({
                    'resource_file': res_file,
                    'chunk_heading': fm.get('chunk_heading', ''),
                    'description': body.strip()[:200] if body else '',
                    'score': fm.get('importance', 3),
                    'file_size': file_size,
                })
        except Exception:
            continue

    matched.sort(key=lambda x: x.get('score', 0), reverse=True)
    return matched[:50]


def main():
    parser = argparse.ArgumentParser(
        description='kb2slides — 知识库数据提取器（为 AHKB-CPS 幻灯片生成模块提供结构化数据）'
    )
    parser.add_argument('command',
                        choices=['list-units', 'get-content', 'search', 'list-docs', 'read-doc'],
                        help='list-units: 列出知识元 | get-content: 读取知识元内容 | search: 全文检索 '
                             '| list-docs: 列出可用文档 | read-doc: 读取文档内容')
    parser.add_argument('--workspace', required=True, help='知识库工作空间路径（Vault 根目录）')
    parser.add_argument('--tag', default=None, help='按标签过滤（仅 list-units）')
    parser.add_argument('--units', default=None, help='知识元名称列表，逗号分隔（仅 get-content）')
    parser.add_argument('--query', default=None, help='搜索关键词（仅 search）')
    parser.add_argument('--top', type=int, default=15, help='返回条数（仅 search，默认15）')
    parser.add_argument('--doc', default=None, help='文档名称或路径（仅 read-doc）')
    parser.add_argument('--force-extract', action='store_true',
                        help='强制重新提取，不使用已有 chunks（仅 read-doc）')

    args = parser.parse_args()

    if args.command == 'list-units':
        cmd_list_units(args)
    elif args.command == 'get-content':
        cmd_get_content(args)
    elif args.command == 'search':
        cmd_search(args)
    elif args.command == 'list-docs':
        cmd_list_docs(args)
    elif args.command == 'read-doc':
        cmd_read_doc(args)


if __name__ == '__main__':
    main()
