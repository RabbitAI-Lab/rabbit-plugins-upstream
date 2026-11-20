"""
Import 依赖分析器 — 文件级变更影响面追踪

功能：
  - 正向分析：变更文件 import 了哪些模块（依赖谁）
  - 反向分析：哪些文件 import 了变更文件（谁依赖我）
  - 影响分级：直接影响 / 间接影响（2层深度）/ 潜在影响（同目录测试文件）

用法：
  python import_analyzer.py --changed file1.py file2.py --root /project [--depth 2]
  python import_analyzer.py --changed-json '["file1.py"]' --root /project

依赖：纯标准库（ast, pathlib, json）
Python 3.10+
"""

from __future__ import annotations

import ast
import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


# ──────────────────────────────────────────────
# 核心函数
# ──────────────────────────────────────────────

def extract_imports(file_path: Path) -> list[str]:
    """提取文件的所有 import 模块名（顶层模块路径）。"""
    try:
        source = file_path.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(file_path))
    except (SyntaxError, UnicodeDecodeError):
        return []

    imports: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(n.name for n in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)
    return imports


def _resolve_import_to_file(import_module: str, project_root: Path) -> list[Path]:
    """
    将 import 模块名解析为项目内的实际文件路径。
    支持包（__init__.py）和模块（.py）两种形式。

    例：'scripts.server' → ['scripts/server.py', 'scripts/server/__init__.py']
    """
    parts = import_module.replace(".", "/")
    candidates = [
        project_root / f"{parts}.py",           # 普通模块
        project_root / parts / "__init__.py",    # 包
    ]
    return [c for c in candidates if c.is_file()]


def _file_to_module_name(file_path: Path, project_root: Path) -> str:
    """将文件路径转换为模块名。"""
    rel = file_path.relative_to(project_root)
    parts = list(rel.with_suffix("").parts)
    # 如果文件名是 __init__.py，去掉最后的 __init__
    if parts and parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def build_import_map(project_root: Path, extensions: tuple[str, ...] = (".py",)) -> dict[Path, list[str]]:
    """
    扫描项目所有 Python 文件，构建 {文件路径: [import的模块名列表]} 映射。
    """
    import_map: dict[Path, list[str]] = {}
    for py_file in project_root.rglob("*.py"):
        # 跳过常见非项目目录
        rel = py_file.relative_to(project_root)
        skip_dirs = {".venv", "venv", "node_modules", "__pycache__", ".git", ".tox", "dist", "build", ".eggs"}
        if any(part in skip_dirs for part in rel.parts):
            continue
        imports = extract_imports(py_file)
        if imports:
            import_map[py_file] = imports
    return import_map


def find_direct_dependents(
    changed_files: set[Path],
    import_map: dict[Path, list[str]],
    project_root: Path,
) -> list[dict]:
    """
    反向分析：找出所有直接 import 了变更文件的文件。
    返回 [{"file": "相对路径", "imports": ["变更文件相对路径", ...]}]
    """
    # 构建变更文件的模块名集合
    changed_module_names: dict[str, Path] = {}
    for cf in changed_files:
        mod_name = _file_to_module_name(cf, project_root)
        changed_module_names[mod_name] = cf

    direct: list[dict] = []
    for file_path, imports in import_map.items():
        if file_path in changed_files:
            continue  # 跳过变更文件自身

        matched_changed: list[str] = []
        for imp in imports:
            # 检查 import 的模块是否匹配变更文件的模块名
            for mod_name, mod_path in changed_module_names.items():
                if imp == mod_name or imp.startswith(f"{mod_name}."):
                    rel = mod_path.relative_to(project_root)
                    matched_changed.append(str(rel))
                    break
            # 也检查 import 解析后的文件路径是否匹配变更文件
            resolved_files = _resolve_import_to_file(imp, project_root)
            for rf in resolved_files:
                if rf in changed_files:
                    rel = rf.relative_to(project_root)
                    rel_str = str(rel)
                    if rel_str not in matched_changed:
                        matched_changed.append(rel_str)

        if matched_changed:
            rel_file = file_path.relative_to(project_root)
            direct.append({
                "file": str(rel_file),
                "imports": matched_changed,
            })

    return direct


def find_indirect_dependents(
    direct_dependents: list[dict],
    import_map: dict[Path, list[str]],
    project_root: Path,
    changed_files: set[Path],
    max_depth: int = 2,
) -> list[dict]:
    """
    间接影响分析：追踪 import 了直接影响文件的文件（BFS，最大 max_depth 层）。
    返回 [{"file": "相对路径", "imports": ["直接文件"], "via": "中间文件"}]
    """
    if not direct_dependents:
        return []

    indirect: list[dict] = []
    # 已访问文件集合（避免循环依赖）
    visited: set[Path] = set(changed_files)
    # 当前层的文件集合
    current_layer: set[Path] = set()

    for d in direct_dependents:
        fp = project_root / d["file"]
        visited.add(fp)
        current_layer.add(fp)

    # BFS 逐层追踪
    depth = 0
    via_map: dict[Path, str] = {}  # 记录 via 路径
    for d in direct_dependents:
        fp = project_root / d["file"]
        via_map[fp] = d["file"]

    while current_layer and depth < max_depth:
        next_layer: set[Path] = set()
        depth += 1

        for file_path, imports in import_map.items():
            if file_path in visited:
                continue

            for imp in imports:
                resolved_files = _resolve_import_to_file(imp, project_root)
                for layer_file in current_layer:
                    if layer_file in resolved_files:
                        rel_file = file_path.relative_to(project_root)
                        via_file = via_map.get(layer_file, str(layer_file.relative_to(project_root)))
                        indirect.append({
                            "file": str(rel_file),
                            "imports": [str(layer_file.relative_to(project_root))],
                            "via": via_file,
                        })
                        visited.add(file_path)
                        next_layer.add(file_path)
                        via_map[file_path] = via_file
                        break
                else:
                    continue
                break

        current_layer = next_layer

    return indirect


def find_potential_impact(
    changed_files: set[Path],
    project_root: Path,
) -> list[dict]:
    """
    潜在影响分析：找出同目录下的测试文件和配置文件。
    返回 [{"file": "相对路径", "reason": "原因"}]
    """
    potential: list[dict] = []
    seen: set[Path] = set()

    for cf in changed_files:
        parent = cf.parent
        stem = cf.stem

        # 查找同目录下的测试文件
        for sibling in parent.iterdir():
            if sibling in seen or sibling in changed_files:
                continue
            if not sibling.is_file():
                continue

            name = sibling.name.lower()
            # 测试文件匹配：test_*.py, *_test.py, *_tests.py, conftest.py
            is_test = (
                name.startswith("test_")
                or name.endswith("_test.py")
                or name.endswith("_tests.py")
                or name == "conftest.py"
            )
            # 与变更文件相关的测试文件（名称包含关系）
            is_related_test = is_test and stem.lower() in name

            if is_related_test:
                rel = sibling.relative_to(project_root)
                potential.append({
                    "file": str(rel),
                    "reason": f"同目录测试文件（关联 {cf.name}）",
                })
                seen.add(sibling)

        # 查找 tests/ 目录下对应的测试文件
        # 约定：src/foo/bar.py → tests/test_bar.py 或 tests/foo/test_bar.py
        rel_cf = cf.relative_to(project_root)
        parts = list(rel_cf.parts)
        # 尝试在 tests/ 目录下找
        tests_dirs = [project_root / "tests", project_root / "test"]
        for tests_dir in tests_dirs:
            if not tests_dir.is_dir():
                continue
            test_name = f"test_{stem}.py"
            for candidate in tests_dir.rglob(test_name):
                if candidate in seen or candidate in changed_files:
                    continue
                rel = candidate.relative_to(project_root)
                potential.append({
                    "file": str(rel),
                    "reason": f"tests目录对应测试文件（关联 {cf.name}）",
                })
                seen.add(candidate)

        # 配置文件匹配
        config_patterns = [f"{stem}.yaml", f"{stem}.yml", f"{stem}.json", f"{stem}.toml", f"{stem}.ini", f"{stem}.cfg"]
        for sibling in parent.iterdir():
            if sibling in seen or sibling in changed_files:
                continue
            if sibling.name in config_patterns:
                rel = sibling.relative_to(project_root)
                potential.append({
                    "file": str(rel),
                    "reason": f"同目录配置文件（关联 {cf.name}）",
                })
                seen.add(sibling)

    return potential


def determine_risk_level(direct: list[dict], indirect: list[dict]) -> str:
    """
    风险等级判定：
      - low: 无直接影响
      - medium: 有直接影响但无间接影响
      - high: 有间接影响
    """
    if indirect:
        return "high"
    elif direct:
        return "medium"
    else:
        return "low"


# ──────────────────────────────────────────────
# 主分析函数
# ──────────────────────────────────────────────

def analyze(
    changed_files: list[str],
    project_root: str | Path,
    max_depth: int = 2,
) -> dict:
    """
    执行完整的变更影响分析。

    参数：
        changed_files: 变更文件列表（相对路径或绝对路径）
        project_root: 项目根目录
        max_depth: 间接影响追踪深度（默认2）

    返回：
        包含 impact_analysis 和 summary 的字典（JSON 可序列化）
    """
    root = Path(project_root).resolve()

    # 规范化变更文件路径
    changed_paths: set[Path] = set()
    for f in changed_files:
        p = Path(f)
        if not p.is_absolute():
            p = root / p
        if p.is_file():
            changed_paths.add(p)

    if not changed_paths:
        return {
            "changed_files": changed_files,
            "impact_analysis": {"direct": [], "indirect": [], "potential": []},
            "summary": {
                "direct_count": 0,
                "indirect_count": 0,
                "potential_count": 0,
                "risk_level": "low",
            },
            "timestamp": datetime.now().isoformat(),
        }

    # 构建项目 import 映射
    import_map = build_import_map(root)

    # 三级影响分析
    direct = find_direct_dependents(changed_paths, import_map, root)
    indirect = find_indirect_dependents(direct, import_map, root, changed_paths, max_depth)
    potential = find_potential_impact(changed_paths, root)

    # 风险等级
    risk_level = determine_risk_level(direct, indirect)

    # 构造输出
    rel_changed = [str(p.relative_to(root)) for p in sorted(changed_paths)]

    return {
        "changed_files": rel_changed,
        "impact_analysis": {
            "direct": direct,
            "indirect": indirect,
            "potential": potential,
        },
        "summary": {
            "direct_count": len(direct),
            "indirect_count": len(indirect),
            "potential_count": len(potential),
            "risk_level": risk_level,
        },
        "timestamp": datetime.now().isoformat(),
    }


# ──────────────────────────────────────────────
# 报告渲染
# ──────────────────────────────────────────────

def render_markdown_report(result: dict) -> str:
    """将分析结果渲染为 Markdown 格式的影响面报告。"""
    ts = result.get("timestamp", datetime.now().isoformat())
    changed = result["changed_files"]
    analysis = result["impact_analysis"]
    summary = result["summary"]

    direct = analysis["direct"]
    indirect = analysis["indirect"]
    potential = analysis["potential"]
    risk_level = summary["risk_level"]

    lines: list[str] = []
    lines.append("## 变更影响面分析\n")
    lines.append(f"**分析时间**: {ts}")
    lines.append(f"**变更文件数**: {len(changed)}")
    lines.append(f"**影响范围**: 直接 {summary['direct_count']} / 间接 {summary['indirect_count']} / 潜在 {summary['potential_count']}\n")

    # 直接影响
    lines.append(f"### 直接影响（{len(direct)}个文件）\n")
    if direct:
        for item in direct:
            imports_str = ", ".join(f"`{i}`" for i in item["imports"])
            lines.append(f"- `{item['file']}` ← import了 {imports_str}")
    else:
        lines.append("_无直接影响_")
    lines.append("")

    # 间接影响
    lines.append(f"### 间接影响（{len(indirect)}个文件）\n")
    if indirect:
        for item in indirect:
            lines.append(f"- `{item['file']}` ← via `{item['via']}`")
    else:
        lines.append("_无间接影响_")
    lines.append("")

    # 潜在影响
    lines.append(f"### 潜在影响（{len(potential)}个文件）\n")
    if potential:
        for item in potential:
            lines.append(f"- `{item['file']}` ← {item['reason']}")
    else:
        lines.append("_无潜在影响_")
    lines.append("")

    # 风险评估
    lines.append(f"**风险评估**: {risk_level}\n")
    if risk_level == "high":
        lines.append("⚠️ 建议重点审查间接影响文件的接口兼容性")
    elif risk_level == "medium":
        lines.append("建议审查直接影响文件的接口兼容性")
    else:
        lines.append("变更影响范围可控")

    return "\n".join(lines)


# ──────────────────────────────────────────────
# CLI 入口
# ──────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Import 依赖分析器 — 文件级变更影响面追踪",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--changed",
        nargs="+",
        help="变更文件列表（相对路径）",
    )
    group.add_argument(
        "--changed-json",
        type=str,
        help="变更文件列表（JSON 字符串格式）",
    )
    parser.add_argument(
        "--root",
        type=str,
        default=".",
        help="项目根目录（默认当前目录）",
    )
    parser.add_argument(
        "--depth",
        type=int,
        default=2,
        help="间接影响追踪深度（默认2）",
    )
    parser.add_argument(
        "--format",
        choices=["json", "markdown"],
        default="json",
        help="输出格式（默认 json）",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="输出文件路径（默认输出到 stdout）",
    )

    args = parser.parse_args()

    # 解析变更文件列表
    if args.changed_json:
        changed_files: list[str] = json.loads(args.changed_json)
    else:
        changed_files = args.changed

    # 执行分析
    result = analyze(changed_files, args.root, args.depth)

    # 输出
    if args.format == "markdown":
        output = render_markdown_report(result)
    else:
        output = json.dumps(result, ensure_ascii=False, indent=2)

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"报告已写入: {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
