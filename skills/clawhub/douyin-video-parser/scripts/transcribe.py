#!/usr/bin/env python3
"""
抖音视频 → 中文字幕稿 + 结构化 HTML 报告（本地、免费、不要 API key）

流程：
    抖音链接 → video_id → iesdouyin share API 拿 mp4 直链 → 下载 → faster-whisper 转写 → 落盘 txt + 生成 HTML

用法：
    python3 transcribe.py "https://www.douyin.com/video/7634579290163531035"
    python3 transcribe.py "https://v.douyin.com/xa-wFiDUUvVs/"
    python3 transcribe.py <链接> --model small                # 用更准的 small 模型
    python3 transcribe.py <链接> --generate-html              # 生成 HTML 报告
    python3 transcribe.py <链接> --out-dir ./outputs          # 自定义输出目录
    python3 transcribe.py <链接> --tag 公共知识女博主           # 给输出文件加个识别标签
"""

import argparse
import datetime as dt
import html
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


# ═══════════════════════════════════════════════════════════
# 辅助函数
# ═══════════════════════════════════════════════════════════

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


def _safe_filename(s: str, max_len: int = 40) -> str:
    for ch in r'\/:*?"<>|':
        s = s.replace(ch, "_")
    return s.strip().replace(" ", "_")[:max_len]


def _format_duration(seconds: float) -> str:
    if not seconds:
        return ""
    m = int(seconds // 60)
    s = int(seconds % 60)
    if m == 0:
        return f"{s}秒"
    return f"{m}分{s}秒"


def _esc(text) -> str:
    """HTML 转义"""
    return html.escape(str(text) if text is not None else "")


# ═══════════════════════════════════════════════════════════
# 1. 视频下载
# ═══════════════════════════════════════════════════════════

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
                locs = re.findall(r"^[Ll]ocation:\s*(\S+)", out, re.M)
                for loc in reversed(locs):
                    m = re.search(r"/video/(\d+)", loc)
                    if m:
                        return m.group(1)
            else:
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


def fetch_video_title(video_id: str) -> str:
    """从 iesdouyin share 页面提取视频标题"""
    share_url = f"https://www.iesdouyin.com/share/video/{video_id}"
    headers = {"User-Agent": MOBILE_UA}

    if HAS_CURL:
        page_html = subprocess.check_output(
            ["curl", "-sL", "--max-time", "20", share_url, "-H", f"User-Agent: {MOBILE_UA}"],
            text=True,
        )
    else:
        page_html = _http_get(share_url, headers, max_timeout=20)

    title = "untitled"
    tm = re.search(r'<title[^>]*>(.*?)</title>', page_html, re.S)
    if tm:
        raw = tm.group(1).strip()
        title = raw.rsplit(" - ", 1)[0].strip() or raw
    return title


def fetch_mp4_url(video_id: str) -> str:
    """从 iesdouyin share 页面里抠出 mp4 直链。"""
    share_url = f"https://www.iesdouyin.com/share/video/{video_id}"
    headers = {"User-Agent": MOBILE_UA}

    if HAS_CURL:
        page_html = subprocess.check_output(
            ["curl", "-sL", "--max-time", "20", share_url, "-H", f"User-Agent: {MOBILE_UA}"],
            text=True,
        )
    else:
        page_html = _http_get(share_url, headers, max_timeout=20)

    m = re.search(r'"play_addr":\{[^}]*"url_list":\[([^\]]+)\]', page_html)
    if not m:
        sys.exit(f"[ERROR] iesdouyin 没返回 play_addr，可能是反爬或视频已删。video_id={video_id}")
    raw_urls = re.findall(r'"([^"]+)"', m.group(1))
    if not raw_urls:
        sys.exit("[ERROR] play_addr.url_list 为空")
    # \u002F → /
    return raw_urls[0].encode("utf-8").decode("unicode_escape")


def download_video(url: str, dest: str) -> None:
    print(f"[1/3] 下载 mp4 -> {dest}")
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


# ═══════════════════════════════════════════════════════════
# 2. 转写
# ═══════════════════════════════════════════════════════════

def transcribe(mp4_path: str, model_size: str, language: str):
    print(f"[2/3] 加载 faster-whisper '{model_size}' 模型（首次会下载到 {MODEL_DIR}）")
    from faster_whisper import WhisperModel
    model = WhisperModel(
        model_size,
        device="cpu",
        compute_type="int8",
        download_root=MODEL_DIR,
    )
    print(f"[3/3] 转写中... (语言={language})")
    segments, info = model.transcribe(
        mp4_path,
        language=language,
        beam_size=1,
        vad_filter=True,
    )
    return list(segments), info


# ═══════════════════════════════════════════════════════════
# 3. 本地智能提取（无 API Key 时）
# ═══════════════════════════════════════════════════════════

def local_analysis(title: str, plain_text: str) -> dict:
    """无 LLM 时的本地规则提取

    通过关键词密度、段落结构和数字线索尝试提取有意义的分析结果。
    """
    sentences = [s.strip() for s in re.split(r'[。！？；\n]', plain_text) if len(s.strip()) > 4]
    full_text = plain_text[:6000]

    # ── 摘要 ──
    summary = ""
    title_keywords = [w for w in re.split(r'[#\s、，,]+', title) if len(w) >= 2]
    start = max(len(sentences) // 3, 1)
    for s in sentences[start:]:
        if len(s) > 10 and len(s) < 80:
            score = sum(1 for kw in title_keywords if kw in s)
            if score >= 1 or ("核心" in s or "关键" in s or "总结" in s or "本质" in s):
                summary = s
                break
    if not summary and sentences:
        mid_idx = len(sentences) // 2
        for offset in range(min(10, len(sentences) // 4)):
            idx = mid_idx + offset
            if idx < len(sentences) and 12 < len(sentences[idx]) < 80:
                summary = sentences[idx]
                break
    if not summary:
        summary = title
    if len(summary) > 100:
        summary = summary[:97] + "..."

    # ── 核心观点 ──
    section_markers = [
        r'(?:第[一二三四五六七八九十\d]|首先|其次|最后|另外|此外|还有|那么|所以|因此|但是|然而)',
        r'(?:什么是|如何|怎么|为什么|方式|方法|途径|步骤|类型|种类|分类)',
        r'(?:问题|答案|结论|重点|关键|核心|本质)',
        r'(?:比如|例如|举个|打个|就是|意思是|简单来说)',
    ]
    marker_pattern = '|'.join(section_markers)

    candidates = []
    for s in sentences:
        if len(s) < 8 or len(s) > 60:
            continue
        has_number = bool(re.search(r'[\d一二三四五六七八九十]', s))
        has_marker = bool(re.search(marker_pattern, s))
        if has_number or has_marker:
            candidates.append(s)

    key_points = []
    seen = set()
    for c in candidates:
        short = c[:15]
        if short not in seen:
            seen.add(short)
            key_points.append(c)
        if len(key_points) >= 6:
            break

    if len(key_points) < 3:
        for s in sentences:
            if len(s) > 15 and len(s) < 60 and s[:15] not in seen:
                seen.add(s[:15])
                key_points.append(s)
            if len(key_points) >= 4:
                break
    if not key_points:
        key_points = [title]

    # ── 金句 ──
    quotes = []
    quote_patterns = [
        r'(?:说过|说过一句话|名言|有句|原话说|经常说|说过一段)',
        r'(?:叫做|称之为|这就是|这就是所谓的)',
        r'(?:不是.*而是|与其.*不如|宁可.*也不)',
    ]
    for s in sentences:
        if len(s) < 10 or len(s) > 55:
            continue
        if s in [q.get("text", "") for q in quotes]:
            continue
        score = sum(1 for p in quote_patterns if re.search(p, s))
        score += 1 if ("?" in s or "!" in s) else 0
        score += 1 if any(kw in s for kw in ["真正", "本质", "根本", "唯一", "所有", "一切", "永远"]) else 0
        if score >= 1:
            quotes.append({"text": s, "context": ""})
            if len(quotes) >= 3:
                break

    if len(quotes) < 2:
        for s in sentences:
            if s in [q["text"] for q in quotes]:
                continue
            if len(s) > 12 and len(s) < 50 and re.search(r'[A-Za-z]{4,}', s):
                quotes.append({"text": s, "context": ""})
                if len(quotes) >= 3:
                    break

    # ── 结构拆解 ──
    struct_type = "通用分析"
    breakdown = {}

    struct_signals = {
        "开场引入": [r'今天', r'大家', r'我们', r'各位', r'分享', r'聊聊'],
        "提出问题": [r'什么是', r'为什么', r'怎么', r'如何', r'问题', r'知道吗'],
        "核心论述": [r'首先', r'第二', r'第三', r'第[一二三四]', r'分类', r'类型', r'方式'],
        "举例说明": [r'比如', r'例如', r'举个', r'假设', r'你看', r'比方'],
        "方法总结": [r'方法', r'方式', r'途径', r'步骤', r'关键', r'重点', r'核心'],
        "结尾收束": [r'综上', r'最后', r'总结', r'所以', r'希望大家', r'下课'],
    }

    third = max(len(sentences) // 3, 3)
    first_part = sentences[:third]
    mid_part = sentences[third:2 * third]
    last_part = sentences[2 * third:]

    for label, patterns in struct_signals.items():
        search_in = first_part if "开场" in label or "提出" in label else (
            last_part if "结尾" in label or "总结" in label else mid_part
        )
        for s in search_in:
            if len(s) > 8 and any(re.search(p, s) for p in patterns):
                breakdown[label] = s[:60]
                break

    if not breakdown:
        breakdown["开场"] = sentences[0][:60] if sentences else ""
        breakdown["核心内容"] = f"全文约 {len(sentences)} 句"
        breakdown["结尾"] = sentences[-1][:60] if len(sentences) > 1 else ""

    if "知识" in title or "学习" in title or "教程" in title or "教你" in title:
        struct_type = "知识口播"
    elif "vlog" in title.lower() or "日常" in title:
        struct_type = "Vlog"
    elif "搞笑" in title or "段子" in title:
        struct_type = "情景剧"
    elif any(kw in title for kw in ["测评", "推荐", "种草", "好物"]):
        struct_type = "营销内容"
    elif any(kw in title for kw in ["采访", "对话", "访谈"]):
        struct_type = "采访"

    # ── 内容判断 ──
    stance = "创作者"
    credibility = "-"
    if any(kw in full_text for kw in ["研究", "数据", "调查", "实验", "论文"]):
        credibility = "中高: 文本含研究/数据类引用"
    elif len(sentences) > 30:
        credibility = "中: 内容有一定篇幅，但无明确数据来源标注"
    else:
        credibility = "-: 文本过短，无法判断可信度"

    takeaway = "-"
    if len(sentences) > 40:
        takeaway = "内容体量较大，适合作为结构化口播学习素材"
    elif len(sentences) > 15:
        takeaway = "中等体量内容，可关注其开头/结尾的结构设计"

    # ── 亮点 ──
    highlights = []
    for i, p in enumerate(key_points[:6]):
        highlights.append({
            "name": p[:20] + ("..." if len(p) > 20 else ""),
            "desc": p if len(p) <= 60 else p[:57] + "...",
            "tag": f"观点{i + 1:02d}"
        })

    return {
        "summary": summary,
        "key_points": key_points,
        "structure": {"type": struct_type, "breakdown": breakdown},
        "quotes": quotes,
        "judgment": {"stance": stance, "credibility": credibility, "takeaway": takeaway},
        "highlights": highlights,
    }


# ═══════════════════════════════════════════════════════════
# 4. HTML 报告
# ═══════════════════════════════════════════════════════════

HTML_CSS = r"""
  :root {
    --bg:          oklch(0.975 0.005 90);
    --bg-warm:     oklch(0.96 0.01 85);
    --surface:     #fff;
    --surface-hover: oklch(0.98 0.005 88);
    --text:        oklch(0.18 0.01 90);
    --text-secondary: oklch(0.42 0.01 90);
    --text-muted:  oklch(0.58 0.01 90);
    --accent:      oklch(0.48 0.18 25);
    --accent-light: oklch(0.70 0.12 30);
    --accent-bg:   oklch(0.92 0.04 35);
    --accent-bg-light: oklch(0.96 0.02 30);
    --border:      oklch(0.88 0.01 85);
    --shadow-sm:   0 1px 3px oklch(0 0 0 / 0.06);
    --shadow-md:   0 4px 16px oklch(0 0 0 / 0.08);
    --shadow-lg:   0 8px 32px oklch(0 0 0 / 0.10);
    --radius-sm:   8px;
    --radius-md:   14px;
    --radius-lg:   22px;
  }

  * { margin:0; padding:0; box-sizing:border-box; }

  body {
    font-family: system-ui, -apple-system, 'PingFang SC', 'Microsoft YaHei', sans-serif;
    background: var(--bg); color: var(--text); line-height:1.75;
    -webkit-font-smoothing: antialiased;
  }
  h1, .big-text, .quote-text, .detail-title, .cap-title,
  .point-num, .pd-rank, .quote-mark {
    font-family: 'PingFang SC', 'Noto Serif CJK SC', 'SimSun', serif;
  }

  .container { max-width:880px; margin:0 auto; padding:0 24px 80px; }

  /* Hero */
  .hero { text-align:center; padding:80px 0 48px; }
  .hero-badge {
    display:inline-flex; align-items:center; gap:8px;
    padding:5px 16px; border-radius:999px;
    background: oklch(0.85 0.06 30 / 0.12);
    font-size:12px; color:var(--accent); font-weight:600;
    letter-spacing:0.5px; margin-bottom:20px;
  }
  .hero-badge .dot { width:6px; height:6px; border-radius:50%; background:var(--accent); }
  .hero h1 {
    font-size:clamp(1.8rem, 4.5vw, 2.8rem);
    font-weight:900; line-height:1.35; letter-spacing:0.02em;
  }
  .hero-meta {
    display:flex; gap:24px; justify-content:center;
    margin-top:14px; font-size:13px; color:var(--text-muted);
  }

  /* Summary */
  .summary-card {
    background:var(--surface); border-radius:var(--radius-lg);
    padding:48px 40px; margin-bottom:44px;
    box-shadow:var(--shadow-lg);
    position:relative; overflow:hidden;
  }
  .summary-card::before {
    content:''; position:absolute; top:0; left:0;
    width:4px; height:100%;
    background:linear-gradient(180deg, var(--accent), var(--accent-light));
  }
  .summary-card .label {
    font-size:11px; text-transform:uppercase; letter-spacing:0.14em;
    color:var(--accent); font-weight:700; margin-bottom:14px;
  }
  .summary-card .big-text {
    font-size:clamp(1.15rem, 2.2vw, 1.45rem);
    font-weight:600; line-height:1.9;
  }
  .big-text em {
    font-style:normal; color:var(--accent); font-weight:700;
  }

  /* Section */
  .section-head {
    display:flex; align-items:center; gap:12px; margin-bottom:24px;
  }
  .section-head .icon {
    width:32px; height:32px; border-radius:8px;
    background:var(--accent-bg);
    display:flex; align-items:center; justify-content:center;
    font-size:15px; flex-shrink:0;
  }
  .section-head h2 {
    font-size:1.25rem; font-weight:700;
  }

  /* Quotes */
  .quotes-section { margin-bottom:44px; }
  .quotes-grid {
    display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:20px;
  }
  .quote-card {
    background:var(--surface); border-radius:var(--radius-md);
    padding:36px 28px 32px; box-shadow:var(--shadow-md);
    transition:transform 0.2s,box-shadow 0.2s; position:relative;
  }
  .quote-card:hover { transform:translateY(-2px); box-shadow:var(--shadow-lg); }
  .quote-mark {
    font-size:4rem; font-weight:900; color:var(--accent-bg);
    line-height:0.6; margin-bottom:12px;
  }
  .quote-text {
    font-size:1.15rem; font-weight:700; line-height:1.8;
  }
  .share-tag {
    display:inline-block; margin-top:16px;
    padding:3px 12px; font-size:11px; border-radius:999px;
    background:var(--accent-bg-light); color:var(--accent);
    font-weight:500; letter-spacing:0.5px;
  }

  /* Bookshelf (Capsules) */
  .bookshelf-section { margin-bottom:44px; }
  .capsule-grid {
    display:grid; grid-template-columns:repeat(2, 1fr); gap:14px;
  }
  .capsule {
    background:var(--surface); border-radius:var(--radius-md);
    padding:26px 22px; cursor:pointer;
    border:1px solid var(--border); box-shadow:var(--shadow-sm);
    transition:all 0.2s;
  }
  .capsule:hover {
    transform:translateY(-1px); box-shadow:var(--shadow-md);
    border-color:var(--accent-light);
  }
  .cap-icon { font-size:1.6rem; display:block; margin-bottom:14px; }
  .cap-title { font-size:0.95rem; font-weight:700; margin-bottom:4px; }
  .cap-sub {
    font-size:12px; color:var(--text-muted);
    display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical;
    overflow:hidden;
  }

  .capsule-detail {
    display:none;
    background:var(--surface); border-radius:var(--radius-lg);
    padding:40px 36px; margin-top:20px;
    box-shadow:var(--shadow-lg); position:relative;
    animation:slideUp 0.3s ease;
  }
  .capsule-detail.active { display:block; }

  @keyframes slideUp {
    from { opacity:0; transform:translateY(12px); }
    to   { opacity:1; transform:translateY(0); }
  }

  .close-btn {
    position:absolute; top:12px; right:16px;
    width:36px; height:36px; border-radius:50%;
    display:flex; align-items:center; justify-content:center;
    font-size:1.2rem; color:var(--text-muted); cursor:pointer;
    background:none; border:none;
    transition:background 0.15s;
  }
  .close-btn:hover { background:var(--surface-hover); color:var(--text); }

  .detail-title {
    font-size:1.25rem; font-weight:700; padding-right:40px;
    margin-bottom:24px;
  }

  /* Points List */
  .points-list { display:flex; flex-direction:column; gap:18px; }
  .point-item { display:flex; gap:16px; align-items:flex-start; }
  .point-num {
    width:36px; height:36px; border-radius:10px;
    background:var(--accent-bg);
    display:flex; align-items:center; justify-content:center;
    font-weight:700; color:var(--accent); flex-shrink:0;
  }
  .point-content h4 { font-size:0.95rem; font-weight:700; margin-bottom:4px; }
  .point-content p { font-size:0.85rem; color:var(--text-secondary); line-height:1.7; }

  /* Struct List */
  .struct-list { display:flex; flex-direction:column; gap:14px; }
  .struct-item { display:flex; gap:16px; align-items:baseline; }
  .struct-label {
    flex-shrink:0; font-weight:700; font-size:0.88rem;
    color:var(--accent); min-width:72px;
  }
  .struct-content { font-size:0.9rem; color:var(--text-secondary); line-height:1.7; }

  /* Judge Grid */
  .judge-grid {
    display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:16px;
  }
  .judge-mini {
    background:oklch(0.97 0.005 88); border-radius:var(--radius-sm);
    padding:22px 18px;
  }
  .jm-label {
    font-size:11px; text-transform:uppercase; letter-spacing:0.08em;
    color:var(--accent); font-weight:600; margin-bottom:6px;
  }
  .jm-title { font-weight:700; font-size:0.9rem; margin-bottom:6px; }
  .jm-desc { font-size:0.82rem; color:var(--text-secondary); line-height:1.7; }

  /* Paradox List */
  .paradox-detail-list {
    display:flex; flex-direction:column; gap:1px;
    background:var(--border); border-radius:var(--radius-sm);
    overflow:hidden;
  }
  .paradox-detail-item {
    display:grid; grid-template-columns:52px 1fr auto;
    gap:16px; padding:14px 18px; background:var(--surface);
  }
  .pd-rank {
    font-size:1.5rem; font-weight:900; color:var(--accent-light);
    text-align:center; line-height:1.2;
  }
  .pd-rank.top3 { color:var(--accent); }
  .pd-name { font-weight:700; font-size:0.9rem; line-height:1.2; }
  .pd-desc { font-size:0.82rem; color:var(--text-secondary); margin-top:2px; }
  .pd-tag {
    font-size:11px; border-radius:999px; padding:2px 10px;
    background:var(--accent-bg-light); color:var(--text-muted);
    align-self:center; white-space:nowrap;
  }

  /* Footer */
  .footer {
    text-align:center; color:var(--text-muted); font-size:12px;
    margin-top:52px; padding-top:20px; border-top:1px solid var(--border);
  }
  .footer p { margin:0; }
  .footer .brand { font-weight:600; color:var(--text-secondary); }

  /* Responsive */
  @media (max-width:640px) {
    .hero             { padding:48px 0 32px; }
    .summary-card     { padding:32px 24px; }
    .capsule-grid     { grid-template-columns:repeat(2, 1fr); }
    .capsule-detail   { padding:28px 20px; }
    .quote-card       { padding:28px 20px 24px; }
    .paradox-detail-item { grid-template-columns:40px 1fr; gap:10px; padding:12px 14px; }
    .paradox-detail-item .pd-tag { display:none; }
    .judge-grid       { grid-template-columns:1fr; }
  }
"""

HTML_PAGE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} - 视频解析报告</title>
<style>{css}</style>
</head>
<body>
<div class="container">

<header class="hero">
  <div class="hero-badge"><span class="dot"></span>抖音 - 视频解析</div>
  <h1>{title}</h1>
  {hero_meta}
</header>

<div class="summary-card">
  <div class="label">一句话总结</div>
  <div class="big-text">{summary_body}</div>
</div>

<section class="quotes-section">
  <div class="section-head"><div class="icon">&#10022;</div><h2>金句卡片 - 适合分享</h2></div>
  <div class="quotes-grid">{quote_cards}</div>
</section>

<section class="bookshelf-section">
  <div class="section-head"><div class="icon" style="font-size:18px;">&#128218;</div><h2>深度解析：点击查看详情</h2></div>
  <div class="capsule-grid">
    <div class="capsule" data-cid="points">
      <span class="cap-icon">&#128161;</span>
      <div class="cap-title">{point_count}个核心观点</div>
      <div class="cap-sub">{point_sub}</div>
    </div>
    <div class="capsule" data-cid="structure">
      <span class="cap-icon">&#128196;</span>
      <div class="cap-title">视频结构拆解</div>
      <div class="cap-sub">{struct_type}</div>
    </div>
    <div class="capsule" data-cid="judgment">
      <span class="cap-icon">&#128270;</span>
      <div class="cap-title">内容判断</div>
      <div class="cap-sub">{judge_sub}</div>
    </div>
    <div class="capsule" data-cid="highlight">
      <span class="cap-icon">&#129352;</span>
      <div class="cap-title">内容亮点</div>
      <div class="cap-sub">{highlight_sub}</div>
    </div>
  </div>

  <div class="capsule-detail" id="detail-points">
    <button class="close-btn" data-action="close">&#10005;</button>
    <div class="detail-title">{point_count}个核心观点</div>
    <div class="points-list">{point_items}</div>
  </div>

  <div class="capsule-detail" id="detail-structure">
    <button class="close-btn" data-action="close">&#10005;</button>
    <div class="detail-title">视频结构拆解</div>
    <div class="struct-list">{struct_items}</div>
  </div>

  <div class="capsule-detail" id="detail-judgment">
    <button class="close-btn" data-action="close">&#10005;</button>
    <div class="detail-title">内容判断</div>
    <div class="judge-grid">{judge_cards}</div>
  </div>

  <div class="capsule-detail" id="detail-highlight">
    <button class="close-btn" data-action="close">&#10005;</button>
    <div class="detail-title">内容亮点</div>
    <div class="paradox-detail-list">{highlight_items}</div>
  </div>
</section>

<div class="footer">
  <p class="brand">douyin-video-parser</p>
  <p>丢个抖音链接，还你一份结构化分析 &middot; {date}</p>
</div>

</div>

<script>
(function(){{
  var active=null;
  document.addEventListener('click', function(e){{
    var cap = e.target.closest('[data-cid]');
    if (cap) {{
      var id = cap.getAttribute('data-cid');
      if(active) active.classList.remove('active');
      var d = document.getElementById('detail-' + id);
      if (d) {{ d.classList.add('active'); d.scrollIntoView({{behavior:'smooth',block:'nearest'}}); active = d; }}
      return;
    }}
    if (e.target.closest('[data-action="close"]')) {{
      if (active) {{ active.classList.remove('active'); active = null; }}
    }}
  }});
}})();
</script>

</body>
</html>"""


def generate_html(title: str, duration_sec, plain_text: str,
                  timed_text: str, analysis: dict) -> str:
    """生成 HTML 报告（所有用户内容均经 html.escape 转义）"""
    a = analysis or {}

    # Hero meta
    meta_parts = []
    if duration_sec:
        meta_parts.append(f"<span>时长 {_esc(_format_duration(duration_sec))}</span>")
    meta_parts.append("<span>抖音</span>")
    hero_meta = f'<div class="hero-meta">{"".join(meta_parts)}</div>' if meta_parts else ""

    # 一句话总结
    summary = a.get("summary", title)
    summary_esc = _esc(summary)
    # 给【关键词】加 em 强调
    summary_body = re.sub(
        r'【(.+?)】', r'<em>\1</em>', summary_esc
    )
    if "[" not in summary_esc and len(summary) > 15:
        words = summary[:15]
        summary_body = summary_esc.replace(_esc(words), f"<em>{_esc(words)}</em>", 1)

    # 金句
    share_tags = ["朋友圈金句", "情感共鸣", "引人深思", "社交媒体", "职场共鸣", "人生感悟"]
    quotes = a.get("quotes", [])[:3]
    quote_cards = ""
    for i, q in enumerate(quotes):
        tag = share_tags[i % len(share_tags)]
        qtext = q.get("text", q) if isinstance(q, dict) else q
        quote_cards += f"""<div class="quote-card">
  <div class="quote-mark">&ldquo;</div>
  <div class="quote-text">{_esc(qtext)}</div>
  <span class="share-tag">{_esc(tag)}</span>
</div>"""
    if not quote_cards:
        quote_cards = '<p style="color:var(--text-muted);font-size:14px;">暂无金句数据</p>'

    # 核心观点
    points = a.get("key_points", [])
    point_items = ""
    point_sub = ""
    for i, p in enumerate(points):
        if isinstance(p, dict):
            point_items += f"""<div class="point-item">
  <div class="point-num">{i+1:02d}</div>
  <div class="point-content">
    <h4>{_esc(p.get('title',''))}</h4>
    <p>{_esc(p.get('desc',''))}</p>
  </div>
</div>"""
            if i < 2:
                point_sub += (", " if point_sub else "") + _esc(p.get("title", ""))[:10]
            elif i == 2:
                point_sub += "..."
        else:
            point_items += f"""<div class="point-item">
  <div class="point-num">{i+1:02d}</div>
  <div class="point-content"><h4>{_esc(p)}</h4></div>
</div>"""
            if i < 2:
                point_sub += (", " if point_sub else "") + _esc(p[:10])
            elif i == 2:
                point_sub += "..."

    point_count = len(points)
    if not point_sub:
        point_sub = "点击查看详情"

    # 结构拆解
    st = a.get("structure", {}) or {}
    struct_type = _esc(st.get("type", "分段解读"))
    bd = st.get("breakdown", {})
    struct_items = ""
    if bd:
        for k, v in bd.items():
            struct_items += f"""<div class="struct-item">
  <span class="struct-label">{_esc(k)}</span>
  <span class="struct-content">{_esc(v)}</span>
</div>"""
    else:
        struct_items = '<p style="color:var(--text-muted);font-size:14px;">暂无结构拆解数据</p>'

    # 内容判断
    j = a.get("judgment", {}) or {}
    judge_cards = ""
    jmap = [
        ("立场", "stance"),
        ("可信度", "credibility"),
        ("可借鉴", "takeaway"),
    ]
    for label, key in jmap:
        val = j.get(key, "-")
        val_esc = _esc(val)
        if isinstance(val, str) and "-" not in val and len(val) < 60:
            judge_cards += f"""<div class="judge-mini">
  <div class="jm-label">{_esc(label)}</div>
  <div class="jm-title">{val_esc if len(val)<30 else val_esc[:27]+"..."}</div>
</div>"""
        else:
            title_part = val_esc[:24] + "..." if len(val) > 24 else val_esc
            judge_cards += f"""<div class="judge-mini">
  <div class="jm-label">{_esc(label)}</div>
  <div class="jm-title">{title_part}</div>
  <div class="jm-desc">{val_esc}</div>
</div>"""

    judge_sub = _esc(j.get("stance", "-")) + " - " + _esc(j.get("credibility", "-"))

    # 内容亮点
    highlights = a.get("highlights", [])
    if not highlights:
        for i, p in enumerate(points[:5]):
            text = p if isinstance(p, str) else p.get("title", "")
            highlights.append({"name": text, "desc": "", "tag": f"观点{i+1:02d}"})
    highlight_items = ""
    highlight_sub = ""
    for i, h in enumerate(highlights):
        if isinstance(h, dict):
            name = _esc(h.get("name", ""))
            desc = _esc(h.get("desc", ""))
            tag = _esc(h.get("tag", ""))
            top3_class = " top3" if i < 3 else ""
            highlight_items += f"""<div class="paradox-detail-item">
  <div class="pd-rank{top3_class}">{i+1:02d}</div>
  <div>
    <div class="pd-name">{name}</div>
    <div class="pd-desc">{desc}</div>
  </div>
  <span class="pd-tag">{tag}</span>
</div>"""
            if i < 2:
                highlight_sub += (", " if highlight_sub else "") + name[:8]
            elif i == 2:
                highlight_sub += "..."
    if not highlight_items:
        highlight_items = '<p style="color:var(--text-muted);font-size:14px;">暂无数据</p>'
    if not highlight_sub:
        highlight_sub = "点击查看详情"

    return HTML_PAGE.format(
        title=_esc(title),
        hero_meta=hero_meta,
        summary_body=summary_body,
        quote_cards=quote_cards,
        point_count=point_count, point_sub=_esc(point_sub), point_items=point_items,
        struct_type=struct_type, struct_items=struct_items,
        judge_sub=_esc(judge_sub), judge_cards=judge_cards,
        highlight_sub=_esc(highlight_sub), highlight_items=highlight_items,
        css=HTML_CSS,
        date=dt.datetime.now().strftime("%Y-%m-%d"),
    )


# ═══════════════════════════════════════════════════════════
# 5. 主入口
# ═══════════════════════════════════════════════════════════

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
    parser = argparse.ArgumentParser(description="抖音视频 -> 字幕稿 + HTML 报告（本地 whisper）")
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
    parser.add_argument("--generate-html", action="store_true", default=True,
                        help="生成 HTML 报告（默认开启）")
    parser.add_argument("--no-html", action="store_true",
                        help="不生成 HTML 报告（仅输出 txt）")
    args = parser.parse_args()

    # 默认输出目录：脚本同级目录下的 work/
    if args.out_dir is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        args.out_dir = os.path.join(script_dir, "work")

    t0 = time.time()
    video_id = extract_video_id(args.url)
    print(f"[0/4] video_id = {video_id}")

    # 获取视频标题
    title = fetch_video_title(video_id)
    print(f"      title: {title}")

    mp4_url = fetch_mp4_url(video_id)
    print(f"      mp4 url: {mp4_url[:80]}...")

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

    # 生成 HTML 报告
    if not args.no_html:
        print(f"\n[html] 生成报告...")
        with open(plain, "r", encoding="utf-8") as f:
            transcript_text = f.read()

        analysis = local_analysis(title, transcript_text)

        html_content = generate_html(
            title=title,
            duration_sec=info.duration if info else None,
            plain_text=transcript_text,
            timed_text=None,
            analysis=analysis,
        )

        date_prefix = dt.datetime.now().strftime("%m%d")
        label = f"{args.tag}-" if args.tag else ""
        html_path = os.path.join(args.out_dir, f"{date_prefix}-{label}{video_id}-报告.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"  HTML:   {html_path}")

    # 额外输出连贯稿内容，方便 AI 直接读取做后处理
    print(f"\n---连贯稿内容---")
    with open(plain, "r", encoding="utf-8") as f:
        print(f.read())
    print(f"---连贯稿结束---")


if __name__ == "__main__":
    main()
