"""适配器健康检查（独立于业务调用，60s 缓存）。"""
from __future__ import annotations
import time
import logging

logger = logging.getLogger("health_check")
_CACHE: dict[str, tuple[bool, float]] = {}
_TTL = 60  # 秒


def check(adapter, name: str) -> bool:
    """检查适配器健康状态，60s 内缓存。"""
    cached = _CACHE.get(name)
    if cached and time.time() - cached[1] < _TTL:
        return cached[0]
    try:
        ok = adapter.health_check()
    except Exception as e:
        logger.warning("health_check %s 异常: %s", name, e)
        ok = False
    _CACHE[name] = (ok, time.time())
    return ok
