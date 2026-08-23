#!/usr/bin/env python3
"""
AI生图 - LinkFox Skill (异步模式)
调用 aigc/imageGenAsync 创建任务，然后轮询 aigc/taskQuery 获取结果。
"""

import json
import os
import sys
import time
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

from linkfox_paths import decode_nl_in_obj, download_media, get_api_base, resolve_data_path

CREATE_PATH = "/aigc/imageGenAsync"
QUERY_PATH = "/aigc/taskQuery"
SLUG = "linkfox-aigc-imagegen"
POLL_INTERVAL_START = 10
POLL_INTERVAL_MIN = 5
POLL_INTERVAL_STEP = 1
MAX_POLL_TIME = 600

def get_api_key():
    """
    获取配置在环境变量的API Key。
    如果获取不到，按 SKILL.md 的 **## 解决认证和积分问题** 处理。
    """
    key = os.environ.get("LINKFOX_AGENT_API_KEY") or os.environ.get("LINKFOXAGENT_API_KEY")
    if not key:
        print("API Key 未配置", file=sys.stderr)
        sys.exit(1)
    return key


def _post(url, params):
    api_key = get_api_key()
    data = json.dumps(params, ensure_ascii=False).encode("utf-8")
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json",
        "User-Agent": "LinkFox-Skill/2.0",
        "SESSION_ID": os.environ.get("SESSION_ID", ""),
        "MESSAGE_ID": os.environ.get("MESSAGE_ID", ""),
        "MODE_ID": os.environ.get("MODE_ID", ""),
        "APP_NAME": os.environ.get("APP_NAME", ""),
    }
    req = Request(url, data=data, headers=headers, method="POST")
    try:
        with urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as e:
        body = e.read().decode("utf-8") if e.fp else ""
        try:
            return json.loads(body) if body else {"error": f"HTTP {e.code}: {e.reason}"}
        except Exception:
            return {"error": f"HTTP {e.code}: {e.reason}", "details": body}
    except URLError as e:
        return {"error": f"Connection failed: {e.reason}"}


def create_task(params):
    url = get_api_base() + CREATE_PATH
    return _post(url, params)


def query_task(task_id, member_id):
    url = get_api_base() + QUERY_PATH
    return _post(url, {"taskId": task_id, "memberId": member_id})


def poll_until_done(task_id, member_id):
    start = time.time()
    interval = POLL_INTERVAL_START
    while time.time() - start < MAX_POLL_TIME:
        time.sleep(interval)
        result = query_task(task_id, member_id)
        if result.get("error"):
            print(f"  Poll error: {result['error']}", file=sys.stderr)
            interval = max(interval - POLL_INTERVAL_STEP, POLL_INTERVAL_MIN)
            continue
        status = result.get("status")
        if status == "SUCCESS":
            return result
        elif status == "FAILED":
            return result
        elapsed = int(time.time() - start)
        print(f"  Polling... status={status}, elapsed={elapsed}s, next in {interval}s", file=sys.stderr)
        interval = max(interval - POLL_INTERVAL_STEP, POLL_INTERVAL_MIN)
    return {"error": f"Polling timeout after {MAX_POLL_TIME}s", "taskId": task_id}


def _resolve_output_path(ts):
    return resolve_data_path(SLUG, ts)


def _download_results(result):
    try:
        if not isinstance(result, dict):
            return []
        if result.get("error"):
            return []
        result_list = result.get("resultList") or []
        local_paths = []
        for i, item in enumerate(result_list):
            url = item.get("url") if isinstance(item, dict) else None
            if not url:
                continue
            ts = time.time() + i * 0.01
            path = download_media(url, SLUG, ts)
            if path:
                local_paths.append(path)
            else:
                print(f"  Download failed: {url}", file=sys.stderr)
        return local_paths
    except Exception as e:
        print(f"[_download_results] error: {e}", file=sys.stderr)
        return []


def summarize(result):
    if not isinstance(result, dict):
        print(json.dumps(result, ensure_ascii=False)[:500])
        return
    print(f"Top-level keys: {list(result.keys())}")
    for k in ("errcode", "code", "msg", "costToken", "status"):
        if k in result:
            print(f"  {k}: {result[k]}")
    result_list = result.get("resultList") or []
    if result_list:
        print(f"\nresultList (length={len(result_list)}):")
        print(json.dumps(result_list[:3], indent=2, ensure_ascii=False))


def main():
    argv = sys.argv[1:]
    if "--inline" in argv:
        argv = [a for a in argv if a != "--inline"]

    if not argv:
        print("Usage: aigc_imagegen.py '<JSON>'", file=sys.stderr)
        sys.exit(1)

    try:
        params = json.loads(argv[0])
    except json.JSONDecodeError as e:
        print(f"Invalid parameter format: {e}", file=sys.stderr)
        sys.exit(1)

    params = decode_nl_in_obj(params)

    member_id = params.get("memberId", "")

    create_result = create_task(params)
    if create_result.get("error"):
        print(json.dumps(create_result, ensure_ascii=False))
        sys.exit(1)

    task_id = create_result.get("taskId")
    cost_token = create_result.get("costToken", 0)

    if not task_id:
        print(json.dumps(create_result, ensure_ascii=False))
        sys.exit(1)

    print(f"Task created: taskId={task_id}, costToken={cost_token}", file=sys.stderr)

    result = poll_until_done(task_id, member_id)
    result["costToken"] = cost_token

    media_paths = _download_results(result)

    # 原始响应无论成功失败都落盘（静默）
    serialized = json.dumps(result, ensure_ascii=False, indent=2)
    # 用浮点秒（毫秒精度）而非 int(time.time())：套图多任务在同一秒内并发完成时，
    # 整秒时间戳会让 data 文件名碰撞、互相覆盖并在 _meta.json 留下重复条目。
    ts = time.time()
    out_path = _resolve_output_path(ts)
    try:
        with open(out_path, "w") as f:
            f.write(serialized)
    except OSError as e:
        print(f"Failed to save raw response to {out_path}: {e}", file=sys.stderr)

    # 有图片时：只输出图片路径数组（前端可依赖此格式）；无图片时：输出原始响应路径
    if media_paths:
        print(f"Saved full response: {json.dumps(media_paths, ensure_ascii=False)}")
    else:
        print(f"Saved full response: {out_path} ({len(serialized)} bytes)")
        summarize(result)


if __name__ == "__main__":
    main()
