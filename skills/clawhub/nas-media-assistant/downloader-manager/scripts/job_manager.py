"""下载任务状态机管理。

状态流转: queued -> downloading -> completed/error
"""
from __future__ import annotations
import json
import os
import time
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Optional

STATE_FILE = os.environ.get("JOB_STATE_FILE", "/tmp/downloader_jobs.json")


class JobState(str, Enum):
    QUEUED = "queued"
    DOWNLOADING = "downloading"
    COMPLETED = "completed"
    ERROR = "error"
    CANCELLED = "cancelled"


@dataclass
class Job:
    job_id: str
    url: str
    adapter: str
    task_id: str = ""
    name: str = ""
    media_type: str = ""
    state: JobState = JobState.QUEUED
    progress: float = 0.0
    error: str = ""
    created_at: float = field(default_factory=time.time)
    updated_at: float = field(default_factory=time.time)
    meta: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        d = asdict(self)
        d["state"] = self.state.value
        d["created_at"] = round(self.created_at, 1)
        d["updated_at"] = round(self.updated_at, 1)
        return d


class JobManager:
    """简易 JSON 文件持久化的任务管理器。"""

    def __init__(self, state_file: str = STATE_FILE):
        self.state_file = state_file
        self.jobs: dict[str, Job] = {}
        self._load()

    def _load(self):
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, encoding="utf-8") as f:
                    data = json.load(f)
                for jid, j in data.items():
                    j["state"] = JobState(j.get("state", "queued"))
                    self.jobs[jid] = Job(**j)
            except Exception:
                pass

    def _save(self):
        os.makedirs(os.path.dirname(self.state_file) or ".", exist_ok=True)
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.jobs.items()},
                      f, ensure_ascii=False, indent=2)

    def create(self, job_id: str, url: str, adapter: str, **kw) -> Job:
        job = Job(job_id=job_id, url=url, adapter=adapter, **kw)
        self.jobs[job_id] = job
        self._save()
        return job

    def update(self, job_id: str, **kw):
        job = self.jobs.get(job_id)
        if not job:
            return
        for k, v in kw.items():
            setattr(job, k, v)
        job.updated_at = time.time()
        self._save()

    def get(self, job_id: str) -> Optional[Job]:
        return self.jobs.get(job_id)

    def list_active(self) -> list[Job]:
        return [j for j in self.jobs.values()
                if j.state in (JobState.QUEUED, JobState.DOWNLOADING)]

    def list_all(self) -> list[Job]:
        return list(self.jobs.values())
