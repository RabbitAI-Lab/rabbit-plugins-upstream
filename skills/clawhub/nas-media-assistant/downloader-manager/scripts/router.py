#!/usr/bin/env python3
"""下载路由器 — 链接分类、适配器选择、去重、监控、完成/失败事件。

支持两种下载器（完全解耦）：
  - qBittorrent: magnet / http(s).torrent（BT 生态，种子管理）
  - 迅雷 Cloud MCP: ed2k / thunder:// / magnet / http(s)（全协议）

用法:
  router.py add <url> [--name NAME] [--category CAT] [--adapter xunlei|qbittorrent]
  router.py status <job_id>
  router.py list [--adapter xunlei|qbittorrent]
  router.py monitor <job_id> [--timeout 3600]
  router.py health
  router.py tools
"""
from __future__ import annotations
import argparse
import json
import logging
import os
import re
import sys
import time
import uuid

# 确保 import 路径
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPTS_DIR)

from base import (BaseAdapter, LinkType, TaskState,  # noqa: E402
                  TaskStatus, classify_link)
from job_manager import JobManager, JobState  # noqa: E402
from utils.thunderlink import try_decode  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("router")

# ---------- 适配器构建 ----------
# 所有 secrets 仅通过 os.environ 注入,本仓库不读任何本地文件:
#   - NAS 容器:由首次启动 agent 引导用户输入后写入进程环境
#   - 本地调试:直接 export XUNLEI_SSE_URL=...
# 避免硬编码任何用户名/路径/文件,符合开源项目的"零隐私"原则。


def _read_sse_url() -> str:
    """从环境变量读取迅雷 SSE URL（agent 首次加载时由用户输入注入）。"""
    return os.environ.get("XUNLEI_SSE_URL", "")


def _build_xunlei_adapter() -> BaseAdapter | None:
    """构建迅雷 Cloud MCP 适配器。"""
    sse_url = _read_sse_url()
    if not sse_url:
        logger.warning("未找到迅雷 SSE URL，迅雷适配器不可用")
        return None
    from adapters.xunlei_cloud_adapter import XunleiCloudAdapter
    return XunleiCloudAdapter(sse_url)


def _build_qb_adapter() -> BaseAdapter | None:
    """构建 qBittorrent 适配器（兼容 DOWNLOADER_* 别名）。

    所有配置仅从 os.environ 读取,无任何默认值/兜底/凭据占位:
      - NAS 容器:由 agent 首次加载时引导用户输入,写入进程环境
      - 本地调试:export QB_URL=... QB_USER=... QB_PASS=...
    """
    url = os.environ.get("QB_URL") or os.environ.get("DOWNLOADER_URL", "")
    user = os.environ.get("QB_USER") or os.environ.get("DOWNLOADER_USER", "")
    pwd = os.environ.get("QB_PASS") or os.environ.get("DOWNLOADER_PASS", "")
    save_path = os.environ.get("QB_SAVE_PATH", "/downloads")  # 容器内约定路径
    if not url or not user or not pwd:
        logger.warning("qBittorrent 适配器不可用:缺少 QB_URL / QB_USER / QB_PASS")
        return None
    from adapters.qbittorrent_adapter import QbittorrentAdapter
    return QbittorrentAdapter(url, user, pwd, save_path)


def _get_adapters() -> dict[str, BaseAdapter]:
    """构建所有可用适配器（各适配器独立初始化，互不影响）。"""
    adapters: dict[str, BaseAdapter] = {}
    xl = _build_xunlei_adapter()
    if xl:
        adapters["xunlei"] = xl
    qb = _build_qb_adapter()
    if qb:
        adapters["qbittorrent"] = qb
    return adapters


# ---------- 适配器选择 ----------

def select_adapter(adapters: dict[str, BaseAdapter],
                   link_type: LinkType,
                   preferred: str = "") -> BaseAdapter | None:
    """选择适配器（迅雷会员优先，回退 qBittorrent）。

    规则:
      所有协议 -> 迅雷优先（会员高速下载，全协议支持）
      迅雷不可用 -> qBittorrent（仅 magnet/http）
    """
    # 用户显式指定优先
    if preferred and preferred in adapters:
        a = adapters[preferred]
        if a.supports_link_type(link_type):
            return a
        logger.warning("指定适配器 %s 不支持 %s", preferred, link_type.value)

    # 迅雷优先（会员，全协议支持）
    xl = adapters.get("xunlei")
    if xl and xl.supports_link_type(link_type):
        return xl

    # 迅雷不可用时回退 qBittorrent（仅 magnet/http）
    qb = adapters.get("qbittorrent")
    if qb and qb.supports_link_type(link_type):
        return qb
    return None


# ---------- 去重检查 ----------

def _find_duplicate(adapters: dict[str, BaseAdapter],
                    jm: JobManager, url: str, name: str = "") -> dict | None:
    """检查是否已有相同任务（避免重复下载）。

    1. 查 JobManager 中活跃任务的 URL
    2. 查各适配器任务列表中同名任务
    """
    # 1. JobManager 活跃任务去重
    for job in jm.list_active():
        if job.url == url:
            return {"job_id": job.job_id, "reason": "URL 已存在活跃任务",
                    "adapter": job.adapter, "task_id": job.task_id}
    # 2. 适配器任务列表去重（按名称匹配）
    if name:
        for aname, a in adapters.items():
            for t in a.list_tasks():
                if t.name and t.name == name and not t.is_terminal:
                    return {"job_id": "", "reason": f"适配器 {aname} 已有同名任务",
                            "adapter": aname, "task_id": t.task_id}
    return None


# ---------- 元数据携带（media-search -> downloader -> media-organizer）----------

def _load_metadata(args) -> list:
    """从 --metadata(JSON) 或 --metadata-file 读取 media-lookup 归一化元数据。

    接受单个对象 {...} 或数组 [{...}]，统一归一为 list。
    来源链路: media-search(携 media-lookup 元数据) -> add --metadata -> Job.meta
    -> download_completed 事件回传 -> 编排器喂给 media-organizer --metadata。
    """
    raw = None
    mf = getattr(args, "metadata_file", "") or ""
    if mf:
        with open(mf, encoding="utf-8") as f:
            raw = json.load(f)
    else:
        ms = getattr(args, "metadata", "") or ""
        if ms:
            raw = json.loads(ms)
    if not raw:
        return []
    if isinstance(raw, dict):
        return [raw]
    if isinstance(raw, list):
        return [e for e in raw if isinstance(e, dict)]
    return []


def _job_metadata(job) -> list:
    """从 Job 取出携带的 media-lookup 元数据列表（无则空）。"""
    if job and getattr(job, "meta", None):
        md = job.meta.get("media_metadata")
        if isinstance(md, list):
            return md
    return []



# ---------- CLI 命令 ----------

def cmd_add(args):
    """添加下载任务（含链接分类、适配器选择、去重、Job 创建）。"""
    url = args.url
    real_url = try_decode(url)  # thunder:// 等专用链接解码
    # 本地 .torrent 文件 -> 强制 qBittorrent（迅雷不支持文件上传）
    is_torrent_file = real_url.startswith("/") and real_url.lower().endswith(".torrent")
    if is_torrent_file:
        lt = LinkType.HTTP
        if not args.adapter:
            args.adapter = "qbittorrent"
    else:
        lt = classify_link(real_url)

    adapters = _get_adapters()
    if not adapters:
        print(json.dumps({"success": False, "error": "无可用适配器"}))
        return

    adapter = select_adapter(adapters, lt, args.adapter)
    if not adapter:
        print(json.dumps({"success": False,
                          "error": f"无适配器支持链接类型 {lt.value}"}))
        return

    jm = JobManager()

    # --- 去重检查 ---
    dup = _find_duplicate(adapters, jm, real_url, args.name)
    if dup:
        dup["success"] = True
        dup["message"] = f"跳过重复下载: {dup['reason']}"
        print(json.dumps(dup, ensure_ascii=False, indent=2))
        return

    logger.info("选择适配器: %s (链接类型: %s)", adapter.name, lt.value)

    # --- 解析携带的元数据（media-search 经 media-lookup 取回，随下载链路沉淀）---
    media_metadata = _load_metadata(args)

    # --- 提交任务 ---
    save_path = args.save_path or os.environ.get("QB_SAVE_PATH", "")
    result = adapter.add_task(
        url=real_url, name=args.name or "",
        save_path=save_path, category=args.category or "",
    )

    # --- 创建 Job 记录（元数据存入 meta 域，完成时随事件回传）---
    job_id = f"dl_{int(time.time())}_{uuid.uuid4().hex[:6]}"
    jm.create(job_id, real_url, adapter.name,
              task_id=result.task_id, name=args.name or "",
              media_type=args.category or "",
              state=JobState.QUEUED if result.success else JobState.ERROR,
              error=result.error,
              meta={"media_metadata": media_metadata} if media_metadata else {})

    out = {
        "success": result.success,
        "job_id": job_id,
        "adapter": adapter.name,
        "task_id": result.task_id,
        "message": result.message,
        "error": result.error,
        "link_type": lt.value,
        "download_dir": adapter.download_dir,
        "metadata": media_metadata,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_status(args):
    """查询任务状态（支持 job_id 或 task_id）。"""
    jm = JobManager()
    job = jm.get(args.task_id)

    # 优先按 job_id 查找
    if job:
        adapters = _get_adapters()
        adapter = adapters.get(job.adapter)
        if adapter:
            s = adapter.query_task(job.task_id)
            jm.update(job.job_id, state=_map_state(s.state),
                      progress=s.progress, error=s.error)
            print(json.dumps({
                "job_id": job.job_id, "task_id": s.task_id, "name": s.name,
                "state": s.state.value, "progress": s.progress,
                "size": s.size, "speed": s.speed, "error": s.error,
                "adapter": job.adapter,
            }, ensure_ascii=False, indent=2))
            return

    # 回退: 按 task_id 搜索所有适配器
    adapters = _get_adapters()
    adapter = adapters.get(args.adapter) if args.adapter else None
    if adapter is None:
        for a in adapters.values():
            s = a.query_task(args.task_id)
            if s.state != TaskState.UNKNOWN:
                adapter = a
                break
    if adapter is None and adapters:
        adapter = list(adapters.values())[0]
    if not adapter:
        print(json.dumps({"error": "无可用适配器"}))
        return
    s = adapter.query_task(args.task_id)
    print(json.dumps({
        "task_id": s.task_id, "name": s.name,
        "state": s.state.value, "progress": s.progress,
        "size": s.size, "speed": s.speed, "error": s.error,
        "adapter": adapter.name,
    }, ensure_ascii=False, indent=2))


def cmd_list(args):
    """列出所有任务（跨适配器聚合）。"""
    adapters = _get_adapters()
    all_tasks = []
    for name, a in adapters.items():
        if args.adapter and args.adapter != name:
            continue
        for t in a.list_tasks():
            all_tasks.append({
                "task_id": t.task_id, "name": t.name,
                "state": t.state.value, "progress": t.progress,
                "size": t.size, "adapter": name,
            })
    print(json.dumps({"total": len(all_tasks), "tasks": all_tasks},
                     ensure_ascii=False, indent=2))


def cmd_monitor(args):
    """监控任务直到完成/失败/超时，输出结构化事件。

    迅雷优先下载，检测到慢速或卡死时自动切换 qBittorrent（仅一次）。
    完成时输出 download_completed（含 file_path 供 media-organizer 使用）。
    """
    jm = JobManager()
    job = jm.get(args.task_id)

    # 确定 adapter 和 task_id
    adapters = _get_adapters()
    if job:
        adapter = adapters.get(job.adapter)
        task_id = job.task_id
        if not adapter:
            print(json.dumps({"error": f"Job {args.task_id} 的适配器 {job.adapter} 不可用"}))
            return
    else:
        # 回退: 按 task_id 搜索所有适配器
        adapter = adapters.get(args.adapter) if args.adapter else None
        task_id = args.task_id
        if adapter is None:
            for a in adapters.values():
                s = a.query_task(task_id)
                if s.state != TaskState.UNKNOWN:
                    adapter = a
                    break
        if adapter is None and adapters:
            adapter = list(adapters.values())[0]
        if not adapter:
            print(json.dumps({"error": "无可用适配器"}))
            return

    # --- 轮询监控 ---
    timeout = args.timeout
    start = time.time()
    last_progress = -1.0
    stall_count = 0
    speed_history: list[int] = []
    switched = False  # 是否已切换过适配器（只切换一次）

    STALL_THRESHOLD = 20   # 20 * 30s = 10 分钟无进度
    SLOW_THRESHOLD = 50 * 1024   # 50KB/s 低速阈值
    SLOW_POLL_COUNT = 10  # 10 * 30s = 5 分钟持续低速

    while time.time() - start < timeout:
        s = adapter.query_task(task_id)
        now = time.time() - start

        if s.progress != last_progress:
            logger.info("[%3.0fs] %s | %s | %5.1f%% | %s | %dMB/s",
                        now, s.name[:40], s.state.value,
                        s.progress,
                        f"{s.size/1e9:.1f}GB" if s.size else "?",
                        s.speed // 1048576)

        # --- 完成: 输出 download_completed 事件 ---
        if s.state == TaskState.COMPLETED:
            file_path = adapter.get_file_path(task_id)
            if job:
                jm.update(job.job_id, state=JobState.COMPLETED,
                          progress=100.0, task_id=task_id)
            event = {
                "event": "download_completed",
                "job_id": job.job_id if job else "",
                "client": adapter.name,
                "file_path": file_path,
                "task_id": task_id,
                "name": s.name,
                "size": s.size,
                "elapsed": round(now),
                "metadata": _job_metadata(job),
            }
            print(json.dumps(event, ensure_ascii=False, indent=2))
            return

        # --- 错误状态 ---
        if s.state == TaskState.ERROR:
            if job:
                jm.update(job.job_id, state=JobState.ERROR, error=s.error)
            _emit_failure(job, s.error or "下载器返回错误状态",
                          "DL_UNKNOWN", "investigate")
            return

        # --- 停滞检测 ---
        if s.progress == last_progress:
            stall_count += 1
        else:
            stall_count = 0
        last_progress = s.progress

        # --- 慢速检测 ---
        speed_history.append(s.speed)
        if len(speed_history) > SLOW_POLL_COUNT:
            speed_history.pop(0)

        # --- 判断是否需要切换适配器 ---
        need_switch = False
        switch_reason = ""

        if stall_count >= STALL_THRESHOLD and s.state == TaskState.DOWNLOADING:
            need_switch = True
            switch_reason = f"任务停滞 {STALL_THRESHOLD * 30 // 60} 分钟无进度，判为死链"

        if (len(speed_history) >= SLOW_POLL_COUNT
                and s.state == TaskState.DOWNLOADING):
            avg_speed = sum(speed_history) / len(speed_history)
            if avg_speed < SLOW_THRESHOLD:
                need_switch = True
                switch_reason = (f"持续 {SLOW_POLL_COUNT * 30 // 60} 分钟"
                                 f"平均速度 {int(avg_speed / 1024)}KB/s 低于阈值")

        if need_switch:
            # 尝试切换到 qBittorrent（仅一次）
            if not switched and adapter.name == "xunlei":
                new_info = _switch_to_qbittorrent(
                    adapters, adapter, task_id, job, jm, s.name)
                if new_info:
                    adapter, task_id = new_info
                    switched = True
                    stall_count = 0
                    speed_history = []
                    last_progress = -1.0
                    logger.info("已从迅雷切换到 qBittorrent，继续监控")
                    continue
            # 无法切换或已切换过 -> 输出失败
            if job:
                jm.update(job.job_id, state=JobState.ERROR, error=switch_reason)
            _emit_failure(job, switch_reason, "DL_DEAD", "switch_link")
            return

        time.sleep(30)

    # --- 超时 ---
    if job:
        jm.update(job.job_id, state=JobState.ERROR, error="监控超时")
    print(json.dumps({
        "event": "download_timeout",
        "job_id": job.job_id if job else "",
        "task_id": task_id,
        "message": f"监控超时 {timeout}s",
    }, ensure_ascii=False, indent=2))

def _switch_to_qbittorrent(adapters: dict[str, BaseAdapter],
                              current_adapter: BaseAdapter,
                              task_id: str, job, jm: JobManager,
                              task_name: str):
    """从迅雷切换到 qBittorrent（慢速/卡死时自动触发）。

    1. 删除当前迅雷任务
    2. 用相同 URL 创建 qBittorrent 任务
    3. 更新 Job 记录

    返回 (新 adapter, 新 task_id) 或 None（无法切换）。
    """
    qb = adapters.get("qbittorrent")
    if not qb:
        logger.warning("qBittorrent 适配器不可用，无法切换")
        return None

    # 从 Job 获取原始 URL
    url = job.url if job else ""
    if not url:
        logger.warning("无法获取原始 URL，无法切换")
        return None

    # qB 仅支持 magnet/http（ed2k/thunder 无法切换）
    lt = classify_link(url)
    if not qb.supports_link_type(lt):
        logger.warning("qBittorrent 不支持 %s 链接，无法切换", lt.value)
        return None

    # 1. 删除迅雷任务
    logger.info("删除迅雷任务 %s，准备切换 qBittorrent", task_id)
    current_adapter.cancel_task(task_id)

    # 2. 创建 qBittorrent 任务
    save_path = os.environ.get("QB_SAVE_PATH", "/downloads")
    result = qb.add_task(url=url, name=task_name, save_path=save_path)
    if not result.success:
        logger.error("qBittorrent 创建任务失败: %s", result.error)
        return None

    # 3. 更新 Job
    if job:
        jm.update(job.job_id, adapter="qbittorrent",
                 task_id=result.task_id, state=JobState.DOWNLOADING)

    logger.info("qBittorrent 任务已创建: %s", result.task_id)
    return qb, result.task_id


def _emit_failure(job, msg: str, code: str, action: str):
    """输出结构化失败事件（供编排器换链/回报用户）。

    同时回传携带的元数据：换链重试时编排器可复用同一元数据，
    或在放弃后连同 metadata 转交 media-organizer 做部分归档。
    """
    print(json.dumps({
        "event": "download_failed",
        "job_id": job.job_id if job else "",
        "metadata": _job_metadata(job),
        "failure": {
            "code": code,
            "msg": msg,
            "suggested_action": action,
        },
    }, ensure_ascii=False, indent=2))


def _map_state(ts: TaskState) -> JobState:
    """TaskState -> JobState 映射。"""
    return {
        TaskState.COMPLETED: JobState.COMPLETED,
        TaskState.ERROR: JobState.ERROR,
        TaskState.PAUSED: JobState.QUEUED,
        TaskState.DOWNLOADING: JobState.DOWNLOADING,
        TaskState.QUEUED: JobState.QUEUED,
        TaskState.UNKNOWN: JobState.QUEUED,
    }.get(ts, JobState.QUEUED)


def cmd_health(args):
    """适配器健康检查（各自独立，互不影响）。"""
    adapters = _get_adapters()
    results = {}
    for name, a in adapters.items():
        ok = a.health_check()
        results[name] = "✅ 健康" if ok else "❌ 不可用"
        print(f"  {name}: {'✅ 健康' if ok else '❌ 不可用'}")
    print(json.dumps({"adapters": results}, ensure_ascii=False))


def cmd_tools(args):
    """列出迅雷 MCP 可用工具。"""
    xl = _build_xunlei_adapter()
    if not xl:
        print(json.dumps({"error": "迅雷适配器不可用"}))
        return
    if xl._client.connect():
        tools = xl._client.list_tools()
        print(json.dumps({"tools": [
            {"name": t.get("name"), "description": t.get("description", "")[:120]}
            for t in tools
        ]}, ensure_ascii=False, indent=2))
    else:
        print(json.dumps({"error": "迅雷 MCP 连接失败"}))
    xl.disconnect()


def main():
    p = argparse.ArgumentParser(description="下载路由器")
    sub = p.add_subparsers(dest="command")

    p_add = sub.add_parser("add", help="添加下载任务")
    p_add.add_argument("url")
    p_add.add_argument("--name", default="")
    p_add.add_argument("--category", default="")
    p_add.add_argument("--save-path", default="")
    p_add.add_argument("--adapter", default="", choices=["", "xunlei", "qbittorrent"])
    p_add.add_argument("--metadata", default="",
                       help="携带的 media-lookup 归一化元数据(JSON, 单对象或数组)")
    p_add.add_argument("--metadata-file", default="",
                       help="同 --metadata, 从文件读(大体积优先)")

    p_status = sub.add_parser("status", help="查询任务状态")
    p_status.add_argument("task_id", help="job_id 或 task_id")
    p_status.add_argument("--adapter", default="")

    p_list = sub.add_parser("list", help="列出所有任务")
    p_list.add_argument("--adapter", default="")

    p_mon = sub.add_parser("monitor", help="监控任务直到完成/失败/超时")
    p_mon.add_argument("task_id", help="job_id 或 task_id")
    p_mon.add_argument("--adapter", default="")
    p_mon.add_argument("--timeout", type=int, default=3600)

    sub.add_parser("health", help="适配器健康检查")
    sub.add_parser("tools", help="列出迅雷 MCP 工具")

    args = p.parse_args()
    if not args.command:
        p.print_help()
        return
    {
        "add": cmd_add, "status": cmd_status, "list": cmd_list,
        "monitor": cmd_monitor, "health": cmd_health, "tools": cmd_tools,
    }[args.command](args)


if __name__ == "__main__":
    main()
