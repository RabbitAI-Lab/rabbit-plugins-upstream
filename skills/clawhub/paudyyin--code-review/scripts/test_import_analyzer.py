"""
import_analyzer 测试脚本

创建测试项目结构，验证：
  1. extract_imports 正确解析 import 语句
  2. 直接影响识别（谁 import 了我）
  3. 间接影响追踪（2层深度）
  4. 潜在影响识别（同目录测试文件）
  5. 风险等级判定
  6. 完整分析流程

测试项目结构：
  test_project/
    src/
      a.py   # import src.b
      b.py   # import src.c
      c.py   # 无 import
    tests/
      test_a.py  # import src.a
"""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
from pathlib import Path

# 确保能导入同目录下的模块
sys.path.insert(0, str(Path(__file__).parent))

from import_analyzer import (
    analyze,
    extract_imports,
    find_direct_dependents,
    find_indirect_dependents,
    find_potential_impact,
    build_import_map,
    determine_risk_level,
    render_markdown_report,
)


def create_test_project(base_dir: Path) -> Path:
    """创建测试项目结构。"""
    project = base_dir / "test_project"
    src = project / "src"
    tests = project / "tests"
    src.mkdir(parents=True)
    tests.mkdir(parents=True)

    # a.py: import src.b
    (src / "a.py").write_text(
        "import src.b\n\n"
        "def func_a():\n"
        "    return src.b.func_b()\n",
        encoding="utf-8",
    )

    # b.py: import src.c
    (src / "b.py").write_text(
        "from src.c import func_c\n\n"
        "def func_b():\n"
        "    return func_c()\n",
        encoding="utf-8",
    )

    # c.py: 无 import
    (src / "c.py").write_text(
        "def func_c():\n"
        "    return 42\n",
        encoding="utf-8",
    )

    # tests/test_a.py: import src.a
    (tests / "test_a.py").write_text(
        "import src.a\n\n"
        "def test_func_a():\n"
        "    assert src.a.func_a() == 42\n",
        encoding="utf-8",
    )

    # src/__init__.py, tests/__init__.py
    (src / "__init__.py").write_text("", encoding="utf-8")
    (tests / "__init__.py").write_text("", encoding="utf-8")

    return project


def test_extract_imports():
    """测试 1: extract_imports 正确解析 import 语句。"""
    print("=" * 50)
    print("测试 1: extract_imports")
    print("=" * 50)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)

        # 测试 import 语句
        f1 = tmp_path / "test1.py"
        f1.write_text("import os\nimport sys\nimport json\n", encoding="utf-8")
        result1 = extract_imports(f1)
        assert "os" in result1, f"期望 'os' 在 {result1}"
        assert "sys" in result1, f"期望 'sys' 在 {result1}"
        assert "json" in result1, f"期望 'json' 在 {result1}"
        print(f"  ✓ import 语句解析: {result1}")

        # 测试 from...import 语句
        f2 = tmp_path / "test2.py"
        f2.write_text("from os.path import join\nfrom collections import defaultdict\n", encoding="utf-8")
        result2 = extract_imports(f2)
        assert "os.path" in result2, f"期望 'os.path' 在 {result2}"
        assert "collections" in result2, f"期望 'collections' 在 {result2}"
        print(f"  ✓ from...import 语句解析: {result2}")

        # 测试语法错误文件不崩溃
        f3 = tmp_path / "test3.py"
        f3.write_text("this is not valid python {{{{\n", encoding="utf-8")
        result3 = extract_imports(f3)
        assert result3 == [], f"语法错误文件应返回空列表，得到 {result3}"
        print("  ✓ 语法错误文件安全处理")

    print("  ✅ 测试 1 通过\n")


def test_full_analysis_chain():
    """测试 2: 完整分析链 — 变更 c.py → 直接影响 b.py → 间接影响 a.py。"""
    print("=" * 50)
    print("测试 2: 完整分析链（c.py 变更）")
    print("=" * 50)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        project = create_test_project(tmp_path)

        result = analyze(["src/c.py"], project)

        direct = result["impact_analysis"]["direct"]
        indirect = result["impact_analysis"]["indirect"]
        potential = result["impact_analysis"]["potential"]
        summary = result["summary"]

        print(f"  变更文件: {result['changed_files']}")
        print(f"  直接影响: {[d['file'] for d in direct]}")
        print(f"  间接影响: {[d['file'] for d in indirect]}")
        print(f"  潜在影响: {[d['file'] for d in potential]}")
        print(f"  风险等级: {summary['risk_level']}")

        # 验证直接影响：b.py import 了 c.py
        direct_files = [d["file"] for d in direct]
        assert any("b.py" in f for f in direct_files), f"期望 b.py 在直接影响中，得到 {direct_files}"
        print("  ✓ 直接影响：b.py 正确识别")

        # 验证间接影响：a.py import 了 b.py
        indirect_files = [d["file"] for d in indirect]
        assert any("a.py" in f for f in indirect_files), f"期望 a.py 在间接影响中，得到 {indirect_files}"
        print("  ✓ 间接影响：a.py 正确识别")

        # 验证风险等级
        assert summary["risk_level"] == "high", f"期望 high，得到 {summary['risk_level']}"
        print("  ✓ 风险等级：high 正确")

    print("  ✅ 测试 2 通过\n")


def test_direct_only():
    """测试 3: 仅有直接影响（变更独立模块，只有直接依赖方受影响）。"""
    print("=" * 50)
    print("测试 3: 仅直接影响（独立模块变更）")
    print("=" * 50)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        # 创建简化项目：只有 x.py 和 import_x.py
        project = tmp_path / "test_project3"
        src = project / "src"
        src.mkdir(parents=True)
        (src / "__init__.py").write_text("", encoding="utf-8")
        (src / "x.py").write_text("def func_x():\n    return 1\n", encoding="utf-8")
        (src / "y.py").write_text("from src.x import func_x\ndef func_y():\n    return func_x()\n", encoding="utf-8")

        result = analyze(["src/x.py"], project)

        direct = result["impact_analysis"]["direct"]
        indirect = result["impact_analysis"]["indirect"]
        summary = result["summary"]

        print(f"  直接影响: {[d['file'] for d in direct]}")
        print(f"  间接影响: {[d['file'] for d in indirect]}")
        print(f"  风险等级: {summary['risk_level']}")

        # y.py import 了 x.py → 直接影响
        direct_files = [d["file"] for d in direct]
        assert any("y.py" in f for f in direct_files), f"期望 y.py 在直接影响中，得到 {direct_files}"
        print("  ✓ 直接影响：y.py 正确识别")

        # 无间接影响（没有文件 import y.py）
        assert len(indirect) == 0, f"期望无间接影响，得到 {indirect}"
        print("  ✓ 无间接影响")

        # 风险等级应为 medium
        assert summary["risk_level"] == "medium", f"期望 medium，得到 {summary['risk_level']}"
        print("  ✓ 风险等级：medium 正确")

    print("  ✅ 测试 3 通过\n")


def test_no_impact():
    """测试 4: 无影响（变更一个独立文件）。"""
    print("=" * 50)
    print("测试 4: 无影响（独立文件变更）")
    print("=" * 50)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        project = create_test_project(tmp_path)

        # 添加一个独立文件
        (project / "standalone.py").write_text("x = 1\n", encoding="utf-8")

        result = analyze(["standalone.py"], project)

        summary = result["summary"]
        print(f"  风险等级: {summary['risk_level']}")

        assert summary["direct_count"] == 0
        assert summary["indirect_count"] == 0
        assert summary["risk_level"] == "low"
        print("  ✓ 风险等级：low 正确")

    print("  ✅ 测试 4 通过\n")


def test_potential_impact():
    """测试 5: 潜在影响识别（同目录测试文件）。"""
    print("=" * 50)
    print("测试 5: 潜在影响识别")
    print("=" * 50)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        project = create_test_project(tmp_path)

        # 在 src/ 目录添加同目录测试文件
        (project / "src" / "test_c.py").write_text(
            "from src.c import func_c\n\ndef test_func_c():\n    assert func_c() == 42\n",
            encoding="utf-8",
        )

        result = analyze(["src/c.py"], project)
        potential = result["impact_analysis"]["potential"]

        print(f"  潜在影响: {[(p['file'], p['reason']) for p in potential]}")

        potential_files = [p["file"] for p in potential]
        # 应该找到 tests/test_a.py（通过 tests 目录查找）和 src/test_c.py（同目录）
        assert any("test_c.py" in f for f in potential_files), f"期望 test_c.py 在潜在影响中，得到 {potential_files}"
        print("  ✓ 同目录测试文件 test_c.py 正确识别")

    print("  ✅ 测试 5 通过\n")


def test_markdown_report():
    """测试 6: Markdown 报告渲染。"""
    print("=" * 50)
    print("测试 6: Markdown 报告渲染")
    print("=" * 50)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        project = create_test_project(tmp_path)

        result = analyze(["src/c.py"], project)
        md = render_markdown_report(result)

        assert "## 变更影响面分析" in md
        assert "直接影响" in md
        assert "间接影响" in md
        assert "风险评估" in md
        print("  ✓ Markdown 报告包含必要章节")
        print(f"  报告预览（前 300 字）:\n{md[:300]}...")

    print("  ✅ 测试 6 通过\n")


def main() -> None:
    """运行所有测试。"""
    print("\n🧪 import_analyzer 测试套件\n")

    tests = [
        test_extract_imports,
        test_full_analysis_chain,
        test_direct_only,
        test_no_impact,
        test_potential_impact,
        test_markdown_report,
    ]

    passed = 0
    failed = 0

    for test_fn in tests:
        try:
            test_fn()
            passed += 1
        except AssertionError as e:
            print(f"  ❌ 失败: {e}\n")
            failed += 1
        except Exception as e:
            print(f"  ❌ 异常: {e}\n")
            failed += 1

    print("=" * 50)
    print(f"📊 测试结果: {passed} 通过 / {failed} 失败 / {len(tests)} 总计")
    print("=" * 50)

    if failed > 0:
        sys.exit(1)
    else:
        print("\n✅ 所有测试通过！\n")


if __name__ == "__main__":
    main()
