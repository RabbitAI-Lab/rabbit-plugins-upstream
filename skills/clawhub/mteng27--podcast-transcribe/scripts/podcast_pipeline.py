#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
播客自动化流水线 —— 下载 + 语音转文字 (通用版)
=========================================================================
支持任意播客 RSS Feed，自动下载音频并通过 AuralWise API 转写为文字。

完整流程：
  Phase 1  解析 RSS Feed，获取全部单集信息（标题、音频直链、Show Notes）
  Phase 2  逐集处理：
           a) 下载音频到本地（断点续传，已存在则跳过）
           b) 提交音频 URL 到 AuralWise API 进行语音转写
           c) 轮询任务状态直到完成
           d) 保存文字稿：.txt（纯文本）/ .md（带时间戳）/ .srt（字幕）
           e) 保存 Show Notes 为 Markdown
           f) 更新进度状态文件
  Phase 3  生成汇总报告

特性：
  - 断点续传：state.json 记录每集状态，中断后可恢复
  - 测试模式：--test N 按音频大小排序取最小 N 集
  - 直接 URL 转写：AuralWise 直接抓取音频 URL，无需先下载再上传
  - 余额不足自动跳过转写，继续下载剩余音频

使用方式：
  # 基本用法（RSS + API Key）
  python3 podcast_pipeline.py --rss-url "https://example.com/feed.xml" --api-key "asr_xxx"

  # 指定播客名称和输出目录
  python3 podcast_pipeline.py --rss-url "..." --podcast-name "我的播客" --output-dir ~/Desktop/播客合集

  # 测试模式（处理最小的 2 集）
  python3 podcast_pipeline.py --rss-url "..." --api-key "asr_xxx" --test 2

  # 仅下载音频
  python3 podcast_pipeline.py --rss-url "..." --download-only

  # 仅转写（已有音频文件）
  python3 podcast_pipeline.py --rss-url "..." --transcribe-only

  # 从 .env 文件读取 API Key
  python3 podcast_pipeline.py --rss-url "..." --env-file .env

转写服务：AuralWise API (https://auralwise.cn)
  - 优化档（中文）：0.27元/小时
  - 标准档：0.6元/小时
  - 说话人分离：+0.2元/小时
=========================================================================
"""

import os
import re
import sys
import json
import time
import logging
import argparse
import traceback
import requests
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
from html import unescape

# =====================================================================
#  工具函数
# =====================================================================

def sanitize_filename(name: str, max_len: int = 80) -> str:
    """清理文件名中的非法字符"""
    name = re.sub(r'[<>:"/\\|?*\u3000]', "", name)
    name = re.sub(r"[\U0001F000-\U0001FFFF\u2600-\u27BF]", "", name)
    name = re.sub(r'[\u300a\u300b\u3001\u3002\uff08\uff09\uff1a\uff1b\uff0c\uff01\uff1f]', "", name)
    name = re.sub(r"[…—–·•~`'\"{}^#%&=+@]", "", name)
    name = re.sub(r"\s+", " ", name).strip()
    if len(name) > max_len:
        name = name[:max_len].strip()
    return name if name else "untitled"


def extract_ep_number(title: str) -> str:
    """从标题中提取集数编号"""
    m = re.search(r"EP\s*\.?\s*(\d+)", title, re.IGNORECASE)
    return m.group(1) if m else ""


def make_filename(ep_num: str, title: str, ext: str) -> str:
    """生成标准文件名"""
    clean_title = re.sub(r"^EP\s*\.?\s*\d+\s*", "", title, flags=re.IGNORECASE)
    clean_title = sanitize_filename(clean_title)
    ep_prefix = f"EP{ep_num}" if ep_num else "EP"
    return f"{ep_prefix}-{clean_title}.{ext}"


def html_to_markdown(html_str: str) -> str:
    """简单 HTML 转 Markdown"""
    if not html_str:
        return ""
    text = re.sub(r"<br\s*/?>", "\n", html_str)
    text = re.sub(r"</?p[^>]*>", "\n", text)
    text = re.sub(r"</?span[^>]*>", "", text)
    text = re.sub(r"</?div[^>]*>", "\n", text)
    text = re.sub(r"<img[^>]*/?>", "", text)
    text = re.sub(r"<a[^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>", r"\2 (\1)", text)
    text = re.sub(r"<[^>]+>", "", text)
    return unescape(text).strip()


def format_timestamp(seconds: float) -> str:
    """秒数转 HH:MM:SS 或 MM:SS"""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    if h > 0:
        return f"{h:d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"


def format_srt_timestamp(seconds: float) -> str:
    """秒数转 SRT 时间戳 HH:MM:SS,mmm"""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds % 1) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def load_env_file(env_path: str) -> dict:
    """从 .env 文件加载环境变量"""
    env = {}
    p = Path(env_path)
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, val = line.partition("=")
                env[key.strip()] = val.strip()
    return env


# =====================================================================
#  状态管理（断点续传）
# =====================================================================

class StateManager:
    """管理流水线进度状态，支持断点续传"""

    def __init__(self, state_file: Path):
        self.state_file = state_file
        self.state = self._load()

    def _load(self) -> dict:
        if self.state_file.exists():
            try:
                return json.loads(self.state_file.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, Exception):
                pass
        return {"episodes": {}, "last_updated": "", "total_episodes": 0}

    def save(self):
        self.state["last_updated"] = datetime.now().isoformat()
        self.state_file.write_text(
            json.dumps(self.state, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    def get_episode(self, ep_key: str) -> dict:
        return self.state["episodes"].get(ep_key, {
            "download_status": "pending",
            "transcribe_status": "pending",
            "transcript_files": [],
            "auralwise_task_id": "",
            "error": "",
        })

    def update_episode(self, ep_key: str, updates: dict):
        ep = self.get_episode(ep_key)
        ep.update(updates)
        self.state["episodes"][ep_key] = ep
        self.save()

    def is_episode_done(self, ep_key: str) -> bool:
        ep = self.get_episode(ep_key)
        return ep.get("transcribe_status") == "done"

    def get_stats(self) -> dict:
        eps = self.state["episodes"]
        total = len(eps)
        dl_ok = sum(1 for e in eps.values() if e.get("download_status") == "done")
        tr_ok = sum(1 for e in eps.values() if e.get("transcribe_status") == "done")
        tr_fail = sum(1 for e in eps.values() if e.get("transcribe_status") == "failed")
        return {
            "total": total,
            "downloaded": dl_ok,
            "transcribed": tr_ok,
            "transcribe_failed": tr_fail,
            "pending": total - dl_ok - tr_fail,
        }


# =====================================================================
#  Phase 1: RSS Feed 解析
# =====================================================================

def parse_rss_feed(rss_url: str, ua: str) -> list:
    """解析 RSS Feed，返回全部单集信息"""
    logging.info("=" * 60)
    logging.info("Phase 1: 解析 RSS Feed")
    logging.info("=" * 60)

    episodes = []
    try:
        resp = requests.get(rss_url, headers={"User-Agent": ua}, timeout=30)
        if resp.status_code != 200:
            logging.error(f"RSS 请求失败: HTTP {resp.status_code}")
            return []

        root = ET.fromstring(resp.text)
        channel = root.find("channel")
        if channel is None:
            return []

        items = channel.findall("item")
        logging.info(f"RSS Feed 共 {len(items)} 条")

        for i, item in enumerate(items):
            title = item.findtext("title", "").strip()
            pub_date = item.findtext("pubDate", "")
            ep_num = extract_ep_number(title)

            enclosure = item.find("enclosure")
            audio_url = ""
            audio_size = 0
            if enclosure is not None:
                audio_url = enclosure.get("url", "")
                try:
                    audio_size = int(enclosure.get("length", 0))
                except (ValueError, TypeError):
                    audio_size = 0

            description = item.findtext("description", "") or ""
            source_link = item.findtext("link", "") or ""

            episodes.append({
                "idx": i,
                "ep_num": ep_num,
                "title": title,
                "pub_date": pub_date,
                "audio_url": audio_url,
                "audio_size_mb": round(audio_size / (1024 * 1024), 1) if audio_size else 0,
                "shownotes_md": html_to_markdown(description),
                "source_link": source_link,
            })

        total_size = sum(e["audio_size_mb"] for e in episodes)
        logging.info(f"解析完成: {len(episodes)} 集, 总大小 {total_size:.0f} MB ({total_size/1024:.1f} GB)")

    except Exception as e:
        logging.error(f"RSS 解析异常: {e}")
        logging.error(traceback.format_exc())

    return episodes


# =====================================================================
#  Phase 2a: 音频下载
# =====================================================================

def download_audio(audio_url: str, filepath: Path, ep_label: str = "",
                   ua: str = "", referer: str = "", max_retries: int = 3,
                   delay: int = 2, timeout: int = 600) -> bool:
    """流式下载音频，支持断点续传"""
    if filepath.exists() and filepath.stat().st_size > 1024 * 100:
        size_mb = filepath.stat().st_size / (1024 * 1024)
        logging.info(f"  [{ep_label}] 音频已存在 ({size_mb:.1f}MB)，跳过")
        return True

    if not audio_url:
        logging.warning(f"  [{ep_label}] 无音频直链")
        return False

    chunk_size = 1024 * 256  # 256KB
    for attempt in range(1, max_retries + 1):
        try:
            logging.info(f"  [{ep_label}] 下载中 (尝试 {attempt}/{max_retries})...")
            headers = {"User-Agent": ua}
            if referer:
                headers["Referer"] = referer
            resp = requests.get(audio_url, headers=headers, stream=True, timeout=timeout)
            if resp.status_code != 200:
                logging.warning(f"  [{ep_label}] HTTP {resp.status_code}")
                if attempt < max_retries:
                    time.sleep(delay * attempt)
                    continue
                return False

            total_size = int(resp.headers.get("content-length", 0))
            downloaded = 0
            start_time = time.time()

            with open(filepath, "wb") as f:
                for chunk in resp.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if downloaded % (50 * 1024 * 1024) < chunk_size:
                            pct = (downloaded / total_size * 100) if total_size else 0
                            elapsed = time.time() - start_time
                            speed = downloaded / elapsed / 1024 / 1024 if elapsed > 0 else 0
                            logging.info(
                                f"  [{ep_label}] {downloaded/1024/1024:.0f}MB / "
                                f"{total_size/1024/1024:.0f}MB ({pct:.0f}%) {speed:.1f}MB/s"
                            )

            elapsed = time.time() - start_time
            final_size = filepath.stat().st_size
            logging.info(f"  [{ep_label}] 下载完成: {final_size/1024/1024:.1f}MB, {elapsed:.0f}秒")
            return True

        except requests.Timeout:
            logging.warning(f"  [{ep_label}] 下载超时")
            if attempt < max_retries:
                time.sleep(delay * attempt)
                continue
            return False
        except Exception as e:
            logging.error(f"  [{ep_label}] 下载异常: {e}")
            if attempt < max_retries:
                time.sleep(delay * attempt)
                continue
            return False
    return False


# =====================================================================
#  Phase 2b: AuralWise 语音转写
# =====================================================================

class AuralWiseTranscriber:
    """AuralWise API 客户端"""

    BASE_URL = "https://api.auralwise.cn/v1"

    # 默认转写选项（播客单人主讲场景）
    DEFAULT_OPTIONS = {
        "enable_asr": True,
        "enable_diarize": False,
        "enable_audio_events": False,
        "optimize": True,
        "asr_language": "zh",
        "timestamp_level": "segment",
    }

    def __init__(self, api_key: str, options: dict = None):
        self.api_key = api_key
        self.headers = {
            "X-API-Key": api_key,
            "Content-Type": "application/json",
        }
        self.options = options or self.DEFAULT_OPTIONS

    def check_balance(self) -> dict:
        """查询账户余额和并发信息"""
        try:
            resp = requests.get(f"{self.BASE_URL}/account", headers=self.headers, timeout=10)
            if resp.status_code == 200:
                return resp.json()
            logging.warning(f"账户查询失败: HTTP {resp.status_code}")
            return {}
        except Exception as e:
            logging.warning(f"账户查询异常: {e}")
            return {}

    def submit_task(self, audio_url: str, audio_filename: str = "",
                    max_retries: int = 3, delay: int = 2) -> str:
        """
        提交转写任务。
        返回 task_id，失败返回空字符串，余额不足返回 "INSUFFICIENT_BALANCE"。
        """
        payload = {
            "audio_url": audio_url,
            "audio_filename": audio_filename,
            "options": self.options,
        }

        for attempt in range(1, max_retries + 1):
            try:
                resp = requests.post(
                    f"{self.BASE_URL}/tasks",
                    headers=self.headers,
                    json=payload,
                    timeout=30,
                )
                if resp.status_code == 201:
                    data = resp.json()
                    task_id = data.get("id", "")
                    logging.info(f"  转写任务已提交: {task_id}")
                    return task_id
                elif resp.status_code == 402:
                    logging.error("  余额不足！请充值后重新运行（已下载的音频不会重复下载）")
                    return "INSUFFICIENT_BALANCE"
                elif resp.status_code == 429:
                    retry_after = int(resp.headers.get("Retry-After", 10))
                    logging.warning(f"  限速，等待 {retry_after} 秒...")
                    time.sleep(retry_after)
                    continue
                else:
                    error_msg = resp.text[:200]
                    logging.error(f"  提交失败: HTTP {resp.status_code} - {error_msg}")
                    if attempt < max_retries:
                        time.sleep(delay * attempt)
                        continue
                    return ""
            except Exception as e:
                logging.error(f"  提交异常: {e}")
                if attempt < max_retries:
                    time.sleep(delay * attempt)
                    continue
                return ""
        return ""

    def poll_task(self, task_id: str, ep_label: str = "",
                  poll_interval: int = 5, max_wait: int = 1800) -> str:
        """
        轮询任务状态直到完成或超时。
        返回: "done" / "failed" / "abandoned" / "timeout"
        """
        start_time = time.time()
        while True:
            elapsed = time.time() - start_time
            if elapsed > max_wait:
                logging.warning(f"  [{ep_label}] 轮询超时 ({max_wait}秒)")
                return "timeout"

            try:
                resp = requests.get(
                    f"{self.BASE_URL}/tasks/{task_id}",
                    headers=self.headers,
                    timeout=10,
                )
                if resp.status_code == 200:
                    data = resp.json()
                    status = data.get("status", "")
                    if status == "done":
                        logging.info(f"  [{ep_label}] 转写完成 (耗时 {elapsed:.0f}秒)")
                        return "done"
                    elif status in ("failed", "abandoned"):
                        logging.error(f"  [{ep_label}] 转写失败: {status}")
                        return status
                    mins = int(elapsed // 60)
                    secs = int(elapsed % 60)
                    logging.info(f"  [{ep_label}] 转写中... ({mins}分{secs}秒)")
                elif resp.status_code == 429:
                    retry_after = int(resp.headers.get("Retry-After", 5))
                    time.sleep(retry_after)
                    continue
            except Exception as e:
                logging.warning(f"  [{ep_label}] 轮询异常: {e}")

            time.sleep(poll_interval)

    def get_result(self, task_id: str) -> dict:
        """获取转写结果"""
        try:
            resp = requests.get(
                f"{self.BASE_URL}/tasks/{task_id}/result",
                headers=self.headers,
                timeout=30,
            )
            if resp.status_code == 200:
                return resp.json()
            logging.error(f"获取结果失败: HTTP {resp.status_code}")
            return {}
        except Exception as e:
            logging.error(f"获取结果异常: {e}")
            return {}


# =====================================================================
#  Phase 2c: 转写结果保存
# =====================================================================

def save_transcript_txt(result: dict, filepath: Path):
    """保存纯文本文字稿"""
    segments = result.get("segments", [])
    lines = [seg.get("text", "").strip() for seg in segments if seg.get("text", "").strip()]
    filepath.write_text("\n".join(lines), encoding="utf-8")


def save_transcript_md(result: dict, filepath: Path, episode_info: dict):
    """保存 Markdown 格式文字稿（带时间戳和元信息）"""
    segments = result.get("segments", [])
    duration = result.get("audio_duration", 0)
    language = result.get("language", "")
    lang_prob = result.get("language_probability", 0)
    dur_str = format_timestamp(duration) if duration else "未知"

    lines = [
        f"# {episode_info.get('title', '')}",
        "",
        "## 文字稿",
        "",
        f"> 转写服务: AuralWise (优化档)",
        f"> 音频时长: {dur_str}",
        f"> 检测语言: {language} (置信度 {lang_prob:.0%})",
        f"> 转写时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "---",
        "",
    ]

    for seg in segments:
        text = seg.get("text", "").strip()
        if not text:
            continue
        start = seg.get("start", 0)
        speaker = seg.get("speaker", "")
        ts = format_timestamp(start)
        if speaker:
            lines.append(f"**[{ts}] {speaker}:** {text}")
        else:
            lines.append(f"**[{ts}]** {text}")
        lines.append("")

    filepath.write_text("\n".join(lines), encoding="utf-8")


def save_transcript_srt(result: dict, filepath: Path):
    """保存 SRT 字幕格式"""
    segments = result.get("segments", [])
    lines = []
    for i, seg in enumerate(segments, 1):
        text = seg.get("text", "").strip()
        if not text:
            continue
        start = seg.get("start", 0)
        end = seg.get("end", 0)
        lines.append(str(i))
        lines.append(f"{format_srt_timestamp(start)} --> {format_srt_timestamp(end)}")
        lines.append(text)
        lines.append("")

    filepath.write_text("\n".join(lines), encoding="utf-8")


def save_shownotes(ep: dict, filepath: Path):
    """保存 Show Notes 为 Markdown"""
    ep_num = ep.get("ep_num", "")
    title = ep.get("title", "")
    shownotes = ep.get("shownotes_md", "无")

    md = f"""# {title}

## 基本信息

| 字段 | 内容 |
|------|------|
| 期号 | EP{ep_num} |
| 发布日期 | {ep.get('pub_date', '')} |
| 音频大小 | {ep.get('audio_size_mb', 0)} MB |
| 来源链接 | {ep.get('source_link', '')} |

---

## Show Notes

{shownotes}

---

> 自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    filepath.write_text(md, encoding="utf-8")


# =====================================================================
#  主流水线
# =====================================================================

def run_pipeline(
    episodes: list,
    state: StateManager,
    output_dir: Path,
    audio_dir: Path,
    notes_dir: Path,
    transcript_dir: Path,
    transcriber: AuralWiseTranscriber = None,
    download_only: bool = False,
    transcribe_only: bool = False,
    ua: str = "",
    referer: str = "",
):
    """执行主流水线"""
    total = len(episodes)
    logging.info("=" * 60)
    logging.info(f"Phase 2: 逐集处理 ({total} 集)")
    logging.info("=" * 60)

    if not download_only and transcriber:
        account = transcriber.check_balance()
        if account:
            balance = account.get("balance", 0)
            concurrency = account.get("available_concurrency", 0)
            logging.info(f"  AuralWise 账户: 余额 {balance} 元, 可用并发 {concurrency}")
            if balance < 5:
                logging.warning("  余额较低，可能无法完成全部转写")

    balance_depleted = False

    for idx, ep in enumerate(episodes, 1):
        ep_num = ep.get("ep_num", "")
        title = ep.get("title", "")
        ep_label = f"EP{ep_num}" if ep_num else f"#{idx}"
        ep_key = f"ep{ep_num}" if ep_num else f"item{idx}"

        logging.info(f"\n{'='*60}")
        logging.info(f"  [{idx}/{total}] {ep_label} - {title[:50]}")
        logging.info(f"{'='*60}")

        audio_filename = make_filename(ep_num, title, "m4a")
        notes_filename = make_filename(ep_num, title, "md")
        txt_filename = make_filename(ep_num, title, "txt")
        md_filename = make_filename(ep_num, title, "md")
        srt_filename = make_filename(ep_num, title, "srt")

        audio_filepath = audio_dir / audio_filename
        notes_filepath = notes_dir / notes_filename
        txt_filepath = transcript_dir / txt_filename
        md_filepath = transcript_dir / f"带时间戳_{md_filename}"
        srt_filepath = transcript_dir / srt_filename

        ep_state = state.get_episode(ep_key)

        # ---- Step 1: 下载音频 ----
        if not transcribe_only:
            if ep_state.get("download_status") == "done" and audio_filepath.exists():
                logging.info(f"  [{ep_label}] 音频已下载，跳过")
            else:
                audio_url = ep.get("audio_url", "")
                audio_ok = download_audio(audio_url, audio_filepath, ep_label, ua, referer)
                state.update_episode(ep_key, {
                    "download_status": "done" if audio_ok else "failed",
                    "audio_file": str(audio_filepath) if audio_ok else "",
                    "audio_size_mb": audio_filepath.stat().st_size / (1024*1024) if audio_filepath.exists() else 0,
                })
                if not audio_ok:
                    logging.error(f"  [{ep_label}] 音频下载失败，跳过转写")
                    continue

        # ---- Step 2: 保存 Show Notes ----
        save_shownotes(ep, notes_filepath)
        logging.info(f"  [{ep_label}] Show Notes 已保存")

        if download_only:
            continue

        # 余额已耗尽，跳过转写但继续下载
        if balance_depleted:
            logging.info(f"  [{ep_label}] 余额不足，跳过转写")
            continue

        # ---- Step 3: 提交 AuralWise 转写 ----
        if ep_state.get("transcribe_status") == "done":
            logging.info(f"  [{ep_label}] 转写已完成，跳过")
            continue

        audio_url = ep.get("audio_url", "")
        if not audio_url:
            logging.warning(f"  [{ep_label}] 无音频 URL，跳过转写")
            state.update_episode(ep_key, {"transcribe_status": "failed", "error": "no audio url"})
            continue

        task_id = transcriber.submit_task(audio_url, audio_filename)
        if task_id == "INSUFFICIENT_BALANCE":
            balance_depleted = True
            state.update_episode(ep_key, {"transcribe_status": "pending", "error": "insufficient balance"})
            continue
        if not task_id:
            state.update_episode(ep_key, {"transcribe_status": "failed", "error": "submit failed"})
            continue

        state.update_episode(ep_key, {"auralwise_task_id": task_id, "transcribe_status": "processing"})

        result_status = transcriber.poll_task(task_id, ep_label)
        if result_status != "done":
            state.update_episode(ep_key, {
                "transcribe_status": "failed" if result_status in ("failed", "abandoned") else "timeout",
                "error": f"poll returned {result_status}",
            })
            continue

        result = transcriber.get_result(task_id)
        if not result:
            state.update_episode(ep_key, {"transcribe_status": "failed", "error": "no result"})
            continue

        # ---- Step 4: 保存文字稿 ----
        transcript_files = []
        save_transcript_txt(result, txt_filepath)
        transcript_files.append(str(txt_filepath))
        logging.info(f"  [{ep_label}] 纯文本已保存: {txt_filepath.name}")

        save_transcript_md(result, md_filepath, ep)
        transcript_files.append(str(md_filepath))
        logging.info(f"  [{ep_label}] Markdown已保存: {md_filepath.name}")

        save_transcript_srt(result, srt_filepath)
        transcript_files.append(str(srt_filepath))
        logging.info(f"  [{ep_label}] SRT字幕已保存: {srt_filepath.name}")

        billing = result.get("billing", {})
        if billing:
            logging.info(
                f"  [{ep_label}] 计费: {billing.get('billable_minutes', 0)}分钟, "
                f"扣费 {billing.get('amount', 0)}元, 余额 {billing.get('balance', 0)}元"
            )

        state.update_episode(ep_key, {
            "transcribe_status": "done",
            "transcript_files": transcript_files,
            "audio_duration": result.get("audio_duration", 0),
            "language": result.get("language", ""),
            "billing_amount": billing.get("amount", 0),
            "billing_minutes": billing.get("billable_minutes", 0),
        })

    # ---- Phase 3: 汇总 ----
    stats = state.get_stats()
    logging.info("")
    logging.info("=" * 60)
    logging.info("  流水线执行完成！")
    logging.info("=" * 60)
    logging.info(f"  总集数:       {total}")
    logging.info(f"  音频已下载:   {stats['downloaded']}")
    logging.info(f"  转写已完成:   {stats['transcribed']}")
    logging.info(f"  转写失败:     {stats['transcribe_failed']}")
    logging.info(f"  待处理:       {stats['pending']}")
    logging.info(f"  音频目录:     {audio_dir}")
    logging.info(f"  文字稿目录:   {transcript_dir}")
    logging.info(f"  Show Notes:   {notes_dir}")
    logging.info("=" * 60)

    return stats


# =====================================================================
#  CLI 入口
# =====================================================================

def main():
    parser = argparse.ArgumentParser(
        description="播客自动化流水线：下载 + 语音转文字（通用版）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--rss-url", required=True, help="播客 RSS Feed URL")
    parser.add_argument("--podcast-name", default="播客", help="播客名称（用于输出目录命名）")
    parser.add_argument("--output-dir", default=None, help="输出根目录（默认: ~/Desktop/{播客名称}合集）")
    parser.add_argument("--api-key", default=None, help="AuralWise API Key（asr_ 开头）")
    parser.add_argument("--env-file", default=None, help="从 .env 文件读取 API Key")
    parser.add_argument("--test", type=int, metavar="N", help="测试模式：按音频大小排序处理最小 N 集")
    parser.add_argument("--download-only", action="store_true", help="仅下载音频，不做转写")
    parser.add_argument("--transcribe-only", action="store_true", help="仅转写（跳过下载）")
    parser.add_argument("--language", default="zh", help="转写语言（默认 zh）")
    parser.add_argument("--optimize", action="store_true", default=True, help="使用优化档（更便宜更准确）")
    parser.add_argument("--diarize", action="store_true", help="启用说话人分离（+0.2元/小时）")
    args = parser.parse_args()

    print()
    print("=" * 70)
    print(f"  播客自动化流水线 —— {args.podcast_name}")
    print("=" * 70)
    print()

    # 确定 API Key
    api_key = args.api_key
    if not api_key and args.env_file:
        env = load_env_file(args.env_file)
        api_key = env.get("AURALWISE_API_KEY", "")
    if not api_key:
        # 尝试从环境变量读取
        api_key = os.getenv("AURALWISE_API_KEY", "")

    # 确定输出目录
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = Path.home() / "Desktop" / f"{args.podcast_name}合集"

    audio_dir = output_dir / "音频"
    notes_dir = output_dir / "文稿"
    transcript_dir = output_dir / "文字稿"
    state_file = output_dir / "pipeline_state.json"
    log_file = output_dir / "pipeline.log"

    # 创建目录
    output_dir.mkdir(parents=True, exist_ok=True)
    audio_dir.mkdir(parents=True, exist_ok=True)
    notes_dir.mkdir(parents=True, exist_ok=True)
    transcript_dir.mkdir(parents=True, exist_ok=True)

    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(str(log_file), encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
        force=True,
    )

    UA = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

    # 检查 API Key
    if not args.download_only and not api_key:
        print("错误：未配置 AURALWISE_API_KEY！")
        print()
        print("请通过以下方式之一提供 API Key：")
        print("  1. --api-key asr_your_key")
        print("  2. --env-file .env  (文件内含 AURALWISE_API_KEY=asr_xxx)")
        print("  3. 设置环境变量 AURALWISE_API_KEY")
        print()
        print("获取 API Key: https://auralwise.cn/refid=asgbifle")
        print("使用 --download-only 可仅下载音频（不需要 API Key）")
        return

    # 初始化状态管理
    state = StateManager(state_file)

    # 初始化转写器
    transcriber = None
    if not args.download_only:
        options = {
            "enable_asr": True,
            "enable_diarize": args.diarize,
            "enable_audio_events": False,
            "optimize": args.optimize,
            "asr_language": args.language,
            "timestamp_level": "segment",
        }
        transcriber = AuralWiseTranscriber(api_key, options)

    # Phase 1: 解析 RSS
    episodes = parse_rss_feed(args.rss_url, UA)
    if not episodes:
        logging.error("RSS 解析失败，无法继续")
        return

    # 测试模式：按音频大小排序，优先处理最小的 N 集
    if args.test:
        sorted_eps = sorted(episodes, key=lambda e: e.get("audio_size_mb", 0))
        episodes = sorted_eps[:args.test]
        for e in episodes:
            logging.info(f"测试选中: EP{e.get('ep_num','?')} - {e['title'][:40]} ({e.get('audio_size_mb',0)}MB)")

    # 非测试模式：过滤非正式集，跳过已完成
    if not args.test:
        formal_episodes = [e for e in episodes if e["ep_num"]]
        if len(formal_episodes) < len(episodes):
            logging.info(f"过滤非正式内容: {len(episodes)} -> {len(formal_episodes)} 集")
            episodes = formal_episodes

        pending = []
        for ep in episodes:
            ep_key = f"ep{ep['ep_num']}" if ep["ep_num"] else f"item{ep['idx']}"
            if not state.is_episode_done(ep_key):
                pending.append(ep)
            else:
                logging.info(f"  跳过已完成的 EP{ep['ep_num']}")
        if len(pending) < len(episodes):
            logging.info(f"断点续传: {len(episodes)} 集中 {len(episodes)-len(pending)} 集已完成")
        episodes = pending

    if not episodes:
        logging.info("所有集数已处理完成，无需执行")
        return

    # 从 RSS URL 推断 referer
    referer = ""
    if "ximalaya.com" in args.rss_url:
        referer = "https://www.ximalaya.com/"
    elif "xiaoyuzhou" in args.rss_url:
        referer = "https://www.xiaoyuzhou.com/"

    # Phase 2: 执行流水线
    run_pipeline(
        episodes=episodes,
        state=state,
        output_dir=output_dir,
        audio_dir=audio_dir,
        notes_dir=notes_dir,
        transcript_dir=transcript_dir,
        transcriber=transcriber,
        download_only=args.download_only,
        transcribe_only=args.transcribe_only,
        ua=UA,
        referer=referer,
    )


if __name__ == "__main__":
    main()
