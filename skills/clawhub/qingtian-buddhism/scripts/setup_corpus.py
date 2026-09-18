#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
setup_corpus.py — 青田·原始佛教修学助手 语料自动获取（发布版数据分发入口）

设计目标（与发布约束一致）：
  - 用户端「零授权、零凭证、零手动准备」：只需联网。
  - 数据只能从统一公开的「知识库/语料源」调取：这里是一个公开直链 zip（ModelScope 数据集）。
  - 首次启动时检测本地缓存 → 无则下载 → 解压到 data/corpus → 标记就绪。
  - 后续启动若已就绪则直接跳过，不重复下载/解压。

支持的数据源平台（均须为「公开直链」，urllib 可直接拉取，无需登录或密钥）：
  - ModelScope 魔搭 / Hugging Face Datasets（resolve/main/...zip）
  - 七牛云 Kodo 公开空间 / 腾讯云 COS 公开桶
  - GitHub Release 直链

配置（任选其一，优先级：环境变量 > 本文件占位符）：
  - 环境变量  PALI_CANON_ZIP_URL
  - 或改写本文件顶部 CORPUS_ZIP_URL
"""

import os
import sys
import json
import zipfile
import datetime
import urllib.request
import urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.abspath(os.path.join(HERE, ".."))
CORPUS_DIR = os.path.join(SKILL_ROOT, "data", "corpus")
READY_FILE = os.path.join(SKILL_ROOT, "data", "corpus.ready")

# ★ 语料 zip 公开直链（已验证：ModelScope 数据集 Wangzhenren/pali2026-06-21txt，
#   resolve/master 直链，urllib 无需登录即可下载，国内 LFS CDN 加速）。
#   可用环境变量 PALI_CANON_ZIP_URL 覆盖本默认值。
CORPUS_ZIP_URL = os.environ.get(
    "PALI_CANON_ZIP_URL",
    "https://modelscope.cn/datasets/Wangzhenren/pali2026-06-21txt/resolve/master/"
    "%E5%B7%B4%E5%88%A9%E4%B8%89%E8%97%8F%E5%B7%B4%E5%88%A9-%E4%B8%AD%E6%96%87%E5%AF%B9"
    "%E7%85%A7%E8%AF%91%E6%9C%AC%EF%BC%882026-06-21%EF%BC%89%20txt.zip",
)

UA = "Mozilla/5.0 (compatible; qingtian-buddhism/1.0)"
MIN_ZIP_BYTES = 1024 * 1024  # 小于 1MB 视为异常（登录页/错误页远小于此）

# ★ 语义检索索引（与语料同源：ModelScope 数据集 Wangzhenren/pali2026-06-21txt）。
#   pali_index.faiss：FAISS 标量量化索引（101170×768，IP，已 L2 归一化=余弦）。
#   chunks.jsonl.gz：映射表 id → {rel, start, end, text}，id 即 FAISS 向量序号。
#   二者配套使用，查询端另需 BAAI/bge-base-zh 模型（由 semantic_search.py 首次调用时自动拉取）。
#   注：vectors.f32（296MB 原始向量）检索用不到，刻意不下载以省流量。
INDEX_DIR = os.path.join(SKILL_ROOT, "data", "index")
INDEX_READY_FILE = os.path.join(SKILL_ROOT, "data", "index.ready")
INDEX_FILES = {
    "pali_index.faiss": os.environ.get(
        "PALI_INDEX_URL",
        "https://modelscope.cn/datasets/Wangzhenren/pali2026-06-21txt/resolve/master/pali_index.faiss",
    ),
    "chunks.jsonl.gz": os.environ.get(
        "PALI_CHUNKS_URL",
        "https://modelscope.cn/datasets/Wangzhenren/pali2026-06-21txt/resolve/master/chunks.jsonl.gz",
    ),
}
MIN_INDEX_BYTES = 1024 * 1024  # 单文件不应小于 1MB


def log(msg):
    print(f"[setup_corpus] {msg}", file=sys.stderr)


def count_txt(root):
    n = 0
    for _, _, fs in os.walk(root):
        for fn in fs:
            if fn.lower().endswith(".txt"):
                n += 1
    return n


def already_ready():
    if os.path.exists(READY_FILE) and count_txt(CORPUS_DIR) > 0:
        return True
    return False


def download_file(url, dest, min_bytes=MIN_ZIP_BYTES, label="文件"):
    """通用下载：带进度；若服务器回 HTML（登录墙/403）则主动报错。返回下载字节数。"""
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        resp = urllib.request.urlopen(req, timeout=600)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP 错误 {e.code}：{e.reason}（链接可能失效或需登录）")
    except Exception as e:
        raise RuntimeError(f"网络错误：{e}")

    ctype = resp.headers.get("Content-Type", "").lower()
    if "text/html" in ctype:
        body = resp.read(400).decode("utf-8", "replace")
        raise RuntimeError(
            "服务器返回的是 HTML 页面而非文件（Content-Type=text/html），"
            "很可能是登录墙/403 页面。\n"
            "请确认 URL 是真正的公开直链（七牛/COS/ModelScope/HF/GitHub Release），"
            "而非分享页或需登录的链接。\n"
            f"页面片段：{body[:160]!r}"
        )

    total = int(resp.headers.get("Content-Length", "0") or 0)
    downloaded = 0
    with open(dest, "wb") as f:
        while True:
            chunk = resp.read(1024 * 1024)
            if not chunk:
                break
            f.write(chunk)
            downloaded += len(chunk)
            if total:
                pct = downloaded * 100 // total
                sys.stderr.write(
                    f"\r[setup_corpus] 下载 {label} {downloaded // 1048576}MB / "
                    f"{total // 1048576}MB ({pct}%)"
                )
                sys.stderr.flush()
    sys.stderr.write("\n")
    if downloaded < min_bytes:
        raise RuntimeError(f"下载的{label}仅 {downloaded} 字节，疑似异常页面。")
    return downloaded


def download_zip(dest):
    """下载语料 zip 到 dest（封装通用下载，min_bytes 用 zip 阈值）。"""
    return download_file(CORPUS_ZIP_URL, dest, MIN_ZIP_BYTES, "语料 zip")


def verify_zip(path):
    """校验下载到的是真实 zip（PK 头），而非登录页/错误页。"""
    if os.path.getsize(path) < MIN_ZIP_BYTES:
        raise RuntimeError(f"下载文件仅 {os.path.getsize(path)} 字节，疑似异常页面。")
    with open(path, "rb") as f:
        head = f.read(4)
    if head != b"PK\x03\x04":
        with open(path, "rb") as f:
            snippet = f.read(200)
        raise RuntimeError(
            f"下载文件不是 zip（magic={head!r}）。\n"
            f"前 200 字节：{snippet[:120]!r}\n"
            "很可能是登录页/错误页。请确认 URL 为公开直链。"
        )


def _fix_zip_name(name):
    """修复 Windows 打的 zip 中中文文件名被 cp437/gbk 误编码的问题。"""
    if name.isascii():
        return name
    # 已是正常 unicode（zip 带 utf-8 flag）则原样返回
    try:
        name.encode("ascii")
        return name
    except UnicodeEncodeError:
        pass
    for enc in ("utf-8", "gbk"):
        try:
            return name.encode("cp437").decode(enc)
        except (UnicodeEncodeError, UnicodeDecodeError):
            continue
    return name


def extract_zip(path):
    os.makedirs(CORPUS_DIR, exist_ok=True)
    with zipfile.ZipFile(path) as z:
        bad = z.testzip()
        if bad:
            raise RuntimeError(f"zip 校验失败，损坏文件：{bad}")
        for info in z.infolist():
            name = _fix_zip_name(info.filename)
            dest = os.path.normpath(os.path.join(CORPUS_DIR, name))
            if not dest.startswith(os.path.normpath(CORPUS_DIR)):
                continue  # 防目录穿越
            if name.endswith("/"):
                os.makedirs(dest, exist_ok=True)
            else:
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with z.open(info) as src, open(dest, "wb") as out:
                    out.write(src.read())
    n = count_txt(CORPUS_DIR)
    log(f"解压完成 → {CORPUS_DIR}，txt 文件 {n} 个。")
    if n == 0:
        raise RuntimeError("解压后未找到任何 txt 文件，请检查 zip 内部结构。")


def write_ready(url):
    os.makedirs(os.path.dirname(READY_FILE), exist_ok=True)
    with open(READY_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "url": url,
            "corpus_dir": CORPUS_DIR,
            "ready_at": datetime.datetime.now().isoformat(timespec="seconds"),
            "note": "由 setup_corpus.py 自动生成。删除本文件或 data/corpus 可重新获取。",
        }, f, ensure_ascii=False, indent=2)


def index_ready():
    if not os.path.exists(INDEX_READY_FILE):
        return False
    for fn in INDEX_FILES:
        if not os.path.exists(os.path.join(INDEX_DIR, fn)):
            return False
    return True


def download_index():
    os.makedirs(INDEX_DIR, exist_ok=True)
    for fn, url in INDEX_FILES.items():
        dest = os.path.join(INDEX_DIR, fn)
        if os.path.exists(dest) and os.path.getsize(dest) >= MIN_INDEX_BYTES:
            log(f"索引文件已存在，跳过：{fn}")
            continue
        log(f"下载语义索引：{fn}  <-  {url}")
        try:
            download_file(url, dest, MIN_INDEX_BYTES, fn)
        except Exception as e:
            log(f"[错误] {fn} 下载失败：{e}")
            return 1
    with open(INDEX_READY_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "index_dir": INDEX_DIR,
            "files": list(INDEX_FILES.keys()),
            "ready_at": datetime.datetime.now().isoformat(timespec="seconds"),
            "note": "由 setup_corpus.py 自动生成。删除本文件或 data/index 可重新获取。",
        }, f, ensure_ascii=False, indent=2)
    log("✅ 语义索引就绪（data/index/）。语义检索需 BAAI/bge-base-zh 模型，"
        "首次调用 semantic_search.py 时自动拉取并缓存。")
    return 0


def main():
    # 1) 原文语料（若未就绪则下载）
    if already_ready():
        log("语料已就绪（corpus.ready 存在且有 txt），跳过下载。")
    else:
        if CORPUS_ZIP_URL.startswith("https://REPLACE-ME"):
            log("[错误] 尚未配置语料 zip 直链。请二选一：\n"
                "        1) 设置环境变量 PALI_CANON_ZIP_URL；\n"
                "        2) 修改 scripts/setup_corpus.py 顶部的 CORPUS_ZIP_URL。\n"
                "       可用平台：七牛 Kodo 公开空间 / 腾讯云 COS 公开桶 / ModelScope / "
                "Hugging Face / GitHub Release 直链（均须公开直链）。")
            return 2

        os.makedirs(os.path.dirname(READY_FILE), exist_ok=True)
        tmp = os.path.join(SKILL_ROOT, "data", "_corpus_download.zip")

        log(f"下载语料：{CORPUS_ZIP_URL}")
        try:
            size = download_zip(tmp)
        except Exception as e:
            log(f"[错误] 下载失败：{e}")
            return 1
        log(f"下载完成：{size // 1048576}MB")

        try:
            verify_zip(tmp)
            extract_zip(tmp)
        except Exception as e:
            log(f"[错误] {e}")
            return 1
        finally:
            try:
                if os.path.exists(tmp):
                    os.remove(tmp)
            except OSError:
                pass

        write_ready(CORPUS_ZIP_URL)
        log("✅ 语料就绪。技能现在可离线全文读经与检索（data/corpus/）。")

    # 2) 语义索引（与语料独立；缺失则补下载）
    if index_ready():
        log("语义索引已就绪，跳过下载。")
    else:
        rc = download_index()
        if rc != 0:
            log("[警告] 语义索引下载失败，语义检索暂不可用；Grep 检索不受影响。")

    log("✅ 初始化完成。技能现在可离线读经与检索（data/corpus/ + data/index/）。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
