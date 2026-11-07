# -*- coding: utf-8 -*-
"""MC Skill Agent 入口脚本

Agent AI 通过此脚本调用 MC Skill 的各功能，返回 JSON 格式结果。

用法:
    python scripts/mc_skill.py <feature> [参数...]

示例:
    python scripts/mc_skill.py jar_parser --jar-path "create.jar"
    python scripts/mc_skill.py mod_searcher --query "Create" --mc-version "1.21.1" --loader "neoforge"
    python scripts/mc_skill.py mixin_scanner --mods-dir "./mods"
    python scripts/mc_skill.py crash_analyzer --crash-log "crash.txt"
    python scripts/mc_skill.py migration_assess --jar-path "create.jar" --from-mc-version "1.20.1" --to-mc-version "1.21.1" --from-loader "forge" --to-loader "neoforge"
    python scripts/mc_skill.py onboarding_info          # 🔑 首对话引导 —— 拿动态数据（免费期/额度/功能列表/套餐）
    python scripts/mc_skill.py mark_onboarding_shown    # 🔑 标记引导已展示（防重复打扰）
    python scripts/mc_skill.py gen_test_id --label "付费流程" --admin 2  # 🧪 生成标准化测试码
"""

import sys
import os
import json
import re
from datetime import datetime

# ================================================================
# 🔧 Windows 编码修复（QClaw 反馈 #3）
# 问题：Windows cmd 默认 GBK，输出 emoji / 特殊字符会
#       抛 UnicodeEncodeError，脚本直接崩，Agent 拿不到 JSON。
# 策略：1. 强制环境变量 PYTHONIOENCODING=utf-8
#       2. 重绑 sys.stdout / sys.stderr 为 UTF-8 writer
#       3. 失败时 fallback：所有输出用 ? 替换无法编码字符
# ================================================================
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
try:
    import io
    _stdout_wrapper = io.TextIOWrapper(
        sys.stdout.buffer if hasattr(sys.stdout, "buffer") else sys.__stdout__.buffer,
        encoding="utf-8", errors="replace", line_buffering=True,
    )
    _stderr_wrapper = io.TextIOWrapper(
        sys.stderr.buffer if hasattr(sys.stderr, "buffer") else sys.__stderr__.buffer,
        encoding="utf-8", errors="replace", line_buffering=True,
    )
    sys.stdout = _stdout_wrapper
    sys.stderr = _stderr_wrapper
except Exception:
    # 极端情况退到 ignore
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# 将项目根目录加入路径
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)


def _handle_onboarding_info():
    """Agent AI 首对话时调这个拿动态引导数据"""
    try:
        from core.auth_manager import get_onboarding_info
        info = get_onboarding_info()
        print(json.dumps(info, ensure_ascii=False, indent=2))
        return 0
    except Exception as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False))
        return 1


def _handle_mark_onboarding_shown():
    """引导展示完后调这个标记，防止后续对话重复打扰"""
    try:
        from core.auth_manager import mark_onboarding_shown
        mark_onboarding_shown()
        print(json.dumps({"ok": True, "message": "onboarding_shown marked"}, ensure_ascii=False))
        return 0
    except Exception as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False))
        return 1


# ==================== 🧪 标准化测试码生成器 ====================
# 格式：TEST-{admin号}-{用途}-{日期}
# 例：TEST-1-ONBOARDING-20260828  TEST-2-PAYFLOW-20260828
# 系统自动识别：机器码含 TEST/NGROK/DEV/ADMIN 等关键词 → user_type=admin
_LABEL_KEYWORDS = {
    # 英文
    "onboarding": "ONBOARDING",    # 首对话引导
    "pay": "PAYFLOW",              # 付费流程
    "payment": "PAYFLOW",
    "register": "REG",             # 注册链路
    "reg": "REG",
    "auth": "AUTH",                # 授权校验
    "jar": "JAR",                  # JAR 解析
    "mod": "MOD",                  # 模组检索
    "mixin": "MIXIN",              # Mixin 扫描
    "save": "SAVE",                # 存档同步
    "translate": "TRANSLATE",      # 汉化
    "crash": "CRASH",              # 报错修复
    "migrate": "MIGRATE",          # 移植评估
    "version": "VERSION",          # 版本检测
    "cold": "COLD",                # 冷启动
    "setup": "SETUP",              # 环境搭建
    "full": "FULL",                # 全链路
    # 中文
    "引导": "ONBOARDING",
    "付费": "PAYFLOW",
    "支付": "PAYFLOW",
    "注册": "REG",
    "授权": "AUTH",
    "存档": "SAVE",
    "汉化": "TRANSLATE",
    "翻译": "TRANSLATE",
    "崩溃": "CRASH",
    "报错": "CRASH",
    "移植": "MIGRATE",
    "冷启动": "COLD",
    "环境": "SETUP",
    "全链路": "FULL",
    "完整": "FULL",
}

# 中文编号映射
_CN_NUM = {1: "一", 2: "二", 3: "三", 4: "四", 5: "五", 6: "六", 7: "七", 8: "八", 9: "九", 10: "十"}


def _resolve_label(raw_label: str) -> str:
    """把用户输入的 label（中文/英文）转成 4-8 位大写英文 code"""
    if not raw_label:
        return "GENERAL"
    key = raw_label.strip().lower()
    for k, v in _LABEL_KEYWORDS.items():
        if k in key:
            return v
    # 兜底：取前 6 个字母的大写
    clean = re.sub(r"[^A-Za-z]", "", raw_label)[:6].upper()
    return clean or "GENERAL"


def _handle_gen_test_id(args: list) -> int:
    """
    生成标准化测试机器码 + 自动写入 auth_state.json + 自动注册到服务器
    
    参数:
        --label <用途>     测试用途（中文/英文都行，例：付费流程 / onboarding / 注册链路）
        --admin <编号>     管理员编号 1-10（默认自动取下一个）
        --register         是否立即注册到服务器（默认 True，需服务器在跑）
    
    示例:
        python scripts/mc_skill.py gen_test_id --label "付费流程" --admin 2
        python scripts/mc_skill.py gen_test_id --label "onboarding"
        python scripts/mc_skill.py gen_test_id --label "全链路" --admin 1
    """
    # 解析参数
    label_raw = ""
    admin_num = None
    do_register = True
    
    i = 0
    while i < len(args):
        if args[i] == "--label" and i + 1 < len(args):
            label_raw = args[i + 1]; i += 2
        elif args[i] == "--admin" and i + 1 < len(args):
            try: admin_num = int(args[i + 1]); i += 2
            except ValueError: i += 1
        elif args[i] == "--no-register":
            do_register = False; i += 1
        else:
            i += 1
    
    # 解析 label
    label_code = _resolve_label(label_raw)
    date_str = datetime.now().strftime("%Y%m%d")
    
    # 如果没指定 admin 编号，自动找 registry.json 里最小可用编号
    if admin_num is None:
        admin_num = 1
        try:
            reg_path = os.path.join(PROJECT_ROOT, "server", "data", "registry.json")
            if os.path.exists(reg_path):
                import json as _json
                reg = _json.load(open(reg_path, encoding="utf-8"))
                # 收集所有已占用的管理员编号
                _used = set()
                for _u in reg:
                    _rn = _u.get("nickname", "")
                    _m = re.search(r"管理员(\d+)", _rn)
                    if _m:
                        _used.add(int(_m.group(1)))
                    _cn_map = {"一":1,"二":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9,"十":10}
                    _m2 = re.search(r"管理员([一二三四五六七八九十])", _rn)
                    if _m2 and _m2.group(1) in _cn_map:
                        _used.add(_cn_map[_m2.group(1)])
                # 找最小可用编号
                admin_num = 1
                while admin_num in _used:
                    admin_num += 1
        except Exception:
            pass
    
    # 生成机器码
    machine_id = f"TEST-{admin_num}-{label_code}-{date_str}"
    nickname = f"管理员{_CN_NUM.get(admin_num, admin_num)}"
    
    result = {
        "ok": True,
        "machine_id": machine_id,
        "nickname": nickname,
        "label": label_raw or label_code,
        "admin_num": admin_num,
        "date": date_str,
        "format_rule": "TEST-{admin号}-{用途code}-{日期}",
        "instructions": [
            f"1. 已生成测试码: {machine_id}",
            f"2. 用户列表里会显示为: 🛡️测试用户 / {nickname} / 🆓免费用户 / 🔒永久",
            "3. 用完后直接调下一条命令就能生成新的，admin 号自动递增",
        ],
    }
    
    # 自动写入 auth_state.json（让当前客户端下次启动就用这个机器码）
    try:
        state_dir = os.path.join(PROJECT_ROOT, "data")
        os.makedirs(state_dir, exist_ok=True)
        state_path = os.path.join(state_dir, "auth_state.json")
        
        state = {}
        if os.path.exists(state_path):
            state = json.load(open(state_path, encoding="utf-8"))
        
        # 如果已有 state，保留 first_use_date 等字段；没有就初始化
        if not state.get("machine_id"):
            from datetime import timedelta
            today = datetime.now().strftime("%Y-%m-%d")
            state = {
                "machine_id": machine_id,
                "first_use_date": state.get("first_use_date", today),
                "free_period_end": state.get("free_period_end", (datetime.now() + timedelta(days=60)).strftime("%Y-%m-%d")),
                "onboarding_shown": True,  # 测试用户跳过引导
                "tier": "free",
                "daily_usage": {},
                "license_expires": "",
            }
        else:
            state["machine_id"] = machine_id
            state["onboarding_shown"] = True
        
        json.dump(state, open(state_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        result["auth_state_saved"] = True
        result["auth_state_path"] = state_path
    except Exception as e:
        result["auth_state_saved"] = False
        result["auth_state_error"] = str(e)
    
    # 自动注册到服务器（如果服务器在跑）
    if do_register:
        try:
            import urllib.request
            import ssl  # V1.0.5 修复：显式 SSL 上下文
            auth_url = os.environ.get("MC_SKILL_AUTH_URL", "")
            if not auth_url:
                # 本地测试模式
                auth_url = "http://127.0.0.1:8000"
            
            api_url = f"{auth_url.rstrip('/')}/api/auth/quick-check"
            body = json.dumps({
                "machine_id": machine_id,
                "fingerprint": "TEST_GENERATOR",
                "version": "1.0.4-test",
                "source": "qclaw_test",
            }).encode("utf-8")
            req = urllib.request.Request(api_url, data=body, headers={"Content-Type": "application/json"}, method="POST")
            with urllib.request.urlopen(req, timeout=5, context=ssl.create_default_context()) as resp:
                resp_data = json.loads(resp.read().decode("utf-8"))
                result["server_registered"] = True
                result["server_response"] = resp_data
        except Exception as e:
            result["server_registered"] = False
            result["server_error"] = str(e) + "（服务器没在跑？没关系，下次客户端启动时会自动注册）"
    
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "error": "缺少功能参数",
            "usage": "python scripts/mc_skill.py <feature> [参数...]",
            "features": [
                "jar_parser - JAR结构解析",
                "mod_searcher - 模组检索下载",
                "env_builder - 环境引导搭建",
                "mixin_scanner - Mixin冲突扫描",
                "repacker - 资源重打包",
                "save_sync - 存档同步",
                "translator - 基础汉化",
                "crash_analyzer - 报错修复",
                "auto_fix - 自动修复",
                "migration_assess - 移植可行性评估",
                "onboarding_info - 🔑 首对话引导数据（免费期/额度/功能列表/套餐）",
                "mark_onboarding_shown - 🔑 标记引导已展示",
                "gen_test_id - 🧪 生成标准化测试机器码（自动注册+自动写入auth_state）",
            ],
        }, ensure_ascii=False, indent=2))
        return 1

    feature = sys.argv[1]
    args = sys.argv[2:]

    # ========== 认证层专用命令（不走 main.py feature 机制）==========
    if feature == "onboarding_info":
        return _handle_onboarding_info()
    elif feature == "mark_onboarding_shown":
        return _handle_mark_onboarding_shown()
    elif feature == "gen_test_id":
        return _handle_gen_test_id(args)

    # ========== 业务功能 → 转调 main.py --feature ==========
    cmd_args = ["main.py", "--feature", feature] + args

    original_argv = sys.argv
    sys.argv = cmd_args

    try:
        from main import main as main_entry
        main_entry()
        return 0
    except Exception as e:
        print(json.dumps({
            "error": str(e),
            "feature": feature,
        }, ensure_ascii=False, indent=2))
        return 1
    finally:
        sys.argv = original_argv


if __name__ == "__main__":
    sys.exit(main())
