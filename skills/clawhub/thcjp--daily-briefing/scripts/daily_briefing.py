#!/usr/bin/env python3
"""每日动态任务清单聚合器

从三省六部各部门汇总待办事项，生成个性化今日任务清单。
支持QQBot和企业微信推送。

用法:
  python daily_briefing.py
  python daily_briefing.py --mode weekly
  python daily_briefing.py --push qqbot
  python daily_briefing.py --push wecom
  python daily_briefing.py --push stdout
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from typing import Any, List

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))  # T4-4: 添加项目根以支持mcps.shared导入
from mcps.shared.db_logger import get_logger
logger = get_logger("daily-briefing", source="skills/daily-briefing/scripts/daily_briefing.py")

# 添加scripts/到sys.path(atomic_write所在目录)
_SCRIPTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "scripts")
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)
from mcps.shared.atomic_write import atomic_read_json, atomic_write_json

BRIEFING_DIR = os.environ.get("BRIEFING_DIR", "d:/JueJin/data/briefing")
os.makedirs(BRIEFING_DIR, exist_ok=True)

try:
    from mcp_caller import call_mcp as _call_mcp_safe
    MCP_CALLER_AVAILABLE = True
except ImportError:
    MCP_CALLER_AVAILABLE = False
    logger.error("mcp_caller不可用，将使用requests直连模式")


def _http_request(method: str, url: str, **kwargs) -> dict:
    """统一HTTP请求包装器（优先使用mcp_caller）"""
    timeout = kwargs.pop('timeout', 10)

    if MCP_CALLER_AVAILABLE and 'alist' in url.lower():
        try:
            return _call_mcp_safe(
                "alist-mcp",
                "request",
                {"method": method, "url": url, **kwargs},
                timeout=timeout
            )
        except Exception as e:
            logger.error(f"mcp_caller调用失败({url}), 降级到requests: {e}")

    import requests
    try:
        resp = getattr(requests, method.lower())(url, timeout=timeout, **kwargs)
        if resp.status_code == 200:
            try:
                return {"success": True, "data": resp.json()}
            except ValueError:
                return {"success": True, "data": {"raw": resp.text[:1000]}}
        return {"success": False, "error": f"HTTP {resp.status_code}", "code": f"HTTP_{resp.status_code}"}
    except Exception as e:
        logger.error(f"HTTP请求失败 [{method}] {url}: {e}")
        return {"success": False, "error": str(e), "code": "REQUEST_FAILED"}


def _check_service_health(service_name: str, url: str, timeout: int = 5) -> dict:
    result = _http_request('get', f"{url}/health", timeout=timeout)
    return {"service": service_name, "healthy": result.get('success', False)}


def hubu_tasks() -> List[dict]:
    """户部(财务)汇总: 销售数据异常检查(优先postgres直查，降级HTTP接口)

    Returns:
        List[dict]: 返回值说明
    """
    tasks = []
    try:
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        gmv = 0.0
        orders = 0
        prev_gmv = 0.0
        data_source = ""

        # 优先：postgres直查
        conn = None
        try:
            # 全局视图: daily-briefing查询全局GMV,有意绕过RLS,非bug
            # R75.2/E-3修复: 使用db_pool统一连接(替代psycopg2.connect碎片化)
            from mcps.shared.db_pool import get_connection, return_connection
            conn = get_connection()
            if conn:
                cur = conn.cursor()
                cur.execute(
                    "SELECT COALESCE(SUM(price*quantity),0), COUNT(*) FROM orders WHERE created_at >= %s AND created_at < %s",
                    (yesterday, datetime.now().strftime("%Y-%m-%d"))
                )
                row = cur.fetchone()
                gmv = float(row[0]) if row else 0.0
                orders = int(row[1]) if row else 0
                # 前日GMV
                day_before = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")
                cur.execute(
                    "SELECT COALESCE(SUM(price*quantity),0) FROM orders WHERE created_at >= %s AND created_at < %s",
                    (day_before, yesterday)
                )
                prev_row = cur.fetchone()
                prev_gmv = float(prev_row[0]) if prev_row else 0.0
                data_source = "postgres"
        except Exception as e:
            logger.error(f"[daily-briefing] 户部postgres直查失败: {e}")
        finally:
            if conn:
                try:
                    return_connection(conn)
                except Exception as _e:
                    logger.error(f"[daily-briefing] 连接归还失败: {_e}")

        # 降级：HTTP接口
        if not data_source:
            try:
                agent_url = os.environ.get("XIANYU_AUTO_REPLY_URL", "http://localhost:8090")
                result = _http_request('get',
                    f"{agent_url}/api/sales/daily",
                    params={"date": yesterday},
                    timeout=10
                )
                if result.get('success'):
                    data = result.get('data', {})
                    gmv = data.get("gmv", 0)
                    orders = data.get("orders", 0)
                    prev_gmv = data.get("prev_gmv", 0)
                    data_source = "http_api"
            except Exception as e:
                logger.error(f"[daily-briefing] 户部HTTP接口也失败: {e}")

        if not data_source:
            tasks.append({
                "department": "户部",
                "priority": "P2",
                "task": "查看昨日销售日报(数据不可用: postgres和HTTP接口均失败)",
                "action": "手动检查销售数据",
            })
            return tasks

        if orders < 3:
            tasks.append({
                "department": "户部",
                "priority": "P0",
                "task": f"昨日仅{orders}笔订单(阈值<3)，检查商品曝光和流量",
                "action": "检查商品曝光量+浏览量+我想要数",
            })

        if prev_gmv > 0 and gmv > 0:
            change = (gmv - prev_gmv) / prev_gmv
            if change < -0.2:
                tasks.append({
                    "department": "户部",
                    "priority": "P0",
                    "task": f"昨日GMV环比下降{abs(change)*100:.0f}%，分析流量原因",
                    "action": "分析流量来源+竞品动态+平台算法变化",
                })

        tasks.append({
            "department": "户部",
            "priority": "P2",
            "task": f"查看昨日销售日报(GMV: ¥{gmv}, 订单: {orders}笔)",
            "action": "查看详细销售数据",
            "summary_data": {"gmv": gmv, "orders": orders},
        })
    except Exception as e:
        logger.error(f"daily briefing异常: {e}", exc_info=True)
        tasks.append({
            "department": "户部",
            "priority": "P2",
            "task": f"户部数据汇总失败: {e}",
            "action": "手动检查销售数据",
        })
    return tasks


def _read_delivery_tracking() -> dict:
    """直接读取delivery_tracking.json，替代delivery_security.py导入"""
    tracking = {"active": 0, "expired": 0, "redeliverable": 0, "expiring_soon": 0, "records": []}
    # 尝试多个可能路径
    candidates = [
        os.path.join(BRIEFING_DIR, "..", "openclaw", "delivery_tracking.json"),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "data", "openclaw", "delivery_tracking.json"),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "data", "delivery_tracking.json"),
    ]
    for path in candidates:
        abs_path = os.path.abspath(path)
        if os.path.exists(abs_path):
            try:
                data = atomic_read_json(abs_path)
                if data is None:
                    continue
                if isinstance(data, list):
                    now = datetime.now()
                    for rec in data:
                        status = rec.get("status", "")
                        if status == "active":
                            tracking["active"] += 1
                            expires_at = rec.get("expires_at", "")
                            if expires_at:
                                try:
                                    exp_time = datetime.fromisoformat(expires_at)
                                    if (exp_time - now).days <= 1:
                                        tracking["expiring_soon"] += 1
                                except (ValueError, TypeError) as e:
                                    logger.debug(f"[daily-briefing] 过期时间解析失败: {e}")
                        elif status == "expired":
                            tracking["expired"] += 1
                            if rec.get("redeliverable", False):
                                tracking["redeliverable"] += 1
                    tracking["records"] = data[:20]
                elif isinstance(data, dict):
                    tracking.update({k: data.get(k, tracking.get(k, 0)) for k in ["active", "expired", "redeliverable", "expiring_soon"]})
                return tracking
            except Exception as e:
                logger.error(f"[daily-briefing] 读取delivery_tracking.json失败({abs_path}): {e}")
    return tracking


def bingbu_tasks() -> List[dict]:
    """兵部(执行)汇总: 待处理订单/发货/重发(优先直接读取JSON，降级导入delivery_security)

    Returns:
        List[dict]: 返回值说明
    """
    tasks = []
    try:
        stats = None
        redeliverable_count = 0
        expiring_count = 0

        # 优先：直接读取delivery_tracking.json
        tracking = _read_delivery_tracking()
        if tracking.get("records") or tracking.get("active", 0) > 0 or tracking.get("expired", 0) > 0:
            stats = {"active": tracking["active"], "expired": tracking["expired"], "redeliverable": tracking["redeliverable"]}
            redeliverable_count = tracking["redeliverable"]
            expiring_count = tracking.get("expiring_soon", 0)

        # 降级：导入delivery_security.py
        if stats is None:
            try:
                sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "mcps", "shared"))
                from delivery_security import delivery_tracker
                redeliverable = delivery_tracker.find_redeliverable()
                if redeliverable:
                    redeliverable_count = len(redeliverable)
                    tasks.append({
                        "department": "兵部",
                        "priority": "P1",
                        "task": f"{len(redeliverable)}个买家请求重发过期链接",
                        "action": "执行auto-delivery --redeliver",
                        "details": [{"buyer_id": r.buyer_id, "product": r.product_name} for r in redeliverable[:5]],
                    })
                expiring = delivery_tracker.find_expiring_soon()
                if expiring:
                    expiring_count = len(expiring)
                stats = delivery_tracker.get_stats()
            except Exception as e:
                logger.error(f"[daily-briefing] delivery_security导入失败: {e}")

        if stats is None:
            tasks.append({
                "department": "兵部",
                "priority": "P2",
                "task": "兵部数据汇总失败: delivery_tracking.json和delivery_security均不可用",
                "action": "手动检查订单状态",
            })
            return tasks

        # 基于stats生成任务(JSON路径)
        if redeliverable_count > 0 and not any(t.get("task", "").startswith(f"{redeliverable_count}个买家") for t in tasks):
            tasks.append({
                "department": "兵部",
                "priority": "P1",
                "task": f"{redeliverable_count}个买家请求重发过期链接",
                "action": "执行auto-delivery --redeliver",
            })

        if expiring_count > 0:
            tasks.append({
                "department": "兵部",
                "priority": "P1",
                "task": f"{expiring_count}个链接即将过期，需发送提醒",
                "action": "执行auto-delivery --check-expiring",
            })

        if stats["active"] > 0 or stats["expired"] > 0:
            tasks.append({
                "department": "兵部",
                "priority": "P2",
                "task": f"发货跟踪: 活跃{stats['active']}条/过期{stats['expired']}条/待重发{stats['redeliverable']}条",
                "action": "查看发货跟踪详情",
            })
    except Exception as e:
        logger.error(f"daily briefing异常: {e}", exc_info=True)
        tasks.append({
            "department": "兵部",
            "priority": "P2",
            "task": f"兵部数据汇总失败: {e}",
            "action": "手动检查订单状态",
        })
    return tasks


def gongbu_tasks() -> List[dict]:
    """工部(基础设施)汇总: 系统健康状态

    Returns:
        List[dict]: 返回值说明
    """
    tasks = []
    services = [
        ("alist", os.environ.get("ALIST_BASE_URL", "http://localhost:5244")),
        ("xianyu-auto-reply", os.environ.get("XIANYU_AUTO_REPLY_URL", "http://localhost:8090")),
        ("gateway", os.environ.get("OPENCLAW_GATEWAY_URL", "http://localhost:18789")),
    ]

    unhealthy = []
    for name, url in services:
        result = _check_service_health(name, url)
        if not result["healthy"]:
            unhealthy.append(name)

    if unhealthy:
        tasks.append({
            "department": "工部",
            "priority": "P0",
            "task": f"服务异常: {', '.join(unhealthy)}，需要修复",
            "action": "检查Docker容器+重启服务",
        })

    try:
        cookie = os.environ.get("XIANYU_COOKIE_1", "")
        if not cookie:
            tasks.append({
                "department": "工部",
                "priority": "P0",
                "task": "闲鱼Cookie未配置，无法自动运营",
                "action": "发送'登录闲鱼'获取Cookie",
            })
    except Exception as e:
        logger.error(f"daily briefing异常: {e}", exc_info=True)
        logger.warning(f"[daily-briefing] Cookie检查失败: {e}")

    try:
        import requests
        dailyhot_url = os.environ.get("DAILYHOT_BASE_URL", "http://localhost:6688")
        resp = requests.get(f"{dailyhot_url}/health", timeout=5)
        if resp.status_code != 200:
            tasks.append({
                "department": "工部",
                "priority": "P1",
                "task": "热搜API不可用，内容选题受影响",
                "action": "重启DailyHotApi服务",
            })
    except Exception as e:
        logger.error(f"[daily_briefing] 热搜API检查失败: {e}")
        tasks.append({
            "department": "工部",
            "priority": "P1",
            "task": "热搜API不可用，内容选题受影响",
            "action": "重启DailyHotApi服务",
        })

    if not tasks:
        tasks.append({
            "department": "工部",
            "priority": "P2",
            "task": "所有服务运行正常",
            "action": None,
        })

    return tasks


def libu_tasks() -> List[dict]:
    """礼部(内容)汇总: 内容发布计划

    Returns:
        List[dict]: 返回值说明
    """
    tasks = []

    invite_url = os.environ.get("COMMUNITY_INVITE_URL", "")
    if not invite_url:
        tasks.append({
            "department": "礼部",
            "priority": "P1",
            "task": "社群邀请链接未配置，发货无法附带邀请卡",
            "action": "配置COMMUNITY_INVITE_URL环境变量",
        })

    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "mcps", "shared"))
        from delivery_security import delivery_tracker
        stats = delivery_tracker.get_stats()
        if stats["active"] > 0:
            tasks.append({
                "department": "礼部",
                "priority": "P2",
                "task": f"当前{stats['active']}个活跃发货链接，社群运营跟进",
                "action": "检查社群入群率和活跃度",
            })
    except Exception as e:
        logger.error(f"daily briefing异常: {e}", exc_info=True)
        logger.warning(f"[daily-briefing] 发货链接统计失败: {e}")

    return tasks


def xingbu_tasks() -> List[dict]:
    """刑部(风控)汇总: 风控告警

    Returns:
        List[dict]: 返回值说明
    """
    tasks = []

    alert_file = os.path.join(BRIEFING_DIR, "..", "openclaw", "alerts.json")
    if os.path.exists(alert_file):
        try:
            alerts = atomic_read_json(alert_file)
            if alerts is None:
                alerts = []
            today_alerts = [a for a in alerts if a.get("date") == datetime.now().strftime("%Y-%m-%d")]
            if today_alerts:
                tasks.append({
                    "department": "刑部",
                    "priority": "P1",
                    "task": f"今日{len(today_alerts)}条风控告警",
                    "action": "查看告警详情并处理",
                })
        except Exception as e:
            logger.error(f"daily briefing异常: {e}", exc_info=True)
            logger.warning(f"[daily-briefing] 风控告警读取失败: {e}")

    return tasks


def libu_hr_tasks() -> List[dict]:
    """吏部(人事)汇总: 账号池状态

    Returns:
        List[dict]: 返回值说明
    """
    tasks = []

    for i in range(1, 4):
        cookie = os.environ.get(f"XIANYU_COOKIE_{i}", "")
        if not cookie:
            tasks.append({
                "department": "吏部",
                "priority": "P1",
                "task": f"{i}号账号Cookie未配置",
                "action": f"发送'登录闲鱼'获取{i}号账号Cookie",
            })

    return tasks


def aggregate_tasks(mode: str = "daily") -> dict[str, Any]:
    """汇总所有部门任务

    Args:
        mode (str): 参数说明

    Returns:
        dict[str, Any]: 返回值说明
    """
    all_tasks = []
    all_tasks.extend(hubu_tasks())
    all_tasks.extend(bingbu_tasks())
    all_tasks.extend(gongbu_tasks())
    all_tasks.extend(libu_tasks())
    all_tasks.extend(xingbu_tasks())
    all_tasks.extend(libu_hr_tasks())

    priority_order = {"P0": 0, "P1": 1, "P2": 2}
    all_tasks.sort(key=lambda t: priority_order.get(t.get("priority", "P2"), 2))

    p0_tasks = [t for t in all_tasks if t.get("priority") == "P0"]
    p1_tasks = [t for t in all_tasks if t.get("priority") == "P1"]
    p2_tasks = [t for t in all_tasks if t.get("priority") == "P2"]

    summary_data = {}
    for t in all_tasks:
        if "summary_data" in t:
            summary_data.update(t["summary_data"])

    return {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "mode": mode,
        "total": len(all_tasks),
        "p0_count": len(p0_tasks),
        "p1_count": len(p1_tasks),
        "p2_count": len(p2_tasks),
        "p0_tasks": p0_tasks,
        "p1_tasks": p1_tasks,
        "p2_tasks": p2_tasks,
        "summary": summary_data,
    }


def format_qqbot_message(briefing: dict) -> str:
    """格式化为QQBot推送消息

    Args:
        briefing (dict): 参数说明

    Returns:
        str: 返回值说明
    """
    date = briefing["date"]
    lines = [
        f"📋 今日任务清单 | {date}",
        "━━━━━━━━━━━━━━━━━━━━━━",
    ]

    if briefing["p0_tasks"]:
        lines.append(f"🔴 紧急(P0) - {briefing['p0_count']}项")
        for i, t in enumerate(briefing["p0_tasks"], 1):
            lines.append(f"  {i}. [{t['department']}] {t['task']}")

    if briefing["p1_tasks"]:
        start = briefing["p0_count"] + 1
        lines.append(f"🟡 重要(P1) - {briefing['p1_count']}项")
        for i, t in enumerate(briefing["p1_tasks"], start):
            lines.append(f"  {i}. [{t['department']}] {t['task']}")

    if briefing["p2_tasks"]:
        start = briefing["p0_count"] + briefing["p1_count"] + 1
        lines.append(f"🟢 常规(P2) - {briefing['p2_count']}项")
        for i, t in enumerate(briefing["p2_tasks"], start):
            lines.append(f"  {i}. [{t['department']}] {t['task']}")

    if briefing["summary"]:
        gmv = briefing["summary"].get("gmv", "N/A")
        orders = briefing["summary"].get("orders", "N/A")
        lines.append("")
        lines.append("📊 昨日概览")
        lines.append(f"  GMV: ¥{gmv} | 订单: {orders}笔")

    lines.append("━━━━━━━━━━━━━━━━━━━━━━")
    lines.append('回复"详情 N"查看任务详情')
    lines.append('回复"完成 N"标记任务完成')

    return "\n".join(lines)


def push_to_qqbot(message: str) -> dict[str, Any]:
    """推送消息到QQBot（通过统一通知器）

    Args:
        message (str): 参数说明

    Returns:
        dict[str, Any]: 返回值说明
    """
    try:
        from scripts.notification import send_alert
        result = send_alert(message, level="INFO")
        if result.get("success"):
            return {"success": True, "data": {"channel": "qqbot", "method": result.get("method"), "status": "sent"}}
        return {"success": False, "error": result.get("error", "QQBot推送降级")}
    except Exception as e:
        logger.error(f"QQBot推送异常: {e}")
        return {"success": False, "error": f"QQBot推送异常: {e}"}


def push_to_wecom(message: str) -> dict[str, Any]:
    """已废弃：所有通知统一通过QQBot发送

    Args:
        message (str): 参数说明

    Returns:
        dict[str, Any]: 返回值说明
    """
    logger.warning("push_to_wecom 已废弃，自动重定向到QQBot")
    return push_to_qqbot(message)


def main() -> int:
    """main

    Returns:
        int: 返回值说明
    """
    parser = argparse.ArgumentParser(description="每日动态任务清单聚合器")
    parser.add_argument("--mode", default="daily", choices=["daily", "weekly"], help="清单模式")
    parser.add_argument("--push", default="stdout", choices=["qqbot", "wecom", "stdout", "all"], help="推送渠道")
    parser.add_argument("--output", default=None, help="输出文件路径")

    args = parser.parse_args()

    briefing = aggregate_tasks(args.mode)

    briefing_file = os.path.join(BRIEFING_DIR, f"briefing_{datetime.now().strftime('%Y%m%d')}.json")
    try:
        atomic_write_json(briefing_file, briefing, indent=2, ensure_ascii=False)
    except (OSError, TypeError) as e:
        logger.warning(f"[daily-briefing] 日报文件保存失败: {e}")

    message = format_qqbot_message(briefing)

    push_results = {}
    if args.push in ("qqbot", "all"):
        result = push_to_qqbot(message)
        push_results["qqbot"] = result

    if args.push == "wecom":
        logger.warning("wecom推送已废弃，自动切换为qqbot")
        result = push_to_qqbot(message)
        push_results["qqbot"] = result

    if args.push == "stdout":
        print(message)

    report = {
        "success": True,
        "data": {
            "date": briefing["date"],
            "total_tasks": briefing["total"],
            "p0_count": briefing["p0_count"],
            "p1_count": briefing["p1_count"],
            "p2_count": briefing["p2_count"],
            "push_results": push_results,
            "briefing_file": briefing_file,
        },
        "error": None,
        "code": None,
    }

    if args.output:
        os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
        atomic_write_json(args.output, report, indent=2, ensure_ascii=False)

    if args.push != "stdout":
        print(json.dumps(report, ensure_ascii=False, indent=2))

    return 0


if __name__ == "__main__":
    sys.exit(main())
