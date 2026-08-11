#!/usr/bin/env python3
"""
抖音视频 → 中文字幕稿（本地、免费、不要 API key）

流程：
    抖音链接 → video_id → iesdouyin share API 拿 mp4 直链 → 下载 → faster-whisper 转写 → 落盘

用法：
    python3 transcribe.py "https://www.douyin.com/video/7634579290163531035"
    python3 transcribe.py "https://v.douyin.com/xa-wFiDUVVs/"
    python3 transcribe.py <链接> --model small         # 用更准的 small 模型
    python3 transcribe.py <链接> --out-dir ./outputs   # 自定义输出目录
    python3 transcribe.py <链接> --tag 公共知识女博主    # 给输出文件加个识别标签
"""

import argparse
import datetime as dt
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.request

# 跨平台临时目录
TEMP_DIR = tempfile.gettempdir()
MODEL_DIR = os.path.join(TEMP_DIR, "whisper-models")

MOBILE_UA = ("Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) "
             "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1")


def _have_curl() -> bool:
    """检测系统是否有 curl"""
    try:
        subprocess.run(["curl", "--version"], capture_output=True, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False


HAS_CURL = _have_curl()


def _http_get(url: str, headers: dict, max_timeout: int = 20) -> str:
    """用 urllib 降级获取（curl 不可用时）"""
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=max_timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def _http_download(url: str, dest: str, headers: dict, max_timeout: int = 180) -> bool:
    """用 urllib 降级下载文件"""
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=max_timeout) as resp:
            with open(dest, "wb") as f:
                while True:
                    chunk = resp.read(8192)
                    if not chunk:
                        break
                    f.write(chunk)
        return True
    except Exception as e:
        print(f"[ERROR] 下载失败: {e}", file=sys.stderr)
        return False


def extract_video_id(url: str) -> str:
    """从抖音链接里掏出 video_id。短链会先 follow 一次。"""
    m = re.search(r"/video/(\d+)", url) or re.search(r"/shipin/(\d+)", url)
    if m:
        return m.group(1)

    # 短链：跟一次 302
    if "v.douyin.com" in url or "iesdouyin.com" in url:
        try:
            if HAS_CURL:
                out = subprocess.check_output(
                    ["curl", "-sI", "--max-time", "10", "-L", url, "-H", f"User-Agent: {MOBILE_UA}"],
                    text=True,
                )
                # 找最后一个 Location 头里的 video_id
                locs = re.findall(r"^[Ll]ocation:\s*(\S+)", out, re.M)
                for loc in reversed(locs):
                    m = re.search(r"/video/(\d+)", loc)
                    if m:
                        return m.group(1)
            else:
                # urllib 降级：urlopen 会自动跟随重定向
                req = urllib.request.Request(url, headers={"User-Agent": MOBILE_UA})
                with urllib.request.urlopen(req, timeout=10) as resp:
                    final_url = resp.geturl()
                    m = re.search(r"/video/(\d+)", final_url)
                    if m:
                        return m.group(1)
        except Exception as e:
            print(f"[WARN] 跟随短链失败: {e}", file=sys.stderr)

    sys.exit(f"[ERROR] 无法从 URL 提取 video_id: {url}\n"
             f"        请改用 https://www.douyin.com/video/<id> 形式的长链")


def fetch_mp4_url(video_id: str) -> str:
    """从 iesdouyin share 页面里抠出 mp4 直链。"""
    share_url = f"https://www.iesdouyin.com/share/video/{video_id}"
    headers = {"User-Agent": MOBILE_UA}

    if HAS_CURL:
        html = subprocess.check_output(
            ["curl", "-sL", "--max-time", "20", share_url, "-H", f"User-Agent: {MOBILE_UA}"],
            text=True,
        )
    else:
        html = _http_get(share_url, headers, max_timeout=20)

    m = re.search(r'"play_addr":\{[^}]*"url_list":\[([^\]]+)\]', html)
    if not m:
        sys.exit(f"[ERROR] iesdouyin 没返回 play_addr，可能是反爬或视频已删。video_id={video_id}")
    raw_urls = re.findall(r'"([^"]+)"', m.group(1))
    if not raw_urls:
        sys.exit("[ERROR] play_addr.url_list 为空")
    # \u002F → /
    return raw_urls[0].encode("utf-8").decode("unicode_escape")


def download_video(url: str, dest: str) -> None:
    print(f"[1/3] 下载 mp4 → {dest}")
    headers = {"User-Agent": MOBILE_UA}

    if HAS_CURL:
        rc = subprocess.call([
            "curl", "-fL", "--max-time", "180", "-o", dest,
            "-H", f"User-Agent: {MOBILE_UA}", url,
        ])
        if rc != 0 or not os.path.exists(dest):
            sys.exit(f"[ERROR] mp4 下载失败，curl 退出码 {rc}")
    else:
        if not _http_download(url, dest, headers, max_timeout=180):
            sys.exit("[ERROR] mp4 下载失败（urllib 降级模式）")

    size_mb = os.path.getsize(dest) / 1024 / 1024
    print(f"      ok, {size_mb:.1f} MB")


def transcribe(mp4_path: str, model_size: str, language: str):
    print(f"[2/3] 加载 faster-whisper '{model_size}' 模型（首次会下载到 {MODEL_DIR}）")
    from faster_whisper import WhisperModel
    model = WhisperModel(
        model_size,
        device="cpu",
        compute_type="int8",
        download_root=MODEL_DIR,
    )
    print(f"[3/3] 转写中…（语言={language}）")
    segments, info = model.transcribe(
        mp4_path,
        language=language,
        beam_size=1,
        vad_filter=True,
    )
    return list(segments), info


def write_outputs(segments, out_dir: str, tag: str, video_id: str):
    os.makedirs(out_dir, exist_ok=True)
    date_prefix = dt.datetime.now().strftime("%m%d")
    label = f"{tag}-" if tag else ""

    timed_path = os.path.join(out_dir, f"{date_prefix}-{label}{video_id}-逐字稿.txt")
    plain_path = os.path.join(out_dir, f"{date_prefix}-{label}{video_id}-连贯稿.txt")

    with open(timed_path, "w", encoding="utf-8") as f_t, \
         open(plain_path, "w", encoding="utf-8") as f_p:
        plain_chunks = []
        for seg in segments:
            text = seg.text.strip()
            f_t.write(f"[{seg.start:6.1f}-{seg.end:6.1f}] {text}\n")
            plain_chunks.append(text)
        f_p.write(" ".join(plain_chunks))

    return timed_path, plain_path


def main():
    parser = argparse.ArgumentParser(description="抖音视频 → 字幕稿（本地 whisper）")
    parser.add_argument("url", help="抖音视频链接（长链或短链都行）")
    parser.add_argument("--model", default="base",
                        choices=["tiny", "base", "small", "medium", "large-v3"],
                        help="whisper 模型大小，默认 base（速度/准确度平衡）")
    parser.add_argument("--language", default="zh", help="语言代码，默认 zh")
    parser.add_argument("--out-dir", default=None,
                        help="输出目录，默认写到脚本同级目录下的 work/ 下")
    parser.add_argument("--tag", default="",
                        help="文件名里加个识别标签，例如 '公共知识女博主'")
    parser.add_argument("--keep-mp4", action="store_true",
                        help="保留下载的 mp4 文件（默认转写完会删）")
    args = parser.parse_args()

    # 默认输出目录：脚本同级目录下的 work/
    if args.out_dir is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        args.out_dir = os.path.join(script_dir, "work")

    t0 = time.time()
    video_id = extract_video_id(args.url)
    print(f"[0/3] video_id = {video_id}")

    mp4_url = fetch_mp4_url(video_id)
    print(f"      mp4 url: {mp4_url[:80]}…")

    mp4_path = os.path.join(TEMP_DIR, f"douyin_{video_id}.mp4")
    download_video(mp4_url, mp4_path)

    segments, info = transcribe(mp4_path, args.model, args.language)

    timed, plain = write_outputs(segments, args.out_dir, args.tag, video_id)

    if not args.keep_mp4:
        try:
            os.remove(mp4_path)
        except OSError:
            pass

    elapsed = time.time() - t0
    print(f"\n[done] 用时 {elapsed:.0f} 秒，视频 {info.duration:.1f} 秒，共 {len(segments)} 段")
    print(f"  逐字稿: {timed}")
    print(f"  连贯稿: {plain}")
    # 额外输出连贯稿内容，方便 AI 直接读取做后处理
    print(f"\n---连贯稿内容---")
    with open(plain, "r", encoding="utf-8") as f:
        print(f.read())
    print(f"---连贯稿结束---")


if __name__ == "__main__":
    main()
