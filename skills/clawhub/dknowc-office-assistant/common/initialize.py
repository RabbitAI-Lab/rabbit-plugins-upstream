#!/usr/bin/env python3
"""深知晓办公助手统一初始化与环境检查。

整合深知公文写作 / 深知可信咨询 / 深知可信搜索 / 深知可信PPT四个能力模块的公共层。
统一只从环境变量 DKNOWC_API_KEY 读取 API Key。

三层门禁划分（本脚本只报告状态，是否阻断由 SKILL.md 按任务类型判定）：
- `ready`：基础运行环境（python3、requests）就绪；缺失暂停全部能力。
- `search_ready`：可调用深知可信检索/咨询（API Key 已配置且 requests 可用）。
  仅公文写作的纯排版任务、PPT 的材料免检索模式不要求。
- `pptx_ready`：可直接执行 SVG→PPTX 编译导出（python-pptx + XlsxWriter 可用）。
  缺失不阻断其他能力；导出时可用 `uv run --with python-pptx --with XlsxWriter python3 …` 隔离提供。

可选参数（仅公文写作能力使用，须用户明确授权 --save 才写入）：
  --organization / --doc-prefix / --region / --print-unit / --save
"""

import argparse
import json
import os
import platform
import shutil

from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
API_KEY_ENV = "DKNOWC_API_KEY"
# 公文写作用户偏好：写入 doc-writer 模块 config/，与其排版脚本读取位置一致。
PROFILE_PATH = SKILL_ROOT / "doc-writer" / "config" / "user_profile.json"
# 依赖安装提示等本地状态：写入综合 skill 根目录 config/。
ENV_STATE_PATH = SKILL_ROOT / "config" / "environment_state.json"

PLACEHOLDER_KEYS = {
    "",
    "your_api_key_here",
    "你的深知可信统一接口 API Key",
    "你的深知可信咨询 API Key",
    "你的深知可信搜索 API Key",
    "你的深知搜索 API Key",
}


def _module_available(module_name):
    try:
        __import__(module_name)
        return True
    except ImportError:
        return False


def _looks_like_key(value: str) -> bool:
    value = (value or "").strip()
    return value not in PLACEHOLDER_KEYS


def check_api_key_config():
    api_key = os.environ.get(API_KEY_ENV, "").strip()
    if _looks_like_key(api_key):
        return {
            "api_key_configured": True,
            "api_key_env": API_KEY_ENV,
            "api_key_source": "environment",
            "api_key_hint": None,
        }
    return {
        "api_key_configured": False,
        "api_key_env": API_KEY_ENV,
        "api_key_source": None,
        "api_key_hint": f"本 Skill 的检索/咨询能力需要通过环境变量 {API_KEY_ENV} 连接深知可信智能服务。当前未检测到可用 Key，请先注册或登录深知可信智能 MaaS 账号获取 API Key，再注入该环境变量。",
    }


def load_environment_state():
    if not ENV_STATE_PATH.exists():
        return {}
    try:
        with ENV_STATE_PATH.open("r", encoding="utf-8") as state_file:
            state = json.load(state_file)
        return state if isinstance(state, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def save_environment_state(state):
    ENV_STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with ENV_STATE_PATH.open("w", encoding="utf-8") as state_file:
        json.dump(state, state_file, ensure_ascii=False, indent=2)


def check_environment():
    state = load_environment_state()
    python3_available = shutil.which("python3") is not None
    requests_available = _module_available("requests")
    python_docx_available = _module_available("docx")
    python_pptx_available = _module_available("pptx")
    xlsxwriter_available = _module_available("XlsxWriter")
    config_status = check_api_key_config()

    blocking_issues = []
    if not python3_available:
        blocking_issues.append("python3_missing")
    if not requests_available:
        blocking_issues.append("requests_missing")

    word_blocking_issues = []
    if not python_docx_available:
        word_blocking_issues.append("python_docx_missing")

    pptx_blocking_issues = []
    if not python_pptx_available:
        pptx_blocking_issues.append("python_pptx_missing")
    if not xlsxwriter_available:
        pptx_blocking_issues.append("xlsxwriter_missing")

    search_blocking_issues = []
    if not config_status["api_key_configured"]:
        search_blocking_issues.append("api_key_missing")

    return {
        "python": platform.python_version(),
        "python3_available": python3_available,
        "requests": requests_available,
        "python_docx": python_docx_available,
        "python_pptx": python_pptx_available,
        "xlsxwriter": xlsxwriter_available,
        "api_key_configured": config_status["api_key_configured"],
        "api_key_env": API_KEY_ENV,
        "api_key_source": config_status["api_key_source"],
        "api_key_hint": config_status["api_key_hint"],
        # 检索/咨询层：公文纯排版与PPT材料免检索模式不要求。
        "search_ready": config_status["api_key_configured"] and requests_available,
        "search_blocking_issues": search_blocking_issues,
        # Word 排版层：仅公文写作能力需要；缺失时可用 uv run --with python-docx 提供。
        "word_ready": python3_available and python_docx_available,
        "word_blocking_issues": word_blocking_issues,
        # PPT 编译层：仅深知可信PPT能力需要；缺失不阻断其他能力。
        "pptx_ready": python3_available and python_pptx_available and xlsxwriter_available,
        "pptx_blocking_issues": pptx_blocking_issues,
        "pptx_hint": (
            "SVG 编译导出可用 `uv run --with python-pptx --with XlsxWriter python3 …` 隔离提供依赖；"
            if pptx_blocking_issues else None
        ),
        "blocking_issues": blocking_issues,
        "ready": not blocking_issues,
        "maas_platform_url": "https://platform.dknowc.cn/",
        "environment_state": {
            "dependency_install_declined": bool(state.get("dependency_install_declined")),
        },
    }


def main():
    parser = argparse.ArgumentParser(description="深知晓办公助手统一初始化与环境检查")
    parser.add_argument("--organization", help="常用发文机关；不填写则使用 XX单位（仅公文写作能力）")
    parser.add_argument("--doc-prefix", help="常用发文字号前缀；不填写则使用 XX（仅公文写作能力）")
    parser.add_argument("--region", help="常用搜索地域；不填写则按任务询问")
    parser.add_argument("--print-unit", help="常用印发单位")
    parser.add_argument("--save", action="store_true", help="经用户授权后，将所填设置仅保存到本机")
    parser.add_argument("--decline-dependency-install", action="store_true", help="记录用户已拒绝依赖安装提示，后续不再反复询问")
    parser.add_argument("--reset-environment-prompts", action="store_true", help="清除依赖安装提示的拒绝记录")
    args = parser.parse_args()

    state = load_environment_state()
    if args.reset_environment_prompts:
        state.pop("dependency_install_declined", None)
    if args.decline_dependency_install:
        state["dependency_install_declined"] = True
    if args.reset_environment_prompts or args.decline_dependency_install:
        save_environment_state(state)

    if args.save:
        profile = {
            "organization": args.organization or "",
            "doc_prefix": args.doc_prefix or "",
            "region": args.region or "",
            "print_unit": args.print_unit or "",
        }
        PROFILE_PATH.parent.mkdir(parents=True, exist_ok=True)
        with PROFILE_PATH.open("w", encoding="utf-8") as profile_file:
            json.dump(profile, profile_file, ensure_ascii=False, indent=2)

    result = check_environment()
    result["profile_saved"] = args.save
    result["profile_path"] = "doc-writer/config/user_profile.json" if args.save else None
    result["environment_state_path"] = "config/environment_state.json"
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
