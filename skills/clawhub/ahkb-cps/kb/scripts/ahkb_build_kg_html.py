#!/usr/bin/env python3
"""
AHKB 知识地图 HTML 生成器
从 知识元/ 目录读取所有知识元，构建 D3.js 力导向图数据，
注入到 知识地图模板.html 中，生成交互式知识地图 HTML。

用法:
  python ahkb_build_kg_html.py [--workspace <vault-path>]

输出:
  <Vault>/<知识库名称>-知识地图.html
"""

import argparse
import json
import re
import sys
import io
from pathlib import Path

# Windows 控制台 UTF-8 输出支持
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


def find_workspace(args):
    """确定工作空间（Vault）路径。"""
    if args.workspace:
        ws = Path(args.workspace)
        if ws.exists():
            ws = ws.resolve()
        else:
            print(json.dumps({"error": f"工作空间不存在: {args.workspace}"}))
            sys.exit(1)
    else:
        # 尝试从当前目录向上查找
        cwd = Path.cwd().resolve()
        for parent in [cwd] + list(cwd.parents):
            if (parent / "知识元").exists():
                ws = parent
                break
        else:
            print(json.dumps({"error": "未找到知识库目录（知识元/），请使用 --workspace 指定路径"}))
            sys.exit(1)

    # 🔴 禁止将 skill 目录作为工作空间
    skill_dir = Path(__file__).resolve().parent.parent  # kb/
    _banned = {skill_dir}
    _p = skill_dir.parent
    while _p.name in ("skills", ".claude") or _p.name.startswith("."):
        _banned.add(_p)
        _p = _p.parent
    for _bp in _banned:
        if ws == _bp or _bp in ws.parents:
            print(json.dumps({"error": f"不允许将 skill 目录作为工作空间: {ws}"}))
            sys.exit(1)

    return ws


def parse_frontmatter(content):
    """解析 Markdown frontmatter，返回字典。"""
    if not content.startswith("---"):
        return None
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    fm_text = parts[1].strip()
    fm = {}
    # 简易 YAML 解析（只处理本系统的字段格式）
    current_key = None
    current_list = None
    for line in fm_text.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue
        # 列表项
        if stripped.startswith("- "):
            item = stripped[2:].strip().strip('"').strip("'")
            if current_key and isinstance(current_list, list):
                current_list.append(item)
            continue
        # 键值对
        if ":" in stripped:
            # 处理缩进键
            indent = len(line) - len(line.lstrip())
            if indent > 0 and current_key and isinstance(current_list, list):
                # 可能是 resources 下的子字段，忽略细节
                continue
            k, v = stripped.split(":", 1)
            k = k.strip()
            v = v.strip()
            # 去除引号
            if v.startswith("[") and v.endswith("]"):
                # 行内数组: [a, b, c]
                items = [x.strip().strip('"').strip("'") for x in v[1:-1].split(",") if x.strip()]
                fm[k] = items
                current_key = k
                current_list = items if isinstance(items, list) else None
            elif v.startswith('"') and v.endswith('"'):
                fm[k] = v[1:-1]
                current_key = k
                current_list = None
            elif v.startswith("'") and v.endswith("'"):
                fm[k] = v[1:-1]
                current_key = k
                current_list = None
            elif v.lower() == "true":
                fm[k] = True
                current_key = k
                current_list = None
            elif v.lower() == "false":
                fm[k] = False
                current_key = k
                current_list = None
            else:
                fm[k] = v
                current_key = k
                current_list = None

    return fm


def extract_wikilinks(body):
    """提取正文中的所有 [[链接]]。"""
    return re.findall(r'\[\[([^\]]+?)\]\]', body)


def clean_body(content):
    """去除 frontmatter、H1 标题、关联资源章节，返回纯正文。"""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            content = parts[2]
    # 去除 H1 标题行（# 开头的第一行）
    lines = content.split("\n")
    while lines and (lines[0].strip().startswith("# ") or lines[0].strip() == ""):
        lines = lines[1:]
    # 去除 "## 关联资源" 段落（从 "## 关联资源" 到下一个 "## " 或结尾）
    result = []
    skip = False
    for line in lines:
        if line.strip().startswith("## 关联资源"):
            skip = True
            continue
        if skip and line.strip().startswith("## "):
            skip = False
        if not skip:
            result.append(line)
    return "\n".join(result).strip()


def extract_units(knowledge_dir):
    """从知识元目录读取所有 .md 文件，返回知识元列表。"""
    units = []
    for f in sorted(knowledge_dir.glob("*.md")):
        try:
            with open(f, "r", encoding="utf-8") as fh:
                content = fh.read()
        except Exception as e:
            print(f"  ⚠ 读取失败: {f.name} — {e}", file=sys.stderr)
            continue

        fm = parse_frontmatter(content)
        if fm is None:
            print(f"  ⚠ 无 frontmatter: {f.name}", file=sys.stderr)
            continue

        title = fm.get("title", f.stem)
        tags = fm.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        summary = fm.get("summary", "")
        # 清理 summary 中的 markdown 格式符号
        if summary:
            summary = summary.replace("> ", "").replace(">", "").replace("**", "").replace("*", "").replace("__", "").strip()
        source = fm.get("source", "")

        body = clean_body(content)

        # 提取 [[链接]]
        wikilinks = extract_wikilinks(body)

        # 提取 related_files（frontmatter 中可能包含列表状对象）
        related_files = []
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm_text2 = parts[1]
            for rf_line in re.finditer(r'^\s+-\s+file:\s*"([^"]+)"\s*$', fm_text2, re.MULTILINE):
                related_files.append(rf_line.group(1))

        units.append({
            "file": f.name,
            "title": title,
            "tags": tags,
            "summary": summary,
            "source": source,
            "body": body,
            "wikilinks": wikilinks,
            "related_files": related_files,
        })

    return units


def build_graph_data(units):
    """
    从知识元列表构建 D3.js 所需的 DATA 结构。
    颜色分组：取每个知识元的最后一个标签（类型标签），按频次排序，
    前 10 个独立成组，其余归入"其他"。
    返回: {nodes: [...], links: [...], colorGroups: [...]}
    """
    # 构建节点
    nodes = []
    title_to_id = {}

    for u in units:
        node_id = u["title"]
        title_to_id[u["title"]] = node_id

        text_len = len(u["body"]) if u["body"] else 0

        heading = u["summary"]
        if heading:
            heading = heading.replace("> ", "").replace(">", "")
            heading = heading.replace("**", "").replace("*", "")
            heading = heading.strip()
        if not heading and u["body"]:
            first_line = u["body"].strip().split("\n")[0][:60]
            heading = first_line.replace("> ", "").replace(">", "").replace("**", "").replace("*", "").strip()
        # body 首行若与 heading 文字重复，则跳过（避免 summary 与正文重复显示）
        _body = u["body"]
        if heading and _body:
            _first = _body.strip().split("\n")[0]
            _clean = _first.replace("> ", "").replace(">", "").replace("**", "").replace("*", "").strip()
            if _clean == heading:
                _body = "\n".join(_body.strip().split("\n")[1:]).strip()

        nodes.append({
            "id": node_id,
            "name": node_id,
            "displayName": u["title"],
            "heading": heading,
            "tags": u["tags"],
            "text_len": text_len,
            "content": _body,
            "source": u.get("source", ""),
            "file": u.get("file", ""),
            "related_files": u.get("related_files", []),
            "isRoot": u.get("is_root", False),
        })

    # 构建链接 — 匹配 [[title]] 到节点 ID
    links = []
    link_count = {}

    for u in units:
        src_id = title_to_id.get(u["title"])
        if not src_id:
            continue
        for wl in u["wikilinks"]:
            target = wl.split("|")[0].strip()
            target = target.lstrip("#")
            if target in title_to_id:
                tgt_id = title_to_id[target]
                if src_id != tgt_id:
                    links.append({"source": src_id, "target": tgt_id})
                    link_count[src_id] = link_count.get(src_id, 0) + 1
                    link_count[tgt_id] = link_count.get(tgt_id, 0) + 1

    # 去重链接
    seen_links = set()
    unique_links = []
    for l in links:
        key = (l["source"], l["target"])  # 有向去重，保留 A→B 和 B→A 双向连线
        if key not in seen_links:
            seen_links.add(key)
            unique_links.append(l)
    links = unique_links

    # 计算节点大小（基于链接数）
    max_links = max(link_count.values()) if link_count else 1
    min_links = min(link_count.values()) if link_count else 0
    for node in nodes:
        cnt = link_count.get(node["id"], 0)
        if max_links > min_links:
            node["size"] = (8 + (cnt - min_links) / (max_links - min_links) * 22) * 0.49
        else:
            node["size"] = 7
        node["size"] = round(node["size"], 1)

    # ─── 基于倒数第2个标签聚类 ───
    # 取最后一个标签（类型标签）作为颜色分组依据。
    _tag_counts = {}
    for u in units:
        if u["tags"] and len(u["tags"]) > 0:
            # 取最后一个标签作为颜色分组依据
            ft = u["tags"][-1]
            _tag_counts[ft] = _tag_counts.get(ft, 0) + 1

    # 按频次降序排列
    sorted_tags = sorted(_tag_counts.items(), key=lambda x: -x[1])

    # 模板调色板有 11 个颜色槽，前 10 个独立分组，第 11 个给"其他"
    MAX_COLORS = 10
    top_tags = [t for t, _ in sorted_tags[:MAX_COLORS]]
    other_tags = [t for t, _ in sorted_tags[MAX_COLORS:]]

    color_groups = [{"tags": [tag], "label": tag} for tag in top_tags]
    if other_tags:
        color_groups.append({"tags": other_tags, "label": "其他"})

    return {
        "nodes": nodes,
        "links": links,
        "colorGroups": color_groups,
    }


def generate_html(template_path, graph_data, kb_name="知识库"):
    """读取模板，替换 DATA 标记，返回完整 HTML。"""
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # 将 kb_name 注入到 graph_data 中供模板使用
    graph_data["kb_name"] = kb_name

    data_json = json.dumps(graph_data, ensure_ascii=False, indent=2)

    # 模板中用于注入数据的标记
    start_marker = "/*** ✦✦✦ LLM: 替换此处 DATA 为项目数据 ✦✦✦ ***/"
    end_marker = "/*** ****** LLM: DATA END ****** ***/"

    start_idx = template.find(start_marker)
    end_idx = template.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        print(json.dumps({"error": "模板中未找到 DATA 替换标记"}))
        sys.exit(1)

    new_section = start_marker + "\nvar DATA = " + data_json + ";\n" + end_marker


    html = template[:start_idx] + new_section + template[end_idx + len(end_marker):]

    return html
def get_kb_name(workspace, args):
    """获取知识库名称：优先用 --kb-name，其次从 project_settings.json 读取，然后从根节点文件名推断，兜底为'知识库'。"""
    if args.kb_name:
        return args.kb_name.strip()
    settings_path = workspace / "系统设置" / "project_settings.json"
    if settings_path.exists():
        try:
            with open(settings_path, "r", encoding="utf-8") as f:
                settings = json.load(f)
            name = settings.get("kb_name", "").strip()
            if name:
                return name
        except Exception:
            pass
    manifest_path = workspace / "原始文件" / "_processed_docs.json"
    if manifest_path.exists():
        try:
            with open(manifest_path, "r", encoding="utf-8") as f:
                manifest = json.load(f)
            name = manifest.get("knowledge_base", "").strip()
            if name:
                return name
        except Exception:
            pass
    # 从根节点文件名推断（确保 HTML 文件名与根节点一致）
    for f in workspace.iterdir():
        if f.suffix.lower() == ".md":
            try:
                if "root_node: true" in f.read_text(500, errors="ignore"):
                    return f.stem
            except Exception:
                pass
    return "知识库"


def main():
    parser = argparse.ArgumentParser(description="AHKB 知识地图 HTML 生成器")
    parser.add_argument("--workspace", "-w", help="知识库 Vault 路径")
    parser.add_argument("--kb-name", help="知识库名称（如不提供则从 settings 自动读取）")
    args = parser.parse_args()

    workspace = find_workspace(args)
    knowledge_dir = workspace / "知识元"

    if not knowledge_dir.exists():
        print(json.dumps({"error": f"知识元目录不存在: {knowledge_dir}"}))
        sys.exit(1)

    print(f"📂 知识库路径: {workspace}", file=sys.stderr)
    print(f"📖 扫描知识元...", file=sys.stderr)

    units = extract_units(knowledge_dir)
    print(f"   找到 {len(units)} 个知识元", file=sys.stderr)

    # ★ 查找并纳入核心总纲（根节点 .md 文件），它位于工作区根部而非知识元/ 下
    # 🔴 只在工作空间根目录搜索，不包括任何子目录
    root_node_found = False
    for f in workspace.iterdir():
        if not (f.suffix.lower() == ".md" and f.is_file()):
            continue
        try:
            with open(f, "r", encoding="utf-8") as fh:
                root_content = fh.read()
        except Exception:
            continue
        fm = parse_frontmatter(root_content)
        if fm and fm.get("root_node"):
            print(f"   包含核心总纲: {f.name}", file=sys.stderr)
            root_tags = fm.get("tags", ["总纲"])
            if isinstance(root_tags, str):
                root_tags = [root_tags]
            root_unit = {
                "file": f.name,
                "title": fm.get("title", f.stem),
                "tags": root_tags,
                "summary": fm.get("summary", ""),
                "source": "",
                "body": clean_body(root_content),
                "wikilinks": extract_wikilinks(root_content),
                "is_root": True,
            }
            units.insert(0, root_unit)  # 总纲作为第一个知识元
            root_node_found = True
            break

    # 🛡 按 title 去重：根节点（已插在位置 0）优先保留，
    #    后续知识元若与根节点 title 相同则跳过，避免 D3 图中出现重复节点。
    seen_titles = set()
    deduped_units = []
    for u in units:
        if u["title"] not in seen_titles:
            seen_titles.add(u["title"])
            deduped_units.append(u)
        else:
            print(f"   跳过重复标题: {u['title']} (文件: {u['file']}, 被根节点优先占据)", file=sys.stderr)
    units = deduped_units

    if not root_node_found:
        print(json.dumps({"error": "工作空间根目录下未找到核心总纲（root_node: true）文件。\n"
                                    "请先通过菜单6「🏗 重建知识地图+HTML」或运行 python ahkb.py build-graph 创建根节点。"}))
        sys.exit(1)

    if not units:
        print(json.dumps({"error": "没有找到任何知识元"}))
        sys.exit(1)

    print(f"🔗 构建图谱数据...", file=sys.stderr)
    graph_data = build_graph_data(units)
    print(f"   节点: {len(graph_data['nodes'])} | 链接: {len(graph_data['links'])} | 颜色组: {len(graph_data['colorGroups'])}", file=sys.stderr)

    # 找模板
    script_dir = Path(__file__).parent.resolve()
    template_path = script_dir / "知识地图模板.html"
    if not template_path.exists():
        print(json.dumps({"error": f"模板文件不存在: {template_path}"}))
        sys.exit(1)

    # 确定输出路径和知识库名称
    kb_name = get_kb_name(workspace, args)
    output_path = workspace / f"{kb_name}-知识地图.html"

    print(f"📄 生成 HTML...", file=sys.stderr)
    html = generate_html(template_path, graph_data, kb_name)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    result = {
        "ok": True,
        "html_path": str(output_path.relative_to(workspace)),
        "stats": {
            "units": len(units),
            "nodes": len(graph_data["nodes"]),
            "links": len(graph_data["links"]),
            "color_groups": len(graph_data["colorGroups"]),
        },
    }
    print(json.dumps(result, ensure_ascii=False))
    print(f"\n✅ 知识地图已生成: {output_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
