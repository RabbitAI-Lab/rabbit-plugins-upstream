"""迅雷 Cloud MCP 适配器。

通过 SSE 连接迅雷官方 Cloud MCP，调用 4 个工具管理下载任务。
支持: magnet / ed2k / thunder:// / http(s) 全协议。
"""
from __future__ import annotations
import logging
import os
import sys
from typing import Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from base import BaseAdapter, LinkType, TaskResult, TaskState, TaskStatus  # noqa: E402
from utils.mcp_sse_client import McpSseClient, McpSseError  # noqa: E402
from utils.thunderlink import try_decode  # noqa: E402

logger = logging.getLogger("xunlei_cloud")

# 迅雷任务状态 -> 我们的 TaskState
_PHASE_MAP = {
    "PHASE_TYPE_PENDING": TaskState.QUEUED,
    "PHASE_TYPE_RUNNING": TaskState.DOWNLOADING,
    "PHASE_TYPE_PAUSED": TaskState.PAUSED,
    "PHASE_TYPE_ERROR": TaskState.ERROR,
    "PHASE_TYPE_COMPLETE": TaskState.COMPLETED,
}
# 中文状态映射
_STATUS_CN_MAP = {
    "等待中": TaskState.QUEUED,
    "进行中": TaskState.DOWNLOADING,
    "已暂停": TaskState.PAUSED,
    "失败": TaskState.ERROR,
    "完成": TaskState.COMPLETED,
    "已完成": TaskState.COMPLETED,
}


class XunleiCloudAdapter(BaseAdapter):
    """迅雷 Cloud MCP 适配器。"""

    name = "xunlei_cloud"
    download_dir = "/media/xunlei-inbox"  # openclaw 容器视角

    def __init__(self, sse_url: str, call_timeout: int = 30):
        self._sse_url = sse_url
        self._client = McpSseClient(sse_url, call_timeout=call_timeout)
        self._target: Optional[str] = None       # 缓存设备 ID

    # ---- 适配器接口 ----

    def supports_link_type(self, link_type: LinkType) -> bool:
        return True  # 迅雷支持全协议

    def health_check(self) -> bool:
        try:
            if not self._ensure_session():
                return False
            devices = self._list_devices()
            return bool(devices)
        except Exception as e:
            logger.warning("health_check 失败: %s", e)
            return False

    def add_task(self, url: str, name: str = "", save_path: str = "",
                 category: str = "") -> TaskResult:
        if not self._ensure_session():
            return TaskResult(False, error="无法建立迅雷 MCP 会话")
        # thunder:// 先解码
        real_url = try_decode(url)
        urls = [real_url]
        names = [name] if name else None
        try:
            # 1. 校验链接
            check = self._client.call_tool("xunlei_download_check_urls", {"urls": urls})
            logger.info("check_urls 结果: %s", check)
            # 2. 创建任务
            args = {"target": self._target, "urls": urls}
            if names:
                args["names"] = names
            result = self._client.call_tool("xunlei_download_create", args)
            logger.info("create 结果: %s", result)
            # 解析任务 ID — 处理多种返回结构
            task_id = ""
            if isinstance(result, list) and result:
                first = result[0]
                if isinstance(first, dict):
                    if "task" in first:
                        task_id = str(first["task"].get("id", ""))
                    elif "id" in first:
                        task_id = str(first.get("id", ""))
            elif isinstance(result, dict):
                tasks = result.get("tasks") or result.get("task") or []
                if isinstance(tasks, list) and tasks:
                    t = tasks[0]
                    if isinstance(t, dict):
                        task_id = str(t.get("id", "") or t.get("task", {}).get("id", ""))
                elif isinstance(tasks, dict):
                    task_id = str(tasks.get("id", ""))
            if not task_id:
                task_id = str(result)
            return TaskResult(True, task_id=task_id, message="迅雷任务已创建")
        except McpSseError as e:
            return TaskResult(False, error=str(e))

    def query_task(self, task_id: str) -> TaskStatus:
        tasks = self._list_all_tasks()
        for t in tasks:
            if str(t.task_id) == str(task_id):
                return t
        return TaskStatus(task_id=task_id, state=TaskState.UNKNOWN,
                          error="任务未找到")

    def list_tasks(self) -> list[TaskStatus]:
        return self._list_all_tasks()

    def cancel_task(self, task_id: str) -> bool:
        """删除迅雷任务（不可恢复）。"""
        if not self._ensure_session():
            return False
        try:
            result = self._client.call_tool("xunlei_download_operate", {
                "target": self._target,
                "task_id": task_id,
                "action": "delete",
            })
            logger.info("cancel result: %s", result)
            return True
        except McpSseError as e:
            logger.error("cancel_task 失败: %s", e)
            return False

    def pause_task(self, task_id: str) -> bool:
        if not self._ensure_session():
            return False
        try:
            self._client.call_tool("xunlei_download_operate", {
                "target": self._target, "task_id": task_id, "action": "pause",
            })
            return True
        except McpSseError:
            return False

    def resume_task(self, task_id: str) -> bool:
        if not self._ensure_session():
            return False
        try:
            self._client.call_tool("xunlei_download_operate", {
                "target": self._target, "task_id": task_id, "action": "running",
            })
            return True
        except McpSseError:
            return False


    def get_file_path(self, task_id: str) -> str:
        """返回下载文件在 openclaw 容器中的路径。

        迅雷下载的文件位于 /media/xunlei-inbox/<文件名>。
        通过任务名（即文件名）拼接路径。
        """
        s = self.query_task(task_id)
        name = s.name or s.extra.get('file_name', '')
        if not name:
            return ''
        return f"{self.download_dir}/{name}"

    # ---- 内部方法 ----

    def _ensure_session(self) -> bool:
        if self._client.connected and self._target:
            return True
        if not self._client.connect():
            return False
        self._target = self._get_target()
        return bool(self._target)

    def _get_target(self) -> Optional[str]:
        devices = self._list_devices()
        if devices:
            return devices[0].get("target", "")
        return None

    def _list_devices(self) -> list[dict]:
        try:
            result = self._client.call_tool("xunlei_download_list_device", {})
            if isinstance(result, dict):
                return result.get("device", [])
            return []
        except Exception as e:
            logger.error("list_device 失败: %s", e)
            return []

    def _list_all_tasks(self) -> list[TaskStatus]:
        if not self._ensure_session():
            return []
        all_tasks: list[TaskStatus] = []
        page_token = ""
        try:
            while True:
                args = {"target": self._target, "page_size": 50}
                if page_token:
                    args["page_token"] = page_token
                result = self._client.call_tool("xunlei_download_list", args)
                if not isinstance(result, dict):
                    break
                for t in result.get("tasks", []):
                    all_tasks.append(self._parse_task(t))
                page_token = result.get("next_page_token", "")
                if not page_token:
                    break
        except Exception as e:
            logger.error("list_tasks 失败: %s", e)
        return all_tasks

    def _parse_task(self, raw: dict) -> TaskStatus:
        tid = str(raw.get("id", raw.get("task_id", "")))
        name = raw.get("name", raw.get("file_name", ""))
        status_str = str(raw.get("status", raw.get("phase", "")))
        progress = float(raw.get("progress", 0))
        size = int(raw.get("size", raw.get("file_size", 0)) or 0)
        speed = int(raw.get("speed", 0) or 0)
        # 状态映射
        state = _PHASE_MAP.get(status_str) or _STATUS_CN_MAP.get(status_str)
        if state is None:
            # 完成度 100 视为完成
            state = TaskState.COMPLETED if progress >= 100 else TaskState.DOWNLOADING
        return TaskStatus(
            task_id=tid, name=name, state=state,
            progress=progress, size=size, speed=speed,
            extra={"raw_status": status_str},
        )

    def disconnect(self):
        self._client.disconnect()
