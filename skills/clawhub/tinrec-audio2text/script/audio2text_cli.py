#!/usr/bin/env python3
"""浏览 Tinrec 录音和文件夹，导入本地文件或网络媒体并转写。仅使用 Python 标准库。"""

from __future__ import annotations

import argparse
import http.client
import json
import os
import re
import shutil
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path

GLOBAL_BASE_URL = "https://api.tinrec.com/api"
CN_BASE_URL = "https://api.tinrec.cn/api"
REGIONAL_BASE_URLS = {"mt-cn-": CN_BASE_URL, "mt-global-": GLOBAL_BASE_URL}
COMMANDS = ("list-recordings", "list-folders", "detail", "transcript", "upload", "import-url")
MEDIA_EXTENSIONS = {
    ".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac", ".opus", ".mp4", ".webm", ".mov",
    ".mkv", ".m4s", ".flv",
}
MEDIA_TYPES = {
    "audio/aac": ".aac",
    "audio/flac": ".flac",
    "audio/mp4": ".m4a",
    "audio/mpeg": ".mp3",
    "audio/ogg": ".ogg",
    "audio/wav": ".wav",
    "audio/webm": ".webm",
    "audio/x-m4a": ".m4a",
    "audio/x-wav": ".wav",
    "video/mp4": ".mp4",
    "video/quicktime": ".mov",
    "video/webm": ".webm",
    "video/x-flv": ".flv",
}
NON_MEDIA_TYPES = {"application/json", "application/dash+xml", "application/vnd.apple.mpegurl", "application/x-mpegurl"}


def _print_json(data):
    print(json.dumps(data, ensure_ascii=False, indent=2))


class APIError(RuntimeError):
    def __init__(self, action, code, message):
        super().__init__(f"{action}失败：{message}")
        self.code = code
        self.message = message


def _request_data(base, headers, endpoint, action, *, query=None, body=None, timeout=30):
    url = f"{base}/{endpoint}"
    if query:
        url += "?" + urllib.parse.urlencode(query)
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers = {**headers, "Content-Type": "application/json"}
    request = urllib.request.Request(url, data=data, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            result = json.load(response)
    except urllib.error.HTTPError as exc:
        try:
            message = json.load(exc).get("message") or f"HTTP {exc.code}"
        except (ValueError, AttributeError, OSError):
            message = f"HTTP {exc.code}"
        raise APIError(action, exc.code, message) from exc
    except (OSError, ValueError, http.client.HTTPException) as exc:
        raise RuntimeError(f"{action}失败：{exc}") from exc
    if not isinstance(result, dict):
        raise RuntimeError(f"{action}失败：响应格式错误")
    if result.get("code") != 200:
        raise APIError(action, result.get("code"), result.get("message") or result.get("code"))
    data = result.get("data")
    if not isinstance(data, dict):
        raise RuntimeError(f"{action}失败：响应缺少数据")
    return data


def _put_file(url, path):
    try:
        with path.open("rb") as media:
            size = os.fstat(media.fileno()).st_size
            headers = {"Content-Type": "application/octet-stream", "Content-Length": str(size)}
            request = urllib.request.Request(url, data=media, headers=headers, method="PUT")
            with urllib.request.urlopen(request, timeout=120) as response:
                if response.status not in (200, 201):
                    raise RuntimeError(f"上传 TOS 失败：HTTP {response.status}")
    except (OSError, http.client.HTTPException) as exc:
        raise RuntimeError(f"上传 TOS 失败：{exc}") from exc


def _add_folder(values, folder_id):
    if folder_id is None:
        return
    if folder_id.startswith("fld_"):
        values["folder_public_id"] = folder_id
    else:
        values["folder_id"] = int(folder_id)


def _upload(base, headers, path, args, network_task_id=None):
    if not path.is_file():
        raise RuntimeError(f"文件不存在：{path}")
    filename = path.name
    suffix = path.suffix.lower()
    audio_format = suffix[1:] if suffix in MEDIA_EXTENSIONS else "mp3"
    # 兼容按文件名生成对象 Key 的旧接口，同时保留录音的原始文件名。
    storage_filename = f"{uuid.uuid4().hex}.{audio_format}"
    token = _request_data(
        base, headers, "tos/openclaw/upload-token", "获取上传凭证",
        query={"filename": storage_filename, "auto_generate_key": "true"},
    )
    signed_url, key = token.get("signed_url"), token.get("key")
    if not signed_url or not key:
        raise RuntimeError("上传凭证缺少 signed_url 或 key")
    _put_file(signed_url, path)

    body = {
        "oss_key": key,
        "format": audio_format,
        "filename": filename,
        "source": "upload",
        "duration": 0,
    }
    _add_folder(body, args.folder_id)
    if network_task_id is not None:
        body.update(source="network", network_task_id=network_task_id)
    result = _request_data(base, headers, "upload-v2", "提交转写", body=body)
    audio_id = result.get("id") or result.get("public_id")
    if audio_id is None:
        raise RuntimeError("提交转写响应缺少录音 ID")
    return audio_id


def _download_media(resolved, directory):
    audio_urls = resolved.get("audio_urls") or []
    video_urls = resolved.get("video_urls") or []
    platform = resolved.get("platform")
    # TikTok 的独立音频地址通常是配乐，转写视频应使用内嵌音轨。
    candidates = [(url, ".mp4") for url in video_urls]
    if platform != "tiktok":
        candidates[:0] = [(url, ".mp3") for url in audio_urls]

    title = re.sub(r"[\\/\x00-\x1f\x7f]+|\.{2,}", " ", resolved.get("title") or "").strip(" .")
    title = title.encode("utf-8")[:240].decode("utf-8", errors="ignore") or f"network-{resolved['network_task_id']}"
    headers = {"User-Agent": "Mozilla/5.0"}
    if platform == "bilibili":
        headers["Referer"] = "https://www.bilibili.com/"

    seen = set()
    for url, default_extension in candidates:
        if url in seen:
            continue
        seen.add(url)
        try:
            parsed = urllib.parse.urlsplit(url)
            if parsed.scheme not in ("http", "https") or not parsed.hostname:
                continue
            request = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(request, timeout=120) as response:
                content_type = response.headers.get_content_type()
                if response.status != 200 or content_type in NON_MEDIA_TYPES or content_type.startswith(("text/", "image/")):
                    continue
                start = response.read(512)
                if not start or start.lstrip().startswith((b"#EXTM3U", b"<", b"{")):
                    continue
                suffix = Path(urllib.parse.urlsplit(response.url).path).suffix.lower()
                # 音频 CDN 可能用无后缀 URL 或通用的 MP4 容器扩展名。
                extension = MEDIA_TYPES.get(content_type) or (suffix if suffix in MEDIA_EXTENSIONS else default_extension)
                path = directory / (title + extension)
                with path.open("wb") as media:
                    media.write(start)
                    shutil.copyfileobj(response, media)
                if response.length not in (None, 0):
                    continue
                return path
        except (OSError, ValueError, http.client.HTTPException):
            continue
    raise RuntimeError("下载网络媒体失败：解析结果没有可下载的完整音视频文件")


def _import_url(base, headers, args):
    resolved = _request_data(
        base, headers, "network-download/resolve", "解析网络链接",
        body={"share_url": args.share_url}, timeout=90,
    )
    network_task_id = resolved.get("network_task_id")
    if not network_task_id:
        raise RuntimeError("网络解析响应缺少 network_task_id")
    with tempfile.TemporaryDirectory(prefix="tinrec-media-") as directory:
        path = _download_media(resolved, Path(directory))
        return _upload(base, headers, path, args, network_task_id)


def _audio_endpoint(endpoint, audio_id):
    return f"{endpoint}/{urllib.parse.quote(str(audio_id), safe='')}"


def _wait_for_result(base, headers, audio_id, args):
    detail_path = _audio_endpoint("audio-detail", audio_id)
    deadline = time.monotonic() + args.timeout
    while (remaining := deadline - time.monotonic()) > 0:
        try:
            detail = _request_data(base, headers, detail_path, "获取录音详情", timeout=min(30, remaining))
        except RuntimeError:
            time.sleep(min(args.poll_interval, max(0, deadline - time.monotonic())))
            continue
        transcript_status = detail.get("transcript_status")
        if transcript_status in ("limit", "failed"):
            return _build_result(detail, None)
        if transcript_status == "success" and detail.get("task_status") == "success":
            transcript_data = None
            try:
                transcript_data = _request_data(
                    base, headers, _audio_endpoint("transcript", audio_id), "获取转写正文",
                )
            except RuntimeError:
                pass
            return _build_result(detail, transcript_data)
        time.sleep(min(args.poll_interval, max(0, deadline - time.monotonic())))
    raise RuntimeError(f"轮询超时（录音 ID：{audio_id}）")


def _read_api_key(args):
    key = (args.api_key or os.environ.get("TINREC_API_KEY") or "").strip()
    if key:
        return key
    path = Path(args.api_keys_file)
    if path.is_file():
        with path.open(encoding="utf-8") as key_file:
            for line in key_file:
                line = line.strip()
                if line and not line.startswith("#"):
                    return line
    raise RuntimeError(
        "未提供 API Key，请通过 --api-keys-file 或 --api-key 指定。"
        "创建地址为 https://tinrec.cn/api-keys 或 https://tinrec.com/api-keys"
    )


def _select_base_url(api_key, headers, override):
    if override:
        return override.rstrip("/")
    for prefix, base in REGIONAL_BASE_URLS.items():
        if api_key.startswith(prefix):
            return base
    if not re.fullmatch(r"mt-[a-f0-9]{64}", api_key):
        return GLOBAL_BASE_URL

    # 旧 Key 没有地区前缀，先用只读请求确认地区，再执行用户命令。
    probe_headers = {**headers, "locale": "zh-CN"}
    for base in (GLOBAL_BASE_URL, CN_BASE_URL):
        try:
            _request_data(
                base, probe_headers, "audio-list/simple", "验证 API Key",
                query={"page_size": 1}, timeout=10,
            )
            return base
        except APIError as exc:
            if exc.code != 401 or exc.message != "无效的 API Key":
                raise
    raise RuntimeError("验证 API Key 失败：CN 和海外均返回无效的 API Key")


def _folder_id(value):
    if (value.isascii() and value.isdecimal() and int(value) > 0) or re.fullmatch(r"fld_[A-Za-z0-9]{16}", value):
        return value
    raise argparse.ArgumentTypeError("文件夹 ID 应为正整数或 fld_ 公开 ID")


def _positive_number(value):
    number = float(value)
    if not 0 < number < float("inf"):
        raise argparse.ArgumentTypeError("请输入大于 0 的有限数值")
    return number


def _build_parser():
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--api-key", help="Tinrec API Key")
    common.add_argument("--api-keys-file", default="api-keys", help="API Key 文件路径（默认 api-keys）")
    common.add_argument("--base-url", help="覆盖按 API Key 自动选择的 API 地址")

    pagination = argparse.ArgumentParser(add_help=False, parents=[common])
    pagination.add_argument("--page", type=int, default=1, help="页码（默认 1）")
    pagination.add_argument("--page-size", type=int, default=10, help="每页数量（1–100，默认 10）")

    uploader = argparse.ArgumentParser(add_help=False, parents=[common])
    uploader.add_argument("--folder-id", type=_folder_id, help="归档到指定文件夹")
    uploader.add_argument("--json", action="store_true", help="以 JSON 输出转写结果")
    uploader.add_argument("--no-wait", action="store_true", help="提交后返回录音 ID")
    uploader.add_argument("--poll-interval", type=_positive_number, default=3.0, help="轮询间隔（秒）")
    uploader.add_argument("--timeout", type=_positive_number, default=600.0, help="轮询超时（秒）")

    parser = argparse.ArgumentParser(description="Tinrec 录音与文件夹。先看列表，再按录音 ID 获取详情或转写。")
    commands = parser.add_subparsers(dest="command", required=True)
    recordings = commands.add_parser("list-recordings", parents=[pagination], help="获取录音概览")
    recordings.add_argument("--folder-id", type=_folder_id, help="仅查看指定文件夹中的录音")
    recordings.add_argument("--filename", help="按文件名、AI 标题或主题搜索")
    commands.add_parser("list-folders", parents=[pagination], help="获取文件夹列表")

    for name, help_text in (("detail", "获取录音详情和 AI 产出"), ("transcript", "获取逐字稿和发言人")):
        command = commands.add_parser(name, parents=[common], help=help_text)
        command.add_argument("audio_id", help="录音 ID 或 aud_ 公开 ID")

    upload = commands.add_parser("upload", parents=[uploader], help="上传本地音频并转写")
    upload.add_argument("audio_path", help="本地文件路径")
    network = commands.add_parser("import-url", parents=[uploader], help="解析分享链接、下载媒体并转写")
    network.add_argument("share_url", help="分享链接或含链接的分享文案")
    return parser


def _run(args):
    api_key = _read_api_key(args)
    headers = {"Authorization": f"Bearer {api_key}"}
    base = _select_base_url(api_key, headers, args.base_url)

    if args.command in ("list-recordings", "list-folders"):
        query = {"page": args.page, "page_size": args.page_size}
        endpoint = "folders"
        if args.command == "list-recordings":
            endpoint = "audio-list/simple"
            _add_folder(query, args.folder_id)
            if args.filename:
                query["filename"] = args.filename
        data = _request_data(base, headers, endpoint, "获取列表", query=query)
        if data.get("list") is None:
            data["list"] = []
        _print_json(data)
        return

    if args.command in ("detail", "transcript"):
        endpoint = "audio-detail" if args.command == "detail" else "transcript"
        _print_json(_request_data(base, headers, _audio_endpoint(endpoint, args.audio_id), "获取录音数据"))
        return

    if args.command == "upload":
        audio_id = _upload(base, headers, Path(args.audio_path), args)
    else:
        audio_id = _import_url(base, headers, args)
    if args.no_wait:
        print(json.dumps({"audio_id": audio_id, "message": "已提交，请自行轮询 GET /api/audio-detail/{id}"}))
        return

    result = _wait_for_result(base, headers, audio_id, args)
    if args.json:
        _print_json(result)
    else:
        _print_detail(result)


def main():
    parser = _build_parser()
    argv = sys.argv[1:]
    if not argv:
        parser.print_help()
        return
    # 兼容 1.0.0 的 python audio2text_cli.py /path/to/audio.mp3 [选项]。
    if argv[0] not in (*COMMANDS, "-h", "--help"):
        argv.insert(0, "upload")
    args = parser.parse_args(argv)
    if args.command in ("list-recordings", "list-folders") and (args.page < 1 or not 1 <= args.page_size <= 100):
        parser.error("页码须大于 0，每页数量须为 1–100")
    try:
        _run(args)
    except (RuntimeError, OSError, ValueError) as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)


def _build_result(detail: dict, transcript_data: dict | None) -> dict:
    """合并详情与转写。转写状态(transcript_status)决定是否有正文；任务状态(task_status)完成后才有 summary/要点/发言人。"""
    out = {
        "id": detail.get("id"),
        "file_name": detail.get("file_name"),
        "duration": detail.get("duration"),
        "transcript_status": detail.get("transcript_status"),  # 转写状态
        "task_status": detail.get("task_status"),              # 任务状态，完成后才有总结/要点/发言人
        "summary": detail.get("summary"),
        "chapters": detail.get("chapters"),
        "todos": detail.get("todos"),
        "recommend": detail.get("recommend"),
    }
    if transcript_data:
        out["transcripts"] = transcript_data.get("transcripts")
        out["speaker_data"] = transcript_data.get("speaker_data")
        out["enable_speaker"] = transcript_data.get("enable_speaker")
    return out


def _print_detail(out: dict) -> None:
    """输出转写与 AI 总结、要点、发言人等，便于人类阅读。总结/要点/发言人仅在任务状态完成后有值。"""
    print("--- 任务信息 ---")
    print(f"ID: {out.get('id')}  转写状态: {out.get('transcript_status')}  任务状态: {out.get('task_status')}")
    print(f"文件名: {out.get('file_name')}  时长: {out.get('duration')}s")
    print()
    summary = out.get("summary")
    if summary:
        print("--- AI 总结 / 录音要点 ---")
        if isinstance(summary, dict):
            text = summary.get("summary") or summary.get("content") or json.dumps(summary, ensure_ascii=False)
        else:
            text = str(summary)
        print(text)
        print()
    chapters = out.get("chapters")
    if chapters:
        print("--- 章节/要点 ---")
        print(json.dumps(chapters, ensure_ascii=False, indent=2))
        print()
    speaker_data = out.get("speaker_data")
    if speaker_data:
        print("--- 发言人 ---")
        print(json.dumps(speaker_data, ensure_ascii=False, indent=2))
        print()
    transcripts = out.get("transcripts")
    if transcripts:
        print("--- 转写正文（发言人区分） ---")
        print(json.dumps(transcripts, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
