#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zy_platform.py — ZY Action Platform WorkBuddy 技能客户端（纯标准库，零第三方依赖）。

在 WorkBuddy（或任何终端）里通过本脚本调用本机/远端部署的 ZY Action Platform
REST API。支持五个产品：aip(18080)/foundry(18081)/apollo(18082)/gotham(18083)/swift(18084)。

用法示例：
  python zy_platform.py health --product aip
  python zy_platform.py login --product foundry --username admin --password '******'
  python zy_platform.py chat --product aip --query '各区域销售额 Top5'
  python zy_platform.py workflow-list --product aip
  python zy_platform.py ontology-search --product foundry --query '库存低于补货点的商品'
  python zy_platform.py search --product gotham --query '订单'
  python zy_platform.py deployment-list --product apollo
  python zy_platform.py request --product foundry --method GET --path='metrics/catalog'

约定：
  * --base-url 默认 http://127.0.0.1:<产品端口>；以 "/v1" 结尾视为完整 API 根（如
    http://127.0.0.1/aip-api/v1 网关形态），否则视为服务器根并自动拼 /api/v1。
  * 除 health/login 外都需要登录 token；token 来源优先级 --token > 本地会话缓存
    (~/.workbuddy/zy_action_session.json) > 无。
  * 退出码：0 成功 / 1 参数或本地错误 / 2 网络不可达或超时 / 3 HTTP 错误(4xx/5xx，非401)
            / 4 鉴权失败(401，提示重新 login) / 5 业务信封 code!=0。
  * 不硬编码任何账号口令密钥；stdout 仅输出 JSON，提示类信息走 stderr。
"""

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

PRODUCTS = {
    "aip":     {"port": 18080, "name": "LightAIP 智能查数（NLQ）"},
    "foundry": {"port": 18081, "name": "LightFoundry 数据集成/本体"},
    "apollo":  {"port": 18082, "name": "LightApollo 部署平台"},
    "gotham":  {"port": 18083, "name": "LightGotham 情报分析"},
    "swift":   {"port": 18084, "name": "LightSwift 星上结算"},
}

SESSION_FILE = Path.home() / ".workbuddy" / "zy_action_session.json"
DEFAULT_TIMEOUT = 25

# 产品 -> 允许的精选子命令（通用命令 health/login/me/request 不在列，见 COMMANDS）
ALLOW = {
    "aip":     {"datasource-list", "chat", "workflow-list", "workflow-run",
                "workflow-status", "workflow-cancel", "audit-list"},
    "foundry": {"datasource-list", "dataset-list", "dataset-preview",
                "ontology-objects", "ontology-search", "metric-list",
                "dashboard-list", "report-list"},
    "apollo":  {"apollo-docs", "desired-state-list", "deployment-list",
                "deployment-status", "drift-list", "bundle-list", "agent-list"},
    "gotham":  {"search", "graph-nodes", "graph-stats", "entity-list",
                "timeline-events", "map-features", "report-list"},
    "swift":   set(),
}

COMMAND_INTRO = {
    "health":             "检查产品健康状态（公开）",
    "login":              "登录并缓存 token（username/password）",
    "me":                 "返回当前登录用户（AIP/Apollo 提供）",
    "datasource-list":    "列出数据源（AIP/Foundry）",
    "chat":               "NLQ 自然语言查数（AIP）",
    "workflow-list":      "列出自动化/工作流（AIP）",
    "workflow-run":       "运行一次工作流（AIP，--workflow-id，可 --params）",
    "workflow-status":    "查询执行结果（AIP，--execution-id）",
    "workflow-cancel":    "取消执行（AIP，--execution-id）",
    "audit-list":         "审计日志（AIP 管理员）",
    "dataset-list":       "数据集列表（Foundry）",
    "dataset-preview":    "数据集行预览（Foundry，--dataset-id）",
    "ontology-objects":   "本体对象类型列表（Foundry）",
    "ontology-search":    "本体语义检索（Foundry，--query）",
    "metric-list":        "指标列表（Foundry）",
    "dashboard-list":     "看板列表（Foundry）",
    "report-list":        "报告列表（Foundry/Gotham）",
    "search":             "全局搜索（Gotham，--query）",
    "graph-nodes":        "知识图谱节点列表（Gotham）",
    "graph-stats":        "图统计（Gotham）",
    "entity-list":        "多源融合实体列表（Gotham）",
    "timeline-events":    "时间轴事件（Gotham）",
    "map-features":       "地图要素（Gotham）",
    "apollo-docs":        "Apollo API 文档自省（公开）",
    "desired-state-list": "期望状态列表（Apollo）",
    "deployment-list":    "部署列表（Apollo）",
    "deployment-status":  "部署详情（Apollo，--deployment-id）",
    "drift-list":         "漂移事件（Apollo）",
    "bundle-list":        "bundle 制品列表（Apollo）",
    "agent-list":         "Spoke Agent 节点列表（Apollo）",
    "request":            "通用请求透传：--method GET --path=datasets?limit=5 [--data json] [--query-str k=v]",
}

# 业务接口定义：method 与 path_template（{} 占位由参数填充）
ENDPOINTS = {
    "health":             ("GET",  "/health"),
    "login":              ("POST", "/api/v1/auth/login"),
    "me":                 ("GET",  "/api/v1/me"),
    "datasource-list":    ("GET",  "/api/v1/datasources"),
    "chat":               ("POST", "/api/v1/chat"),
    "workflow-list":      ("GET",  "/api/v1/workflows"),
    "workflow-run":       ("POST", "/api/v1/workflows/{workflow_id}/run"),
    "workflow-status":    ("GET",  "/api/v1/workflows/executions/{execution_id}"),
    "workflow-cancel":    ("POST", "/api/v1/workflows/executions/{execution_id}/cancel"),
    "audit-list":         ("GET",  "/api/v1/audit/logs"),
    "dataset-list":       ("GET",  "/api/v1/datasets"),
    "dataset-preview":    ("GET",  "/api/v1/datasets/{dataset_id}/preview"),
    "ontology-objects":   ("GET",  "/api/v1/ontology/objects"),
    "ontology-search":    ("POST", "/api/v1/ontology/semantic-search"),
    "metric-list":        ("GET",  "/api/v1/metrics"),
    "dashboard-list":     ("GET",  "/api/v1/dashboards"),
    "report-list":        ("GET",  "/api/v1/reports"),
    "search":             ("GET",  "/api/v1/search"),
    "graph-nodes":        ("GET",  "/api/v1/graph/nodes"),
    "graph-stats":        ("GET",  "/api/v1/graph/stats"),
    "entity-list":        ("GET",  "/api/v1/ingestion/entities"),
    "timeline-events":    ("GET",  "/api/v1/timeline/events"),
    "map-features":       ("GET",  "/api/v1/map/features"),
    "apollo-docs":        ("GET",  "/api/v1/docs"),
    "desired-state-list": ("GET",  "/api/v1/desired-states"),
    "deployment-list":    ("GET",  "/api/v1/deployments"),
    "deployment-status":  ("GET",  "/api/v1/deployments/{deployment_id}"),
    "drift-list":         ("GET",  "/api/v1/drift/events"),
    "bundle-list":        ("GET",  "/api/v1/bundles"),
    "agent-list":         ("GET",  "/api/v1/agents"),
}

PUBLIC_COMMANDS = {"health"}          # 无需 token
AUTHED_ONLY = {"login", "me"} | {c for c, (m, _) in ENDPOINTS.items() if c != "health"}


# ---------------------------------------------------------------------------
# 会话缓存
# ---------------------------------------------------------------------------
def load_session():
    try:
        return json.loads(SESSION_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_session(session):
    SESSION_FILE.parent.mkdir(parents=True, exist_ok=True)
    SESSION_FILE.write_text(json.dumps(session, ensure_ascii=False, indent=2),
                            encoding="utf-8")


def get_token(args, product):
    if args.token:
        return args.token
    if args.no_cache:
        return None
    return load_session().get(product, {}).get("token")


# ---------------------------------------------------------------------------
# URL 组装
# ---------------------------------------------------------------------------
def resolve_root(args, product):
    """返回 (api_root, health_root)。api_root 以 /api/v1 结尾；health 打服务器根。"""
    if args.base_url:
        base = args.base_url.rstrip("/")
        if base.endswith("/api/v1") or base.endswith("/v1") or base.endswith("/aip-api/v1") \
                or base.endswith("/apollo-api/v1") or base.endswith("/gotham-api/v1") \
                or base.endswith("/swift-api/v1"):
            api_root = base
        else:
            api_root = base + "/api/v1"
    else:
        api_root = "http://127.0.0.1:{}/api/v1".format(PRODUCTS[product]["port"])
    health_root = api_root
    for suffix in ("/api/v1", "/aip-api/v1", "/apollo-api/v1", "/gotham-api/v1", "/swift-api/v1"):
        if api_root.endswith(suffix):
            health_root = api_root[: -len(suffix)]
            break
    return api_root, health_root


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------
def _extract_message(obj):
    if isinstance(obj, dict):
        for k in ("message", "error", "detail", "msg", "trace"):
            if isinstance(obj.get(k), str) and obj[k]:
                return obj[k]
        data = obj.get("data")
        if isinstance(data, dict) and not data:
            return None
    return None


def http_call(method, url, payload=None, token=None, timeout=DEFAULT_TIMEOUT):
    body = None
    if payload is not None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=body, method=method)
    req.add_header("Content-Type", "application/json")
    req.add_header("Accept", "application/json")
    if token:
        req.add_header("Authorization", "Bearer " + token)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
            obj = json.loads(raw) if raw.strip() else {}
            return resp.status, obj
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", errors="replace")
        try:
            obj = json.loads(raw) if raw.strip() else {}
        except Exception:
            obj = {"error": raw[:200]}
        return e.code, obj
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        fail(2, "网络错误，无法访问 {}：{}。请确认平台已启动（双击「运行AI商业行动系统-ZY Action.exe」）且 --base-url/--product 正确。".format(url, e))
    except json.JSONDecodeError:
        fail(2, "响应不是合法 JSON：{}".format(url))
    return None, None  # unreachable


def emit(obj, args):
    kwargs = {"ensure_ascii": False}
    if args.pretty:
        kwargs["indent"] = 2
    print(json.dumps(obj, **kwargs))


def fail(rc, msg):
    print("[zy_platform] " + msg, file=sys.stderr)
    sys.exit(rc)


def check_business(obj, args):
    """信封 {code,message,data} 业务码检查；裸 JSON 视为成功。返回要展示的对象。"""
    if isinstance(obj, dict) and isinstance(obj.get("code"), int) and obj["code"] != 0:
        msg = _extract_message(obj) or "业务处理失败（code=%s）" % obj["code"]
        fail(5, msg)
    return obj


def check_http(status, obj, args):
    if status == 401:
        fail(4, "鉴权失败（401）：登录已失效，请先运行 login 子命令重新登录（或检查 --token）。")
    if status >= 400:
        msg = _extract_message(obj) or "HTTP {}".format(status)
        fail(3, "请求失败 HTTP {}：{}".format(status, msg))


# ---------------------------------------------------------------------------
# 命令实现
# ---------------------------------------------------------------------------
def run_health(args, product):
    _, health_root = resolve_root(args, product)
    status, obj = http_call("GET", health_root + "/health", timeout=args.timeout)
    check_http(status, obj, args)
    return obj


def run_login(args, product):
    if not args.username or not args.password:
        fail(1, "login 需要 --username 与 --password。新安装默认管理员 admin/admin1，也可在平台页面自助注册账号。")
    api_root, _ = resolve_root(args, product)
    payload = {"username": args.username, "password": args.password}
    status, obj = http_call("POST", api_root + "/auth/login", payload=payload, timeout=args.timeout)
    check_http(status, obj, args)
    token = None
    if isinstance(obj, dict):
        token = obj.get("token")                       # AIP/Apollo/Gotham/Swift 平铺
        if token is None and isinstance(obj.get("data"), dict):   # Foundry {code,data:{token}}
            token = obj["data"].get("token")
    if not token:
        fail(5, "登录响应中未找到 token，请检查账号密码或该产品登录接口。")
    if not args.no_cache:
        session = load_session()
        session[product] = {"token": token, "username": args.username,
                            "base": args.base_url or "http://127.0.0.1:%d" % PRODUCTS[product]["port"],
                            "time": int(time.time())}
        save_session(session)
    return {"login": "ok", "product": product, "username": args.username, "token_saved": not args.no_cache}


def run_request(args, product):
    if not args.method or not args.path:
        fail(1, "request 需要 --method(如 GET/POST) 与 --path。--path 相对 API 根："
                "如 --path=datasets?limit=5 表示 {base}/api/v1/datasets?limit=5；health 开头的路径打到服务器根 /health。")
    api_root, health_root = resolve_root(args, product)
    path = args.path.strip().lstrip("/")
    if path == "health" or path.startswith("health"):
        url = health_root + "/" + path
    else:
        url = api_root + "/" + path
    if args.query_str and "?" not in url.split("#")[0]:
        url += "?" + args.query_str.lstrip("?")
    payload = None
    if args.data:
        try:
            payload = json.loads(args.data)
        except ValueError:
            fail(1, "--data 需为合法 JSON 字符串，例如 '{\"query\":\"x\"}'。")
    token = get_token(args, product)
    status, obj = http_call(args.method.upper(), url, payload=payload, token=token, timeout=args.timeout)
    check_http(status, obj, args)
    return obj


def _append_query(url, params):
    """把非空查询参数拼到 url。params 值类型为 int/str。"""
    qs = {k: v for k, v in params.items() if v is not None}
    if qs and "?" not in url.split("#")[0]:
        url += "?" + urllib.parse.urlencode(qs)
    return url


def _build_query(name, args):
    if name == "search":
        if not args.query:
            fail(1, "search 需要 --query（搜索关键词）。")
        return {"q": args.query, "limit": args.limit}
    if name == "workflow-list":
        return {"page": args.page, "page_size": args.page_size}
    if name == "dataset-list":
        return {"limit": args.limit}
    if name == "dataset-preview":
        return {"limit": args.limit}
    if name == "audit-list":
        return {"page": args.page, "page_size": args.page_size}
    return {}


def run_command(name, args, product):
    method, tmpl = ENDPOINTS[name]
    api_root, _ = resolve_root(args, product)
    path = tmpl.format(workflow_id=args.workflow_id or "", execution_id=args.execution_id or "",
                       dataset_id=args.dataset_id or "", deployment_id=args.deployment_id or "")
    # ENDPOINTS 模板带 /api/v1 前缀；api_root 已含该前缀，去除避免双前缀。
    if path.startswith("/api/v1"):
        path = path[len("/api/v1"):]
    url = _append_query(api_root + path, _build_query(name, args))
    payload = None
    if method == "POST":
        if name == "login":
            return run_login(args, product)
        if name == "chat":
            if not args.query:
                fail(1, "chat 需要 --query（自然语言问题）。")
            payload = {"query": args.query}
        elif name == "workflow-run":
            if not args.workflow_id:
                fail(1, "workflow-run 需要 --workflow-id（可先 workflow-list 查看）。")
            payload = {}
            if args.params:
                try:
                    payload = json.loads(args.params)
                except ValueError:
                    fail(1, "--params 需为合法 JSON 对象，如 '{\"region\":\"华东\"}'。")
        elif name == "ontology-search":
            if not args.query:
                fail(1, "ontology-search 需要 --query。")
            payload = {"query": args.query}
            if args.limit:
                payload["limit"] = args.limit
        elif name == "workflow-cancel":
            if not args.execution_id:
                fail(1, "workflow-cancel 需要 --execution-id。")
    token = None if name in PUBLIC_COMMANDS else get_token(args, product)
    status, obj = http_call(method, url, payload=payload, token=token, timeout=args.timeout)
    check_http(status, obj, args)
    return obj


def build_parser():
    p = argparse.ArgumentParser(
        prog="zy_platform.py",
        description="ZY Action Platform REST 客户端（五产品）。",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("command", nargs="?", help="命令：" + " / ".join(COMMAND_INTRO))
    p.add_argument("--product", choices=list(PRODUCTS), default="aip",
                   help="产品：aip/foundry/apollo/gotham/swift（默认 aip）")
    p.add_argument("--base-url", default=None,
                   help="服务器地址。默认 http://127.0.0.1:<产品端口>；可传网关形态 http://host/aip-api/v1")
    p.add_argument("--username", default=None)
    p.add_argument("--password", default=None)
    p.add_argument("--token", default=None, help="显式 token（优先于会话缓存）")
    p.add_argument("--no-cache", action="store_true", help="不读写本地会话缓存")
    p.add_argument("--pretty", action="store_true", help="JSON 缩进美化输出")
    p.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="请求超时秒数")
    # 业务参数
    p.add_argument("--query", default=None)
    p.add_argument("--limit", type=int, default=None, help="返回条数上限（search/dataset 等）")
    p.add_argument("--page", type=int, default=None)
    p.add_argument("--page-size", dest="page_size", type=int, default=None)
    p.add_argument("--workflow-id", default=None)
    p.add_argument("--execution-id", default=None)
    p.add_argument("--dataset-id", default=None)
    p.add_argument("--deployment-id", default=None)
    p.add_argument("--params", default=None)
    p.add_argument("--method", default=None)
    p.add_argument("--path", default=None,
                   help="request 相对 API 根的路径，勿以 / 开头，如 datasets?limit=5")
    p.add_argument("--data", default=None, help="request 的 JSON 请求体")
    p.add_argument("--query-str", dest="query_str", default=None,
                   help="request 的 query string，如 'limit=5&status=active'")
    p.add_argument("--list-commands", action="store_true", help="列出全部命令")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    if args.list_commands:
        for k, v in COMMAND_INTRO.items():
            print("{:<18} {}".format(k, v))
        return 0
    if not args.command:
        fail(1, "缺少 command。用 --list-commands 查看，或 --help 帮助。")
    name = args.command
    product = args.product

    if name == "request":
        obj = run_request(args, product)
    elif name == "health":
        obj = run_health(args, product)
    elif name == "me":
        token = get_token(args, product)
        api_root, _ = resolve_root(args, product)
        status, obj = http_call("GET", api_root + "/me", token=token, timeout=args.timeout)
        check_http(status, obj, args)
    elif name == "login":
        obj = run_login(args, product)
    else:
        if name not in ENDPOINTS:
            fail(1, "未知命令 {}。--list-commands 查看全部。".format(name))
        if name not in ALLOW[product]:
            ok_products = [pr for pr in ALLOW if name in ALLOW[pr]]
            fail(1, "命令 {} 不适用于产品 {}；适用于：{}。".format(
                name, product, "、".join(ok_products) if ok_products else "无（仅通用命令 health/login/request）"))
        obj = run_command(name, args, product)
    obj = check_business(obj, args)
    emit(obj, args)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
