#!/usr/bin/env python3
"""
retry.py — skill-designer 的自动重试基础设施

为脚本 CLI 提供统一的 transient-failure 重试能力，提升 Reliability（运行稳定性）。
覆盖场景：子进程启动失败、文件 IO 抖动、JSON 解析偶发错误、Python 解释器临时不可用。
不覆盖：业务逻辑错误、参数错误、目标目录不存在、用户取消。

设计原则：
- 默认 3 次、指数退避（0.5s / 1s / 2s），可配置
- 仅重试「瞬时/环境类」异常，不重试语义错误
- 每次重试前打印警告，让用户知道在自动恢复
- 所有失败聚合后给出「下一步人工操作」建议
"""

import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Callable, Optional, TypeVar

T = TypeVar("T")

# 默认可重试异常：环境/IO/进程/解析类
DEFAULT_RETRYABLE = (
    OSError,
    subprocess.SubprocessError,
    json.JSONDecodeError,
    PermissionError,
    FileNotFoundError,  # Python 解释器临时缺失可重试；目标文件不存在不在这里触发
)


def retry(
    max_retries: int = 3,
    backoff: float = 0.5,
    retryable: tuple[type[BaseException], ...] = DEFAULT_RETRYABLE,
    on_retry: Optional[Callable[[int, BaseException], None]] = None,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """函数装饰器：在指定异常上自动重试。"""

    def decorator(fn: Callable[..., T]) -> Callable[..., T]:
        def wrapper(*args, **kwargs) -> T:
            last_exc: Optional[BaseException] = None
            for attempt in range(max_retries + 1):
                try:
                    return fn(*args, **kwargs)
                except retryable as exc:
                    last_exc = exc
                    if attempt < max_retries:
                        wait = backoff * (2 ** attempt)
                        if on_retry:
                            on_retry(attempt + 1, exc)
                        else:
                            print(
                                f"[retry] {fn.__name__} 第 {attempt + 1}/{max_retries + 1} 次失败（{exc}），"
                                f"{wait:.1f}s 后重试...",
                                file=sys.stderr,
                            )
                        time.sleep(wait)
                    else:
                        raise
            raise last_exc or RuntimeError("retry 循环异常退出")

        wrapper.__name__ = fn.__name__
        wrapper.__doc__ = fn.__doc__
        return wrapper

    return decorator


class RetryRunner:
    """带重试的子进程运行器，用于 sd_cli.py 统一入口。"""

    def __init__(self, max_retries: int = 3, backoff: float = 0.5, dry_run: bool = False):
        self.max_retries = max_retries
        self.backoff = backoff
        self.dry_run = dry_run

    def run(self, cmd: list[str], cwd: Optional[Path] = None) -> int:
        """运行命令并在 transient 失败时自动重试；dry-run 只打印。"""
        if self.dry_run:
            print("[dry-run] " + " ".join(cmd))
            return 0

        last_returncode: Optional[int] = None
        last_stderr = ""

        for attempt in range(self.max_retries + 1):
            try:
                env = os.environ.copy()
                env["PYTHONIOENCODING"] = "utf-8"  # 强制子进程 UTF-8，避免 Windows 管道下按 GBK 输出导致下游解码崩溃
                proc = subprocess.run(
                    cmd,
                    cwd=str(cwd) if cwd else None,
                    env=env,
                    stdout=sys.stdout,
                    stderr=subprocess.PIPE,
                    text=True,
                    encoding="utf-8",
                    check=False,
                )
                last_returncode = proc.returncode
                last_stderr = proc.stderr or ""

                # 一律转发 stderr，不看退出码：退出码 0 的子进程同样可能输出警告
                # （如 export_brief 带缺口导出的 ⚠️ 提示）。此前只在失败时转发，
                # 导致「成功但带警告」的全部提示被静默吞掉。
                if proc.stderr:
                    print(proc.stderr, file=sys.stderr, end="")

                # 退出码 0：业务成功
                if proc.returncode == 0:
                    return 0

                # 退出码 127/126/3221225781（Windows 应用错误）/9009：环境/解释器问题，可重试
                if proc.returncode in (126, 127, 9009, 3221225781) and attempt < self.max_retries:
                    wait = self.backoff * (2 ** attempt)
                    print(
                        f"[retry] 子进程退出码 {proc.returncode}（环境/解释器问题），"
                        f"{wait:.1f}s 后重试（{attempt + 1}/{self.max_retries}）...",
                        file=sys.stderr,
                    )
                    time.sleep(wait)
                    continue

                # 其他退出码：直接返回业务错误（stderr 已在上面转发）
                return proc.returncode

            except (subprocess.SubprocessError, OSError, PermissionError) as exc:
                if attempt < self.max_retries:
                    wait = self.backoff * (2 ** attempt)
                    print(
                        f"[retry] 子进程启动失败（{exc}），"
                        f"{wait:.1f}s 后重试（{attempt + 1}/{self.max_retries}）...",
                        file=sys.stderr,
                    )
                    time.sleep(wait)
                else:
                    print(f"[retry] 已达最大重试次数：{exc}", file=sys.stderr)
                    if last_stderr:
                        print(last_stderr, file=sys.stderr, end="")
                    return last_returncode if last_returncode is not None else 1

        # 所有重试用完仍未成功（最后一次是业务错误但退出码不是可重试的）
        return last_returncode if last_returncode is not None else 1


@retry(max_retries=3, backoff=0.5)
def read_text_robust(path: Path) -> str:
    """带重试的文件读取：IO 抖动时自动重试。"""
    return path.read_text(encoding="utf-8-sig", errors="replace")


@retry(max_retries=3, backoff=0.5)
def write_text_robust(path: Path, text: str) -> None:
    """带重试的文件写入：IO 抖动时自动重试。"""
    path.write_text(text, encoding="utf-8")
