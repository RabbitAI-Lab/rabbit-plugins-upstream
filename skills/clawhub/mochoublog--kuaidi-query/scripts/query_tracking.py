#!/usr/bin/env python3
"""Query KDNiao tracking data with stable JSON output."""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

from kuaidi_common import latest_trace_of, sorted_traces, state_icon, state_text

API_URL = "https://api.kdniao.com/api/dist"
HOME_CONFIG = Path(os.path.expanduser(os.environ.get(
    "KUAIDI_CONFIG_FILE", "~/.openclaw/config/kuaidi-query.json"
)))
LOCAL_CONFIG = Path(__file__).resolve().parent.parent / "config.json"
COMPANY_PATTERNS = {
    "SF": (r"^SF\d{13}$",), "JD": (r"^JD\d{11,13}$",),
    "YTO": (r"^Y[TK]\d{10,14}$",), "EMS": (r"^E[A-Z]?\d{9}(?:E|CN)$",),
    "JTSD": (r"^JT\d{11,13}$",),
}

class ConfigError(RuntimeError):
    pass

def load_config(path=None):
    config_path = Path(path) if path else (HOME_CONFIG if HOME_CONFIG.exists() else LOCAL_CONFIG)
    if not config_path.exists():
        raise ConfigError(f"配置文件不存在：{config_path}")
    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ConfigError(f"配置文件无法读取或 JSON 无效：{config_path}") from exc
    if not config.get("app_id") or not config.get("app_key"):
        raise ConfigError("配置文件缺少 app_id 或 app_key")
    return config

def generate_sign(data, app_key):
    digest = hashlib.md5((data + app_key).encode("utf-8")).hexdigest()
    return base64.b64encode(digest.encode("utf-8")).decode("utf-8")

def auto_detect_company(tracking_number):
    for company, patterns in COMPANY_PATTERNS.items():
        if any(re.fullmatch(pattern, tracking_number, re.IGNORECASE) for pattern in patterns):
            return company
    return None

def query_tracking(tracking_number, company_code=None, phone_suffix=None, config_path=None, opener=None):
    try:
        config = load_config(config_path)
    except ConfigError as exc:
        return {"Success": False, "Reason": str(exc), "ErrorType": "config"}
    use_phone = phone_suffix or config.get("phone_suffix", "")
    request_data = {"OrderCode": "", "ShipperCode": company_code or "", "LogisticCode": tracking_number}
    if use_phone:
        if not re.fullmatch(r"\d{4}", str(use_phone)):
            return {"Success": False, "Reason": "手机尾号必须是 4 位数字", "ErrorType": "validation"}
        request_data["CustomerName"] = str(use_phone)
    data_str = json.dumps(request_data, ensure_ascii=False, separators=(",", ":"))
    params = {
        "RequestData": data_str, "EBusinessID": config["app_id"], "RequestType": "8001",
        "DataSign": generate_sign(data_str, config["app_key"]), "DataType": "2",
    }
    try:
        request = urllib.request.Request(API_URL, data=urllib.parse.urlencode(params).encode("utf-8"))
        request.add_header("Content-Type", "application/x-www-form-urlencoded")
        open_url = opener or urllib.request.urlopen
        with open_url(request, timeout=10) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as exc:
        return {"Success": False, "Reason": f"查询失败：{exc}", "ErrorType": "network"}

def format_result(result, tracking_number, company_code=None):
    if not result.get("Success"):
        return f"❌ 查询失败：{result.get('Reason', '未知错误')}"
    company = result.get("ShipperName") or company_code or "未知快递"
    state = str(result.get("State", "0"))
    lines = [f"📦 {company} - {tracking_number}", "", f"状态：{state_text(state)} {state_icon(state)}", ""]
    traces = sorted_traces(result)
    if not traces:
        return "\n".join(lines + ["暂无物流轨迹信息"])
    lines.append("物流轨迹：")
    for trace in reversed(traces):
        time, desc = trace.get("AcceptTime", ""), trace.get("AcceptStation", "")
        if time or desc:
            lines.append(f"{time} {desc}".strip())
    return "\n".join(lines)

def build_query_response(tracking_number, company_code=None, phone_suffix=None, config_path=None, opener=None):
    tracking_number = tracking_number.strip().replace(" ", "")
    detected = None
    warnings = []
    if not company_code:
        detected = auto_detect_company(tracking_number)
        company_code = detected
        if not detected:
            warnings.append("无法可靠自动识别快递公司，建议手动指定")
    result = query_tracking(tracking_number, company_code, phone_suffix, config_path, opener)
    latest = latest_trace_of(result)
    return {
        "success": bool(result.get("Success")), "tracking_number": tracking_number,
        "company_code": company_code, "detected_company_code": detected,
        "state": result.get("State"), "state_ex": result.get("StateEx"),
        "shipper_name": result.get("ShipperName") or company_code or "未知快递",
        "latest_trace": latest, "traces": sorted_traces(result),
        "message": format_result(result, tracking_number, company_code),
        "warnings": warnings, "error": None if result.get("Success") else result.get("Reason", "查询失败"),
        "error_type": result.get("ErrorType"), "checked_at": datetime.now().isoformat(),
    }

def main(argv=None):
    parser = argparse.ArgumentParser(description="查询快递轨迹")
    parser.add_argument("tracking_number", help="快递单号")
    parser.add_argument("company_code", nargs="?", help="快递公司编码，如 SF、JD、YTO")
    parser.add_argument("--phone-suffix", help="收件人手机尾号 4 位")
    parser.add_argument("--json", action="store_true", help="stdout 只输出 JSON")
    args = parser.parse_args(argv)
    response = build_query_response(args.tracking_number, args.company_code, args.phone_suffix)
    if args.json:
        print(json.dumps(response, ensure_ascii=False, indent=2))
    else:
        for warning in response["warnings"]:
            print(f"⚠️ {warning}", file=sys.stderr)
        print(response["message"])
    return 0 if response["success"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
