"""qBittorrent WebUI REST API 适配器。

通过标准 WebUI API 管理下载任务。支持 magnet / http(s) .torrent。
认证: SID cookie + Referer header。
"""
from __future__ import annotations
import logging
import os
import os.path
import time
import sys
from pathlib import Path

import requests

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from base import BaseAdapter, LinkType, TaskResult, TaskState, TaskStatus  # noqa: E402

logger = logging.getLogger("qbittorrent")

# qB state -> TaskState
_QB_STATE_MAP = {
    "downloading": TaskState.DOWNLOADING,
    "stalledDL": TaskState.DOWNLOADING,
    "uploading": TaskState.COMPLETED,
    "stalledUP": TaskState.COMPLETED,
    "pausedDL": TaskState.PAUSED,
    "pausedUP": TaskState.PAUSED,
    "queuedDL": TaskState.QUEUED,
    "queuedUP": TaskState.QUEUED,
    "checkingDL": TaskState.DOWNLOADING,
    "checkingUP": TaskState.DOWNLOADING,
    "error": TaskState.ERROR,
    "missingFiles": TaskState.ERROR,
    "forcedDL": TaskState.DOWNLOADING,
    "forcedMetaDL": TaskState.DOWNLOADING,
    "metaDL": TaskState.DOWNLOADING,
    "moving": TaskState.DOWNLOADING,
}


class QbittorrentAdapter(BaseAdapter):
    """qBittorrent WebUI 适配器。"""

    name = "qbittorrent"
    download_dir = "/media/downloads/qBittorrent下载"  # openclaw 容器视角

    def __init__(self, url: str, username: str, password: str,
                 default_save_path: str = ""):
        self.url = url.rstrip("/")
        self.user = username
        self.pwd = password
        self.default_save_path = default_save_path
        self._sid: str = ""
        self._session = requests.Session()

    # ---- 适配器接口 ----

    def supports_link_type(self, link_type: LinkType) -> bool:
        return link_type in (LinkType.MAGNET, LinkType.HTTP)

    def health_check(self) -> bool:
        try:
            self._ensure_login()
            r = self._api_get("app/version")
            return r.status_code == 200
        except Exception as e:
            logger.warning("health_check 失败: %s", e)
            return False

    def add_task(self, url: str, name: str = "", save_path: str = "",
                 category: str = "") -> TaskResult:
        try:
            self._ensure_login()
        except Exception as e:
            return TaskResult(False, error=f"登录失败: {e}")
        # 本地 .torrent 文件 -> multipart 上传
        if url.startswith("/") and url.lower().endswith(".torrent"):
            return self._add_torrent_file(url, name, save_path, category)
        params: dict[str, str] = {"urls": url}
        sp = save_path or self.default_save_path
        if sp:
            params["savepath"] = sp
        if category:
            params["category"] = category
        try:
            r = self._api_post("torrents/add", data=params)
            body = r.text.strip()
            if body == "Ok.":
                task_id = self._find_task_by_url(url)
                return TaskResult(True, task_id=task_id,
                                  message="qBittorrent 任务已添加")
            # qB 有时对 magnet 返回 "Fails." 但实际已添加（metaDL 阶段）
            if body == "Fails.":
                task_id = self._find_task_by_url(url)
                if task_id:
                    return TaskResult(True, task_id=task_id,
                                      message="qBittorrent 任务已添加（magnet 元数据获取中）")
            return TaskResult(False, error=f"qB 返回: {body}")
        except Exception as e:
            return TaskResult(False, error=str(e))

    def query_task(self, task_id: str) -> TaskStatus:
        try:
            self._ensure_login()
            r = self._api_get(f"torrents/info", params={"hashes": task_id})
            items = r.json()
            if not items:
                return TaskStatus(task_id=task_id, state=TaskState.UNKNOWN,
                                  error="任务未找到")
            return self._parse_torrent(items[0])
        except Exception as e:
            return TaskStatus(task_id=task_id, state=TaskState.ERROR, error=str(e))

    def list_tasks(self) -> list[TaskStatus]:
        try:
            self._ensure_login()
            r = self._api_get("torrents/info", params={"limit": 100,
                                                        "sort": "added_on",
                                                        "reverse": "true"})
            return [self._parse_torrent(t) for t in r.json()]
        except Exception as e:
            logger.error("list_tasks 失败: %s", e)
            return []

    def cancel_task(self, task_id: str) -> bool:
        """删除任务但保留已下载文件。"""
        try:
            self._ensure_login()
            r = self._api_post("torrents/delete",
                               data={"hashes": task_id, "deleteFiles": "false"})
            return r.status_code == 200
        except Exception as e:
            logger.error("cancel_task 失败: %s", e)
            return False

    def pause_task(self, task_id: str) -> bool:
        try:
            self._ensure_login()
            r = self._api_post("torrents/pause", data={"hashes": task_id})
            return r.status_code == 200
        except Exception:
            return False

    def resume_task(self, task_id: str) -> bool:
        try:
            self._ensure_login()
            r = self._api_post("torrents/start", data={"hashes": task_id})
            return r.status_code == 200
        except Exception:
            return False


    def get_file_path(self, task_id: str) -> str:
        """返回下载文件在 openclaw 容器中的路径。

        qBittorrent 的 content_path 形如 /downloads/xxx，
        映射为容器路径 /media/downloads/qBittorrent下载/xxx。
        """
        s = self.query_task(task_id)
        content_path = s.extra.get('content_path', '')
        if not content_path:
            return ''
        # /downloads -> /media/downloads/qBittorrent下载
        if content_path.startswith('/downloads'):
            return content_path.replace('/downloads', self.download_dir, 1)
        return content_path

    # ---- 内部方法 ----

    def _login(self):
        data = {"username": self.user, "password": self.pwd}
        r = self._session.post(
            f"{self.url}/api/v2/auth/login",
            data=data,
            headers={"Referer": self.url},
            timeout=10,
        )
        for c in r.cookies:
            if c.name == "SID":
                self._sid = c.value
                return
        if r.text.strip() == "Ok.":
            # cookie 可能在 session 中
            for c in self._session.cookies:
                if c.name == "SID":
                    self._sid = c.value
                    return
        raise RuntimeError(f"登录失败: {r.text[:100]}")

    def _ensure_login(self):
        if self._sid:
            # 验证 session 是否有效
            r = self._api_get("app/version")
            if r.status_code == 200:
                return
        self._login()

    def _headers(self) -> dict:
        h = {"Referer": self.url}
        if self._sid:
            h["Cookie"] = f"SID={self._sid}"
        return h

    def _api_get(self, endpoint: str, params: dict | None = None) -> requests.Response:
        return self._session.get(
            f"{self.url}/api/v2/{endpoint}",
            params=params, headers=self._headers(), timeout=15,
        )

    def _api_post(self, endpoint: str, data: dict | None = None) -> requests.Response:
        return self._session.post(
            f"{self.url}/api/v2/{endpoint}",
            data=data, headers=self._headers(), timeout=15,
        )


    def _add_torrent_file(self, file_path: str, name: str = "",
                          save_path: str = "", category: str = "") -> TaskResult:
        """上传本地 .torrent 文件到 qBittorrent（multipart/form-data）。"""
        try:
            with open(file_path, "rb") as f:
                data: dict[str, str] = {}
                sp = save_path or self.default_save_path
                if sp:
                    data["savepath"] = sp
                if category:
                    data["category"] = category
                r = self._session.post(
                    f"{self.url}/api/v2/torrents/add",
                    files={"torrents": f}, data=data,
                    headers={"Referer": self.url}, timeout=30,
                )
                body = r.text.strip()
                if body == "Ok.":
                    time.sleep(2)
                    r2 = self._api_get("torrents/info",
                                       params={"limit": 1, "sort": "added_on",
                                               "reverse": "true"})
                    items = r2.json()
                    if items:
                        return TaskResult(True, task_id=items[0].get("hash", ""),
                                          message="qBittorrent 任务已添加（文件上传）")
                    return TaskResult(True, message="qBittorrent 任务已添加（文件上传）")
                return TaskResult(False, error=f"qB 返回: {body}")
        except Exception as e:
            return TaskResult(False, error=str(e))

    def _find_task_by_url(self, url: str) -> str:
        """添加后通过 magnet hash 匹配找到 task hash。"""
        import hashlib
        # 从 magnet 提取 infohash
        infohash = ""
        if "xt=urn:btih:" in url:
            import re
            m = re.search(r"xt=urn:btih:([a-fA-F0-9]{32,40})", url)
            if m:
                infohash = m.group(1).lower()
                if len(infohash) == 32:  # base32 -> hex
                    import base64
                    infohash = base64.b32decode(infohash).hex()
        # 查列表找匹配
        time.sleep(2)
        r = self._api_get("torrents/info", params={"limit": 5,
                                                    "sort": "added_on",
                                                    "reverse": "true"})
        for t in r.json():
            if infohash and t.get("hash", "").lower() == infohash:
                return t["hash"]
        # 回退: 返回最新任务的 hash
        items = r.json()
        if items:
            return items[0].get("hash", "")
        return ""

    def _parse_torrent(self, t: dict) -> TaskStatus:
        raw_state = t.get("state", "unknown")
        state = _QB_STATE_MAP.get(raw_state, TaskState.UNKNOWN)
        progress = float(t.get("progress", 0)) * 100
        if progress >= 100 and state not in (TaskState.ERROR, TaskState.PAUSED):
            state = TaskState.COMPLETED
        return TaskStatus(
            task_id=t.get("hash", ""),
            name=t.get("name", ""),
            state=state,
            progress=round(progress, 1),
            size=int(t.get("size", 0)),
            speed=int(t.get("dlspeed", 0)),
            extra={"save_path": t.get("save_path", ""),
                   "raw_state": raw_state,
                   "content_path": t.get("content_path", "")},
        )
