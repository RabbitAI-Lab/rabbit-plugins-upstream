"""核心类型定义 + 抽象适配器接口 + 链接分类。

所有适配器实现 BaseAdapter，router 据链接类型选择适配器。
"""
from __future__ import annotations
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


# ---------- 链接类型 ----------

class LinkType(str, Enum):
    MAGNET = "magnet"
    ED2K = "ed2k"
    THUNDER = "thunder"
    HTTP = "http"
    UNKNOWN = "unknown"


def classify_link(url: str) -> LinkType:
    """判断下载链接类型。"""
    u = url.strip().lower()
    if u.startswith("magnet:"):
        return LinkType.MAGNET
    if u.startswith("ed2k://"):
        return LinkType.ED2K
    if u.startswith("thunder://"):
        return LinkType.THUNDER
    if u.startswith(("http://", "https://")):
        return LinkType.HTTP
    return LinkType.UNKNOWN


# ---------- 任务状态 ----------

class TaskState(str, Enum):
    QUEUED = "queued"
    DOWNLOADING = "downloading"
    COMPLETED = "completed"
    PAUSED = "paused"
    ERROR = "error"
    UNKNOWN = "unknown"


@dataclass
class TaskStatus:
    """下载任务状态快照。"""
    task_id: str
    name: str = ""
    state: TaskState = TaskState.UNKNOWN
    progress: float = 0.0          # 0-100
    size: int = 0                  # bytes
    speed: int = 0                 # bytes/s
    error: str = ""
    extra: dict = field(default_factory=dict)

    @property
    def is_terminal(self) -> bool:
        return self.state in (TaskState.COMPLETED, TaskState.ERROR)

    @property
    def is_downloading(self) -> bool:
        return self.state in (TaskState.DOWNLOADING, TaskState.QUEUED)


@dataclass
class TaskResult:
    """add_task 返回值。"""
    success: bool
    task_id: str = ""
    message: str = ""
    error: str = ""


# ---------- 抽象适配器 ----------

class BaseAdapter(ABC):
    """下载适配器抽象基类。每个适配器完全独立，互不影响。

    子类需设置 download_dir（openclaw 容器视角的下载根目录），
    并实现 get_file_path() 将下载器内部路径映射为容器路径。
    """

    name: str = "base"
    download_dir: str = ""  # openclaw 容器视角的下载根目录（如 /media/xunlei-inbox）

    @abstractmethod
    def add_task(self, url: str, name: str = "", save_path: str = "",
                 category: str = "") -> TaskResult:
        """提交下载任务。"""

    @abstractmethod
    def query_task(self, task_id: str) -> TaskStatus:
        """查询单个任务状态。"""

    @abstractmethod
    def list_tasks(self) -> list[TaskStatus]:
        """列出所有任务。"""

    @abstractmethod
    def cancel_task(self, task_id: str) -> bool:
        """取消/删除任务（保留已下载文件）。"""

    @abstractmethod
    def health_check(self) -> bool:
        """健康探测（独立于业务调用）。"""

    @abstractmethod
    def supports_link_type(self, link_type: LinkType) -> bool:
        """声明本适配器支持的链接类型。"""

    @abstractmethod
    def get_file_path(self, task_id: str) -> str:
        """返回下载文件在 openclaw 容器中的路径（供 media-organizer 使用）。

        各适配器将下载器内部路径映射为容器路径：
        - qBittorrent: /downloads/xxx -> /media/downloads/qBittorrent下载/xxx
        - 迅雷: 文件名 -> /media/xunlei-inbox/<文件名>
        """
