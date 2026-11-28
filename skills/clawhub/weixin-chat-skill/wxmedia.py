"""媒体本体定位与导出（文件 / 视频为明文；图片 .dat 需图片密钥，当前未解密）。

薇芯 4.x 媒体磁盘布局（账号目录 = db_storage 的上一级）：
- 文件：  msg/file/<YYYY-MM>/<原文件名>                （明文，按文件名匹配）
- 视频：  msg/video/<YYYY-MM>/<内容md5>.mp4            （明文，按内容 md5 匹配）
- 图片：  msg/attach/<talkerhash>/<YYYY-MM>/Img/<id>.dat（V2 加密，需图片 AES 密钥）
"""
from __future__ import annotations

import hashlib
import re
import shutil
from pathlib import Path

_VID_MD5 = re.compile(r'<videomsg[^>]*\bmd5="([0-9a-fA-F]{32})"')
_FILE_TITLE = re.compile(r"<title>([^<]+)</title>")


def account_dir(db_dir: Path) -> Path:
    return Path(db_dir).parent  # .../<wxid>_1034


def media_ref(local_type: int, text: str, is_group: bool) -> dict | None:
    """从消息文本解析可导出的媒体引用。text 应为已 decode/去前缀 的内容。"""
    t = int(local_type) & 0xFFFFFFFF
    if t == 43:
        m = _VID_MD5.search(text)
        return {"kind": "video", "md5": m.group(1).lower()} if m else {"kind": "video"}
    if t == 3:
        return {"kind": "image"}
    if t == 49 and "<type>6</type>" in text:
        m = _FILE_TITLE.search(text)
        return {"kind": "file", "title": m.group(1).strip()} if m else {"kind": "file"}
    return None


# ---- 文件：按原文件名在 msg/file/ 下找 ----
def find_file(db_dir: Path, title: str) -> Path | None:
    if not title:
        return None
    base = account_dir(db_dir) / "msg" / "file"
    if not base.is_dir():
        return None
    for p in base.rglob(title):
        if p.is_file():
            return p
    return None


# ---- 视频：按内容 md5 匹配 msg/video/ 下的 .mp4 ----
_video_index: dict[str, dict[str, Path]] = {}


def _index_videos(db_dir: Path) -> dict[str, Path]:
    key = str(db_dir)
    if key in _video_index:
        return _video_index[key]
    idx: dict[str, Path] = {}
    base = account_dir(db_dir) / "msg" / "video"
    if base.is_dir():
        for p in base.rglob("*.mp4"):
            try:
                idx[hashlib.md5(p.read_bytes()).hexdigest()] = p
            except OSError:
                pass
    _video_index[key] = idx
    return idx


def find_video(db_dir: Path, md5: str | None) -> Path | None:
    if not md5:
        return None
    return _index_videos(db_dir).get(md5.lower())


def export_media(db_dir: Path, ref: dict, dst_dir: Path) -> str | None:
    """把媒体本体复制到 dst_dir，返回复制后的文件名；无法导出（图片/找不到）返回 None。"""
    src = None
    if ref["kind"] == "file":
        src = find_file(db_dir, ref.get("title", ""))
    elif ref["kind"] == "video":
        src = find_video(db_dir, ref.get("md5"))
    # image: 需图片密钥，暂不支持
    if not src or not src.exists():
        return None
    dst_dir = Path(dst_dir)
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / src.name
    if not dst.exists():
        try:
            shutil.copy2(src, dst)
        except OSError:
            return None
    return dst.name
