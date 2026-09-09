#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""文章润色/排版脚本：调用云端润色API（/bailian/chat 兼容接口）

密钥优先级：--api-key（本次临时） > 本机已保存的个人密钥 > 内置公共密钥
个人密钥保存后永久生效，直到 --clear-key 清除。
"""
import argparse
import json
import os
import sys
import urllib.request

API_URL = "https://1257707270-955niawhww.ap-shanghai.tencentscf.com/bailian/chat"
DEFAULT_API_KEY = "sk-16a611a2dbb9270b476c2caf29414e345f587f0548aca4a7"  # 公共免费共享
MODELS = {"runse": "wenzi_runs", "paiban": "wenzi_paiban", "both": "链式：先润色后排版"}
DEFAULT_CONFIG_PATH = os.path.join(os.path.expanduser("~"), ".workbuddy", "wenzi-runse-config.json")


def out(payload):
    print(json.dumps(payload, ensure_ascii=False))


def call_api(text, model_id, api_key):
    """调用云端接口，返回统一结构 {"success", "result", "message"}"""
    body = {"text": text, "model": model_id}
    if api_key != DEFAULT_API_KEY:
        body["api_key"] = api_key

    req = urllib.request.Request(
        API_URL,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as res:
            data = json.loads(res.read().decode("utf-8"))
    except Exception as e:
        return {"success": False, "result": "", "message": f"网络请求失败: {e}"}

    err = str(data.get("error", "") or "").strip()
    if err:
        # API 返回的业务提示（额度用完、密钥无效等），原样转达用户
        return {"success": False, "result": "", "message": err}
    return {"success": True, "result": str(data.get("result", "") or ""), "message": "ok"}


def load_saved_key(config_path=DEFAULT_CONFIG_PATH):
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return str(json.load(f).get("api_key", "") or "").strip()
    except Exception:
        return ""


def save_key(key, config_path=DEFAULT_CONFIG_PATH):
    try:
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        # 以 0600 权限写入，仅限当前用户可读（Windows 下尽力而为）
        fd = os.open(config_path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump({"api_key": key}, f, ensure_ascii=False)
        try:
            os.chmod(config_path, 0o600)
        except Exception:
            pass
        return True
    except Exception as e:
        out({"success": False, "result": "", "message": f"密钥保存失败: {e}"})
        return False


def mask(key):
    return key[:6] + "****" + key[-4:] if len(key) > 12 else "****"


def main():
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=list(MODELS), help="runse=润色 paiban=排版 both=润色+排版一步到位")
    parser.add_argument("--text-file", help="UTF-8 文本文件路径")
    parser.add_argument("--api-key", default="", help="本次临时使用的密钥")
    parser.add_argument("--save-key", default="", help="永久保存个人密钥（保存后自动优先使用）")
    parser.add_argument("--show-key", action="store_true", help="查看当前使用的密钥")
    parser.add_argument("--clear-key", action="store_true", help="清除已保存的个人密钥，回到公共密钥")
    parser.add_argument("--config-path", default=DEFAULT_CONFIG_PATH,
                        help="密钥配置文件路径（默认 ~/.workbuddy/wenzi-runse-config.json，可自定义任意位置）")
    args = parser.parse_args()

    # ---- 密钥管理命令 ----
    if args.save_key:
        key = args.save_key.replace("Bearer", "").strip()
        if not key.startswith("sk-"):
            out({"success": False, "result": "", "message": "密钥格式不对，应以 sk- 开头。"})
            return
        if save_key(key, args.config_path):
            out({"success": True, "result": f"密钥已保存并启用: {mask(key)}，之后润色/排版将自动使用你的个人密钥。（明文保存在本机 {args.config_path}，仅限本人设备，可随时 --clear-key 删除）", "message": "ok"})
        return
    if args.clear_key:
        if os.path.exists(args.config_path):
            os.remove(args.config_path)
        out({"success": True, "result": "已清除个人密钥，恢复使用公共密钥（每日次数有限）。", "message": "ok"})
        return
    if args.show_key:
        saved = load_saved_key(args.config_path)
        out({"success": True, "result": f"当前密钥: {mask(saved) if saved else '公共密钥（每日次数有限）'}", "message": "ok"})
        return

    # ---- 主流程 ----
    if not args.mode or not args.text_file:
        out({"success": False, "result": "", "message": "缺少 --mode 或 --text-file 参数"})
        return
    if not os.path.exists(args.text_file):
        out({"success": False, "result": "", "message": f"找不到文本文件: {args.text_file}"})
        return

    with open(args.text_file, "r", encoding="utf-8") as f:
        text = f.read().strip()

    if len(text) < 300:
        out({"success": False, "result": "", "message": "文章不足300字，无法处理；1000字左右效果更佳。"})
        return

    # 密钥优先级：--api-key > 已保存个人密钥 > 公共密钥
    api_key = args.api_key.replace("Bearer", "").strip() or load_saved_key(args.config_path) or DEFAULT_API_KEY

    if args.mode == "both":
        # 链式处理：先润色，成功后把润色稿送进排版，一次交付最终稿
        r1 = call_api(text, MODELS["runse"], api_key)
        if not r1["success"]:
            out(r1)
            return
        r2 = call_api(r1["result"], MODELS["paiban"], api_key)
        if not r2["success"]:
            # 排版失败但润色已成功：把润色稿交付，并说明排版环节的提示
            out({"success": True, "result": r1["result"],
                 "message": f"润色已完成；排版环节未成功：{r2['message']}"})
            return
        out({"success": True, "result": r2["result"], "message": "润色+排版已完成"})
        return

    result = call_api(text, MODELS[args.mode], api_key)
    out(result)


if __name__ == "__main__":
    main()
