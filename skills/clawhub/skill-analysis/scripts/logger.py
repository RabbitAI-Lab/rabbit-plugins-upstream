#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Skill Analysis 日志模块 —— 杀毒软件风格的扫描日志与统计。

设计约束（借鉴 OWASP Agentic Skills Top 10：2026-02 OpenClaw 日志投毒事件）：
  - 日志仅记录**标识符**（名称/路径/哈希），不写入 Skill 原文或指令内容，防止日志被
    agent 读取时触发间接提示注入（indirect prompt injection via log poisoning）。
  - 日志以 JSONL 为主格式（机器处理），附带可读摘要 .txt。

用法：
  from logger import ScanLogger
  log = ScanLogger()
  log.scan_start()
  for skill in skills:
      result = analyze(skill)
      log.skill_scanned(skill_name, result["verdict"], result["risk_score"]["score"])
  log.scan_end(total_scanned=42)
  stats = log.get_stats()
"""

import datetime
import json
import os
import secrets
import sys
from pathlib import Path


def _instance_token() -> str:
    """每实例随机令牌（v3.2.4 起）：首次运行时生成并持久化到技能根目录 .instance_id，之后复用。
    使状态文件目录（日志）带随机后缀，避免固定可预测路径被定位/投毒。"""
    root = Path(os.path.expanduser("~")) / ".workbuddy" / "skills" / "skill-analysis"
    token_file = root / ".instance_id"
    try:
        if token_file.exists():
            tok = token_file.read_text(encoding="utf-8").strip()
            if tok:
                return tok
    except OSError:
        pass
    tok = secrets.token_hex(8)
    try:
        token_file.parent.mkdir(parents=True, exist_ok=True)
        token_file.write_text(tok, encoding="utf-8")
    except OSError:
        pass
    return tok


# 日志根目录（v3.2.4 起按每实例随机令牌分散，不再固定 logs/）
LOG_ROOT = Path(os.path.expanduser("~")) / ".workbuddy" / "skills" / "skill-analysis" / f"logs-{_instance_token()}"

# 日志保留天数
LOG_RETENTION_DAYS = 30


class ScanLogger:
    """结构化扫描日志，支持 JSONL 事件流 + 可读摘要。"""

    def __init__(self, log_root: Path = LOG_ROOT):
        self.log_root = Path(log_root)
        self.log_root.mkdir(parents=True, exist_ok=True)
        self._today = datetime.date.today().isoformat()
        self._log_path = self.log_root / f"scan_{self._today}.log"
        self._txt_path = self.log_root / f"scan_{self._today}.txt"
        self._session_start = datetime.datetime.now().isoformat()
        self._session_stats = {
            "scanned": 0, "safe": 0, "warning": 0, "danger": 0,
            "blocked": 0, "new": 0, "modified": 0, "errors": 0,
        }
        self._pending = []

    # ── 基础事件 ──────────────────────────────────────────

    def _emit(self, event: str, **kwargs):
        """写入一条 JSONL 事件，并追加一行可读摘要。"""
        record = {
            "ts": datetime.datetime.now().isoformat(),
            "event": event,
            **kwargs,
        }
        # JSONL
        with open(self._log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
        # 可读摘要
        with open(self._txt_path, "a", encoding="utf-8") as f:
            f.write(self._fmt_txt(record) + "\n")

    @staticmethod
    def _fmt_txt(record: dict) -> str:
        ts = record["ts"][:19].replace("T", " ")
        ev = record["event"]
        if ev == "SCAN_START":
            return f"[{ts}] ⏳ 全盘扫描开始 | 会话 {record.get('session','?')}"
        if ev == "SCAN_END":
            return (f"[{ts}] ✅ 扫描完成 | 共扫 {record.get('total',0)} 个 Skill | "
                    f"安全 {record.get('safe',0)} · 警告 {record.get('warn',0)} "
                    f"· 危险 {record.get('danger',0)}")
        if ev == "SKILL_SCANNED":
            level = {"safe": "🟢", "warning": "🟡", "danger": "🟠", "critical": "🔴"}.get(
                record.get("level", "safe"), "⚪")
            return (f"[{ts}] {level} {record.get('skill','?')} | 评级:{record.get('verdict','?')} "
                    f"分:{record.get('score','?')} 路径:{record.get('path','?'):.80s}")
        if ev == "FINDING":
            return (f"[{ts}] ⚠️  {record.get('skill','?')} | "
                    f"[{record.get('sev','?')}] {record.get('label','?')}")
        if ev in ("SKILL_ADDED", "SKILL_MODIFIED", "SKILL_REMOVED"):
            lbl = {"SKILL_ADDED": "➕ 新装", "SKILL_MODIFIED": "✏️ 变更",
                    "SKILL_REMOVED": "➖ 移除"}.get(ev, "📌")
            return f"[{ts}] {lbl} {record.get('skill','?')} | 路径:{record.get('path','?'):.80s}"
        if ev == "UPDATE_POISONING":
            sig = ", ".join(record.get("signals", []))[:120]
            return (f"[{ts}] 🚨 更新投毒！ {record.get('skill','?')} 本次更新"
                    f"新增高危信号: {sig}")
        if ev == "ALERT":
            return (f"[{ts}] 🚨 警告！ {record.get('skill','?')} → {record.get('reason','?')}")
        if ev == "QUARANTINE":
            return f"[{ts}] 🔒 已隔离 {record.get('skill','?')} | 原因:{record.get('reason','?')}"
        if ev == "IGNORE":
            return f"[{ts}] 🔕 {record.get('pattern','?')} → {record.get('reason','?')}"
        if ev == "SCAN_ERROR":
            return (f"[{ts}] ❌ 错误 {record.get('skill','?')} | "
                    f"{record.get('error','?'):.120s}")
        return f"[{ts}] {ev} | {record}"

    # ── 高层事件 ──────────────────────────────────────────

    def scan_start(self):
        self._session_start = datetime.datetime.now().isoformat()
        self._session_stats = {k: 0 for k in self._session_stats}
        self._emit("SCAN_START", session=self._session_start)

    def scan_end(self, total_scanned: int = 0, duration_sec: float = 0):
        self._emit("SCAN_END",
                   total=total_scanned or self._session_stats["scanned"],
                   safe=self._session_stats["safe"],
                   warn=self._session_stats["warning"],
                   danger=self._session_stats["danger"],
                   blocked=self._session_stats["blocked"],
                   duration_s=round(duration_sec, 1))

    def skill_scanned(self, name: str, verdict: str, score: int, path: str = "",
                      new: bool = False, modified: bool = False):
        # 评级归类
        if "低风险" in verdict or "未检出" in verdict:
            level = "safe"
            self._session_stats["safe"] += 1
        elif "中高风险" in verdict or "🔴" in verdict:
            level = "danger"
            self._session_stats["danger"] += 1
        elif "需关注" in verdict or "🟡" in verdict:
            level = "warning"
            self._session_stats["warning"] += 1
        elif "高风险" in verdict:
            level = "critical"
            self._session_stats["danger"] += 1
        else:
            level = "safe"
            self._session_stats["safe"] += 1
        self._session_stats["scanned"] += 1
        if new:
            self._session_stats["new"] += 1
        if modified:
            self._session_stats["modified"] += 1
        self._emit("SKILL_SCANNED", skill=name, verdict=verdict,
                   score=score, path=path, level=level,
                   new=new, modified=modified)

    def finding(self, skill_name: str, sev: str, label: str, line: int = 0,
                snippet: str = ""):
        self._emit("FINDING", skill=skill_name, sev=sev, label=label,
                   line=line, snippet=snippet[:200] if snippet else "")

    def alert(self, skill_name: str, reason: str = ""):
        self._emit("ALERT", skill=skill_name, reason=reason)

    def skill_added(self, name: str, path: str):
        self._session_stats["new"] += 1
        self._emit("SKILL_ADDED", skill=name, path=path)

    def skill_modified(self, name: str, path: str):
        self._session_stats["modified"] += 1
        self._emit("SKILL_MODIFIED", skill=name, path=path)

    def update_poisoning(self, name: str, signals: list):
        """v2.5.0：更新投毒告警——版本更新后新增的高危信号（仅记信号标识，不写 Skill 原文）。"""
        self._emit("UPDATE_POISONING", skill=name, signals=list(signals)[:20])

    def quarantine_action(self, name: str, reason: str = ""):
        self._session_stats["blocked"] += 1
        self._emit("QUARANTINE", skill=name, reason=reason)

    def ignore_pattern(self, pattern: str, reason: str = ""):
        self._emit("IGNORE", pattern=pattern, reason=reason)

    def error(self, skill_name: str, error_msg: str):
        self._session_stats["errors"] += 1
        self._emit("SCAN_ERROR", skill=skill_name, error=error_msg[:200])

    # ── 统计与查询 ──────────────────────────────────────────

    def get_stats(self) -> dict:
        """当前会话统计。"""
        return dict(self._session_stats)

    def get_history(self, days: int = 30) -> list:
        """返回最近 N 天的扫描摘要列表。"""
        history = []
        for f in sorted(self.log_root.glob("scan_*.log"), reverse=True):
            try:
                with open(f, encoding="utf-8") as fh:
                    for line in fh:
                        if '"event":"SCAN_END"' in line:
                            rec = json.loads(line)
                            history.append(rec)
            except Exception:
                pass
            if len(history) >= 100:
                break
        return history

    def last_scan_time(self) -> str:
        """最近一次扫描完成时间（ISO），无记录则返回空字符串。"""
        for f in sorted(self.log_root.glob("scan_*.log"), reverse=True):
            try:
                with open(f, encoding="utf-8") as fh:
                    lines = fh.readlines()
                for line in reversed(lines):
                    if '"event":"SCAN_END"' in line:
                        return json.loads(line).get("ts", "")
            except Exception:
                pass
        return ""

    @staticmethod
    def rotate(keep_days: int = LOG_RETENTION_DAYS):
        """删除超过保留天数的旧日志。"""
        now = datetime.date.today()
        for f in LOG_ROOT.glob("scan_*.log"):
            try:
                stem = f.stem.replace("scan_", "")
                d = datetime.date.fromisoformat(stem)
                if (now - d).days > keep_days:
                    f.unlink(missing_ok=True)
                    txt = f.with_suffix(".txt")
                    if txt.exists():
                        txt.unlink(missing_ok=True)
            except (ValueError, OSError):
                pass
