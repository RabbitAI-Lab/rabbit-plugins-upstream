#!/usr/bin/env python3
"""源健康度管理。

记录每个数据源的成功/失败，连续失败 N 次自动摘除，摘除满一定时间后
允许重试恢复。状态持久化到 health.json。

v2 增量：会话内连续 2 次失败的源，自动降级为「本会话不可用」，
跳过对该源的请求（避免对已知不可达的源做无效请求）。

会话窗口：
- 默认 30 分钟自动窗口（每次 dispatch 重新计算 session_id 决定是否续期）
- 也支持 MEDIA_SEARCH_SESSION 环境变量注入固定 session_id（调试/测试用）
- session_fails 持久化在 health.json 的 session_fails_by_session 下
- 加载时自动清理 1 小时前结束的 session

用法:
  health_check.py record <source_id> <success|fail> [reason]
  health_check.py status
  health_check.py reset <source_id>
  health_check.py reset_session [session_id]   # 重置某会话
  health_check.py reset_all_sessions          # 清空所有 session_fails
"""
import json
import os
import sys
import tempfile
import time

# 健康度状态文件写到系统临时目录,跨平台、无绝对路径、零隐私信息。
# 1h TTL 内的失败摘除缓存,系统清理 tmp 时自然重置(下次 dispatch 重新计算)。
DEFAULT_HEALTH_FILE = os.path.join(
    tempfile.gettempdir(), "media-search", "health.json"
)
FAIL_THRESHOLD = 3        # 连续失败次数达到即摘除
RECOVER_AFTER = 3600      # 摘除后 1 小时尝试恢复
# v2 新增：本会话内连续失败次数达到即会话内降级（不影响持久化）
SESSION_FAIL_THRESHOLD = 2
SESSION_WINDOW_SEC = 1800  # 30 分钟自动会话窗口
SESSION_KEEP_AFTER = 3600  # 1 小时前的 session 自动清理


def _current_session_id():
    """生成或复用 session_id。

    优先级：
    1) 环境变量 MEDIA_SEARCH_SESSION（测试/调试可注入）
    2) 基于 30 分钟时间窗口自动计算：floor(now / SESSION_WINDOW_SEC)
       → 同一窗口内多次 dispatch 共享 session
    """
    env = os.environ.get("MEDIA_SEARCH_SESSION")
    if env:
        return env
    return f"auto-{int(time.time() // SESSION_WINDOW_SEC)}"


class HealthChecker:
    def __init__(self, health_file=None, session_id=None):
        path = health_file or DEFAULT_HEALTH_FILE
        # 展开 ~ 并解析为绝对路径（相对于技能目录）
        self.path = os.path.expanduser(path)
        if not os.path.isabs(self.path):
            self.path = os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                self.path,
            )
        self.session_id = session_id or _current_session_id()
        self._state = self._load()
        self._cleanup_old_sessions()

    # ---- 持久化 ----
    def _load(self):
        if os.path.exists(self.path):
            try:
                with open(self.path, encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def _save(self):
        d = os.path.dirname(self.path)
        if d:
            os.makedirs(d, exist_ok=True)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self._state, f, ensure_ascii=False, indent=2)

    def _get_session_fails(self):
        return self._state.setdefault("session_fails_by_session", {}).setdefault(
            self.session_id, {}
        )

    def _cleanup_old_sessions(self):
        """清理 1 小时前结束的 session（避免健康文件无限增长）。"""
        sessions = self._state.get("session_fails_by_session")
        if not sessions:
            return
        cutoff = time.time() - SESSION_KEEP_AFTER
        stale = []
        for sid, data in sessions.items():
            # 1) 显式结束时间
            ended_at = data.get("ended_at", 0)
            # 2) 隐式：所有源最后一次失败时间都已超时
            last_fail = max(
                (e.get("last_fail", 0) for e in data.get("sources", {}).values()),
                default=0,
            )
            if ended_at and ended_at < cutoff:
                stale.append(sid)
            elif last_fail and last_fail < cutoff:
                stale.append(sid)
        for sid in stale:
            sessions.pop(sid, None)
        if not sessions:
            self._state.pop("session_fails_by_session", None)

    # ---- 记录 ----
    def record(self, source_id, success, reason=""):
        s = self._state.setdefault(
            source_id,
            {"fails": 0, "last_success": 0, "removed_until": 0, "last_reason": ""},
        )
        sf = self._get_session_fails().setdefault(
            source_id, {"count": 0, "last_fail": 0.0}
        )
        if success:
            s["fails"] = 0
            s["last_success"] = time.time()
            s["removed_until"] = 0
            # v2: 成功后重置会话内失败计数
            sf["count"] = 0
        else:
            s["fails"] = s.get("fails", 0) + 1
            if s["fails"] >= FAIL_THRESHOLD:
                s["removed_until"] = time.time() + RECOVER_AFTER
            # v2: 累加会话内失败
            sf["count"] = sf.get("count", 0) + 1
            sf["last_fail"] = time.time()
        s["last_reason"] = reason
        s["last_session"] = self.session_id
        self._save()

    # ---- 判定 ----
    def is_healthy(self, source_id):
        """判定源是否可用（持久化健康度 + 会话内降级综合判断）。"""
        sf = self._get_session_fails().get(source_id, {})
        if sf.get("count", 0) >= SESSION_FAIL_THRESHOLD:
            return False
        s = self._state.get(source_id, {})
        if s.get("removed_until", 0) > time.time():
            return False
        return True

    def session_unhealthy_reason(self, source_id):
        """返回会话内降级原因（用于日志）。"""
        sf = self._get_session_fails().get(source_id, {})
        if sf.get("count", 0) >= SESSION_FAIL_THRESHOLD:
            return f"session_fails={sf.get('count', 0)}"
        return ""

    def status(self):
        return self._state

    def reset(self, source_id):
        self._state.pop(source_id, None)
        for sess in self._state.get("session_fails_by_session", {}).values():
            sess.pop(source_id, None)
        self._save()

    def reset_session(self, session_id=None):
        sid = session_id or self.session_id
        self._state.get("session_fails_by_session", {}).pop(sid, None)
        self._save()

    def reset_all_sessions(self):
        self._state.pop("session_fails_by_session", None)
        self._save()


def main():
    if len(sys.argv) < 2:
        print(
            "用法: health_check.py record <id> <success|fail> [reason] | status | "
            "reset <id> | reset_session [sid] | reset_all_sessions"
        )
        sys.exit(1)
    cmd = sys.argv[1]
    hc = HealthChecker()
    if cmd == "record":
        if len(sys.argv) < 4:
            print("用法: health_check.py record <id> <success|fail> [reason]")
            sys.exit(1)
        sid, ok = sys.argv[2], sys.argv[3] == "success"
        reason = sys.argv[4] if len(sys.argv) > 4 else ""
        hc.record(sid, ok, reason)
        print(json.dumps({"ok": True, "healthy": hc.is_healthy(sid)}))
    elif cmd == "status":
        print(json.dumps(hc.status(), ensure_ascii=False, indent=2))
    elif cmd == "reset":
        hc.reset(sys.argv[2])
        print(json.dumps({"ok": True}))
    elif cmd == "reset_session":
        sid = sys.argv[2] if len(sys.argv) > 2 else None
        hc.reset_session(sid)
        print(json.dumps({"ok": True, "reset_session": sid or hc.session_id}))
    elif cmd == "reset_all_sessions":
        hc.reset_all_sessions()
        print(json.dumps({"ok": True}))
    else:
        print(f"未知命令: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
