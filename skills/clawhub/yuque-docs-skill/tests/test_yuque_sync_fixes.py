#!/usr/bin/env python3
"""Functional tests for yuque_cli.py covering the 9 REQs from the spec.

Run: python3 tests/test_yuque_sync_fixes.py
"""
import sys
import os
import argparse
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import yuque_cli as y


def test_req1_filename_fallback():
    """REQ-1: 无 H1 且无 frontmatter title 时回退到文件名 stem"""
    text = "---\nslug: update-member-permission\n---\n\n> **权限说明：** 测试"
    title, src = y.extract_title(text, file_stem="修改成员权限", slug="update-member-permission")
    assert title == "修改成员权限", f"expected 修改成员权限, got {title!r}"
    assert src == "filename", f"expected filename, got {src!r}"


def test_req1_frontmatter_title_priority():
    """REQ-1: frontmatter title 优先级最高"""
    text = "---\nslug: x\ntitle: 自定义标题\n---\n\n# H1标题"
    t, s = y.extract_title(text, file_stem="file", slug="x")
    assert t == "自定义标题" and s == "frontmatter", f"FAIL: {t!r} {s!r}"


def test_req1_h1_priority_over_filename():
    """REQ-1: H1 优先于文件名"""
    text = "---\nslug: x\n---\n\n# H1标题\n正文"
    t, s = y.extract_title(text, file_stem="file", slug="x")
    assert t == "H1标题" and s == "h1", f"FAIL: {t!r} {s!r}"


def test_req5_force_title():
    """REQ-5: --force-title 跳过 frontmatter/H1"""
    text = "---\nslug: x\ntitle: 自定义\n---\n\n# H1标题"
    t, s = y.extract_title(text, file_stem="file", slug="x", force_filename=True)
    assert t == "file" and s == "filename", f"FAIL force: {t!r} {s!r}"


def test_req6_link_rewrite_same_dir():
    """REQ-6: 同级文件链接转换"""
    slug_map = {"创建起草任务.md": "create-draft-task"}
    body = "[创建起草任务](创建起草任务.md)"
    new_body, unresolved = y.rewrite_links(body, slug_map)
    assert new_body == "[创建起草任务](create-draft-task)", f"FAIL: {new_body!r}"
    assert unresolved == []


def test_req6_link_rewrite_subdir():
    """REQ-6: 子目录路径通过 basename 匹配"""
    slug_map = {"任务状态变更通知.md": "notify-task-status-changed"}
    body = "[通知](notify/任务状态变更通知.md)"
    new_body, _ = y.rewrite_links(body, slug_map)
    assert new_body == "[通知](notify-task-status-changed)", f"FAIL: {new_body!r}"


def test_req6_external_url_and_anchor_preserved():
    """REQ-6: 外部 URL 和锚点不受影响"""
    slug_map = {}
    body = "[外](https://example.com) [锚](#top) [mail](mailto:a@b.com) [//proto](//host/path)"
    new_body, unresolved = y.rewrite_links(body, slug_map)
    assert new_body == body, f"FAIL: {new_body!r}"
    assert unresolved == []


def test_req6_unresolved_link_preserved():
    """REQ-6: 未匹配链接保留并加入 unresolved"""
    slug_map = {}
    body = "[不存在](不存在的文档.md)"
    new_body, unresolved = y.rewrite_links(body, slug_map)
    assert new_body == body, f"FAIL: {new_body!r}"
    assert unresolved == ["不存在的文档.md"], f"FAIL: {unresolved!r}"


def test_req7_reverse_links():
    """REQ-7: pull 反向链接转换"""
    reverse_map = {"create-draft-task": "创建起草任务.md", "error-codes": "协商起草服务错误码.md"}
    body = "[创建起草任务](create-draft-task) 和 [错误码](error-codes) 和 [外](https://example.com)"
    new_body = y.reverse_links(body, reverse_map)
    assert "](创建起草任务.md)" in new_body, f"FAIL: {new_body!r}"
    assert "](协商起草服务错误码.md)" in new_body, f"FAIL: {new_body!r}"
    assert "https://example.com" in new_body, f"FAIL: {new_body!r}"


def test_req8_bold_fix_no_space():
    """REQ-8: **标签：**值 → **标签：** 值"""
    body = "**接口地址：**https://example.com\n**请求方法：**POST"
    fixed = y.fix_bold_format(body)
    assert "**接口地址：** https://example.com" in fixed, f"FAIL: {fixed!r}"
    assert "**请求方法：** POST" in fixed, f"FAIL: {fixed!r}"


def test_req8_bold_already_has_space():
    """REQ-8: 已有空格不受影响"""
    body = "**权限说明：** 值"
    fixed = y.fix_bold_format(body)
    assert fixed == body, f"FAIL: {fixed!r}"


def test_req9_read_body_strips_frontmatter():
    """REQ-9: read_body 剥离 frontmatter"""
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write("---\nslug: test-doc\n---\n\n# 测试文档\n正文")
        tmppath = f.name
    try:
        ns = argparse.Namespace(body=None, body_file=tmppath)
        body = y.read_body(ns)
        assert "slug: test-doc" not in body, f"FAIL: frontmatter leaked: {body!r}"
        assert body.lstrip().startswith("# 测试文档"), f"FAIL: {body!r}"
    finally:
        os.unlink(tmppath)


def test_req9_read_body_no_frontmatter():
    """REQ-9: 无 frontmatter 时 read_body 正常返回"""
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write("# 标题\n正文")
        tmppath = f.name
    try:
        ns = argparse.Namespace(body=None, body_file=tmppath)
        body = y.read_body(ns)
        assert body.lstrip().startswith("# 标题"), f"FAIL: {body!r}"
    finally:
        os.unlink(tmppath)


def test_flat_layout_backward_compat():
    """向后兼容: flat 布局下 file_stem == slug"""
    # In flat layout, slug_for_file returns path.stem, so file_stem == slug
    text = "---\nslug: mydoc\n---\n\n正文无H1"
    t, s = y.extract_title(text, file_stem="mydoc", slug="mydoc")
    assert t == "mydoc", f"FAIL: {t!r}"
    # title value equals slug, backward compatible


def test_bold_mixed_with_links():
    """集成测试: 加粗修复 + 链接重写同时工作"""
    slug_map = {"target.md": "target-slug"}
    body = "**接口地址：**值 [链接](target.md)"
    new_body, _ = y.rewrite_links(body, slug_map)
    new_body = y.fix_bold_format(new_body)
    assert "**接口地址：** 值" in new_body, f"FAIL bold: {new_body!r}"
    assert "](target-slug)" in new_body, f"FAIL link: {new_body!r}"


TESTS = [
    test_req1_filename_fallback,
    test_req1_frontmatter_title_priority,
    test_req1_h1_priority_over_filename,
    test_req5_force_title,
    test_req6_link_rewrite_same_dir,
    test_req6_link_rewrite_subdir,
    test_req6_external_url_and_anchor_preserved,
    test_req6_unresolved_link_preserved,
    test_req7_reverse_links,
    test_req8_bold_fix_no_space,
    test_req8_bold_already_has_space,
    test_req9_read_body_strips_frontmatter,
    test_req9_read_body_no_frontmatter,
    test_flat_layout_backward_compat,
    test_bold_mixed_with_links,
]


def main():
    passed = 0
    failed = 0
    for test in TESTS:
        try:
            test()
            print(f"PASS: {test.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"FAIL: {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"ERROR: {test.__name__}: {type(e).__name__}: {e}")
            failed += 1
    print(f"\n=== {passed} passed, {failed} failed, {len(TESTS)} total ===")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
