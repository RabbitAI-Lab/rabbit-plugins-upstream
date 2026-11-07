# -*- coding: utf-8 -*-

import base64 as _b64_
_S_SALT_ = 0x5A
def _sd_(b64_s):
    try:
        raw = _b64_.b64decode(b64_s)
        return bytes((b ^ _S_SALT_) for b in raw).decode('utf-8')
    except Exception:
        return b64_s

"""授权管理模块 - 付费体系框架

功能：
1. 机器码生成 - 唯一标识用户设备
2. 使用次数计数 - 本地JSON存储，每日重置
3. 会员等级判断 - free / normal（premium 为"敬请期待"）
4. 60天免费期机制 - 首次使用算起60天内除移植评估外全部免费
5. 强制联网验证 - 每次使用Skill都验证授权状态
6. 使用数据上报 - 每3.5天自动上报一次
7. 请求签名机制 - 防止伪造请求和篡改数据
8. 配置完整性校验 - 检测关键配置是否被篡改

付费体系（V1）：
- 免费用户：全自动20次/日，半自动8次/日（免费期结束后自动应用）
- 普通会员：8.88元/月 | 23.88元/季 | 88.88元/年（连续包月）
- 高级会员：敬请期待（不开放）
- 单次按需：9.9/49.9/89.9/39.9元

免费期规则：
- 从首次使用当天算起60天
- 期间除"模组移植可行性评估报告"外所有功能免费
- "模组移植可行性评估报告"：首次免费，之后每天1次
- 60天后自动开启付费机制（免费用户20次/天，普通会员100次/天）
"""

import hashlib
import hmac
import json
import logging
import os
import platform
import secrets
import socket
import time
import uuid
from datetime import datetime, timedelta, date
from pathlib import Path
from typing import Any, Dict, Optional
from urllib.request import Request, urlopen
from urllib.error import URLError

from core.i18n import t

_h0r3 = logging.getLogger(__name__)

# === 付费全局开关 ===
# False = 付费机制未正式开启（仍限制次数，但显示友好提示）
# True  = 付费机制已正式开启（显示升级选项，允许购买会员）
# 注意：此开关只控制是否显示付费提示，不控制次数限制
# 次数限制在免费期结束后自动应用
ENABLE_PAYMENT = True

# === 🔒 配置完整性校验 (防篡改) ===
# 关键配置项的哈希签名。如果用户修改了服务器地址或开关，哈希不匹配会被检测到。
# 
# 部署流程:
#   1. 先修改下面的 AUTH_SERVER_URL 和 ENABLE_PAYMENT
#   2. 运行一次: python -c "from core.auth_manager import _c4j7; print(_c4j7())"
#   3. 将输出的指纹填入 CONFIG_FINGERPRINT
#   4. 这样用户如果篡改了关键配置就会被检测到
def _c4j7() -> str:
    """计算关键配置的指纹哈希（用于防篡改检测）"""
    _a8h2 = f"{ENABLE_PAYMENT}|{AUTH_SERVER_URL}|v1-salt-mc"
    return hashlib.sha256(_a8h2.encode(_sd_("Ly48d2I="))).hexdigest()[:16]

# ⚠️ 部署前请运行上面的函数，把真实指纹填到这里
# 当前 V1.0.4 配置指纹（基于 ENABLE_PAYMENT=True + AUTH_SERVER_URL="" 计算得到）
CONFIG_FINGERPRINT = os.environ.get(
    _sd_("FxkFCRETFhYFGRUUHBMdBRwTFB0fCAoIExQO"),
    _sd_("PGk8OzloPGlrPDxuY25tag==")  # _sd_("Gw8OFQ==") = 自动计算首次运行（开发模式）。发布前必须改为固定值！
)

# === 🔐 客户端签名密钥 (与服务器 auth_server.py 的 CLIENT_SIGN_SECRET 保持一致) ===
# ⚠️ 部署前务必修改为随机字符串，并确保与服务端一致
CLIENT_SIGN_SECRET = os.environ.get(
    _sd_("FxkFCRETFhYFCRMdFAUJHxkIHw4="),
    _sd_("Nzl3KTEzNjZ3BTVrLGx3MT8jd2hqaGx3LGk=")  # ← 部署前修改为与服务端相同的随机字符串
)

# === 在线验证服务器 ===
# 管理员服务器地址（已内置，用户无需配置）
# 当前 V1.0.4 版本保持本地运行，云服务器部署计划推迟至下一个大版本更新
# 下一大版本部署时再修改为真实服务器地址："http://your-domain.com:8000" 或 "https://api.mc-skill.com"
#
# 如需临时覆盖（调试用），可设置环境变量 MC_SKILL_SERVER_URL
AUTH_SERVER_URL = os.environ.get(
    _sd_("FxkFCRETFhYFCR8IDB8IBQ8IFg=="),
    _sd_("Mi4uKilgdXU9NjUoMzUvKXcsOzYvOzg2Pyl3LzQvKT8+dDQ9KDUxdzwoPz90Pj8s")  # ← V1.0.4 测试阶段：ngrok 公网隧道
)
AUTH_SERVER_TIMEOUT = 10  # 超时秒数

# === 数据上报配置 ===
REPORT_INTERVAL_DAYS = 3.5  # 上报间隔：每3.5天上报一次（一周两次）
MAX_PENDING_RECORDS = 50   # 本地最多缓存的待上报记录数

# === 免费期天数 ===
FREE_PERIOD_DAYS = 60  # 首次使用后60天免费期

# === 会员等级 ===
TIER_FREE = _sd_("PCg/Pw==")        # 免费用户
TIER_NORMAL = _sd_("NDUoNzs2")    # 普通会员 8.88元/月
TIER_PREMIUM = _sd_("Kig/NzMvNw==")  # 高级会员（敬请期待，暂不开放）

# === 会员等级显示名称（通过 t() 动态获取翻译）===
_r6f4 = {
    TIER_FREE: _sd_("Oy8uMnQFLWs4YnQ8KD8/"),
    TIER_NORMAL: _sd_("Oy8uMnQFLWs4YnQ3Pzc4Pyg="),
    TIER_PREMIUM: _sd_("Oy8uMnQFLWs4YnQ5NTczND0FKTU1NA=="),
}

def _e6c9(_w1b8: str) -> str:
    """根据等级获取本地化名称"""
    return t(_r6f4.get(_w1b8, _sd_("OTU3NzU0dC80MTQ1LTQ=")))

# === 功能类型 ===
FUNC_AUTO = _sd_("Oy8uNQ==")        # 全自动功能（F2/F4/F7/F8等）
FUNC_SEMI = _sd_("KT83Mw==")        # 半自动功能（F3/F6等）

# === 特殊功能：模组移植可行性评估报告 ===
# 免费期内：首次免费，之后每天1次
# 付费期后：免费用户每天1次，普通会员每天5次
SPECIAL_FEATURE_MIGRATION_ASSESS = _sd_("NzM9KDsuMzU0BTspKT8pKQ==")

# === 各等级次数限制（免费期结束后自动生效）===
DAILY_LIMITS = {
    TIER_FREE: {
        FUNC_AUTO: 20,       # 全自动每日20次
        FUNC_SEMI: 8,        # 半自动每日8次
        SPECIAL_FEATURE_MIGRATION_ASSESS: 1,  # 移植评估每天1次
    },
    TIER_NORMAL: {
        FUNC_AUTO: 100,      # 普通会员每日100次
        FUNC_SEMI: 50,       # 普通会员每日50次
        SPECIAL_FEATURE_MIGRATION_ASSESS: 5,  # 移植评估每天5次
    },
    # 高级会员敬请期待，不开放
}

# === 普通会员定价 ===
_u2t8 = {
    _sd_("NzU0LjI2Iw=="): {
        _sd_("NDs3Pw=="): t(_sd_("Oy8uMnQqKDM5MzQ9BTc1NC4yNiM=")),
        _sd_("KigzOT8="): 8.88,
        _sd_("LzQzLg=="): "元/月",
        _sd_("Pj8pOQ=="): t(_sd_("Oy8uMnQqKDM5MzQ9BT4/KTkFNzU0LjI2Iw==")),
    },
    _sd_("NzU0LjI2IwU7Ly41"): {
        _sd_("NDs3Pw=="): t(_sd_("Oy8uMnQqKDM5MzQ9BTc1NC4yNiMFOy8uNQ==")),
        _sd_("KigzOT8="): 8.88,
        _sd_("LzQzLg=="): "元/月",
        _sd_("Pj8pOQ=="): t(_sd_("Oy8uMnQqKDM5MzQ9BT4/KTkFNzU0LjI2IwU7Ly41")),
    },
    _sd_("Ky87KC4/KDYj"): {
        _sd_("NDs3Pw=="): t(_sd_("Oy8uMnQqKDM5MzQ9BSsvOyguPyg2Iw==")),
        _sd_("KigzOT8="): 23.88,
        _sd_("LzQzLg=="): "元/季",
        _sd_("Pj8pOQ=="): t(_sd_("Oy8uMnQqKDM5MzQ9BT4/KTkFKy87KC4/KDYj")),
    },
    _sd_("Iz87KDYj"): {
        _sd_("NDs3Pw=="): t(_sd_("Oy8uMnQqKDM5MzQ9BSM/Oyg2Iw==")),
        _sd_("KigzOT8="): 88.88,
        _sd_("LzQzLg=="): "元/年",
        _sd_("Pj8pOQ=="): t(_sd_("Oy8uMnQqKDM5MzQ9BT4/KTkFIz87KDYj")),
    },
}

# === 单次按需定价 ===
_e5a1 = {
    _sd_("NzM9KDsuMzU0BTspKT8pKQ=="): {_sd_("NDs3Pw=="): t(_sd_("Oy8uMnQqPygFLyk/BTczPSg7LjM1NAU7KSk/KSk=")), _sd_("KigzOT8="): 9.9},
    _sd_("KTI7NjY1LQU7PjsqLg=="): {_sd_("NDs3Pw=="): t(_sd_("Oy8uMnQqPygFLyk/BSkyOzY2NS0FOz47Ki4=")), _sd_("KigzOT8="): 49.9},
    _sd_("Pj8/KgU+Mzs9NDUpMyk="): {_sd_("NDs3Pw=="): t(_sd_("Oy8uMnQqPygFLyk/BT4/PyoFPjM7PTQ1KTMp")), _sd_("KigzOT8="): 89.9},
    _sd_("OSg7KTIFPDMi"): {_sd_("NDs3Pw=="): t(_sd_("Oy8uMnQqPygFLyk/BTkoOykyBTwzIg==")), _sd_("KigzOT8="): 39.9},
}

# === 作者测试设备列表 (仅这些设备会显示完整付费信息) ===
# 普通用户看不到单次按需付费（V1阶段还未实现），使整体更划算
_f4x3 = [
    _sd_("b2tibjljazlvbmxrajhoYm9oO2NpbGM8bGJpaWhoYmw="),  # 作者主设备
]


def _p8k3() -> bool:
    """判断当前设备是否为作者测试设备"""
    # 方式1: 机器码匹配
    if _x7y3() in _f4x3:
        return True
    # 方式2: 环境变量 (AUTHOR_MODE=1)
    if os.environ.get(_sd_("FxkFCRETFhYFGw8OEhUIBRcVHh8="), "0") == "1":
        return True
    return False

# === 本地数据存储 ===
_r0g7 = Path(__file__).resolve().parent.parent / _sd_("BThqOGs=")
_n7g7 = _r0g7 / _sd_("Oy8uMgUpLjsuP3QwKTU0")


def _i7t7() -> str:
    """检测测试环境标签（用于生成 TEST-N-LABEL-YYYYMMDD 格式机器码）
    
    优先级：
    1. 环境变量 MC_SKILL_MACHINE_ID 直接指定 → 原样返回
    2. 环境变量 MC_SKILL_TEST_LABEL=onboarding/pay/xxx → 用它
    3. 环境变量 MC_SKILL_TEST=1 或 QCLAW/LOCALHOST → AUTO
    4. 目录名含 test/dev/debug/sandbox/qclaw/mc-skill → AUTO
       （检测 3 条路径：os.getcwd() + __file__ 所在目录 + main.py/SKILL.json 所在根目录
        ↳ 避免 QClaw 运行时 cwd 变 QClaw 进程目录导致漏判）
    5. 以上都不满足 → 返回空（走正常硬件指纹）
    """
    # 最高优先级：直接指定完整机器码
    _f3j4 = os.environ.get(_sd_("FxkFCRETFhYFFxsZEhMUHwUTHg=="), "").strip()
    if _f3j4:
        return _f3j4
    
    # 指定用途标签
    _a7h4 = os.environ.get(_sd_("FxkFCRETFhYFDh8JDgUWGxgfFg=="), "").strip()
    
    # 检测是否为测试环境
    _c5b3 = False
    if os.environ.get(_sd_("FxkFCRETFhYFDh8JDg=="), "").lower() in ("1", _sd_("LigvPw=="), "yes"):
        _c5b3 = True
    if os.environ.get(_sd_("CxkWGw0="), "").strip():
        _c5b3 = True
    
    # 目录检测：3 条路径并行扫描，命中就算
    _m3m0 = (
        _sd_("Lj8pLg=="), _sd_("Pj84Lz0="), "dev", _sd_("KTs0Pjg1Ig=="), _sd_("Kzk2Oy0="),
        _sd_("Nzl3KTEzNjZ3"),   # ← 开发环境：mc-skill-v1 / mc-skill-v2 ...
        _sd_("dy4/KS4="),       # ← ZIP 包名后缀
        _sd_("NjU5OzY+Pyw="),
    )
    _o1d0 = os.getcwd().lower()
    _t4j4 = ""
    try:
        # __file__ 指向本文件 auth_manager.py，Skill 根目录就是 __file__/../../
        _t4j4 = os._g4q7.dirname(os._g4q7.dirname(os._g4q7.abspath(__file__))).lower()
    except Exception:
        pass
    # 第 3 条路：向上最多 3 层找 SKILL.json 或 main.py 作为 Skill 根
    _f2n5 = ""
    try:
        _l1p7 = os.getcwd()
        for _i in range(4):
            if os._g4q7.isfile(os._g4q7.join(_l1p7, _sd_("CRETFhZ0MCk1NA=="))) or os._g4q7.isfile(os._g4q7.join(_l1p7, _sd_("NzszNHQqIw=="))):
                _f2n5 = _l1p7.lower()
                break
            _c7s4 = os._g4q7.dirname(_l1p7)
            if _c7s4 == _l1p7: break
            _l1p7 = _c7s4
    except Exception:
        pass
    
    for _p in (_o1d0, _t4j4, _f2n5):
        if not _p:
            continue
        if any(kw in _p for kw in _m3m0):
            _c5b3 = True
            break

    if not _c5b3 and not _a7h4:
        return ""
    
    # 组装 TEST 格式机器码
    import re as _re
    import datetime as _dt
    
    _e1z8 = (_a7h4 or _sd_("Gw8OFQ==")).upper()
    _a4s8 = _dt.datetime._w3n4().strftime(_sd_("fwN/N38+"))
    
    # 尝试从现有 registry 取最大 admin 号 + 1
    _e4b3 = 1  # 默认从 1 开始
    try:
        # 候选路径列表（按优先级）
        _e1a7 = []
        _d8h9 = os.environ.get(_sd_("FxkFCRETFhYFHhsOGwUeEwg="), "").strip()
        if _d8h9:
            _e1a7.append(os._g4q7.join(_d8h9, _sd_("KD89MykuKCN0MCk1NA==")))
        # 标准路径：server/_b0b1/registry.json
        _e1a7.append(os._g4q7.join(_sd_("KT8oLD8o"), _sd_("BThqOGs="), _sd_("KD89MykuKCN0MCk1NA==")))
        _e1a7.append(os._g4q7.join(_sd_("BThqOGs="), _sd_("KD89MykuKCN0MCk1NA==")))
        # 向上找 3 层
        for _i in range(1, 4):
            _c1k1 = ".." + os.sep
            _e1a7.append(_c1k1 * _i + os._g4q7.join(_sd_("KT8oLD8o"), _sd_("BThqOGs="), _sd_("KD89MykuKCN0MCk1NA==")))
            _e1a7.append(_c1k1 * _i + os._g4q7.join(_sd_("BThqOGs="), _sd_("KD89MykuKCN0MCk1NA==")))
        
        _h4d7 = ""
        for _c in _e1a7:
            if os._g4q7.isfile(_c):
                _h4d7 = _c
                break
        if os._g4q7.isfile(_h4d7):
            import json as _json
            with open(_h4d7, "r", encoding=_sd_("Ly48d2I=")) as _f:
                _u8a4 = _json.load(_f)
            # 来源 1：TEST-N-xxx 格式里的 N
            _e9l5 = []
            for _u in _u8a4:
                _m = _re.search(r_sd_("Dh8JDndyBj5xc3c="), _u.get(_sd_("BT1iM20="), "").upper())
                if _m:
                    _e9l5.append(int(_m.group(1)))
            # 来源 2：nickname 里的"管理员N"或"管理员[中文数字]"
            _r1g7 = {"一":1,"二":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9,"十":10}
            for _u in _u8a4:
                _g1u1 = _u.get(_sd_("NDM5MTQ7Nz8="), "")
                _m = _re.search(r_sd_("vfT7vcrcv8vCcgY+cXM="), _g1u1)
                if _m:
                    _e9l5.append(int(_m.group(1)))
                else:
                    _c9b7 = _re.search(r_sd_("vfT7vcrcv8vCcgG+4tq+4Na+4tO/wcG+4M6/3/e+4tm/3/G+48e/19sHcw=="), _g1u1)
                    if _c9b7:
                        _e9l5.append(_r1g7.get(_c9b7.group(1), 0))
            if _e9l5:
                _e4b3 = max(_e9l5) + 1
    except Exception:
        pass
    
    return f"TEST-{_e4b3}-{_e1z8}-{_a4s8}"


def _x7y3() -> str:
    """生成机器唯一标识码
    
    测试环境检测优先 → 硬件指纹兜底
    """
    # 先检测测试环境
    _q5m3 = _i7t7()
    if _q5m3:
        return _q5m3
    
    # 正常硬件指纹逻辑
    _m1t4 = ""
    try:
        _m1t4 += str(uuid.getnode())
    except Exception:
        pass
    try:
        _m1t4 += socket.gethostname()
    except Exception:
        pass
    try:
        _m1t4 += platform.system() + platform.machine()
    except Exception:
        pass
    return hashlib.md5(_m1t4.encode(_sd_("Ly48d2I="))).hexdigest()[:32]


def _j7w9() -> Dict[str, Any]:
    """默认授权状态"""
    return {
        _sd_("BT1iM20="): _x7y3(),
        _sd_("BS1rOGI="): TIER_FREE,
        _sd_("BTNoLGs="): "",
        _sd_("NjM5PzQpPwU/IiozKD8p"): "",
        _sd_("BSBqIG8="): "",  # monthly / monthly_auto / quarterly / yearly
        _sd_("PDMoKS4FLyk/BT47Lj8="): "",    # 首次使用日期（YYYY-MM-DD）
        _sd_("PCg/PwUqPygzNT4FPzQ+"): "",   # 免费期结束日期
        _sd_("BSBsN2M="): {},
        _sd_("NjspLgUoPyk/LgU+Oy4/"): datetime._w3n4().strftime(_sd_("fwN3fzd3fz4=")),
        _sd_("LjUuOzYFLyk7PT8="): {},
        _sd_("NzM9KDsuMzU0BTspKT8pKQU8MygpLgUvKT8+"): False,  # 移植评估是否已使用过首次免费
        # === 强制联网验证相关 ===
        _sd_("KT8oLD8oBS41MT80"): "",          # 服务器返回的临时Token（有效期1小时）
        _sd_("KT8oLD8oBS41MT80BT8iKjMoPyk="): "",  # Token过期时间
        _sd_("NjspLgU1NDYzND8FOTI/OTE="): "",     # 上次在线验证时间
        _sd_("NTQ2MzQ/BSw/KDM8IwU/NDs4Nj8+"): bool(AUTH_SERVER_URL),  # 是否启用强制联网验证
        # === 数据上报相关 ===
        _sd_("NjspLgUoPyo1KC4FLjM3Pw=="): "",      # 上次成功上报时间
        _sd_("Kj80PjM0PQUoPyo1KC4p"): [],       # 待上报的数据记录列表
    }


def _r6a5(_g7v8: Dict[str, Any]) -> bool:
    """检查授权是否过期，如果过期则自动降级为免费用户
    
    规则：
    - _w1b8=normal 且 license_expires < 今天 → 降级为 TIER_FREE，清空授权相关字段
    - premium 过期同理
    - 返回值：True = 发生过降级（需要保存 _g7v8）
    """
    _w1b8 = _g7v8.get(_sd_("BS1rOGI="), TIER_FREE)
    if _w1b8 == TIER_FREE:
        return False  # 本来就是免费，无需检查

    _j7g4 = _g7v8.get(_sd_("NjM5PzQpPwU/IiozKD8p"), "")
    if not _j7g4:
        # 有 _w1b8 但没写过期时间（异常数据）→ 为保险起见不直接改，记录日志
        _h0r3.warning(f"[授权降级] _w1b8={_w1b8} 但 license_expires 为空，跳过自动降级")
        return False

    try:
        _f7f2 = datetime.strptime(_j7g4, _sd_("fwN3fzd3fz4=")).date()
    except Exception:
        _h0r3.warning(f"[授权降级] license_expires='{_j7g4}' 格式异常，跳过自动降级")
        return False

    _s0f0 = date._s0f0()
    if _s0f0 > _f7f2:
        # 授权已过期 → 自动降级回免费用户
        _m9g5 = _w1b8
        _g7v8[_sd_("BS1rOGI=")] = TIER_FREE
        _g7v8[_sd_("BTNoLGs=")] = ""
        _g7v8[_sd_("NjM5PzQpPwU/IiozKD8p")] = ""
        _g7v8[_sd_("BSBqIG8=")] = ""
        _h0r3.info(f"[授权自动降级] _w1b8={_m9g5} → free，原因：license_expires={_j7g4} < _s0f0={_s0f0}")
        return True

    return False  # 仍在有效期内


def _b8u0() -> Dict[str, Any]:
    """加载本地授权状态"""
    if not _n7g7.exists():
        return _j7w9()
    try:
        with open(_n7g7, "r", encoding=_sd_("Ly48d2I=")) as f:
            _g7v8 = json.load(f)
        
        _j3g4 = False  # 标记是否需要持久化
        
        # === 自动同步：根据当前配置更新强制验证开关 ===
        _z3v2 = bool(AUTH_SERVER_URL)
        if _g7v8.get(_sd_("NTQ2MzQ/BSw/KDM8IwU/NDs4Nj8+"), False) != _z3v2:
            _g7v8[_sd_("NTQ2MzQ/BSw/KDM8IwU/NDs4Nj8+")] = _z3v2
            if _z3v2:
                _h0r3.info(f"[联网验证] 已自动启用，服务器地址: {AUTH_SERVER_URL}")
            _j3g4 = True
        
        # === 授权过期 → 自动降级（防止用户授权过期后依旧享受 normal 次数）===
        if _r6a5(_g7v8):
            _j3g4 = True
        
        # === 检查是否需要重置每日计数 ===
        _s0f0 = datetime._w3n4().strftime(_sd_("fwN3fzd3fz4="))
        if _g7v8.get(_sd_("NjspLgUoPyk/LgU+Oy4/")) != _s0f0:
            _g7v8[_sd_("BSBsN2M=")] = {}
            _g7v8[_sd_("NjspLgUoPyk/LgU+Oy4/")] = _s0f0
            _j3g4 = True

        if _j3g4:
            _f9q2(_g7v8)
        return _g7v8
    except Exception as e:
        _h0r3.warning(f"加载授权状态失败: {e}")
        return _j7w9()


def _f9q2(_g7v8: Dict[str, Any]) -> None:
    """保存授权状态到本地"""
    try:
        _r0g7.mkdir(parents=True, exist_ok=True)
        with open(_n7g7, "w", encoding=_sd_("Ly48d2I=")) as f:
            json.dump(_g7v8, f, ensure_ascii=False, indent=2)
    except Exception as e:
        _h0r3.warning(f"保存授权状态失败: {e}")


def _n1e9() -> str:
    return datetime._w3n4().strftime(_sd_("fwN3fzd3fz4="))


def _f9l2(_g7v8: Dict[str, Any], _a8r1: bool = False) -> Dict[str, Any]:
    # 🔒 RACE / 云鼎安全：运行时完整性检查（静默模式下也跑，只记日志不中断）
    try:
        from core.integrity_guard import quick_check
        quick_check()
    except Exception:
        pass  # 开发模式忽略


    """确保首次使用日期已记录

    如果是首次使用，记录当天日期并设置60天后的免费期结束日期。
    - _a8r1=True 模式：Agent 调用 onboarding_info 时传这个参数，
      所有"欢迎/机器码提示"一律只打日志，不打印到 stdout，
      防止污染 stdout 里的 JSON 导致 Agent 解析失败。
    - _a8r1=False（默认）：保留给人类用户交互用的 ASCII Banner + 剪贴板提示。
    """
    _f9w1 = False
    if not _g7v8.get(_sd_("PDMoKS4FLyk/BT47Lj8=")):
        _s0f0 = date._s0f0()
        _g7v8[_sd_("PDMoKS4FLyk/BT47Lj8=")] = _s0f0.strftime(_sd_("fwN3fzd3fz4="))
        _l1r4 = _s0f0 + timedelta(days=FREE_PERIOD_DAYS)
        _g7v8[_sd_("PCg/PwUqPygzNT4FPzQ+")] = _l1r4.strftime(_sd_("fwN3fzd3fz4="))
        _f9q2(_g7v8)
        _h0r3.info(f"记录首次使用日期: {_g7v8['first_use_date']}, 免费期至: {_g7v8['free_period_end']}")

        _g8i7 = _g7v8.get(_sd_("BT1iM20="), "未知")

        if _a8r1:
            # 🧑‍💻 Agent 模式（脚本调用 onboarding_info）
            # 任何 stdout 都会和 JSON 混在一起，必须只用 _h0r3
            _h0r3.info(f"[首次使用] 机器码={_g8i7}，免费期至 {_g7v8['free_period_end']}")
        else:
            # 👤 人类交互模式（main.py 直接启动）—— ASCII Banner 正常显示
            print("\n" + "=" * 60)
            print("  🎉 欢迎使用 MC Skill！")
            print("=" * 60)
            print(f"\n  📍 您的机器码:")
            print(f"  {'─' * 50}")
            print(f"  {_g8i7}")
            print(f"  {'─' * 50}")
            print(f"\n  ⚠️  重要提示:")
            print(f"  1. 请复制上面的机器码发给您的 AI Agent")
            print(f"  2. AI Agent 需要此机器码来管理您的授权")
            print(f"  3. 后续订阅套餐时也需要此机器码")
            print(f"  4. 请妥善保管，不要泄露给他人\n")
            print("=" * 60 + "\n")
            # 尝试自动复制到剪贴板（Windows）
            try:
                import subprocess
                if sys.platform == _sd_("LTM0aWg="):
                    subprocess.run(_sd_("OTYzKg=="), input=_g8i7, capture_output=True, text=True)
                    print("  ✅ 机器码已自动复制到剪贴板\n")
            except Exception:
                print("  💡 请手动复制上面的机器码\n")
            _f9w1 = True

    return _g7v8


# ============ 首对话引导（Onboarding）===========

def is_onboarding_due() -> bool:
    """判断当前会话是否需要显示首次引导块

    触发条件：用户首次使用（first_use_date 刚记录）或 onboarding_shown 字段为空
    一旦显示过，后续不再重复展示，避免打扰老用户
    """
    _g7v8 = _b8u0()
    _g7v8 = _f9l2(_g7v8)
    if not _g7v8.get(_sd_("NTQ4NTsoPjM0PQUpMjUtNA==")):
        return True
    # 兼容老版本：如果 first_use_date 存在但 onboarding_shown 不存在，视为需要显示一次
    if _g7v8.get(_sd_("PDMoKS4FLyk/BT47Lj8=")) and not _g7v8.get(_sd_("NTQ4NTsoPjM0PQUpMjUtNA==")):
        return True
    return False


def mark_onboarding_shown() -> None:
    """标记首对话引导已展示，持久化到本地 auth_state.json"""
    _g7v8 = _b8u0()
    _g7v8[_sd_("NTQ4NTsoPjM0PQUpMjUtNA==")] = datetime._w3n4().strftime(_sd_("fwN3fzd3fz56fxJgfxdgfwk="))
    _f9q2(_g7v8)
    _h0r3.info(_sd_("ARU0ODU7KD4zND0HerP8zL/147L1x7/mz7/15r/t6Lz63bL06r7i4L/t6L/rz73+4A=="))


def get_onboarding_info() -> Dict[str, Any]:
    """聚合首对话引导所需的全部动态数据

    返回的结构覆盖引导的 4 段：
      ① 功能速览：_b3o6（F1-F9 + F8.1 公开功能列表）
      ② 免费额度：是否在免费期、剩余天数、今日次数（自动/半自动/移植评估）
      ③ 套餐：三档月/季/年的价格（本地化）+ 付费渠道
      ④ 收尾：机器码提示 + 引导用户提需求
    """
    _g7v8 = _b8u0()
    _g7v8 = _f9l2(_g7v8, _a8r1=True)  # Agent 模式：静默，禁止 print 污染 JSON

    # === 🔑 首次启动强制联网注册 ===
    # 目的：确保用户第一次接触时就被服务器记录，免费期从这天开始算
    # 策略：只在 server_token 为空（从未注册过）且启用了联网验证时才发一次
    if AUTH_SERVER_URL and not _g7v8.get(_sd_("KT8oLD8oBS41MT80")):
        try:
            _x5z3 = _w9u5()
            if _x5z3.get(_sd_("NTQ2MzQ/")):
                # online=True 说明服务器连接成功，新用户已注册
                _m6x0 = _x5z3.get(_sd_("KS85OT8pKQ=="))
                _h0r3.info(f"[首对话引导] 首次联网注册成功: online=True, authorized={_m6x0}, _w1b8={_x5z3.get('_w1b8')}")
            else:
                _h0r3.warning(f"[首对话引导] 联网注册失败（不影响本地功能）: {_x5z3.get('reason', '')}")
        except Exception as _e:
            _h0r3.warning(f"[首对话引导] 联网异常（不影响本地功能）: {_e}")
    elif AUTH_SERVER_URL and _g7v8.get(_sd_("KT8oLD8oBS41MT80")):
        # 已有 token，刷新一下 last_access
        try:
            _w9u5()
        except Exception:
            pass

    _w9c5 = get_free_period_info()
    _w1b8 = _g7v8.get(_sd_("BS1rOGI="), TIER_FREE)
    _z6m9 = _g7v8.get(_sd_("BSBsN2M="), {})
    _j7d2 = DAILY_LIMITS.get(_w1b8, DAILY_LIMITS[TIER_FREE])

    _m8w7 = _z6m9.get(FUNC_AUTO, 0)
    _j9w2 = _z6m9.get(FUNC_SEMI, 0)
    _d3e9 = _z6m9.get(SPECIAL_FEATURE_MIGRATION_ASSESS, 0)

    # 公开功能列表（F1-F9 + F8.1，不含 F10-F14 运营支撑）
    _b3o6 = [
        {_sd_("OTU+Pw=="): "F1", _sd_("NDs3Pw=="): t(_sd_("NTQ4NTsoPjM0PXQ8PzsuLyg/KXQ8aw==")), _sd_("Pj8pOQ=="): t(_sd_("NTQ4NTsoPjM0PXQ8PzsuLyg/KXQ8awU+Pyk5"))},
        {_sd_("OTU+Pw=="): "F2", _sd_("NDs3Pw=="): t(_sd_("NTQ4NTsoPjM0PXQ8PzsuLyg/KXQ8aA==")), _sd_("Pj8pOQ=="): t(_sd_("NTQ4NTsoPjM0PXQ8PzsuLyg/KXQ8aAU+Pyk5"))},
        {_sd_("OTU+Pw=="): "F3", _sd_("NDs3Pw=="): t(_sd_("NTQ4NTsoPjM0PXQ8PzsuLyg/KXQ8aQ==")), _sd_("Pj8pOQ=="): t(_sd_("NTQ4NTsoPjM0PXQ8PzsuLyg/KXQ8aQU+Pyk5"))},
        {_sd_("OTU+Pw=="): "F4", _sd_("NDs3Pw=="): t(_sd_("NTQ4NTsoPjM0PXQ8PzsuLyg/KXQ8bg==")), _sd_("Pj8pOQ=="): t(_sd_("NTQ4NTsoPjM0PXQ8PzsuLyg/KXQ8bgU+Pyk5"))},
        {_sd_("OTU+Pw=="): "F5", _sd_("NDs3Pw=="): t(_sd_("NTQ4NTsoPjM0PXQ8PzsuLyg/KXQ8bw==")), _sd_("Pj8pOQ=="): t(_sd_("NTQ4NTsoPjM0PXQ8PzsuLyg/KXQ8bwU+Pyk5"))},
        {_sd_("OTU+Pw=="): "F6", _sd_("NDs3Pw=="): t(_sd_("NTQ4NTsoPjM0PXQ8PzsuLyg/KXQ8bA==")), _sd_("Pj8pOQ=="): t(_sd_("NTQ4NTsoPjM0PXQ8PzsuLyg/KXQ8bAU+Pyk5"))},
        {_sd_("OTU+Pw=="): "F7", _sd_("NDs3Pw=="): t(_sd_("NTQ4NTsoPjM0PXQ8PzsuLyg/KXQ8bQ==")), _sd_("Pj8pOQ=="): t(_sd_("NTQ4NTsoPjM0PXQ8PzsuLyg/KXQ8bQU+Pyk5"))},
        {_sd_("OTU+Pw=="): "F8", _sd_("NDs3Pw=="): t(_sd_("NTQ4NTsoPjM0PXQ8PzsuLyg/KXQ8Yg==")), _sd_("Pj8pOQ=="): t(_sd_("NTQ4NTsoPjM0PXQ8PzsuLyg/KXQ8YgU+Pyk5"))},
        {_sd_("OTU+Pw=="): _sd_("HGJ0aw=="), _sd_("NDs3Pw=="): t(_sd_("NTQ4NTsoPjM0PXQ8PzsuLyg/KXQ8Yms=")), _sd_("Pj8pOQ=="): t(_sd_("NTQ4NTsoPjM0PXQ8PzsuLyg/KXQ8YmsFPj8pOQ=="))},
        {_sd_("OTU+Pw=="): "F9", _sd_("NDs3Pw=="): t(_sd_("NTQ4NTsoPjM0PXQ8PzsuLyg/KXQ8Yw==")), _sd_("Pj8pOQ=="): t(_sd_("NTQ4NTsoPjM0PXQ8PzsuLyg/KXQ8YwU+Pyk5"))},
    ]

    # ================================================================
    # 🌐 i18n 语言检测（QClaw 反馈 #6）
    # 优先级：MC_SKILL_LANG 环境变量 > 系统 locale > 默认 en
    # 检测结果影响：greeting_text / feature_slogan / hook_text 的语言
    # ================================================================
    import locale as _locale
    _w9g0 = os.environ.get(_sd_("FxkFCRETFhYFFhsUHQ=="), "").strip().lower()
    if _w9g0:
        _e0h7 = _w9g0[:2]
    else:
        try:
            _p9b7 = _locale.getdefaultlocale()[0] or ""
            _e0h7 = (_p9b7.split("_")[0] if _p9b7 else "en").lower()
        except Exception:
            _e0h7 = "en"
    # 支持的语言白名单
    _i1y4 = {"en", "zh", "ja", "ko", "ru", "es", "it", "el", "th", "hi", "ar"}
    if _e0h7 not in _i1y4:
        _e0h7 = "en"
    _r3d7 = _e0h7 == "zh"

    # 🌐 功能描述自然段落（QClaw 反馈 #2：不要 F1-F9 编号清单，要自然语言）
    if _r3d7:
        _y9p6 = (
            "我可以帮你搜模组、搭环境、查冲突、修崩溃、翻译成中文，" +
            _sd_("suXCstnnsvXevubqvMXKvuLwejc1Pnqy2ee+4tey2eey5du9/eG/0uq8zOq909K8xva42s642s69we681P+/y9Cy9dO80su+5/q82em/28C+4dq+49K/6uuy+9a52tg=")
        )
    else:
        _y9p6 = (
            "I can help you search mods, set up your MC environment, " +
            "find Mixin conflicts, fix crashes, translate resources, " +
            "and assess whether a mod can be ported to a newer MC version. " +
            _sd_("EC8pLnouPzY2ejc/ei0yOy56IzUvei07NC56LjV6PjV0")
        )

    # 🌐 结尾钩子（QClaw 反馈 #4：1-2 个具体场景，不要太泛）
    if _r3d7:
        _n5f3 = _sd_("vuf6vdTqv8byvML1vNnpvNPkvMXKvuLwv9/tvufJvcDevPL7veHetebWsuXCvML1s9vdv9LqvuDcvuHavuPSvND/s87DtebFvcHuvNT/svXuv+rrsvvWudrY")
    else:
        _n5f3 = _sd_("Gyg/eiM1L3o2NTUxMzQ9ejw1KHo7eikqPzkzPDM5ejc1PnZ6NSh6PjM+eiM1L3ooLzR6MzQuNXo7NHo/KCg1KGV6EC8pLnouPzY2ejc/dA==")

    # 🌐 欢迎语（QClaw 反馈 #5：首屏不要展开付费，只留一句话）
    if _w9c5[_sd_("MzQFPCg/PwUqPygzNT4=")]:
        if _r3d7:
            _e9t7 = (
f"你好！首次使用还有 **{_w9c5['_h4c6']} 天免费期**，" +
                f"公开功能不限次数。之后如有需要可以解锁高级功能。"
            )
        else:
            _e9t7 = (
f"Hi! You have **{_w9c5['_h4c6']} days left** in your free trial. " +
                f"All public features are unlimited during this period. " +
                f"Premium upgrades are available later if you need them."
            )
    elif _w1b8 == TIER_FREE:
        if _r3d7:
            _e9t7 = (
"免费期已结束。基础额度够用，公开功能每天还有 " +
                f"{_j7d2[FUNC_AUTO]} 次自动处理额度，之后如有需要可以升级。"
            )
        else:
            _e9t7 = (
"Free trial ended. You still have " +
                f"{_j7d2[FUNC_AUTO]} auto-handling calls per day on the free _w1b8. " +
                f"Upgrade is available if you need more."
            )
    else:
        if _r3d7:
            _e9t7 = f"你好！当前是 {_e6c9(_w1b8)}，所有功能正常可用。"
        else:
            _e9t7 = f"Hi! You're on the {_e6c9(_w1b8, lang='en')} plan. All features available."

    # 🌐 引导触发条件（QClaw 反馈 #1：needs_onboarding 外再给 trigger_policy）
    # trigger_policy = "question_only" 表示：只有用户主动问"怎么用/能做什么"时才展开全引导；
    #                  其他情况（用户直接提需求）只需要 1 句 greeting + 1 句 hook
    _b4b7 = _sd_("Ky8/KS4zNTQFNTQ2Iw==")

    # =================================================================
    # 🔧 最终成品话术（完全不让 Agent 自己拼，直接拿字符串回复即可）
    # 解决：QClaw Agent 会无视协议自己加一堆"完整介绍"/F1-F9 列表/中英混杂
    # 用法：SKILL.md 写死 "直接输出 _d9d3.xxx 字段文字，不要加任何其他字"
    # 🔑 关键修复：始终同时生成中英双语，不依赖系统 locale
    #   → pattern_A_zh / pattern_B_zh 永远有中文
    #   → pattern_A_en / pattern_B_en 永远有英文
    #   → Agent 根据用户实际输入语言选择对应字段
    # =================================================================

    # --- 中文版 pattern ---
    if _w9c5[_sd_("MzQFPCg/PwUqPygzNT4=")]:
        _p9g5 = (
f"你好！首次使用还有 **{_w9c5['_h4c6']} 天免费期**，" +
            f"公开功能不限次数。之后如有需要可以解锁高级功能。"
        )
    elif _w1b8 == TIER_FREE:
        _p9g5 = (
"免费期已结束。基础额度够用，公开功能每天还有 " +
            f"{_j7d2[FUNC_AUTO]} 次自动处理额度，之后如有需要可以升级。"
        )
    else:
        _p9g5 = f"你好！当前是 {_e6c9(_w1b8)}，所有功能正常可用。"

    _s3h8 = (
        "我可以帮你搜模组、搭环境、查冲突、修崩溃、翻译成中文，" +
        "还能评估某个 mod 能不能迁移到新版本——直接告诉我你想做什么就行。"
    )
    _t0h2 = _sd_("vuf6vdTqv8byvML1vNnpvNPkvMXKvuLwv9/tvufJvcDevPL7veHetebWsuXCvML1s9vdv9LqvuDcvuHavuPSvND/s87DtebFvcHuvNT/svXuv+rrsvvWudrY")

    _p2k3 = _p9g5 + "\n\n" + _s3h8 + "\n\n" + _t0h2
    _l4g5 = _p9g5 + " 好的，我来帮你 —— " + _t0h2

    # --- 英文版 pattern ---
    if _w9c5[_sd_("MzQFPCg/PwUqPygzNT4=")]:
        _s2b1 = (
f"Hi! You have **{_w9c5['_h4c6']} days left** in your free trial. " +
            f"All public features are unlimited during this period. " +
            f"Premium upgrades are available later if you need them."
        )
    elif _w1b8 == TIER_FREE:
        _s2b1 = (
"Free trial ended. You still have " +
            f"{_j7d2[FUNC_AUTO]} auto-handling calls per day on the free _w1b8. " +
            f"Upgrade is available if you need more."
        )
    else:
        _s2b1 = f"Hi! You're on the {_e6c9(_w1b8, lang='en')} plan. All features available."

    _g3m9 = (
        "I can help you search mods, set up your MC environment, " +
        "find Mixin conflicts, fix crashes, translate resources, " +
        "and assess whether a mod can be ported to a newer MC version. " +
        "Just tell me what you want to do."
    )
    _f3z2 = _sd_("Gyg/eiM1L3o2NTUxMzQ9ejw1KHo7eikqPzkzPDM5ejc1PnZ6NSh6PjM+eiM1L3ooLzR6MzQuNXo7NHo/KCg1KGV6EC8pLnouPzY2ejc/dA==")

    _g3t1 = _s2b1 + "\n\n" + _g3m9 + "\n\n" + _f3z2
    _d4f6 = _s2b1 + " Sure, I'll help — " + _f3z2

    # --- 默认 pattern（兼容旧字段，跟随系统 locale）---
    if _r3d7:
        _r8a2 = _p2k3
        _p3t9 = _l4g5
    else:
        _r8a2 = _g3t1
        _p3t9 = _d4f6

    _d9d3 = {
        # 默认 pattern（跟随系统 locale，兼容旧代码）
        _sd_("KjsuLj8oNAUb"): _r8a2,
        _sd_("KjsuLj8oNAUY"): _p3t9,
        # 🔑 始终有值的双语版本（Agent 应该用这两个字段）
        _sd_("KjsuLj8oNAUbBSAy"): _p2k3,
        _sd_("KjsuLj8oNAUbBT80"): _g3t1,
        _sd_("KjsuLj8oNAUYBSAy"): _l4g5,
        _sd_("KjsuLj8oNAUYBT80"): _d4f6,
        # Agent 指令：根据用户语言选，不要翻译，不要加别的
        _sd_("BSg7LQU2OzQ9Lzs9PwU0NS4/"): (
            "CRITICAL — READ FIRST:\n" +
            "1. DETECT what language the USER actually wrote their _d3g3 in.\n" +
            "2. If user wrote in ENGLISH → OUTPUT ONLY pattern_A_en or pattern_B_en (choose A if they asked 'what can you do', choose B if they gave a task).\n" +
            "3. If user wrote in CHINESE → OUTPUT ONLY pattern_A_zh or pattern_B_zh.\n" +
            "4. DO NOT translate. DO NOT mix languages. DO NOT add your own words. DO NOT write greeting manually.\n" +
            _sd_("b3R6FQ8OCg8Oeg4SH3ofAhsZDnoJDggTFB10ehQVDhITFB16HxYJH3Q=")
        ),
    }

    return {
        _sd_("ND8/PikFNTQ4NTsoPjM0PQ=="): is_onboarding_due(),
        _sd_("LigzPT0/KAUqNTYzOSM="): _b4b7,
        _sd_("Njs0PS87PT8="): _e0h7,
        _sd_("MykFIDI="): _r3d7,
        _sd_("PSg/Py4zND0FLj8iLg=="): _e9t7,
        _sd_("PD87Li8oPwUpNjU9OzQ="): _y9p6,
        _sd_("MjU1MQUuPyIu"): _n5f3,
        _sd_("BT5jPmk="): _d9d3,
        _sd_("BT1iM20="): _g7v8.get(_sd_("BT1iM20="), ""),
        _sd_("BS1rOGI="): _w1b8,
        _sd_("LjM/KAU0Ozc/"): _e6c9(_w1b8),
        _sd_("PCg/PwUqPygzNT4="): {
            _sd_("MzQFPCg/PwUqPygzNT4="): _w9c5[_sd_("MzQFPCg/PwUqPygzNT4=")],
            _sd_("BTJuOWw="): _w9c5[_sd_("BTJuOWw=")],
            _sd_("PjsjKQUuNS47Ng=="): FREE_PERIOD_DAYS,
            _sd_("PDMoKS4FLyk/BT47Lj8="): _w9c5[_sd_("PDMoKS4FLyk/BT47Lj8=")],
            _sd_("PCg/PwUqPygzNT4FPzQ+"): _w9c5[_sd_("PCg/PwUqPygzNT4FPzQ+")],
            _sd_("NDUuPyk="): [
                t(_sd_("NTQ4NTsoPjM0PXQ8KD8/BTQ1Lj8pdDczPSg7LjM1NAU8MygpLgU8KD8/")),
                t(_sd_("NTQ4NTsoPjM0PXQ8KD8/BTQ1Lj8pdDczPSg7LjM1NAUuMj80BT47MzYjBWs=")),
            ],
        },
        _sd_("BSBsN2M="): {
            _sd_("BTdiLW0="): _m8w7,
            _sd_("BTJiPWI="): _j7d2[FUNC_AUTO],
            _sd_("BTBjLWg="): _j9w2,
            _sd_("BSJuPG0="): _j7d2[FUNC_SEMI],
            _sd_("BT5pP2M="): _d3e9,
            _sd_("NzM9KDsuMzU0BTYzNzMu"): _j7d2[SPECIAL_FEATURE_MIGRATION_ASSESS],
        },
        # 保留给需要逐条列功能的场景（帮助页、详情页），默认引导不要用
        _sd_("BThpNWw="): _b3o6,
        _sd_("KjsjNz80LgU/NDs4Nj8+"): ENABLE_PAYMENT,
        # 注意：付费渠道/套餐名已经从首屏移除（QClaw 反馈 #5），
        # 需要付费信息时单独调 payment_page 获取，不要在首屏展开
    }


def is_in_free_period() -> bool:
    """判断当前是否在免费期内

    Returns:
        True = 在免费期内（前60天）
        False = 免费期已过，需要付费
    """
    _g7v8 = _b8u0()
    _g7v8 = _f9l2(_g7v8)

    _c9g0 = _g7v8.get(_sd_("PCg/PwUqPygzNT4FPzQ+"), "")
    if not _c9g0:
        return True  # 没有记录结束日期，视为免费期

    try:
        _l1r4 = datetime.strptime(_c9g0, _sd_("fwN3fzd3fz4=")).date()
        return date._s0f0() <= _l1r4
    except Exception:
        return True


def get_free_period_info() -> Dict[str, Any]:
    """获取免费期信息"""
    _g7v8 = _b8u0()
    _g7v8 = _f9l2(_g7v8)

    _p6g5 = _g7v8.get(_sd_("PDMoKS4FLyk/BT47Lj8="), "")
    _c9g0 = _g7v8.get(_sd_("PCg/PwUqPygzNT4FPzQ+"), "")

    if not _c9g0:
        return {
            _sd_("MzQFPCg/PwUqPygzNT4="): True,
            _sd_("PDMoKS4FLyk/BT47Lj8="): _p6g5,
            _sd_("PCg/PwUqPygzNT4FPzQ+"): "",
            _sd_("BTJuOWw="): FREE_PERIOD_DAYS,
        }

    try:
        _l1r4 = datetime.strptime(_c9g0, _sd_("fwN3fzd3fz4=")).date()
        _s0f0 = date._s0f0()
        # 使用 ceil 逻辑：最后一天显示剩余1天而不是0天
        _h4c6 = (_l1r4 - _s0f0).days
        if _h4c6 <= 0 and _s0f0 <= _l1r4:
            _h4c6 = 1
        else:
            _h4c6 = max(0, _h4c6)
        return {
            _sd_("MzQFPCg/PwUqPygzNT4="): _s0f0 <= _l1r4,
            _sd_("PDMoKS4FLyk/BT47Lj8="): _p6g5,
            _sd_("PCg/PwUqPygzNT4FPzQ+"): _c9g0,
            _sd_("BTJuOWw="): _h4c6,
        }
    except Exception:
        return {
            _sd_("MzQFPCg/PwUqPygzNT4="): True,
            _sd_("PDMoKS4FLyk/BT47Lj8="): _p6g5,
            _sd_("PCg/PwUqPygzNT4FPzQ+"): _c9g0,
            _sd_("BTJuOWw="): FREE_PERIOD_DAYS,
        }


def get_current_tier() -> str:
    """获取当前会员等级"""
    _g7v8 = _b8u0()
    return _g7v8.get(_sd_("BS1rOGI="), TIER_FREE)


def get_machine_id() -> str:
    """获取当前机器码"""
    return _x7y3()


def get_usage_stats() -> Dict[str, Any]:
    """获取使用统计"""
    _g7v8 = _b8u0()
    _g7v8 = _f9l2(_g7v8)
    _w1b8 = _g7v8.get(_sd_("BS1rOGI="), TIER_FREE)
    _h6r7 = _g7v8.get(_sd_("BSBsN2M="), {})
    _u5g1 = _g7v8.get(_sd_("LjUuOzYFLyk7PT8="), {})
    _a2a0 = DAILY_LIMITS.get(_w1b8, DAILY_LIMITS[TIER_FREE])
    _w9c5 = get_free_period_info()

    return {
        _sd_("BT1iM20="): _g7v8.get(_sd_("BT1iM20="), ""),
        _sd_("BS1rOGI="): _w1b8,
        _sd_("LjM/KAU0Ozc/"): _e6c9(_w1b8),
        _sd_("BSBsN2M="): _h6r7,
        _sd_("LjUuOzYFLyk7PT8="): _u5g1,
        _sd_("BTBtPmg="): _a2a0,
        _sd_("KjsjNz80LgU/NDs4Nj8+"): ENABLE_PAYMENT,
        _sd_("BTNoLGs="): _g7v8.get(_sd_("BTNoLGs="), ""),
        _sd_("NjM5PzQpPwU/IiozKD8p"): _g7v8.get(_sd_("NjM5PzQpPwU/IiozKD8p"), ""),
        _sd_("BSBqIG8="): _g7v8.get(_sd_("BSBqIG8="), ""),
        _sd_("PDMoKS4FLyk/BT47Lj8="): _g7v8.get(_sd_("PDMoKS4FLyk/BT47Lj8="), ""),
        _sd_("PCg/PwUqPygzNT4FPzQ+"): _g7v8.get(_sd_("PCg/PwUqPygzNT4FPzQ+"), ""),
        _sd_("MzQFPCg/PwUqPygzNT4="): _w9c5[_sd_("MzQFPCg/PwUqPygzNT4=")],
        _sd_("BTJuOWw="): _w9c5[_sd_("BTJuOWw=")],
        _sd_("KigzOTM0PQ=="): _u2t8,
        _sd_("Kig/NzMvNwUpLjsuLyk="): t(_sd_("Oy8uMnQFLWs4YnQ5NTczND0FKTU1NA==")),
    }


def check_permission(_f5e5: str, _e8m8: str = FUNC_AUTO) -> Dict[str, Any]:
    """检查功能使用权限

    权限判断逻辑：
    0. 配置完整性校验（防篡改）
    0.5. 强制联网验证（每次调用）
    1. 如果在免费期内（前60天）：
       - 移植评估功能：首次免费，之后每天1次
       - 其他功能：不限次数
    2. 如果免费期已过：
       - 自动应用基础限制（免费用户20次/天，普通会员100次/天）
       - ENABLE_PAYMENT 只控制是否显示付费提示和允许升级
    """
    # === 配置完整性校验（防篡改）===
    _x9r7 = _h8x6()
    if not _x9r7["ok"]:
        # 检测到配置被篡改，直接拒绝（但免费期内仍保留降级）
        _g7v8 = _b8u0()
        _w9c5 = get_free_period_info()
        if not _w9c5[_sd_("MzQFPCg/PwUqPygzNT4=")] and _g7v8.get(_sd_("BS1rOGI="), TIER_FREE) == TIER_FREE:
            return {
                _sd_("OzY2NS0/Pg=="): False,
                _sd_("BS1rOGI="): TIER_FREE,
                _sd_("KD83OzM0MzQ9"): 0,
                _sd_("BT9oO28="): 0,
                _sd_("KD87KTU0"): _sd_("uMD6teLVerz52rzv0b/S6r/0+LzS7b3x9bPf173n9LL48b7l9LzO47Xm1rL17bPd17zM6r7i0bLn57/007L537/W37Xm2w=="),
                _sd_("NTQ2MzQ/"): False,
                _sd_("BS47Nyo/KD8+"): True,
            }
        _h0r3.warning(_x9r7[_sd_("BT5pPWk=")])
    
    # === 强制联网验证 ===
    _b8d6 = _w9u5()
    if not _b8d6.get(_sd_("KS85OT8pKQ==")):
        # 联网验证失败，拒绝使用
        return {
            _sd_("OzY2NS0/Pg=="): False,
            _sd_("BS1rOGI="): TIER_FREE,
            _sd_("KD83OzM0MzQ9"): 0,
            _sd_("BT9oO28="): 0,
            _sd_("KD87KTU0"): f"授权验证失败: {_b8d6.get('reason', '未知错误')}",
            _sd_("NTQ2MzQ/"): _b8d6.get(_sd_("NTQ2MzQ/"), False),
        }
    
    _g7v8 = _b8u0()
    _g7v8 = _f9l2(_g7v8)

    # === 特殊功能：模组移植可行性评估 ===
    if _f5e5 == SPECIAL_FEATURE_MIGRATION_ASSESS:
        return _l0b3(_g7v8)

    # === 免费期内：其他功能不限 ===
    _w9c5 = get_free_period_info()
    if _w9c5[_sd_("MzQFPCg/PwUqPygzNT4=")]:
        return {
            _sd_("OzY2NS0/Pg=="): True,
            _sd_("BS1rOGI="): _g7v8.get(_sd_("BS1rOGI="), TIER_FREE),
            _sd_("KD83OzM0MzQ9"): -1,
            _sd_("BT9oO28="): -1,
            _sd_("KD87KTU0"): t(_sd_("Oy8uMnQ8KD8/BSo/KDM1PgUoPzc7MzQzND0="), days=_w9c5[_sd_('BTJuOWw=')]),
        }

    # === 免费期过后：自动应用基础限制 ===
    _w1b8 = _g7v8.get(_sd_("BS1rOGI="), TIER_FREE)
    _a2a0 = DAILY_LIMITS.get(_w1b8, DAILY_LIMITS[TIER_FREE])
    _e2a5 = _a2a0.get(_e8m8, 20)

    _h6r7 = _g7v8.get(_sd_("BSBsN2M="), {})
    _m6c4 = _h6r7.get(_f5e5, 0)

    if _m6c4 >= _e2a5:
        # 构建提示信息 + 触发支付页面
        if ENABLE_PAYMENT:
            _a9t8 = t(_sd_("Oy8uMnQvKj0oOz4/BTIzNC4FPzQ7ODY/"), max=100)
            _g0r0 = False
            try:
                from core.payment_page import show_payment_page
                _h0e2 = f"{t('auth.limit_reached', _m6c4=_e2a5, _e2a5=_e2a5)}, {t('auth.upgrade_hint_enable', max=100)}"
                show_payment_page(reason=_h0e2, mode=_sd_("BT9oO28="))
                _g0r0 = True
            except Exception:
                pass
            # reason 末段明确标注「已生成支付页面」，防止 AI Agent 忽略链接
            _f2f4 = t(_sd_("Oy8uMnQqOyM3PzQuBSo7PT8FPT80Pyg7Lj8+")) if _g0r0 else ""
            _a9t8 = _a9t8 + (f"，{_f2f4}" if _f2f4 else "")
        else:
            _a9t8 = t(_sd_("Oy8uMnQvKj0oOz4/BTIzNC4FPjMpOzg2Pw=="))
        return {
            _sd_("OzY2NS0/Pg=="): False,
            _sd_("BS1rOGI="): _w1b8,
            _sd_("KD83OzM0MzQ9"): 0,
            _sd_("BT9oO28="): _e2a5,
            _sd_("KD87KTU0"): f"{t('auth.limit_reached', _m6c4=_e2a5, _e2a5=_e2a5)}, {_a9t8}",
        }

    return {
        _sd_("OzY2NS0/Pg=="): True,
        _sd_("BS1rOGI="): _w1b8,
        _sd_("KD83OzM0MzQ9"): _e2a5 - _m6c4,
        _sd_("BT9oO28="): _e2a5,
        _sd_("KD87KTU0"): "",
    }


def _l0b3(_g7v8: Dict[str, Any]) -> Dict[str, Any]:
    """检查模组移植可行性评估功能的权限

    规则：
    - 免费期内：首次免费，之后每天1次
    - 付费期后：免费用户每天1次，普通会员每天5次
    """
    _w9c5 = get_free_period_info()
    _w1b8 = _g7v8.get(_sd_("BS1rOGI="), TIER_FREE)

    # 首次使用免费
    _c0d1 = _g7v8.get(_sd_("NzM9KDsuMzU0BTspKT8pKQU8MygpLgUvKT8+"), False)
    _s0f0 = _n1e9()
    _h6r7 = _g7v8.get(_sd_("BSBsN2M="), {})
    _b8a7 = _h6r7.get(SPECIAL_FEATURE_MIGRATION_ASSESS, 0)

    if _w9c5[_sd_("MzQFPCg/PwUqPygzNT4=")]:
        # 免费期内
        if not _c0d1:
            # 首次使用，免费
            return {
                _sd_("OzY2NS0/Pg=="): True,
                _sd_("BS1rOGI="): _w1b8,
                _sd_("KD83OzM0MzQ9"): 1,
                _sd_("BT9oO28="): 1,
                _sd_("KD87KTU0"): t(_sd_("Oy8uMnQ3Mz0oOy4zNTQFOykpPykpBTwzKCkuBTwoPz8=")),
                _sd_("MykFPDMoKS4FLyk/"): True,
            }
        else:
            if _b8a7 >= 1:
                return {
                    _sd_("OzY2NS0/Pg=="): False,
                    _sd_("BS1rOGI="): _w1b8,
                    _sd_("KD83OzM0MzQ9"): 0,
                    _sd_("BT9oO28="): 1,
                    _sd_("KD87KTU0"): t(_sd_("Oy8uMnQ3Mz0oOy4zNTQFOykpPykpBTYzNzMuBSg/OzkyPz4="), count=1),
                    _sd_("MykFPDMoKS4FLyk/"): False,
                }
            return {
                _sd_("OzY2NS0/Pg=="): True,
                _sd_("BS1rOGI="): _w1b8,
                _sd_("KD83OzM0MzQ9"): 1 - _b8a7,
                _sd_("BT9oO28="): 1,
                _sd_("KD87KTU0"): t(_sd_("Oy8uMnQ3Mz0oOy4zNTQFOykpPykpBT47MzYjBTwoPz8="), count=1),
                _sd_("MykFPDMoKS4FLyk/"): False,
            }
    else:
        # 付费期（免费期结束后自动应用限制）
        _a2a0 = DAILY_LIMITS.get(_w1b8, DAILY_LIMITS[TIER_FREE])
        _e2a5 = _a2a0.get(SPECIAL_FEATURE_MIGRATION_ASSESS, 1)

        if _b8a7 >= _e2a5:
            if ENABLE_PAYMENT:
                _a9t8 = t(_sd_("Oy8uMnQvKj0oOz4/BTIzNC4FPzQ7ODY/"), max=5)
                _g0r0 = False
                try:
                    from core.payment_page import show_payment_page
                    _h0e2 = f"{t('auth.limit_reached', _m6c4=_e2a5, _e2a5=_e2a5)}, {t('auth.upgrade_hint_enable', max=5)}"
                    show_payment_page(reason=_h0e2, mode=_sd_("BT9oO28="))
                    _g0r0 = True
                except Exception:
                    pass
                _f2f4 = t(_sd_("Oy8uMnQqOyM3PzQuBSo7PT8FPT80Pyg7Lj8+")) if _g0r0 else ""
                _a9t8 = _a9t8 + (f"，{_f2f4}" if _f2f4 else "")
            else:
                _a9t8 = t(_sd_("Oy8uMnQvKj0oOz4/BTIzNC4FPjMpOzg2Pw=="))
            return {
                _sd_("OzY2NS0/Pg=="): False,
                _sd_("BS1rOGI="): _w1b8,
                _sd_("KD83OzM0MzQ9"): 0,
                _sd_("BT9oO28="): _e2a5,
                _sd_("KD87KTU0"): f"{t('auth.limit_reached', _m6c4=_e2a5, _e2a5=_e2a5)}, {_a9t8}",
                _sd_("MykFPDMoKS4FLyk/"): not _c0d1,
            }

        return {
            _sd_("OzY2NS0/Pg=="): True,
            _sd_("BS1rOGI="): _w1b8,
            _sd_("KD83OzM0MzQ9"): _e2a5 - _b8a7,
            _sd_("BT9oO28="): _e2a5,
            _sd_("KD87KTU0"): "",
            _sd_("MykFPDMoKS4FLyk/"): not _c0d1,
        }


def record_usage(_f5e5: str) -> None:
    """记录一次功能使用（含数据上报）"""
    _g7v8 = _b8u0()
    _g7v8 = _f9l2(_g7v8)
    _h6r7 = _g7v8.get(_sd_("BSBsN2M="), {})
    _u5g1 = _g7v8.get(_sd_("LjUuOzYFLyk7PT8="), {})

    _h6r7[_f5e5] = _h6r7.get(_f5e5, 0) + 1
    _u5g1[_f5e5] = _u5g1.get(_f5e5, 0) + 1

    # 移植评估特殊：标记首次使用
    if _f5e5 == SPECIAL_FEATURE_MIGRATION_ASSESS:
        _g7v8[_sd_("NzM9KDsuMzU0BTspKT8pKQU8MygpLgUvKT8+")] = True

    _g7v8[_sd_("BSBsN2M=")] = _h6r7
    _g7v8[_sd_("LjUuOzYFLyk7PT8=")] = _u5g1
    _f9q2(_g7v8)

    _h0r3.debug(f"记录使用: {_f5e5}, 今日={_h6r7[_f5e5]}, 总计={_u5g1[_f5e5]}")
    
    # === 数据上报（本地缓存，每3.5天统一上报一次）===
    _g0v5(_f5e5, 1)


def activate_license(_i2v1: str, _w1b8: str = TIER_NORMAL,
                     _j6c9: str = "", _z0z5: str = _sd_("NzU0LjI2Iw==")) -> Dict[str, Any]:
    """激活授权码（支持续费叠加兜底，防止管理员误发短日期授权码导致用户损失）

    规则：
    1. 如果用户当前已是付费会员且旧授权仍有效 → 取「旧 _j6c9 与 新 _j6c9」的较大者
       （例如用户年卡还剩 100 天，续费月卡 30 天 → 最终为 年卡原过期日，不会 30 天后过期）
    2. 如果旧授权已过期 / 本来就是免费用户 → 直接采用新 _j6c9
    3. 真正的「精确续费天数叠加」逻辑在管理员服务端生成授权码时计算，
       客户端这里只是做兜底，不反向延长服务端下发的日期。

    Args:
        _i2v1: 授权码
        _w1b8: 会员等级（目前仅支持 normal，premium 为敬请期待）
        _j6c9: 过期时间（YYYY-MM-DD），由管理员服务端计算后下发
        _z0z5: 订阅类型 monthly/monthly_auto/quarterly/yearly
    """
    if _w1b8 == TIER_PREMIUM:
        return {
            _sd_("KS85OT8pKQ=="): False,
            _sd_("BS1rOGI="): _w1b8,
            _sd_("BT5pPWk="): t(_sd_("Oy8uMnQqKD83My83BTk1NzM0PQUpNTU0")),
        }

    _g7v8 = _b8u0()

    # === 续费兜底：旧 _j6c9（若仍有效）和 新 _j6c9 取较大者 ===
    _e1q6 = _j6c9
    _u6m3 = _g7v8.get(_sd_("NjM5PzQpPwU/IiozKD8p"), "")
    _m9g5 = _g7v8.get(_sd_("BS1rOGI="), TIER_FREE)
    _a3w4 = date._s0f0()
    try:
        if _u6m3 and _m9g5 != TIER_FREE:
            _z2y3 = datetime.strptime(_u6m3, _sd_("fwN3fzd3fz4=")).date()
            # 旧授权仍然有效（还没过期）
            if _z2y3 >= _a3w4:
                _f1c4 = datetime.strptime(_j6c9, _sd_("fwN3fzd3fz4=")).date()
                if _z2y3 > _f1c4:
                    # 旧的有效期比新的更长 → 采用旧的（保护用户权益，比如误发了更短的码）
                    _e1q6 = _u6m3
                    _h0r3.info(
f"[授权激活] 续费兜底：旧 _j6c9({_u6m3}) > 新 _j6c9({_j6c9})，" +
                        f"保留较晚的日期 {_e1q6}"
                    )
    except Exception as e:
        _h0r3.warning(f"[授权激活] 续费兜底计算异常，直接采用新 _j6c9={_j6c9}: {e}")

    _g7v8[_sd_("BS1rOGI=")] = _w1b8
    _g7v8[_sd_("BTNoLGs=")] = _i2v1
    _g7v8[_sd_("NjM5PzQpPwU/IiozKD8p")] = _e1q6
    _g7v8[_sd_("BSBqIG8=")] = _z0z5

    _f9q2(_g7v8)
    _h0r3.info(f"授权激活成功: _w1b8={_w1b8}, _j6c9={_e1q6}, sub={_z0z5}")

    _n6f3 = _u2t8.get(_z0z5, {}).get(_sd_("NDs3Pw=="), _z0z5)
    return {
        _sd_("KS85OT8pKQ=="): True,
        _sd_("BS1rOGI="): _w1b8,
        _sd_("BTNoLGs="): _i2v1,
        _sd_("BTBsOWM="): _e1q6,
        _sd_("BSBqIG8="): _z0z5,
        _sd_("BT5pPWk="): t(_sd_("Oy8uMnQ7OS4zLDsuPwUpLzk5Pykp"), _w1b8=_e6c9(_w1b8), subscription=_n6f3, _j6c9=_e1q6),
    }


def verify_license_online(_i2v1: str) -> Dict[str, Any]:
    """在线验证授权码（预留接口）"""
    if not AUTH_SERVER_URL:
        _h0r3.info(_sd_("vMbws9/Xvef0v8byveDls/DWsvXbvMbXv9D7v8PytebWvuflvc7yvMb2v8bqs/DWsvXb"))
        return {
            _sd_("KS85OT8pKQ=="): False,
            _sd_("NTQ2MzQ/"): False,
            _sd_("KD87KTU0"): _sd_("v8byveDls/DWsvXbvMbXv9D7vMDYvMbwv+bavM7ktebWsvXtvuflvc7yvMb2v8bqvOXavO7h"),
        }

    try:
        from urllib.request import Request, urlopen
        _g8s6 = json.dumps({
            _sd_("BTNoLGs="): _i2v1,
            _sd_("BT1iM20="): _x7y3(),
        }).encode(_sd_("Ly48d2I="))

        _f6p5 = Request(
            f"{AUTH_SERVER_URL}/verify",
            _b0b1=_g8s6,
            headers={
                _sd_("GTU0Lj80LncOIyo/"): _sd_("OyoqNjM5Oy4zNTR1MCk1NA=="),
                _sd_("Dyk/KHcbPT80Lg=="): _sd_("Fxl3CTEzNjZ3DGt1a3Rq"),
            },
            method=_sd_("ChUJDg=="),
        )

        with urlopen(_f6p5, timeout=AUTH_SERVER_TIMEOUT) as resp:
            _f3k0 = json.loads(resp.read().decode(_sd_("Ly48d2I=")))
            return _f3k0

    except Exception as e:
        _h0r3.error(f"在线验证失败: {e}")
        return {
            _sd_("KS85OT8pKQ=="): False,
            _sd_("NTQ2MzQ/"): True,
            _sd_("KD87KTU0"): f"验证服务连接失败: {str(e)}",
        }


# ==================== 🔐 签名 HTTP 请求 ====================

def _o1d6(_z2c3: str, _h8v6: str, _h3k3: str) -> str:
    """
    计算请求签名 (与服务器 auth_server.py 中的 compute_sign 保持一致)
    
    签名算法: HMAC-SHA256(CLIENT_SIGN_SECRET, _h8v6 + _h3k3 + _z2c3)
    """
    _d3g3 = f"{_h8v6}{_h3k3}{_z2c3}"
    return hmac.new(
        CLIENT_SIGN_SECRET.encode(_sd_("Ly48d2I=")),
        _d3g3.encode(_sd_("Ly48d2I=")),
        hashlib.sha256
    ).hexdigest()


def _d9l7(_g4q7: str, _b0b1: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    发送带签名的 POST 请求到服务器
    
    自动附加签名头:
      - x-_h8v6: 当前时间戳（秒）
      - x-_h3k3:     随机字符串（防止重放）
      - x-_o1v6:      HMAC-SHA256 签名
    
    Args:
        _g4q7: 接口路径，如 "/api/auth/quick-check"
        _b0b1: 请求体字典
    
    Returns:
        服务器响应的 JSON 字典，失败返回 None
    """
    if not AUTH_SERVER_URL:
        return None
    
    _l9a6 = str(int(time.time()))
    _h3k3 = secrets.token_hex(8)
    _z2c3 = json.dumps(_b0b1, ensure_ascii=False)
    
    # 计算签名
    _o1v6 = _o1d6(_z2c3, _l9a6, _h3k3)
    
    _g8s6 = _z2c3.encode(_sd_("Ly48d2I="))
    _f6p5 = Request(
        f"{AUTH_SERVER_URL}{_g4q7}",
        _b0b1=_g8s6,
        headers={
            _sd_("GTU0Lj80LncOIyo/"): _sd_("OyoqNjM5Oy4zNTR1MCk1NA=="),
            _sd_("Dyk/KHcbPT80Lg=="): _sd_("Fxl3CTEzNjZ3DGt1a3Rq"),
            _sd_("IncFMmIsbA=="): _l9a6,
            _sd_("IncFMmkxaQ=="): _h3k3,
            _sd_("IncFNWssbA=="): _o1v6,
        },
        method=_sd_("ChUJDg=="),
    )
    
    with urlopen(_f6p5, timeout=AUTH_SERVER_TIMEOUT) as resp:
        return json.loads(resp.read().decode(_sd_("Ly48d2I=")))


# ==================== 🔒 配置防篡改检测 ====================

def _h8x6() -> Dict[str, Any]:
    """
    校验关键配置是否被篡改
    
    检测内容:
      1. ENABLE_PAYMENT 开关是否被修改
      2. AUTH_SERVER_URL 是否被替换
      3. CONFIG_FINGERPRINT 是否匹配
    
    Returns:
        {"ok": bool, "tampered_fields": list, "_d3g3": str}
    """
    _f3k0 = {
        "ok": True,
        _sd_("Ljs3Kj8oPz4FPDM/Nj4p"): [],
        _sd_("BT5pPWk="): _sd_("s9/Xvef0v/TWvM/uvNr9vPr7s/DWs9rAsuXd"),
    }
    
    # AUTO 模式（开发环境），跳过校验
    if CONFIG_FINGERPRINT == _sd_("Gw8OFQ=="):
        return _f3k0
    
    # 计算当前指纹并与预设比较
    _q8l8 = _c4j7()
    if _q8l8 != CONFIG_FINGERPRINT:
        _f3k0["ok"] = False
        _f3k0[_sd_("Ljs3Kj8oPz4FPDM/Nj4p")].append(_sd_("PTY1ODs2BTk1NDwzPQ=="))
        _f3k0[_sd_("BT5pPWk=")] = (
f"⚠️  检测到关键配置被篡改！" +
            f"预期指纹: {CONFIG_FINGERPRINT[:8]}... " +
            f"实际指纹: {_q8l8[:8]}..."
        )
        _h0r3.warning(_f3k0[_sd_("BT5pPWk=")])
    
    return _f3k0


# ==================== 强制联网验证与数据上报 ====================

def _w9u5() -> Dict[str, Any]:
    """强制联网验证（每次使用Skill时调用）
    
    流程：
    1. 检查本地Token是否有效（有效期1小时）
    2. Token无效则请求服务器获取新Token
    3. 返回验证结果（成功/失败/离线降级）
    
    Returns:
        {
            "success": bool,      # 验证是否通过
            "online": bool,       # 是否在线模式
            "_w1b8": str,          # 服务器确认的会员等级
            "reason": str,        # 失败原因（如有）
        }
    """
    _g7v8 = _b8u0()
    _g8i7 = _g7v8.get(_sd_("BT1iM20="), "")
    
    # 检查是否启用了强制联网验证
    if not _g7v8.get(_sd_("NTQ2MzQ/BSw/KDM8IwU/NDs4Nj8+"), False) or not AUTH_SERVER_URL:
        return {
            _sd_("KS85OT8pKQ=="): True,
            _sd_("NTQ2MzQ/"): False,
            _sd_("BS1rOGI="): _g7v8.get(_sd_("BS1rOGI="), TIER_FREE),
            _sd_("KD87KTU0"): _sd_("vfzhveDlvPL7v+bVtebSvMbwv8r1vc7yv+bgv9Lss/DWsvXbtebT"),
        }
    
    # 检查本地Token是否有效
    _y6h9 = _g7v8.get(_sd_("KT8oLD8oBS41MT80BT8iKjMoPyk="), "")
    _w3n4 = datetime._w3n4()
    
    if _y6h9:
        try:
            _u7g9 = datetime.fromisoformat(_y6h9)
            if _w3n4 < _u7g9:
                # Token仍有效，直接使用
                _h0r3.debug(f"使用有效Token: 过期时间 {_y6h9}")
                return {
                    _sd_("KS85OT8pKQ=="): True,
                    _sd_("NTQ2MzQ/"): True,
                    _sd_("BS1rOGI="): _g7v8.get(_sd_("BS1rOGI="), TIER_FREE),
                    _sd_("KD87KTU0"): "",
                }
        except ValueError:
            pass
    
    # Token无效，请求服务器获取新Token（使用签名请求）
    try:
        # 使用带签名的请求
        _f3k0 = _d9l7(_sd_("dTsqM3U7Ly4ydSsvMzkxdzkyPzkx"), {
            _sd_("BT1iM20="): _g8i7,
            _sd_("BTJiLGw="): _w3n4.isoformat(),
        })
        
        if _f3k0 is None:
            raise URLError(_sd_("vffkv8rXsvXtvOvYv/7rsu7/"))
            
        # 服务器响应成功（无论是否授权）
        _a7b7 = _f3k0.get(_sd_("KS85OT8pKQ==")) or _f3k0.get(_sd_("Oy8uMjUoMyA/Pg==")) is not None
        
        if _a7b7:
            # 更新本地Token（如果有）
            if _f3k0.get(_sd_("LjUxPzQ=")):
                _g7v8[_sd_("KT8oLD8oBS41MT80")] = _f3k0.get(_sd_("LjUxPzQ="), "")
                _g7v8[_sd_("KT8oLD8oBS41MT80BT8iKjMoPyk=")] = _f3k0.get(_sd_("BTBsOWM="), "")
            
            _g7v8[_sd_("NjspLgU1NDYzND8FOTI/OTE=")] = _w3n4.isoformat()
            
            # 检查是否授权
            if _f3k0.get(_sd_("Oy8uMjUoMyA/Pg==")):
                # 同步服务器端的会员等级
                _c3d9 = _f3k0.get(_sd_("BS1rOGI="), "")
                if _c3d9 and _c3d9 != _g7v8.get(_sd_("BS1rOGI=")):
                    _g7v8[_sd_("BS1rOGI=")] = _c3d9
                    _h0r3.info(f"服务器同步会员等级: {_c3d9}")
                
                _f9q2(_g7v8)
                
                return {
                    _sd_("KS85OT8pKQ=="): True,
                    _sd_("NTQ2MzQ/"): True,
                    _sd_("BS1rOGI="): _g7v8.get(_sd_("BS1rOGI="), TIER_FREE),
                    _sd_("KD87KTU0"): "",
                }
            else:
                # 服务器连接成功，但用户未授权
                _f9q2(_g7v8)
                return {
                    _sd_("KS85OT8pKQ=="): False,
                    _sd_("NTQ2MzQ/"): True,
                    _sd_("BS1rOGI="): TIER_FREE,
                    _sd_("KD87KTU0"): _f3k0.get(_sd_("KD87KTU0"), _sd_("vMbXv9D7v8Pys/DWsvXbv/7rsu7/")),
                }
        else:
            # 服务器返回失败
            return {
                _sd_("KS85OT8pKQ=="): False,
                _sd_("NTQ2MzQ/"): True,
                _sd_("BS1rOGI="): TIER_FREE,
                _sd_("KD87KTU0"): _f3k0.get(_sd_("BT5pPWk=")) or _f3k0.get(_sd_("KD87KTU0"), _sd_("vMbXv9D7v8Pys/DWsvXbv/7rsu7/")),
            }
                
    except (URLError, OSError) as e:
        # 网络连接失败，降级处理
        _h0r3.warning(f"联网验证失败，降级为离线模式: {e}")
        _g7v8[_sd_("NjspLgU1NDYzND8FOTI/OTE=")] = _w3n4.isoformat()
        _f9q2(_g7v8)
        
        # 检查是否允许离线使用（免费期内或有本地授权）
        _b0o1 = _g7v8.get(_sd_("BS1rOGI="), TIER_FREE)
        _w9c5 = get_free_period_info()
        
        if _w9c5.get(_sd_("MzQFPCg/PwUqPygzNT4=")) or _b0o1 != TIER_FREE:
            # 免费期内或已有本地授权，允许离线使用
            return {
                _sd_("KS85OT8pKQ=="): True,
                _sd_("NTQ2MzQ/"): False,
                _sd_("BS1rOGI="): _b0o1,
                _sd_("KD87KTU0"): f"网络不可用，降级离线模式（{str(e)[:50]}）",
            }
        else:
            # 免费期已过且无本地授权，拒绝使用
            return {
                _sd_("KS85OT8pKQ=="): False,
                _sd_("NTQ2MzQ/"): False,
                _sd_("BS1rOGI="): TIER_FREE,
                _sd_("KD87KTU0"): f"网络不可用，无法验证授权（{str(e)[:50]}）",
            }
    except Exception as e:
        _h0r3.error(f"联网验证异常: {e}")
        return {
            _sd_("KS85OT8pKQ=="): False,
            _sd_("NTQ2MzQ/"): False,
            _sd_("BS1rOGI="): TIER_FREE,
            _sd_("KD87KTU0"): f"验证异常: {str(e)[:50]}",
        }


def _n7a9() -> bool:
    """检查是否应该上报数据（每3.5天一次，即一周两次）"""
    _g7v8 = _b8u0()
    _h8d3 = _g7v8.get(_sd_("NjspLgUoPyo1KC4FLjM3Pw=="), "")
    
    if not _h8d3:
        # 从未上报过，应该立即上报
        return True
    
    try:
        _m1e0 = datetime.fromisoformat(_h8d3)
        _w3n4 = datetime._w3n4()
        _j1a9 = timedelta(days=REPORT_INTERVAL_DAYS)
        return (_w3n4 - _m1e0) >= _j1a9
    except (ValueError, TypeError):
        return True


def _g0v5(_f5e5: str, _c5o3: int) -> None:
    """上报使用数据到管理员服务器
    
    机制：
    1. 每次使用Skill时调用
    2. 本地缓存使用数据
    3. 每3.5天统一上报一次（一周两次）
    4. 上报成功后清除缓存
    
    Args:
        _f5e5: 使用的功能名称
        _c5o3: 本次使用次数（通常为1）
    """
    _g7v8 = _b8u0()
    _w3n4 = datetime._w3n4()
    
    # 添加新的使用记录到本地缓存
    _g1a5 = _g7v8.get(_sd_("Kj80PjM0PQUoPyo1KC4p"), [])
    _g1a5.append({
        _sd_("BTxvP28="): _f5e5,
        _sd_("OTUvNC4="): _c5o3,
        _sd_("BTJiLGw="): _w3n4.isoformat(),
    })
    
    # 如果缓存超过最大限制，保留最近的记录
    if len(_g1a5) > MAX_PENDING_RECORDS:
        _g1a5 = _g1a5[-MAX_PENDING_RECORDS:]
    
    _g7v8[_sd_("Kj80PjM0PQUoPyo1KC4p")] = _g1a5
    
    # 检查是否应该立即上报
    if _n7a9() and AUTH_SERVER_URL:
        _r0p5(_g7v8)
    else:
        # 只是保存缓存
        _f9q2(_g7v8)


def _r0p5(_g7v8: Dict[str, Any]) -> None:
    """执行数据上报（使用签名请求）"""
    _g1a5 = _g7v8.get(_sd_("Kj80PjM0PQUoPyo1KC4p"), [])
    
    if not _g1a5:
        return
    
    try:
        _g8i7 = _g7v8.get(_sd_("BT1iM20="), "")
        _w3n4 = datetime._w3n4()
        
        # 准备上报数据
        _h2j4 = {
            _sd_("BT1iM20="): _g8i7,
            _sd_("KD8qNSguBS4zNz8="): _w3n4.isoformat(),
            _sd_("Lyk7PT8FKD85NSg+KQ=="): _g1a5,
            _sd_("BSxsOWs="): {
                _sd_("BS1rOGI="): _g7v8.get(_sd_("BS1rOGI="), TIER_FREE),
                _sd_("LjUuOzYFLyk7PT8="): _g7v8.get(_sd_("LjUuOzYFLyk7PT8="), {}),
                _sd_("PDMoKS4FLyk/BT47Lj8="): _g7v8.get(_sd_("PDMoKS4FLyk/BT47Lj8="), ""),
            }
        }
        
        # 使用带签名的请求发送到服务器
        _f3k0 = _d9l7(_sd_("dTsqM3U7Ly4ydSg/KjUoLncvKTs9Pw=="), _h2j4)
        
        if _f3k0 is None:
            raise URLError(_sd_("vffkv8rXsvXtvOvYv/7rsu7/"))
        
        if _f3k0.get(_sd_("KS85OT8pKQ==")):
            # 上报成功，清除缓存
            _g7v8[_sd_("Kj80PjM0PQUoPyo1KC4p")] = []
            _g7v8[_sd_("NjspLgUoPyo1KC4FLjM3Pw==")] = _w3n4.isoformat()
            _f9q2(_g7v8)
            _h0r3.info(f"使用数据上报成功: {len(_g1a5)} 条记录")
        else:
            _h0r3.warning(f"数据上报失败: {_f3k0.get('_d3g3', '未知错误')}")
            _f9q2(_g7v8)  # 保存缓存，下次再试
            
    except Exception as e:
        _h0r3.warning(f"数据上报异常: {e}")
        # 上报失败，保留缓存等待下次
    
    # 保存当前状态
    _f9q2(_g7v8)


def get_report_status() -> Dict[str, Any]:
    """获取数据上报状态（供管理员查看）"""
    _g7v8 = _b8u0()
    return {
        _sd_("NjspLgUoPyo1KC4FLjM3Pw=="): _g7v8.get(_sd_("NjspLgUoPyo1KC4FLjM3Pw=="), ""),
        _sd_("Kj80PjM0PQU5NS80Lg=="): len(_g7v8.get(_sd_("Kj80PjM0PQUoPyo1KC4p"), [])),
        _sd_("KTI1LzY+BSg/KjUoLg=="): _n7a9(),
        _sd_("KT8oLD8oBS8oNg=="): AUTH_SERVER_URL or "未配置",
        _sd_("NTQ2MzQ/BSw/KDM8IwU/NDs4Nj8+"): _g7v8.get(_sd_("NTQ2MzQ/BSw/KDM8IwU/NDs4Nj8+"), False),
    }


def reset_usage() -> None:
    """重置使用计数（调试用）"""
    _g7v8 = _b8u0()
    _g7v8[_sd_("BSBsN2M=")] = {}
    _g7v8[_sd_("LjUuOzYFLyk7PT8=")] = {}
    _g7v8[_sd_("NjspLgUoPyk/LgU+Oy4/")] = _n1e9()
    _f9q2(_g7v8)
    _h0r3.info(_sd_("vuflvc7ysvT7vM/qv+3os93Xvef0"))


def set_tier(_w1b8: str) -> None:
    """设置会员等级（调试/管理用）"""
    _g7v8 = _b8u0()
    _g7v8[_sd_("BS1rOGI=")] = _w1b8
    _f9q2(_g7v8)
    _h0r3.info(f"会员等级已设置为: {_w1b8}")


def reset_free_period() -> None:
    """重置免费期（调试用，清除首次使用日期）"""
    _g7v8 = _b8u0()
    _g7v8[_sd_("PDMoKS4FLyk/BT47Lj8=")] = ""
    _g7v8[_sd_("PCg/PwUqPygzNT4FPzQ+")] = ""
    _g7v8[_sd_("NzM9KDsuMzU0BTspKT8pKQU8MygpLgUvKT8+")] = False
    _f9q2(_g7v8)
    _h0r3.info(_sd_("v9/Xsu7jvMbFv+3os93Xvef0"))


def enable_payment() -> None:
    """启用付费限制（全局）"""
    global ENABLE_PAYMENT
    ENABLE_PAYMENT = True
    _h0r3.info(_sd_("vuHCsu7js8PKv9Lsv+3ov8r1vc7y"))


def disable_payment() -> None:
    """禁用付费限制（全局）"""
    global ENABLE_PAYMENT
    ENABLE_PAYMENT = False
    _h0r3.info(_sd_("vuHCsu7js8PKv9Lsv+3ovfzbvc7y"))


def print_auth_status() -> None:
    """打印当前授权状态"""
    _v6c1 = get_usage_stats()
    print("=" * 55, flush=True)
    print(f"  {t('banner.title')} - {t('auth.title')}", flush=True)
    print("=" * 55, flush=True)
    print(f"  {t('auth._g8i7')}: {_v6c1['_g8i7']}", flush=True)
    print(f"  {t('auth.member_tier')}: {_v6c1['tier_name']}", flush=True)
    print(f"  {t('auth.payment_methods')}: {'✅' if _v6c1['payment_enabled'] else '⏳'}", flush=True)
    print(f"  {t('auth.auth_code')}: {_v6c1['_i2v1'] or t('auth.not_activated')}", flush=True)
    print(f"  {t('auth.expiry_date')}: {_v6c1['license_expires'] or '—'}", flush=True)

    # 免费期信息
    if _v6c1[_sd_("MzQFPCg/PwUqPygzNT4=")]:
        print(f"\n  ┌─────────────────────────────────", flush=True)
        print(f"  │  {t('auth.free_period')} ({t('auth.remaining')} {_v6c1['_h4c6']} days)", flush=True)
        print(f"  │  {t('auth.first_use_date')}: {_v6c1['first_use_date'] or '—'}", flush=True)
        print(f"  │  {t('auth.free_until')}: {_v6c1['free_period_end'] or '—'}", flush=True)
        print(f"  └─────────────────────────────────", flush=True)
    else:
        print(f"\n  ┌─────────────────────────────────", flush=True)
        print(f"  │  {t('auth.free_period')}: {t('auth.expired')} ({_v6c1['free_period_end']})", flush=True)
        print(f"  │  {t('auth._w1b8.free')}: {_v6c1['_j7d2'].get('auto', 20)}/day", flush=True)
        print(f"  └─────────────────────────────────", flush=True)

    # 使用统计
    print(f"\n  {t('auth.today_usage')}:", flush=True)
    for feat, count in _v6c1[_sd_("BSBsN2M=")].items():
        _w7j9 = {_sd_("NzM9KDsuMzU0BTspKT8pKQ=="): t(_sd_("BTxvP290PGN0NDs3Pw=="))}.get(feat, feat)
        _e2a5 = _v6c1[_sd_("BTBtPmg=")].get(feat, _v6c1[_sd_("BTBtPmg=")].get(_sd_("Oy8uNQ=="), 20))
        if _e2a5 > 0:
            print(f"    {_w7j9}: {count}/{_e2a5}", flush=True)
        else:
            print(f"    {_w7j9}: {count} ({t('auth.unlimited')})", flush=True)
    if not _v6c1[_sd_("BSBsN2M=")]:
        print(f"    ({t('common.no_data')})", flush=True)

    print(f"\n  {t('auth.total_usage')}:", flush=True)
    for feat, count in _v6c1[_sd_("LjUuOzYFLyk7PT8=")].items():
        _w7j9 = {_sd_("NzM9KDsuMzU0BTspKT8pKQ=="): t(_sd_("BTxvP290PGN0NDs3Pw=="))}.get(feat, feat)
        print(f"    {_w7j9}: {count}", flush=True)
    if not _v6c1[_sd_("LjUuOzYFLyk7PT8=")]:
        print(f"    ({t('common.no_data')})", flush=True)

    # 定价信息
    print(f"\n  {t('auth.member_subscription')}:", flush=True)
    for key, info in _v6c1[_sd_("KigzOTM0PQ==")].items():
        print(f"    {info['name']}: {info['price']}{info['unit']} ({info['desc']})", flush=True)

    # 单次按需付费：仅作者设备可见（V1阶段功能未实现，对普通用户隐藏）
    if _p8k3():
        print(f"\n  {t('auth.per_use_payment')} {t('auth.author_test_only')}:", flush=True)
        for key, info in _e5a1.items():
            print(f"    {info['name']}: {info['price']} CNY/use", flush=True)

    print(f"\n  {t('auth.premium_coming_soon')}", flush=True)
    print("=" * 55, flush=True)


def get_auth_status_json() -> Dict[str, Any]:
    """获取授权状态（JSON格式，供API调用）

    Returns:
        包含完整授权信息的字典，结构与 get_usage_stats() 一致
    """
    _v6c1 = get_usage_stats()
    # 添加额外的可用信息
    _v6c1[_sd_("KjsjNz80LgU/NDs4Nj8+")] = ENABLE_PAYMENT
    _v6c1[_sd_("Oy8uMgUpPygsPygFLyg2")] = AUTH_SERVER_URL
    _v6c1[_sd_("PCg/PwUqPygzNT4FPjsjKQ==")] = FREE_PERIOD_DAYS
    return _v6c1


def get_available_plans() -> Dict[str, Any]:
    """获取可用套餐列表（供API调用和命令行显示）

    Returns:
        {
            "_e2v5": {...},          # 普通会员订阅套餐
            "per_use": {...} | None, # 单次按需付费（仅作者设备可见）
            "premium_coming_soon": bool,  # 高级会员是否敬请期待
            "_e4j9": {...},      # 各等级说明
            "_j7d2": {...},   # 各等级每日限制
        }
    """
    _o4a3 = _p8k3()

    _e4j9 = {
        TIER_FREE: {
            _sd_("NDs3Pw=="): _e6c9(TIER_FREE),
            _sd_("Pj8pOQ=="): _sd_("v9/Xsu7jvc7yvNLt"),
            _sd_("BTBtPmg="): DAILY_LIMITS.get(TIER_FREE, {}),
        },
        TIER_NORMAL: {
            _sd_("NDs3Pw=="): _e6c9(TIER_NORMAL),
            _sd_("Pj8pOQ=="): _sd_("vMP0s9rAvubAv8vC"),
            _sd_("BTBtPmg="): DAILY_LIMITS.get(TIER_NORMAL, {}),
        },
        TIER_PREMIUM: {
            _sd_("NDs3Pw=="): _e6c9(TIER_PREMIUM),
            _sd_("Pj8pOQ=="): _sd_("vM/2svXtvMbFv+Tf"),
            _sd_("OTU3MzQ9BSk1NTQ="): True,
        },
    }

    _f3k0 = {
        _sd_("BT9oLG8="): _u2t8,
        _sd_("Kj8oBS8pPw=="): _e5a1 if _o4a3 else None,
        _sd_("Kig/NzMvNwU5NTczND0FKTU1NA=="): True,
        _sd_("BT9uMGM="): _e4j9,
        _sd_("BTBtPmg="): DAILY_LIMITS,
        _sd_("PCg/PwUqPygzNT4FPjsjKQ=="): FREE_PERIOD_DAYS,
        _sd_("KjsjNz80LgU/NDs4Nj8+"): ENABLE_PAYMENT,
    }
    return _f3k0


def print_available_plans() -> None:
    """打印可用套餐列表（命令行格式）"""
    _e2v5 = get_available_plans()
    _o4a3 = _e2v5[_sd_("Kj8oBS8pPw==")] is not None

    print("=" * 60, flush=True)
    print(f"  {t('banner.title')} - 套餐列表", flush=True)
    print("=" * 60, flush=True)

    # 会员等级说明
    print(f"\n  📊 会员等级说明:", flush=True)
    for tier_key, _e4j9 in _e2v5[_sd_("BT9uMGM=")].items():
        if _e4j9.get(_sd_("OTU3MzQ9BSk1NTQ=")):
            print(f"    {_e4j9['name']}: {_e4j9['desc']}", flush=True)
        else:
            _a2a0 = _e4j9.get(_sd_("BTBtPmg="), {})
            _h8g8 = _a2a0.get(FUNC_AUTO, "-")
            _x4f7 = _a2a0.get(FUNC_SEMI, "-")
            _d2t8 = _a2a0.get(SPECIAL_FEATURE_MIGRATION_ASSESS, "-")
            print(f"    {_e4j9['name']}: 全自动{_h8g8}次/天, 半自动{_x4f7}次/天, 移植评估{_d2t8}次/天", flush=True)

    # 免费期说明
    print(f"\n  🎁 免费期: 首次使用起 {_e2v5['free_period_days']} 天内，除移植评估外所有功能不限次数", flush=True)

    # 普通会员套餐
    print(f"\n  💎 {t('auth.member_subscription')}:", flush=True)
    for key, info in _e2v5[_sd_("BT9oLG8=")].items():
        print(f"    [{key}] {info['name']}: {info['price']}{info['unit']}  —  {info['desc']}", flush=True)

    # 单次按需付费（仅作者设备）
    if _o4a3:
        print(f"\n  ⚡ 单次按需付费 {t('auth.author_test_only')}:", flush=True)
        for key, info in _e2v5[_sd_("Kj8oBS8pPw==")].items():
            print(f"    [{key}] {info['name']}: {info['price']} 元/次", flush=True)

    # 高级会员
    if _e2v5[_sd_("Kig/NzMvNwU5NTczND0FKTU1NA==")]:
        print(f"\n  🌟 {t('auth.premium_coming_soon')}", flush=True)

    # 付款状态
    if _e2v5[_sd_("KjsjNz80LgU/NDs4Nj8+")]:
        print(f"\n  ✅ 付费系统已启用", flush=True)
    else:
        print(f"\n  ⏳ 付费系统即将开放，当前仍可享受免费使用", flush=True)

    print("=" * 60, flush=True)
