#!/usr/bin/env python3
"""
本地大模型图书馆 - 快速起步脚本
依赖:
  - Ollama 已安装并运行 (localhost:11434)
  - Python 库: requests (安装: pip install requests)
用法:
  python quickstart.py init        # 初始化图书馆目录
  python quickstart.py summarize   # 批量摘要
  python quickstart.py ask "问题"  # 提问
  python quickstart.py health      # 健康检查
"""

import os
import sys
import json
from datetime import datetime

try:
    import requests
except ImportError:
    print("[错误] 缺少 Python 依赖库 requests")
    print("       请先安装: pip install requests")
    print("       (或使用: python -m pip install requests)")
    sys.exit(1)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = os.environ.get("LLM_MODEL", "qwen2.5:3b")
LIBRARY_DIR = os.environ.get("LIBRARY_DIR", "my-library")
CHUNK_SIZE = 2000


def check_ollama():
    """检查 Ollama 是否在线"""
    try:
        resp = requests.get("http://localhost:11434/api/tags", timeout=5)
        models = [m["name"] for m in resp.json().get("models", [])]
        if not models:
            print("[!] Ollama 在线但没有已安装的模型")
            print("    请运行: ollama pull qwen2.5:3b")
            return False
        print(f"[OK] Ollama 在线，可用模型: {', '.join(models)}")
        if MODEL not in " ".join(models):
            print(f"[!] 当前设定模型 {MODEL} 未安装，请运行: ollama pull {MODEL}")
            return False
        return True
    except requests.ConnectionError:
        print("[!] Ollama 未运行，请先启动: ollama serve")
        return False


def init_library():
    """初始化图书馆目录结构"""
    dirs = [
        "01-法规",
        "02-产品",
        "03-标准",
        "04-学习笔记",
        "05-运营",
        "06-模板",
    ]
    for d in dirs:
        path = os.path.join(LIBRARY_DIR, d)
        os.makedirs(path, exist_ok=True)
        print(f"  [创建] {path}/")

    # 创建索引文件
    index_path = os.path.join(LIBRARY_DIR, "00-index.md")
    if not os.path.exists(index_path):
        with open(index_path, "w", encoding="utf-8") as f:
            f.write("# 知识库索引\n\n")
            f.write(f"> 最后更新: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write("| 文件 | 分类 | 摘要 | 更新日期 |\n")
            f.write("|------|------|------|----------|\n")
        print(f"  [创建] {index_path}")

    # 创建变更日志
    changelog = os.path.join(LIBRARY_DIR, "changelog.md")
    if not os.path.exists(changelog):
        with open(changelog, "w", encoding="utf-8") as f:
            f.write("# 变更日志\n\n")
            f.write(f"- {datetime.now().strftime('%Y-%m-%d')}: 图书馆初始化\n")
        print(f"  [创建] {changelog}")

    print(f"\n[完成] 图书馆已初始化: {LIBRARY_DIR}/")
    print("下一步: 把你的文档（.md/.txt）放到对应目录，然后运行 summarize")


def summarize_file(filepath):
    """让本地模型给单个文件做摘要"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if len(content) <= CHUNK_SIZE:
        chunks = [content]
    else:
        chunks = [content[i:i+CHUNK_SIZE] for i in range(0, len(content), CHUNK_SIZE)]

    summaries = []
    for i, chunk in enumerate(chunks):
        print(f"    分块 {i+1}/{len(chunks)}...", end="", flush=True)
        try:
            resp = requests.post(OLLAMA_URL, json={
                "model": MODEL,
                "prompt": f"请用中文给以下内容做摘要，提取关键信息，200字以内：\n\n{chunk}",
                "stream": False
            }, timeout=300)
            summary = resp.json().get("response", "[摘要失败]")
            summaries.append(summary)
            print(" OK")
        except Exception as e:
            print(f" 失败: {e}")
            summaries.append(f"[摘要失败: {e}]")

    return "\n\n".join(summaries)


def batch_summarize():
    """批量给知识库所有文件做摘要，更新索引"""
    if not check_ollama():
        return

    print(f"\n开始批量摘要 (模型: {MODEL})\n")

    index_lines = [
        "# 知识库索引\n",
        f"> 最后更新: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n",
        "| 文件 | 分类 | 摘要 | 更新日期 |",
        "|------|------|------|----------|",
    ]
    count = 0

    for root, dirs, files in os.walk(LIBRARY_DIR):
        for fname in sorted(files):
            if not fname.endswith((".md", ".txt")) or fname.startswith("00-index"):
                continue
            filepath = os.path.join(root, fname)
            rel_path = os.path.relpath(filepath, LIBRARY_DIR)
            category = os.path.relpath(root, LIBRARY_DIR)

            print(f"  处理: {rel_path}")
            summary = summarize_file(filepath)
            # 单行摘要（表格用）
            summary_oneline = summary.replace("\n", " ")[:100]
            index_lines.append(f"| {fname} | {category} | {summary_oneline} | {datetime.now().strftime('%Y-%m-%d')} |")
            count += 1

    index_path = os.path.join(LIBRARY_DIR, "00-index.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(index_lines) + "\n")

    print(f"\n[完成] 已处理 {count} 个文件，索引已更新: {index_path}")


def ask_library(question):
    """基于知识库回答问题"""
    if not check_ollama():
        return

    # 收集所有文件内容
    context = ""
    for root, dirs, files in os.walk(LIBRARY_DIR):
        for fname in files:
            if fname.endswith((".md", ".txt")):
                filepath = os.path.join(root, fname)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    context += f"\n--- {fname} ---\n{content}\n"

    # 截断到模型上下文长度内
    max_context = 6000
    if len(context) > max_context:
        context = context[:max_context]
        print(f"[!] 知识库较大，已截断到 {max_context} 字符。建议升级到 RAG 方案。")

    prompt = f"""根据以下知识库内容回答问题。
要求：
1. 仅基于知识库内容回答，不要编造
2. 如果知识库中没有相关信息，明确说"知识库中未找到相关信息"
3. 回答时标注信息来源（文件名）

知识库：
{context}

问题：{question}
"""

    print(f"\n提问: {question}")
    print(f"模型: {MODEL}")
    print(f"知识库上下文: {len(context)} 字符\n")
    print("-" * 60)

    try:
        resp = requests.post(OLLAMA_URL, json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }, timeout=600)
        answer = resp.json().get("response", "[回答失败]")
        print(answer)
    except Exception as e:
        print(f"[错误] {e}")

    print("-" * 60)


def health_check():
    """知识库健康检查"""
    print(f"\n知识库健康检查: {LIBRARY_DIR}/\n")

    issues = []
    stats = {"files": 0, "total_size": 0, "categories": set(), "empty_files": 0}

    for root, dirs, files in os.walk(LIBRARY_DIR):
        if ".git" in root:
            continue
        for fname in files:
            if fname.endswith((".md", ".txt")):
                filepath = os.path.join(root, fname)
                size = os.path.getsize(filepath)
                stats["files"] += 1
                stats["total_size"] += size
                stats["categories"].add(os.path.relpath(root, LIBRARY_DIR))

                if size < 50:
                    stats["empty_files"] += 1
                    issues.append(f"  [!] 空文件: {fname}")

                # 检查是否有元信息头
                with open(filepath, "r", encoding="utf-8") as f:
                    head = f.read(200)
                if "---" not in head[:10]:
                    issues.append(f"  [!] 缺少元信息头: {fname}")

    print(f"文件总数: {stats['files']}")
    print(f"总大小: {stats['total_size'] / 1024:.1f} KB")
    print(f"分类数: {len(stats['categories'])}")
    print(f"空文件: {stats['empty_files']}")

    # 检查索引
    index_path = os.path.join(LIBRARY_DIR, "00-index.md")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            index_content = f.read()
        indexed = index_content.count("|") - 2  # 粗略统计
        print(f"索引文件: 存在 (约 {indexed} 条)")
    else:
        issues.append("  [!] 索引文件不存在，请运行 summarize")
        print("索引文件: 不存在")

    # 检查 Git
    git_dir = os.path.join(LIBRARY_DIR, ".git")
    if os.path.exists(git_dir):
        print("版本管理: Git 已初始化")
    else:
        issues.append("  [!] 未启用 Git 版本管理，建议运行: cd my-library && git init")
        print("版本管理: 未启用")

    if issues:
        print(f"\n发现 {len(issues)} 个问题:")
        for issue in issues:
            print(issue)
    else:
        print("\n[OK] 一切正常!")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1]

    if cmd == "init":
        init_library()
    elif cmd == "summarize":
        batch_summarize()
    elif cmd == "ask":
        if len(sys.argv) < 3:
            print("用法: python quickstart.py ask \"你的问题\"")
            return
        ask_library(sys.argv[2])
    elif cmd == "health":
        health_check()
    elif cmd == "check":
        check_ollama()
    else:
        print(f"未知命令: {cmd}")
        print(__doc__)


if __name__ == "__main__":
    main()
