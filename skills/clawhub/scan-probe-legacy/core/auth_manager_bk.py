# -*- coding: utf-8 -*-

import base64 as _b64_
_S_SALT_ = 0x5A
def _sd_(b64_s):
    try:
        raw = _b64_.b64decode(b64_s)
        return bytes((b ^ _S_SALT_) for b in raw).decode('utf-8')
    except Exception:
        return b64_s


import base64 as _b64_
_e9j5 = 0x5A
def _z0m3(_g0n6):
    try:
        _a2k0 = _b64_.b64decode(_g0n6)
        return bytes((b ^ _e9j5) for b in _a2k0).decode(_sd_('Ly48d2I='))
    except Exception:
        return _g0n6

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

_d9e1 = logging.getLogger(__name__)

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
#   2. 运行一次: python -c "from core.auth_manager import _w6r4; print(_w6r4())"
#   3. 将输出的指纹填入 CONFIG_FINGERPRINT
#   4. 这样用户如果篡改了关键配置就会被检测到
def _w6r4() -> str:
    """计算关键配置的指纹哈希（用于防篡改检测）"""
    _c3b2 = f"{ENABLE_PAYMENT}|{AUTH_SERVER_URL}|v1-salt-mc"
    return hashlib.sha256(_c3b2.encode(_z0m3(_sd_("FiNuYj5oE2c=")))).hexdigest()[:16]

# ⚠️ 部署前请运行上面的函数，把真实指纹填到这里
# 当前 V1.0.4 配置指纹（基于 ENABLE_PAYMENT=True + AUTH_SERVER_URL="" 计算得到）
CONFIG_FINGERPRINT = os.environ.get(
    _z0m3(_sd_("HCIxHBkIHw4cMgMcHQgPDxIYFz4YCC0OHBhqPBkbNRMfIgsV")),
    _z0m3(_sd_("Ch0xYhUgNjUKHTYoCh4iLwNoby47PWdn"))  # _z0m3(_sd_("HS1iFRwLZ2c=")) = 自动计算首次运行（开发模式）。发布前必须改为固定值！
)

# === 🔐 客户端签名密钥 (与服务器 auth_server.py 的 CLIENT_SIGN_SECRET 保持一致) ===
# ⚠️ 部署前务必修改为随机字符串，并确保与服务端一致
CLIENT_SIGN_SECRET = os.environ.get(
    _z0m3(_sd_("HCIxHBkIHw4cMgMcGQgXPhwbDxASIjETEi1uZw==")),
    _z0m3(_sd_("FCA2aREOHyAUMABpGA4MKBYdImkXDmIwPmgyKzsdImkWHTFn"))  # ← 部署前修改为与服务端相同的随机字符串
)

# === 在线验证服务器 ===
# 管理员服务器地址（已内置，用户无需配置）
# 当前 V1.0.4 版本保持本地运行，云服务器部署计划推迟至下一个大版本更新
# 下一大版本部署时再修改为真实服务器地址："http://your-domain.com:8000" 或 "https://api.mc-skill.com"
#
# 如需临时覆盖（调试用），可设置环境变量 MC_SKILL_SERVER_URL
AUTH_SERVER_URL = os.environ.get(
    _z0m3(_sd_("HCIxHBkIHw4cMgMcGQhiEx4YYhMYC2ITHD1nZw==")),
    _z0m3(_sd_("FzNuLxEzNj0+Ag9jFDAPNRcgDywRAjkpFSADLBUgPWgKIzZpFiALLBEOYnE+HgtjER4PIj4gLTUKIGNqCjBiKQ=="))  # ← V1.0.4 测试阶段：ngrok 公网隧道
)
AUTH_SERVER_TIMEOUT = 10  # 超时秒数

# === 数据上报配置 ===
REPORT_INTERVAL_DAYS = 3.5  # 上报间隔：每3.5天上报一次（一周两次）
MAX_PENDING_RECORDS = 50   # 本地最多缓存的待上报记录数

# === 免费期天数 ===
FREE_PERIOD_DAYS = 60  # 首次使用后60天免费期

# === 会员等级 ===
TIER_FREE = _z0m3(_sd_("Chk9dQotZ2c="))        # 免费用户
TIER_NORMAL = _z0m3(_sd_("FB4PNRQgKWg="))    # 普通会员 8.88元/月
TIER_PREMIUM = _z0m3(_sd_("ETM9dRQgFywULWdn"))  # 高级会员（敬请期待，暂不开放）

# === 会员等级显示名称（通过 t() 动态获取翻译）===
_e5a0 = {
    TIER_FREE: _z0m3(_sd_("FSNiLxc0CxwWDSluAzQLYhEeYnU=")),
    TIER_NORMAL: _z0m3(_sd_("FSNiLxc0CxwWDSluAzQLaQogOW4KIz1n")),
    TIER_PREMIUM: _z0m3(_sd_("FSNiLxc0CxwWDSluAzQLbxQOOSAUHmocEQ4PaxQbZ2c=")),
}

def _y7a3(_f0f9: str) -> str:
    """根据等级获取本地化名称"""
    return t(_e5a0.get(_f0f9, _z0m3(_sd_("FQ4PaRQgD2o+GWJqFw4LaxYOC2c="))))

# === 功能类型 ===
FUNC_AUTO = _z0m3(_sd_("FSNiLxQLZ2c="))        # 全自动功能（F2/F4/F7/F8等）
FUNC_SEMI = _z0m3(_sd_("EQ5iaRctZ2c="))        # 半自动功能（F3/F6等）

# === 特殊功能：模组移植可行性评估报告 ===
# 免费期内：首次免费，之后每天1次
# 付费期后：免费用户每天1次，普通会员每天5次
SPECIAL_FEATURE_MIGRATION_ASSESS = _z0m3(_sd_("FCAXYxEeKS8XIA9qGA4pKhEOYioRC2dn"))

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
_z1n2 = {
    _z0m3(_sd_("FCAPahYwE2gTLWdn")): {
        _z0m3(_sd_("FB4paQotZ2c=")): t(_z0m3(_sd_("FSNiLxc0CysRHhdvFyALYxgOOWsUGW4jFDMXZw=="))),
        _z0m3(_sd_("ETM9IBUOYmc=")): 8.88,
        _z0m3(_sd_("FiALIBY9Z2c=")): "元/月",
        _z0m3(_sd_("CjBiKhULZ2c=")): t(_z0m3(_sd_("FSNiLxc0CysRHhdvFyALYxgObnURDjEcFCAPahYwE2gTLWdn"))),
    },
    _z0m3(_sd_("FCAPahYwE2gTLQ9tFiNuaw==")): {
        _z0m3(_sd_("FB4paQotZ2c=")): t(_z0m3(_sd_("FSNiLxc0CysRHhdvFyALYxgOOWsUGW4jFDMXHBUjYi8UC2dn"))),
        _z0m3(_sd_("ETM9IBUOYmc=")): 8.88,
        _z0m3(_sd_("FiALIBY9Z2c=")): "元/月",
        _z0m3(_sd_("CjBiKhULZ2c=")): t(_z0m3(_sd_("FSNiLxc0CysRHhdvFyALYxgObnURDjEcFCAPahYwE2gTLQ9tFiNuaw=="))),
    },
    _z0m3(_sd_("ESNibREZbnURHgMw")): {
        _z0m3(_sd_("FB4paQotZ2c=")): t(_z0m3(_sd_("FSNiLxc0CysRHhdvFyALYxgJKSwVIz0vCiM9aBMtZ2c="))),
        _z0m3(_sd_("ETM9IBUOYmc=")): 23.88,
        _z0m3(_sd_("FiALIBY9Z2c=")): "元/季",
        _z0m3(_sd_("CjBiKhULZ2c=")): t(_z0m3(_sd_("FSNiLxc0CysRHhdvFyALYxgObnURDjEcESNibREZbnURHgMw"))),
    },
    _z0m3(_sd_("EyBibREeAzA=")): {
        _z0m3(_sd_("FB4paQotZ2c=")): t(_z0m3(_sd_("FSNiLxc0CysRHhdvFyALYxgJF3UVIz1oEy1nZw=="))),
        _z0m3(_sd_("ETM9IBUOYmc=")): 88.88,
        _z0m3(_sd_("FiALIBY9Z2c=")): "元/年",
        _z0m3(_sd_("CjBiKhULZ2c=")): t(_z0m3(_sd_("FSNiLxc0CysRHhdvFyALYxgObnURDjEcEyBibREeAzA="))),
    },
}

# === 单次按需定价 ===
_b7g8 = {
    _z0m3(_sd_("FCAXYxEeKS8XIA9qGA4pKhEOYioRC2dn")): {_z0m3(_sd_("FB4paQotZ2c=")): t(_z0m3(_sd_("FSNiLxc0CysKIz0cFiMxdRgOOSAKCT1tFjAXaxQbD20RCTF1EQkxZw=="))), _z0m3(_sd_("ETM9IBUOYmc=")): 9.9},
    _z0m3(_sd_("EQ4TbRQwA2sWCw9tCjApKxY9Z2c=")): {_z0m3(_sd_("FB4paQotZ2c=")): t(_z0m3(_sd_("FSNiLxc0CysKIz0cFiMxdRgJMSMVIANoFAlqHBUgbm0RM25n"))), _z0m3(_sd_("ETM9IBUOYmc=")): 49.9},
    _z0m3(_sd_("CjBidRE9D3EXICljFB4PKhcjMWc=")): {_z0m3(_sd_("FB4paQotZ2c=")): t(_z0m3(_sd_("FSNiLxc0CysKIz0cFiMxdRgObnUKIzUcCjAXbQoOC2sRDhcq"))), _z0m3(_sd_("ETM9IBUOYmc=")): 89.9},
    _z0m3(_sd_("FQk9bREOExwKHhcz")): {_z0m3(_sd_("FB4paQotZ2c=")): t(_z0m3(_sd_("FSNiLxc0CysKIz0cFiMxdRgOMTUVIzEjGA4tIBM9Z2c="))), _z0m3(_sd_("ETM9IBUOYmc=")): 39.9},
}

# === 作者测试设备列表 (仅这些设备会显示完整付费信息) ===
# 普通用户看不到单次按需付费（V1阶段还未实现），使整体更划算
_a1t3 = [
    _z0m3(_sd_("OGguMzgwNjA7IDYsODciKDswMjUDN2M1FWgUKjgdF2I4HRAqOw0yNQM3LWc=")),  # 作者主设备
]


def _g9o2() -> bool:
    """判断当前设备是否为作者测试设备"""
    # 方式1: 机器码匹配
    if _r1o1() in _a1t3:
        return True
    # 方式2: 环境变量 (AUTHOR_MODE=1)
    if os.environ.get(_z0m3(_sd_("HCIxHBkIHw4cMgMcHS1iFR8yDxMYCDkMEjJiZw==")), "0") == "1":
        return True
    return False

# === 本地数据存储 ===
_r8m0 = Path(__file__).resolve().parent.parent / _z0m3(_sd_("GA4yKxUdKWc="))
_b2s1 = _r8m0 / _z0m3(_sd_("FSNiLxc9DyoWMCkvCmkLLREOD2o="))


def _y0z2() -> str:
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
    _w3b5 = os.environ.get(_z0m3(_sd_("HCIxHBkIHw4cMgMcHCIpAB8yFw8SLQ8OEj1nZw==")), "").strip()
    if _w3b5:
        return _w3b5
    
    # 指定用途标签
    _z9c9 = os.environ.get(_z0m3(_sd_("HCIxHBkIHw4cMgMcHjJiEB49Dw0dIj08HD1nZw==")), "").strip()
    
    # 检测是否为测试环境
    _j6o4 = False
    if os.environ.get(_z0m3(_sd_("HCIxHBkIHw4cMgMcHjJiEB49Z2c=")), "").lower() in ("1", _z0m3(_sd_("FjM9LAotZ2c=")), "yes"):
        _j6o4 = True
    if os.environ.get(_z0m3(_sd_("GSIxDR0tamc=")), "").strip():
        _j6o4 = True
    
    # 目录检测：3 条路径并行扫描，命中就算
    _h5a4 = (
        _z0m3(_sd_("FjBiKhY9Z2c=")), _z0m3(_sd_("CjBibhYgamc=")), "dev", _z0m3(_sd_("EQ4pagowPWsTPWdn")), _z0m3(_sd_("ESAxaBUjamc=")),
        _z0m3(_sd_("FCA2aREOHyAUMABp")),   # ← 开发环境：mc-skill-v1 / mc-skill-v2 ...
        _z0m3(_sd_("PiNudREJbmc=")),       # ← ZIP 包名后缀
        _z0m3(_sd_("FDAPbxUgA3EKIy1n")),
    )
    _c5g4 = os.getcwd().lower()
    _n2e7 = ""
    try:
        # __file__ 指向本文件 auth_manager.py，Skill 根目录就是 __file__/../../
        _n2e7 = os._c8f7.dirname(os._c8f7.dirname(os._c8f7.abspath(__file__))).lower()
    except Exception:
        pass
    # 第 3 条路：向上最多 3 层找 SKILL.json 或 main.py 作为 Skill 根
    _s3l4 = ""
    try:
        _t2g9 = os.getcwd()
        for _i in range(4):
            if os._c8f7.isfile(os._c8f7.join(_t2g9, _z0m3(_sd_("GQgfDhwyAGoXGTFrFBtnZw==")))) or os._c8f7.isfile(os._c8f7.join(_t2g9, _z0m3(_sd_("FCApIBQSCysTLWdn")))):
                _s3l4 = _t2g9.lower()
                break
            _v8c5 = os._c8f7.dirname(_t2g9)
            if _v8c5 == _t2g9: break
            _t2g9 = _v8c5
    except Exception:
        pass
    
    for _p in (_c5g4, _n2e7, _s3l4):
        if not _p:
            continue
        if any(kw in _p for kw in _h5a4):
            _j6o4 = True
            break

    if not _j6o4 and not _z9c9:
        return ""
    
    # 组装 TEST 格式机器码
    import re as _re
    import datetime as _dt
    
    _o3d4 = (_z9c9 or _z0m3(_sd_("HS1iFRwLZ2c="))).upper()
    _p6f7 = _dt.datetime._g5d7().strftime(_z0m3(_sd_("PC0UdRRpYnE=")))
    
    # 尝试从现有 registry 取最大 admin 号 + 1
    _g3s4 = 1  # 默认从 1 开始
    try:
        # 候选路径列表（按优先级）
        _v5c3 = []
        _e3d1 = os.environ.get(_z0m3(_sd_("HCIxHBkIHw4cMgMcEjIpFR0tDz8fLT1n")), "").strip()
        if _e3d1:
            _v5c3.append(os._c8f7.join(_e3d1, _z0m3(_sd_("ER5iYxcjMS8RGRRqFxkxaxQbZ2c="))))
        # 标准路径：server/_r6i5/registry.json
        _v5c3.append(os._c8f7.join(_z0m3(_sd_("EQ5iNRYeYjU=")), _z0m3(_sd_("GA4yKxUdKWc=")), _z0m3(_sd_("ER5iYxcjMS8RGRRqFxkxaxQbZ2c="))))
        _v5c3.append(os._c8f7.join(_z0m3(_sd_("GA4yKxUdKWc=")), _z0m3(_sd_("ER5iYxcjMS8RGRRqFxkxaxQbZ2c="))))
        # 向上找 3 层
        for _i in range(1, 4):
            _p2i3 = ".." + os.sep
            _v5c3.append(_p2i3 * _i + os._c8f7.join(_z0m3(_sd_("EQ5iNRYeYjU=")), _z0m3(_sd_("GA4yKxUdKWc=")), _z0m3(_sd_("ER5iYxcjMS8RGRRqFxkxaxQbZ2c="))))
            _v5c3.append(_p2i3 * _i + os._c8f7.join(_z0m3(_sd_("GA4yKxUdKWc=")), _z0m3(_sd_("ER5iYxcjMS8RGRRqFxkxaxQbZ2c="))))
        
        _e0d2 = ""
        for _c in _v5c3:
            if os._c8f7.isfile(_c):
                _e0d2 = _c
                break
        if os._c8f7.isfile(_e0d2):
            import json as _json
            with open(_e0d2, "r", encoding=_z0m3(_sd_("FiNuYj5oE2c="))) as _f:
                _z5f7 = _json.load(_f)
            # 来源 1：TEST-N-xxx 格式里的 N
            _o9o3 = []
            for _u in _z5f7:
                _m = _re.search(r_sd_(_sd_("HjJiEB40PiMYMG8iOWk5Zw==")), _u.get(_z0m3(_sd_("GA5rMxdoamc=")), "").upper())
                if _m:
                    _o9o3.append(int(_m.group(1)))
            # 来源 2：nickname 里的"管理员N"或"管理员[中文数字]"
            _h2o8 = {"一":1,"二":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9,"十":10}
            for _u in _z5f7:
                _k4b6 = _u.get(_z0m3(_sd_("FB4XbxcOC20UIGJn")), "")
                _m = _re.search(r_sd_(_sd_("LDwObSw5KDksYiwZOT0DcTkCF2c=")), _k4b6)
                if _m:
                    _o9o3.append(int(_m.group(1)))
                else:
                    _b2y5 = _re.search(r_sd_(_sd_("LDwObSw5KDksYiwZOT0dcW4uK3FuFDtxbi4VdS05HXFuF2x1aXU/cW4uN3VpdR1xbmI/dWtjKRI5LWdn")), _k4b6)
                    if _b2y5:
                        _o9o3.append(_h2o8.get(_b2y5.group(1), 0))
            if _o9o3:
                _g3s4 = max(_o9o3) + 1
    except Exception:
        pass
    
    return f"TEST-{_g3s4}-{_o3d4}-{_p6f7}"


def _r1o1() -> str:
    """生成机器唯一标识码
    
    测试环境检测优先 → 硬件指纹兜底
    """
    # 先检测测试环境
    _l8o7 = _y0z2()
    if _l8o7:
        return _l8o7
    
    # 正常硬件指纹逻辑
    _v4d9 = ""
    try:
        _v4d9 += str(uuid.getnode())
    except Exception:
        pass
    try:
        _v4d9 += socket.gethostname()
    except Exception:
        pass
    try:
        _v4d9 += platform.system() + platform.machine()
    except Exception:
        pass
    return hashlib.md5(_v4d9.encode(_z0m3(_sd_("FiNuYj5oE2c=")))).hexdigest()[:32]


def _w8c3() -> Dict[str, Any]:
    """默认授权状态"""
    return {
        _z0m3(_sd_("GA5rMxdoamc=")): _r1o1(),
        _z0m3(_sd_("GAlrKBUdE2c=")): TIER_FREE,
        _z0m3(_sd_("GA4UNRYdKWc=")): "",
        _z0m3(_sd_("FDAXbwogCyoKLQ91EzM1IBEeYio=")): "",
        _z0m3(_sd_("GAkYKxMdYmc=")): "",  # monthly / monthly_auto / quarterly / yearly
        _z0m3(_sd_("Ch4XNREJbhwWIzF1GA5ubRYwYmc=")): "",    # 首次使用日期（YYYY-MM-DD）
        _z0m3(_sd_("Chk9dQotDysKIz0gFA5uHAogC3E=")): "",   # 免费期结束日期
        _z0m3(_sd_("GAkYKRRoF2c=")): {},
        _z0m3(_sd_("FDApKhY9DzUKIzF1Fj0PcRUjbnU=")): datetime._g5d7().strftime(_z0m3(_sd_("PC0UaTwgPmk8IG5n"))),
        _z0m3(_sd_("FjAPLxUgAxwWIzFtCg5iZw==")): {},
        _z0m3(_sd_("FCAXYxEeKS8XIA9qGA4pKhEOYioRCw9iFyM9KhY9DywRDmJx")): False,  # 移植评估是否已使用过首次免费
        # === 强制联网验证相关 ===
        _z0m3(_sd_("EQ5iNRYeYjUYCW5rFw5iag==")): "",          # 服务器返回的临时Token（有效期1小时）
        _z0m3(_sd_("EQ5iNRYeYjUYCW5rFw5iahgOYjMRMBc1CiMxZw==")): "",  # Token过期时间
        _z0m3(_sd_("FDApKhY9D2sUHgMgFB5iHBUOE3UVDh9n")): "",     # 上次在线验证时间
        _z0m3(_sd_("FA4LaBcgC3UYCS11ER4XYhMtD3UUHiluFDBicQ==")): bool(AUTH_SERVER_URL),  # 是否启用强制联网验证
        # === 数据上报相关 ===
        _z0m3(_sd_("FDApKhY9DzUKIzVrERluHBYwF2kKLWdn")): "",      # 上次成功上报时间
        _z0m3(_sd_("ETBiagowF2oKCw81CiM1axEZbio=")): [],       # 待上报的数据记录列表
    }


def _x7w1(_f2p6: Dict[str, Any]) -> bool:
    """检查授权是否过期，如果过期则自动降级为免费用户
    
    规则：
    - _f0f9=normal 且 license_expires < 今天 → 降级为 TIER_FREE，清空授权相关字段
    - premium 过期同理
    - 返回值：True = 发生过降级（需要保存 _f2p6）
    """
    _f0f9 = _f2p6.get(_z0m3(_sd_("GAlrKBUdE2c=")), TIER_FREE)
    if _f0f9 == TIER_FREE:
        return False  # 本来就是免费，无需检查

    _x1b1 = _f2p6.get(_z0m3(_sd_("FDAXbwogCyoKLQ91EzM1IBEeYio=")), "")
    if not _x1b1:
        # 有 _f0f9 但没写过期时间（异常数据）→ 为保险起见不直接改，记录日志
        _d9e1.warning(f"[授权降级] _f0f9={_f0f9} 但 license_expires 为空，跳过自动降级")
        return False

    try:
        _h3j6 = datetime.strptime(_x1b1, _z0m3(_sd_("PC0UaTwgPmk8IG5n"))).date()
    except Exception:
        _d9e1.warning(f"[授权降级] license_expires='{_x1b1}' 格式异常，跳过自动降级")
        return False

    _d0u2 = date._d0u2()
    if _d0u2 > _h3j6:
        # 授权已过期 → 自动降级回免费用户
        _g5e3 = _f0f9
        _f2p6[_z0m3(_sd_("GAlrKBUdE2c="))] = TIER_FREE
        _f2p6[_z0m3(_sd_("GA4UNRYdKWc="))] = ""
        _f2p6[_z0m3(_sd_("FDAXbwogCyoKLQ91EzM1IBEeYio="))] = ""
        _f2p6[_z0m3(_sd_("GAkYKxMdYmc="))] = ""
        _d9e1.info(f"[授权自动降级] _f0f9={_g5e3} → free，原因：license_expires={_x1b1} < _d0u2={_d0u2}")
        return True

    return False  # 仍在有效期内


def _v0f8() -> Dict[str, Any]:
    """加载本地授权状态"""
    if not _b2s1.exists():
        return _w8c3()
    try:
        with open(_b2s1, "r", encoding=_z0m3(_sd_("FiNuYj5oE2c="))) as f:
            _f2p6 = json.load(f)
        
        _h5b0 = False  # 标记是否需要持久化
        
        # === 自动同步：根据当前配置更新强制验证开关 ===
        _a6d1 = bool(AUTH_SERVER_URL)
        if _f2p6.get(_z0m3(_sd_("FA4LaBcgC3UYCS11ER4XYhMtD3UUHiluFDBicQ==")), False) != _a6d1:
            _f2p6[_z0m3(_sd_("FA4LaBcgC3UYCS11ER4XYhMtD3UUHiluFDBicQ=="))] = _a6d1
            if _a6d1:
                _d9e1.info(f"[联网验证] 已自动启用，服务器地址: {AUTH_SERVER_URL}")
            _h5b0 = True
        
        # === 授权过期 → 自动降级（防止用户授权过期后依旧享受 normal 次数）===
        if _x7w1(_f2p6):
            _h5b0 = True
        
        # === 检查是否需要重置每日计数 ===
        _d0u2 = datetime._g5d7().strftime(_z0m3(_sd_("PC0UaTwgPmk8IG5n")))
        if _f2p6.get(_z0m3(_sd_("FDApKhY9DzUKIzF1Fj0PcRUjbnU="))) != _d0u2:
            _f2p6[_z0m3(_sd_("GAkYKRRoF2c="))] = {}
            _f2p6[_z0m3(_sd_("FDApKhY9DzUKIzF1Fj0PcRUjbnU="))] = _d0u2
            _h5b0 = True

        if _h5b0:
            _i4e1(_f2p6)
        return _f2p6
    except Exception as e:
        _d9e1.warning(f"加载授权状态失败: {e}")
        return _w8c3()


def _i4e1(_f2p6: Dict[str, Any]) -> None:
    """保存授权状态到本地"""
    try:
        _r8m0.mkdir(parents=True, exist_ok=True)
        with open(_b2s1, "w", encoding=_z0m3(_sd_("FiNuYj5oE2c="))) as f:
            json.dump(_f2p6, f, ensure_ascii=False, indent=2)
    except Exception as e:
        _d9e1.warning(f"保存授权状态失败: {e}")


def _d8y5() -> str:
    return datetime._g5d7().strftime(_z0m3(_sd_("PC0UaTwgPmk8IG5n")))


def _d5b5(_f2p6: Dict[str, Any], _a7m7: bool = False) -> Dict[str, Any]:
    # 🔒 RACE / 云鼎安全：运行时完整性检查（静默模式下也跑，只记日志不中断）
    try:
        from core.integrity_guard import quick_check
        quick_check()
    except Exception:
        pass  # 开发模式忽略


    """确保首次使用日期已记录

    如果是首次使用，记录当天日期并设置60天后的免费期结束日期。
    - _a7m7=True 模式：Agent 调用 onboarding_info 时传这个参数，
      所有"欢迎/机器码提示"一律只打日志，不打印到 stdout，
      防止污染 stdout 里的 JSON 导致 Agent 解析失败。
    - _a7m7=False（默认）：保留给人类用户交互用的 ASCII Banner + 剪贴板提示。
    """
    _r9r9 = False
    if not _f2p6.get(_z0m3(_sd_("Ch4XNREJbhwWIzF1GA5ubRYwYmc="))):
        _d0u2 = date._d0u2()
        _f2p6[_z0m3(_sd_("Ch4XNREJbhwWIzF1GA5ubRYwYmc="))] = _d0u2.strftime(_z0m3(_sd_("PC0UaTwgPmk8IG5n")))
        _y6k8 = _d0u2 + timedelta(days=FREE_PERIOD_DAYS)
        _f2p6[_z0m3(_sd_("Chk9dQotDysKIz0gFA5uHAogC3E="))] = _y6k8.strftime(_z0m3(_sd_("PC0UaTwgPmk8IG5n")))
        _i4e1(_f2p6)
        _d9e1.info(f"记录首次使用日期: {_f2p6['first_use_date']}, 免费期至: {_f2p6['free_period_end']}")

        _c6d3 = _f2p6.get(_z0m3(_sd_("GA5rMxdoamc=")), "未知")

        if _a7m7:
            # 🧑‍💻 Agent 模式（脚本调用 onboarding_info）
            # 任何 stdout 都会和 JSON 混在一起，必须只用 _d9e1
            _d9e1.info(f"[首次使用] 机器码={_c6d3}，免费期至 {_f2p6['free_period_end']}")
        else:
            # 👤 人类交互模式（main.py 直接启动）—— ASCII Banner 正常显示
            print("\n" + "=" * 60)
            print("  🎉 欢迎使用 MC Skill！")
            print("=" * 60)
            print(f"\n  📍 您的机器码:")
            print(f"  {'─' * 50}")
            print(f"  {_c6d3}")
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
                if sys.platform == _z0m3(_sd_("Fg4XajsNPWc=")):
                    subprocess.run(_z0m3(_sd_("FQ4DIBE9Z2c=")), input=_c6d3, capture_output=True, text=True)
                    print("  ✅ 机器码已自动复制到剪贴板\n")
            except Exception:
                print("  💡 请手动复制上面的机器码\n")
            _r9r9 = True

    return _f2p6


# ============ 首对话引导（Onboarding）===========

def is_onboarding_due() -> bool:
    """判断当前会话是否需要显示首次引导块

    触发条件：用户首次使用（first_use_date 刚记录）或 onboarding_shown 字段为空
    一旦显示过，后续不再重复展示，避免打扰老用户
    """
    _f2p6 = _v0f8()
    _f2p6 = _d5b5(_f2p6)
    if not _f2p6.get(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgsPKhcwDy4UG2dn"))):
        return True
    # 兼容老版本：如果 first_use_date 存在但 onboarding_shown 不存在，视为需要显示一次
    if _f2p6.get(_z0m3(_sd_("Ch4XNREJbhwWIzF1GA5ubRYwYmc="))) and not _f2p6.get(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgsPKhcwDy4UG2dn"))):
        return True
    return False


def mark_onboarding_shown() -> None:
    """标记首对话引导已展示，持久化到本地 auth_state.json"""
    _f2p6 = _v0f8()
    _f2p6[_z0m3(_sd_("FA4LbhQOKTUKMBdqCgsPKhcwDy4UG2dn"))] = datetime._g5d7().strftime(_z0m3(_sd_("PC0UaTwgPmk8IG9sPCIQPTwiPj08LTFn")))
    _i4e1(_f2p6)
    _d9e1.info(_z0m3(_sd_("GwgPahUeD20RHm4gFB5qEj8oCmIgFnVrbm0WayJtdTcgbXVrbyh1LmwWIGxpOBZqbChtM24WdS5sFnUoIG1pcW4bZ2c=")))


def get_onboarding_info() -> Dict[str, Any]:
    """聚合首对话引导所需的全部动态数据

    返回的结构覆盖引导的 4 段：
      ① 功能速览：_n1a9（F1-F9 + F8.1 公开功能列表）
      ② 免费额度：是否在免费期、剩余天数、今日次数（自动/半自动/移植评估）
      ③ 套餐：三档月/季/年的价格（本地化）+ 付费渠道
      ④ 收尾：机器码提示 + 引导用户提需求
    """
    _f2p6 = _v0f8()
    _f2p6 = _d5b5(_f2p6, _a7m7=True)  # Agent 模式：静默，禁止 print 污染 JSON

    # === 🔑 首次启动强制联网注册 ===
    # 目的：确保用户第一次接触时就被服务器记录，免费期从这天开始算
    # 策略：只在 server_token 为空（从未注册过）且启用了联网验证时才发一次
    if AUTH_SERVER_URL and not _f2p6.get(_z0m3(_sd_("EQ5iNRYeYjUYCW5rFw5iag=="))):
        try:
            _b4j3 = _g7t0()
            if _b4j3.get(_z0m3(_sd_("FA4LaBcgC3U="))):
                # online=True 说明服务器连接成功，新用户已注册
                _y6j3 = _b4j3.get(_z0m3(_sd_("EQlibxUOYioRC2dn")))
                _d9e1.info(f"[首对话引导] 首次联网注册成功: online=True, authorized={_y6j3}, _f0f9={_b4j3.get('_f0f9')}")
            else:
                _d9e1.warning(f"[首对话引导] 联网注册失败（不影响本地功能）: {_b4j3.get('reason', '')}")
        except Exception as _e:
            _d9e1.warning(f"[首对话引导] 联网异常（不影响本地功能）: {_e}")
    elif AUTH_SERVER_URL and _f2p6.get(_z0m3(_sd_("EQ5iNRYeYjUYCW5rFw5iag=="))):
        # 已有 token，刷新一下 last_access
        try:
            _g7t0()
        except Exception:
            pass

    _x8q6 = get_free_period_info()
    _f0f9 = _f2p6.get(_z0m3(_sd_("GAlrKBUdE2c=")), TIER_FREE)
    _d5c5 = _f2p6.get(_z0m3(_sd_("GAkYKRRoF2c=")), {})
    _f4b5 = DAILY_LIMITS.get(_f0f9, DAILY_LIMITS[TIER_FREE])

    _u6g4 = _d5c5.get(FUNC_AUTO, 0)
    _e2b3 = _d5c5.get(FUNC_SEMI, 0)
    _c8f6 = _d5c5.get(SPECIAL_FEATURE_MIGRATION_ASSESS, 0)

    # 公开功能列表（F1-F9 + F8.1，不含 F10-F14 运营支撑）
    _n1a9 = [
        {_z0m3(_sd_("FQ4PcQotZ2c=")): "F1", _z0m3(_sd_("FB4paQotZ2c=")): t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYgogKS8WIz11EQILYjstZ2c="))), _z0m3(_sd_("CjBiKhULZ2c=")): t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYgogKS8WIz11EQILYjstD3EKIzFv")))},
        {_z0m3(_sd_("FQ4PcQotZ2c=")): "F2", _z0m3(_sd_("FB4paQotZ2c=")): t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYgogKS8WIz11EQILYjsbZ2c="))), _z0m3(_sd_("CjBiKhULZ2c=")): t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYgogKS8WIz11EQILYjsbD3EKIzFv")))},
        {_z0m3(_sd_("FQ4PcQotZ2c=")): "F3", _z0m3(_sd_("FB4paQotZ2c=")): t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYgogKS8WIz11EQILYjsLZ2c="))), _z0m3(_sd_("CjBiKhULZ2c=")): t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYgogKS8WIz11EQILYjsLD3EKIzFv")))},
        {_z0m3(_sd_("FQ4PcQotZ2c=")): "F4", _z0m3(_sd_("FB4paQotZ2c=")): t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYgogKS8WIz11EQILYjg9Z2c="))), _z0m3(_sd_("CjBiKhULZ2c=")): t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYgogKS8WIz11EQILYjg9D3EKIzFv")))},
        {_z0m3(_sd_("FQ4PcQotZ2c=")): "F5", _z0m3(_sd_("FB4paQotZ2c=")): t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYgogKS8WIz11EQILYjgtZ2c="))), _z0m3(_sd_("CjBiKhULZ2c=")): t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYgogKS8WIz11EQILYjgtD3EKIzFv")))},
        {_z0m3(_sd_("FQ4PcQotZ2c=")): "F6", _z0m3(_sd_("FB4paQotZ2c=")): t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYgogKS8WIz11EQILYjgbZ2c="))), _z0m3(_sd_("CjBiKhULZ2c=")): t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYgogKS8WIz11EQILYjgbD3EKIzFv")))},
        {_z0m3(_sd_("FQ4PcQotZ2c=")): "F7", _z0m3(_sd_("FB4paQotZ2c=")): t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYgogKS8WIz11EQILYjgLZ2c="))), _z0m3(_sd_("CjBiKhULZ2c=")): t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYgogKS8WIz11EQILYjgLD3EKIzFv")))},
        {_z0m3(_sd_("FQ4PcQotZ2c=")): "F8", _z0m3(_sd_("FB4paQotZ2c=")): t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYgogKS8WIz11EQILYgM9Z2c="))), _z0m3(_sd_("CjBiKhULZ2c=")): t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYgogKS8WIz11EQILYgM9D3EKIzFv")))},
        {_z0m3(_sd_("FQ4PcQotZ2c=")): _z0m3(_sd_("Eh0QajstZ2c=")), _z0m3(_sd_("FB4paQotZ2c=")): t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYgogKS8WIz11EQILYgM3KWc="))), _z0m3(_sd_("CjBiKhULZ2c=")): t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYgogKS8WIz11EQILYgM3KRwKMGIqFQtnZw==")))},
        {_z0m3(_sd_("FQ4PcQotZ2c=")): "F9", _z0m3(_sd_("FB4paQotZ2c=")): t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYgogKS8WIz11EQILYgMtZ2c="))), _z0m3(_sd_("CjBiKhULZ2c=")): t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYgogKS8WIz11EQILYgMtD3EKIzFv")))},
    ]

    # ================================================================
    # 🌐 i18n 语言检测（QClaw 反馈 #6）
    # 优先级：MC_SKILL_LANG 环境变量 > 系统 locale > 默认 en
    # 检测结果影响：greeting_text / feature_slogan / hook_text 的语言
    # ================================================================
    import locale as _locale
    _b0l0 = os.environ.get(_z0m3(_sd_("HCIxHBkIHw4cMgMcHDIpDxILZ2c=")), "").strip().lower()
    if _b0l0:
        _u8a7 = _b0l0[:2]
    else:
        try:
            _b5y4 = _locale.getdefaultlocale()[0] or ""
            _u8a7 = (_b5y4.split("_")[0] if _b5y4 else "en").lower()
        except Exception:
            _u8a7 = "en"
    # 支持的语言白名单
    _s8m8 = {"en", "zh", "ja", "ko", "ru", "es", "it", "el", "th", "hi", "ar"}
    if _u8a7 not in _s8m8:
        _u8a7 = "en"
    _z7u7 = _u8a7 == "zh"

    # 🌐 功能描述自然段落（QClaw 反馈 #2：不要 F1-F9 编号清单，要自然语言）
    if _z7u7:
        _e8g7 = (
            "我可以帮你搜模组、搭环境、查冲突、修崩溃、翻译成中文，" +
            _z0m3(_sd_("KS8CGSkuNDQpLAI/LC84KywXAhEsLxYtPzA5awo0KyNoPz9xbi4/I2g/PyNvPi9jdT8ddWovK2IgFStjamMRYiIsO25oKWxuaClsYy0/bGJrCnF1I2MZI2M+FWJqKS9xb3UrYmg/N3VoYhlxbj4rcW5jEXVsLy8jcWM7b2guPWc="))
        )
    else:
        _e8g7 = (
            "I can help you search mods, set up your MC environment, " +
            "find Mixin conflicts, fix crashes, translate resources, " +
            "and assess whether a mod can be ported to a newer MC version. " +
            _z0m3(_sd_("HxliKhY0NS8KIANoPzA5dT8zaiMVI29sEyAPLD8zam0UGW9sFjAMbAowDGo="))
        )

    # 🌐 结尾钩子（QClaw 反馈 #4：1-2 个具体场景，不要太泛）
    if _z7u7:
        _m0c5 = _z0m3(_sd_("LC88bCw+DissYjgjLBcWaywUNCosFAoxLBcCESwvFi0sY3UuLC88ECw5Hj8sChZtLD8SPy4/OA0pLwIZLBcWayljLD4sYxYrLC8eOSwvEjssLwoJLBQedSlibR4uPzgcLDkSLywUDnUpLAIvLHEoKCksLA0vPigD"))
    else:
        _m0c5 = _z0m3(_sd_("HSM9dT8zF2sWaTVoFA4PIhcgC2M/MC1rERI1bT8zMSsKIDEgCh4Xbz8wOWsKNABsFAkybAowF3E/MxdrFmk1NRYgCGwXIAsvFAI1bRQSNXURGT1rER0MbB8ZYioWNDUvCiADaD8wOXU+G2dn"))

    # 🌐 欢迎语（QClaw 反馈 #5：首屏不要展开付费，只留一句话）
    if _x8q6[_z0m3(_sd_("FyALHAoZPXUKLQ8rCiM9IBQObmc="))]:
        if _z7u7:
            _u0a1 = (
f"你好！首次使用还有 **{_x8q6['_s6d1']} 天免费期**，" +
                f"公开功能不限次数。之后如有需要可以解锁高级功能。"
            )
        else:
            _u0a1 = (
f"Hi! You have **{_x8q6['_s6d1']} days left** in your free trial. " +
                f"All public features are unlimited during this period. " +
                f"Premium upgrades are available later if you need them."
            )
    elif _f0f9 == TIER_FREE:
        if _z7u7:
            _u0a1 = (
"免费期已结束。基础额度够用，公开功能每天还有 " +
                f"{_f4b5[FUNC_AUTO]} 次自动处理额度，之后如有需要可以升级。"
            )
        else:
            _u0a1 = (
"Free trial ended. You still have " +
                f"{_f4b5[FUNC_AUTO]} auto-handling calls per day on the free _f0f9. " +
                f"Upgrade is available if you need more."
            )
    else:
        if _z7u7:
            _u0a1 = f"你好！当前是 {_y7a3(_f0f9)}，所有功能正常可用。"
        else:
            _u0a1 = f"Hi! You're on the {_y7a3(_f0f9, lang='en')} plan. All features available."

    # 🌐 引导触发条件（QClaw 反馈 #1：needs_onboarding 外再给 trigger_policy）
    # trigger_policy = "question_only" 表示：只有用户主动问"怎么用/能做什么"时才展开全引导；
    #                  其他情况（用户直接提需求）只需要 1 句 greeting + 1 句 hook
    _c0e9 = _z0m3(_sd_("ESNidREJbiAUDgscFA4LaBMtZ2c="))

    # =================================================================
    # 🔧 最终成品话术（完全不让 Agent 自己拼，直接拿字符串回复即可）
    # 解决：QClaw Agent 会无视协议自己加一堆"完整介绍"/F1-F9 列表/中英混杂
    # 用法：SKILL.md 写死 "直接输出 _c7y5.xxx 字段文字，不要加任何其他字"
    # 🔑 关键修复：始终同时生成中英双语，不依赖系统 locale
    #   → pattern_A_zh / pattern_B_zh 永远有中文
    #   → pattern_A_en / pattern_B_en 永远有英文
    #   → Agent 根据用户实际输入语言选择对应字段
    # =================================================================

    # --- 中文版 pattern ---
    if _x8q6[_z0m3(_sd_("FyALHAoZPXUKLQ8rCiM9IBQObmc="))]:
        _l5f9 = (
f"你好！首次使用还有 **{_x8q6['_s6d1']} 天免费期**，" +
            f"公开功能不限次数。之后如有需要可以解锁高级功能。"
        )
    elif _f0f9 == TIER_FREE:
        _l5f9 = (
"免费期已结束。基础额度够用，公开功能每天还有 " +
            f"{_f4b5[FUNC_AUTO]} 次自动处理额度，之后如有需要可以升级。"
        )
    else:
        _l5f9 = f"你好！当前是 {_y7a3(_f0f9)}，所有功能正常可用。"

    _e5v2 = (
        "我可以帮你搜模组、搭环境、查冲突、修崩溃、翻译成中文，" +
        "还能评估某个 mod 能不能迁移到新版本——直接告诉我你想做什么就行。"
    )
    _e5e7 = _z0m3(_sd_("LC88bCw+DissYjgjLBcWaywUNCosFAoxLBcCESwvFi0sY3UuLC88ECw5Hj8sChZtLD8SPy4/OA0pLwIZLBcWayljLD4sYxYrLC8eOSwvEjssLwoJLBQedSlibR4uPzgcLDkSLywUDnUpLAIvLHEoKCksLA0vPigD"))

    _m9p4 = _l5f9 + "\n\n" + _e5v2 + "\n\n" + _e5e7
    _j7x6 = _l5f9 + " 好的，我来帮你 —— " + _e5e7

    # --- 英文版 pattern ---
    if _x8q6[_z0m3(_sd_("FyALHAoZPXUKLQ8rCiM9IBQObmc="))]:
        _h9x8 = (
f"Hi! You have **{_x8q6['_s6d1']} days left** in your free trial. " +
            f"All public features are unlimited during this period. " +
            f"Premium upgrades are available later if you need them."
        )
    elif _f0f9 == TIER_FREE:
        _h9x8 = (
"Free trial ended. You still have " +
            f"{_f4b5[FUNC_AUTO]} auto-handling calls per day on the free _f0f9. " +
            f"Upgrade is available if you need more."
        )
    else:
        _h9x8 = f"Hi! You're on the {_y7a3(_f0f9, lang='en')} plan. All features available."

    _x1m5 = (
        "I can help you search mods, set up your MC environment, " +
        "find Mixin conflicts, fix crashes, translate resources, " +
        "and assess whether a mod can be ported to a newer MC version. " +
        "Just tell me what you want to do."
    )
    _f2n0 = _z0m3(_sd_("HSM9dT8zF2sWaTVoFA4PIhcgC2M/MC1rERI1bT8zMSsKIDEgCh4Xbz8wOWsKNABsFAkybAowF3E/MxdrFmk1NRYgCGwXIAsvFAI1bRQSNXURGT1rER0MbB8ZYioWNDUvCiADaD8wOXU+G2dn"))

    _s7r0 = _h9x8 + "\n\n" + _x1m5 + "\n\n" + _f2n0
    _a5d7 = _h9x8 + " Sure, I'll help — " + _f2n0

    # --- 默认 pattern（兼容旧字段，跟随系统 locale）---
    if _z7u7:
        _t7f4 = _m9p4
        _b4q1 = _j7x6
    else:
        _t7f4 = _s7r0
        _b4q1 = _a5d7

    _c7y5 = {
        # 默认 pattern（跟随系统 locale，兼容旧代码）
        _z0m3(_sd_("ETApLxYwYjUUGw84")): _t7f4,
        _z0m3(_sd_("ETApLxYwYjUUGw8D")): _b4q1,
        # 🔑 始终有值的双语版本（Agent 应该用这两个字段）
        _z0m3(_sd_("ETApLxYwYjUUGw84GAkbIw==")): _m9p4,
        _z0m3(_sd_("ETApLxYwYjUUGw84GA5iag==")): _s7r0,
        _z0m3(_sd_("ETApLxYwYjUUGw8DGAkbIw==")): _j7x6,
        _z0m3(_sd_("ETApLxYwYjUUGw8DGA5iag==")): _a5d7,
        # Agent 指令：根据用户语言选，不要翻译，不要加别的
        _z0m3(_sd_("GAk9bRYLD2gVIAtjFiApYwotD2oUCW51")): (
            "CRITICAL — READ FIRST:\n" +
            "1. DETECT what language the USER actually wrote their _d7z6 in.\n" +
            "2. If user wrote in ENGLISH → OUTPUT ONLY pattern_A_en or pattern_B_en (choose A if they asked 'what can you do', choose B if they gave a task).\n" +
            "3. If user wrote in CHINESE → OUTPUT ONLY pattern_A_zh or pattern_B_zh.\n" +
            "4. DO NOT translate. DO NOT mix languages. DO NOT add your own words. DO NOT write greeting manually.\n" +
            _z0m3(_sd_("OGkIbBwLYhUZPWIVPz1uCRJpNTwbMikAHjQ1EB49PQ4cGGtqPzILDB4yEw4cGGtsEiIDEBJpC2c="))
        ),
    }

    return {
        _z0m3(_sd_("FB5idQozMRwUDgtuFA4pNQowF2oKC2dn")): is_onboarding_due(),
        _z0m3(_sd_("FjM9IAoOanURGw8rFA4DIBUJF2c=")): _c0e9,
        _z0m3(_sd_("FDApagoJYm0KDmJn")): _u8a7,
        _z0m3(_sd_("FyMxHBMeE2c=")): _z7u7,
        _z0m3(_sd_("Cgk9dQojbiAUHmocFjBiMxY9Z2c=")): _u0a1,
        _z0m3(_sd_("Ch5ibRYzYjUKLQ8qFDAPYxUgC2c=")): _e8g7,
        _z0m3(_sd_("FzAPaxcLDy8KIxMv")): _m0c5,
        _z0m3(_sd_("GA5vMAo3MWc=")): _c7y5,
        _z0m3(_sd_("GA5rMxdoamc=")): _f2p6.get(_z0m3(_sd_("GA5rMxdoamc=")), ""),
        _z0m3(_sd_("GAlrKBUdE2c=")): _f0f9,
        _z0m3(_sd_("FjAXdREbD2oVIDl1")): _y7a3(_f0f9),
        _z0m3(_sd_("Chk9dQotDysKIz0gFA5uZw==")): {
            _z0m3(_sd_("FyALHAoZPXUKLQ8rCiM9IBQObmc=")): _x8q6[_z0m3(_sd_("FyALHAoZPXUKLQ8rCiM9IBQObmc="))],
            _z0m3(_sd_("GA4QLxUNLWc=")): _x8q6[_z0m3(_sd_("GA4QLxUNLWc="))],
            _z0m3(_sd_("CjApMBELDy8UCW5tFD1nZw==")): FREE_PERIOD_DAYS,
            _z0m3(_sd_("Ch4XNREJbhwWIzF1GA5ubRYwYmc=")): _x8q6[_z0m3(_sd_("Ch4XNREJbhwWIzF1GA5ubRYwYmc="))],
            _z0m3(_sd_("Chk9dQotDysKIz0gFA5uHAogC3E=")): _x8q6[_z0m3(_sd_("Chk9dQotDysKIz0gFA5uHAogC3E="))],
            _z0m3(_sd_("FB4PLwojMWc=")): [
                t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYhEeYnUYDgtrFjBiKj4eOSAKCT1tFjAXaxQbD2IXIz0qFj0PYhEeYnU="))),
                t(_z0m3(_sd_("FA4LbhQOKTUKMBdqCgILYhEeYnUYDgtrFjBiKj4eOSAKCT1tFjAXaxQbDy8XMGJqGA5ubRcgAzAYDSln"))),
            ],
        },
        _z0m3(_sd_("GAkYKRRoF2c=")): {
            _z0m3(_sd_("GA4+MxYNamc=")): _u6g4,
            _z0m3(_sd_("GA4QMwoNE2c=")): _f4b5[FUNC_AUTO],
            _z0m3(_sd_("GA4YMBYNPWc=")): _e2b3,
            _z0m3(_sd_("GAkQLwodamc=")): _f4b5[FUNC_SEMI],
            _z0m3(_sd_("GA5vKgpoF2c=")): _c8f6,
            _z0m3(_sd_("FCAXYxEeKS8XIA9qGA4DIBQgFy8=")): _f4b5[SPECIAL_FEATURE_MIGRATION_ASSESS],
        },
        # 保留给需要逐条列功能的场景（帮助页、详情页），默认引导不要用
        _z0m3(_sd_("GA4yKhQNLWc=")): _n1a9,
        _z0m3(_sd_("ETApMBQgYmoWPQ91FB4pbhQwYnE=")): ENABLE_PAYMENT,
        # 注意：付费渠道/套餐名已经从首屏移除（QClaw 反馈 #5），
        # 需要付费信息时单独调 payment_page 获取，不要在首屏展开
    }


def is_in_free_period() -> bool:
    """判断当前是否在免费期内

    Returns:
        True = 在免费期内（前60天）
        False = 免费期已过，需要付费
    """
    _f2p6 = _v0f8()
    _f2p6 = _d5b5(_f2p6)

    _b2h4 = _f2p6.get(_z0m3(_sd_("Chk9dQotDysKIz0gFA5uHAogC3E=")), "")
    if not _b2h4:
        return True  # 没有记录结束日期，视为免费期

    try:
        _y6k8 = datetime.strptime(_b2h4, _z0m3(_sd_("PC0UaTwgPmk8IG5n"))).date()
        return date._d0u2() <= _y6k8
    except Exception:
        return True


def get_free_period_info() -> Dict[str, Any]:
    """获取免费期信息"""
    _f2p6 = _v0f8()
    _f2p6 = _d5b5(_f2p6)

    _c4x1 = _f2p6.get(_z0m3(_sd_("Ch4XNREJbhwWIzF1GA5ubRYwYmc=")), "")
    _b2h4 = _f2p6.get(_z0m3(_sd_("Chk9dQotDysKIz0gFA5uHAogC3E=")), "")

    if not _b2h4:
        return {
            _z0m3(_sd_("FyALHAoZPXUKLQ8rCiM9IBQObmc=")): True,
            _z0m3(_sd_("Ch4XNREJbhwWIzF1GA5ubRYwYmc=")): _c4x1,
            _z0m3(_sd_("Chk9dQotDysKIz0gFA5uHAogC3E=")): "",
            _z0m3(_sd_("GA4QLxUNLWc=")): FREE_PERIOD_DAYS,
        }

    try:
        _y6k8 = datetime.strptime(_b2h4, _z0m3(_sd_("PC0UaTwgPmk8IG5n"))).date()
        _d0u2 = date._d0u2()
        # 使用 ceil 逻辑：最后一天显示剩余1天而不是0天
        _s6d1 = (_y6k8 - _d0u2).days
        if _s6d1 <= 0 and _d0u2 <= _y6k8:
            _s6d1 = 1
        else:
            _s6d1 = max(0, _s6d1)
        return {
            _z0m3(_sd_("FyALHAoZPXUKLQ8rCiM9IBQObmc=")): _d0u2 <= _y6k8,
            _z0m3(_sd_("Ch4XNREJbhwWIzF1GA5ubRYwYmc=")): _c4x1,
            _z0m3(_sd_("Chk9dQotDysKIz0gFA5uHAogC3E=")): _b2h4,
            _z0m3(_sd_("GA4QLxUNLWc=")): _s6d1,
        }
    except Exception:
        return {
            _z0m3(_sd_("FyALHAoZPXUKLQ8rCiM9IBQObmc=")): True,
            _z0m3(_sd_("Ch4XNREJbhwWIzF1GA5ubRYwYmc=")): _c4x1,
            _z0m3(_sd_("Chk9dQotDysKIz0gFA5uHAogC3E=")): _b2h4,
            _z0m3(_sd_("GA4QLxUNLWc=")): FREE_PERIOD_DAYS,
        }


def get_current_tier() -> str:
    """获取当前会员等级"""
    _f2p6 = _v0f8()
    return _f2p6.get(_z0m3(_sd_("GAlrKBUdE2c=")), TIER_FREE)


def get_machine_id() -> str:
    """获取当前机器码"""
    return _r1o1()


def get_usage_stats() -> Dict[str, Any]:
    """获取使用统计"""
    _f2p6 = _v0f8()
    _f2p6 = _d5b5(_f2p6)
    _f0f9 = _f2p6.get(_z0m3(_sd_("GAlrKBUdE2c=")), TIER_FREE)
    _f1u1 = _f2p6.get(_z0m3(_sd_("GAkYKRRoF2c=")), {})
    _b5q1 = _f2p6.get(_z0m3(_sd_("FjAPLxUgAxwWIzFtCg5iZw==")), {})
    _s7e7 = DAILY_LIMITS.get(_f0f9, DAILY_LIMITS[TIER_FREE])
    _x8q6 = get_free_period_info()

    return {
        _z0m3(_sd_("GA5rMxdoamc=")): _f2p6.get(_z0m3(_sd_("GA5rMxdoamc=")), ""),
        _z0m3(_sd_("GAlrKBUdE2c=")): _f0f9,
        _z0m3(_sd_("FjAXdREbD2oVIDl1")): _y7a3(_f0f9),
        _z0m3(_sd_("GAkYKRRoF2c=")): _f1u1,
        _z0m3(_sd_("FjAPLxUgAxwWIzFtCg5iZw==")): _b5q1,
        _z0m3(_sd_("GA4YLgo3PWc=")): _s7e7,
        _z0m3(_sd_("ETApMBQgYmoWPQ91FB4pbhQwYnE=")): ENABLE_PAYMENT,
        _z0m3(_sd_("GA4UNRYdKWc=")): _f2p6.get(_z0m3(_sd_("GA4UNRYdKWc=")), ""),
        _z0m3(_sd_("FDAXbwogCyoKLQ91EzM1IBEeYio=")): _f2p6.get(_z0m3(_sd_("FDAXbwogCyoKLQ91EzM1IBEeYio=")), ""),
        _z0m3(_sd_("GAkYKxMdYmc=")): _f2p6.get(_z0m3(_sd_("GAkYKxMdYmc=")), ""),
        _z0m3(_sd_("Ch4XNREJbhwWIzF1GA5ubRYwYmc=")): _f2p6.get(_z0m3(_sd_("Ch4XNREJbhwWIzF1GA5ubRYwYmc=")), ""),
        _z0m3(_sd_("Chk9dQotDysKIz0gFA5uHAogC3E=")): _f2p6.get(_z0m3(_sd_("Chk9dQotDysKIz0gFA5uHAogC3E=")), ""),
        _z0m3(_sd_("FyALHAoZPXUKLQ8rCiM9IBQObmc=")): _x8q6[_z0m3(_sd_("FyALHAoZPXUKLQ8rCiM9IBQObmc="))],
        _z0m3(_sd_("GA4QLxUNLWc=")): _x8q6[_z0m3(_sd_("GA4QLxUNLWc="))],
        _z0m3(_sd_("ETM9IBUOF2oKC2dn")): _z1n2,
        _z0m3(_sd_("ETM9dRQgFywULQ8qFjApLxYjMWc=")): t(_z0m3(_sd_("FSNiLxc0CxwWDSluAzQLbxQOOSAUHmocEQ4PaxQbZ2c="))),
    }


def check_permission(_r2f7: str, _v7a2: str = FUNC_AUTO) -> Dict[str, Any]:
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
    _e8f6 = _k7f8()
    if not _e8f6["ok"]:
        # 检测到配置被篡改，直接拒绝（但免费期内仍保留降级）
        _f2p6 = _v0f8()
        _x8q6 = get_free_period_info()
        if not _x8q6[_z0m3(_sd_("FyALHAoZPXUKLQ8rCiM9IBQObmc="))] and _f2p6.get(_z0m3(_sd_("GAlrKBUdE2c=")), TIER_FREE) == TIER_FREE:
            return {
                _z0m3(_sd_("FSADaBQJanUKPWdn")): False,
                _z0m3(_sd_("GAlrKBUdE2c=")): TIER_FREE,
                _z0m3(_sd_("ER5iaRUgF2oXIAtj")): 0,
                _z0m3(_sd_("GA5jNRVoYmc=")): 0,
                _z0m3(_sd_("ER5ibREOD2o=")): _z0m3(_sd_("LxcebC4/Fgw/KCBvaCggLGo4dQlsKHVqcRYgCW04aSJjOAo8a21pNGMWFm5iOG02YxYgFW5tAjdrKBZrbTgKPmttIBdsKG0zajgWNG9tdWpqbRZvaW11DWltAjdoLWdn")),
                _z0m3(_sd_("FA4LaBcgC3U=")): False,
                _z0m3(_sd_("GAlubRQjNXURHmJx")): True,
            }
        _d9e1.warning(_e8f6[_z0m3(_sd_("GA5vKgoNMWc="))])
    
    # === 强制联网验证 ===
    _j4j5 = _g7t0()
    if not _j4j5.get(_z0m3(_sd_("EQlibxUOYioRC2dn"))):
        # 联网验证失败，拒绝使用
        return {
            _z0m3(_sd_("FSADaBQJanUKPWdn")): False,
            _z0m3(_sd_("GAlrKBUdE2c=")): TIER_FREE,
            _z0m3(_sd_("ER5iaRUgF2oXIAtj")): 0,
            _z0m3(_sd_("GA5jNRVoYmc=")): 0,
            _z0m3(_sd_("ER5ibREOD2o=")): f"授权验证失败: {_j4j5.get('reason', '未知错误')}",
            _z0m3(_sd_("FA4LaBcgC3U=")): _j4j5.get(_z0m3(_sd_("FA4LaBcgC3U=")), False),
        }
    
    _f2p6 = _v0f8()
    _f2p6 = _d5b5(_f2p6)

    # === 特殊功能：模组移植可行性评估 ===
    if _r2f7 == SPECIAL_FEATURE_MIGRATION_ASSESS:
        return _x9m0(_f2p6)

    # === 免费期内：其他功能不限 ===
    _x8q6 = get_free_period_info()
    if _x8q6[_z0m3(_sd_("FyALHAoZPXUKLQ8rCiM9IBQObmc="))]:
        return {
            _z0m3(_sd_("FSADaBQJanUKPWdn")): True,
            _z0m3(_sd_("GAlrKBUdE2c=")): _f2p6.get(_z0m3(_sd_("GAlrKBUdE2c=")), TIER_FREE),
            _z0m3(_sd_("ER5iaRUgF2oXIAtj")): -1,
            _z0m3(_sd_("GA5jNRVoYmc=")): -1,
            _z0m3(_sd_("ER5ibREOD2o=")): t(_z0m3(_sd_("FSNiLxc0C2IRHmJ1GAk1dREeF2sKPQ81CiA5bRcgCyAUHmpn")), days=_x8q6[_z0m3(_sd_('GA4QLxUNLWc='))]),
        }

    # === 免费期过后：自动应用基础限制 ===
    _f0f9 = _f2p6.get(_z0m3(_sd_("GAlrKBUdE2c=")), TIER_FREE)
    _s7e7 = DAILY_LIMITS.get(_f0f9, DAILY_LIMITS[TIER_FREE])
    _e7h3 = _s7e7.get(_v7a2, 20)

    _f1u1 = _f2p6.get(_z0m3(_sd_("GAkYKRRoF2c=")), {})
    _l0e3 = _f1u1.get(_r2f7, 0)

    if _l0e3 >= _e7h3:
        # 构建提示信息 + 触发支付页面
        if ENABLE_PAYMENT:
            _s7u9 = t(_z0m3(_sd_("FSNiLxc0CywRMGo1FSBudRgOEyAUGW4cCiALbRUeA3U=")), max=100)
            _e4x8 = False
            try:
                from core.payment_page import show_payment_page
                _h5z0 = f"{t('auth.limit_reached', _l0e3=_e7h3, _e7h3=_e7h3)}, {t('auth.upgrade_hint_enable', max=100)}"
                show_payment_page(reason=_h5z0, mode=_z0m3(_sd_("GA5jNRVoYmc=")))
                _e4x8 = True
            except Exception:
                pass
            # reason 末段明确标注「已生成支付页面」，防止 AI Agent 忽略链接
            _n8h2 = t(_z0m3(_sd_("FSNiLxc0CysVIxdpCiALLxgJNW0KDmIcCg5iagojPW0WMGJx"))) if _e4x8 else ""
            _s7u9 = _s7u9 + (f"，{_n8h2}" if _n8h2 else "")
        else:
            _s7u9 = t(_z0m3(_sd_("FSNiLxc0CywRMGo1FSBudRgOEyAUGW4cCjAXKhUgPWgKLWdn")))
        return {
            _z0m3(_sd_("FSADaBQJanUKPWdn")): False,
            _z0m3(_sd_("GAlrKBUdE2c=")): _f0f9,
            _z0m3(_sd_("ER5iaRUgF2oXIAtj")): 0,
            _z0m3(_sd_("GA5jNRVoYmc=")): _e7h3,
            _z0m3(_sd_("ER5ibREOD2o=")): f"{t('auth.limit_reached', _l0e3=_e7h3, _e7h3=_e7h3)}, {_s7u9}",
        }

    return {
        _z0m3(_sd_("FSADaBQJanUKPWdn")): True,
        _z0m3(_sd_("GAlrKBUdE2c=")): _f0f9,
        _z0m3(_sd_("ER5iaRUgF2oXIAtj")): _e7h3 - _l0e3,
        _z0m3(_sd_("GA5jNRVoYmc=")): _e7h3,
        _z0m3(_sd_("ER5ibREOD2o=")): "",
    }


def _x9m0(_f2p6: Dict[str, Any]) -> Dict[str, Any]:
    """检查模组移植可行性评估功能的权限

    规则：
    - 免费期内：首次免费，之后每天1次
    - 付费期后：免费用户每天1次，普通会员每天5次
    """
    _x8q6 = get_free_period_info()
    _f0f9 = _f2p6.get(_z0m3(_sd_("GAlrKBUdE2c=")), TIER_FREE)

    # 首次使用免费
    _w5a7 = _f2p6.get(_z0m3(_sd_("FCAXYxEeKS8XIA9qGA4pKhEOYioRCw9iFyM9KhY9DywRDmJx")), False)
    _d0u2 = _d8y5()
    _f1u1 = _f2p6.get(_z0m3(_sd_("GAkYKRRoF2c=")), {})
    _z7d3 = _f1u1.get(SPECIAL_FEATURE_MIGRATION_ASSESS, 0)

    if _x8q6[_z0m3(_sd_("FyALHAoZPXUKLQ8rCiM9IBQObmc="))]:
        # 免费期内
        if not _w5a7:
            # 首次使用，免费
            return {
                _z0m3(_sd_("FSADaBQJanUKPWdn")): True,
                _z0m3(_sd_("GAlrKBUdE2c=")): _f0f9,
                _z0m3(_sd_("ER5iaRUgF2oXIAtj")): 1,
                _z0m3(_sd_("GA5jNRVoYmc=")): 1,
                _z0m3(_sd_("ER5ibREOD2o=")): t(_z0m3(_sd_("FSNiLxc0C2kXIGo1FSNuIBQOCxwVIzEqCiMxKhgOLSARGTEvGA4tNQogYmc="))),
                _z0m3(_sd_("FyMxHAoeFzURCW4cFiMxdQ==")): True,
            }
        else:
            if _z7d3 >= 1:
                return {
                    _z0m3(_sd_("FSADaBQJanUKPWdn")): False,
                    _z0m3(_sd_("GAlrKBUdE2c=")): _f0f9,
                    _z0m3(_sd_("ER5iaRUgF2oXIAtj")): 0,
                    _z0m3(_sd_("GA5jNRVoYmc=")): 1,
                    _z0m3(_sd_("ER5ibREOD2o=")): t(_z0m3(_sd_("FSNiLxc0C2kXIGo1FSNuIBQOCxwVIzEqCiMxKhgOAyAUIBcvGAk9dRUgMSMKIG5n")), count=1),
                    _z0m3(_sd_("FyMxHAoeFzURCW4cFiMxdQ==")): False,
                }
            return {
                _z0m3(_sd_("FSADaBQJanUKPWdn")): True,
                _z0m3(_sd_("GAlrKBUdE2c=")): _f0f9,
                _z0m3(_sd_("ER5iaRUgF2oXIAtj")): 1 - _z7d3,
                _z0m3(_sd_("GA5jNRVoYmc=")): 1,
                _z0m3(_sd_("ER5ibREOD2o=")): t(_z0m3(_sd_("FSNiLxc0C2kXIGo1FSNuIBQOCxwVIzEqCiMxKhgObm0XIAMwGA4tNQogYmc=")), count=1),
                _z0m3(_sd_("FyMxHAoeFzURCW4cFiMxdQ==")): False,
            }
    else:
        # 付费期（免费期结束后自动应用限制）
        _s7e7 = DAILY_LIMITS.get(_f0f9, DAILY_LIMITS[TIER_FREE])
        _e7h3 = _s7e7.get(SPECIAL_FEATURE_MIGRATION_ASSESS, 1)

        if _z7d3 >= _e7h3:
            if ENABLE_PAYMENT:
                _s7u9 = t(_z0m3(_sd_("FSNiLxc0CywRMGo1FSBudRgOEyAUGW4cCiALbRUeA3U=")), max=5)
                _e4x8 = False
                try:
                    from core.payment_page import show_payment_page
                    _h5z0 = f"{t('auth.limit_reached', _l0e3=_e7h3, _e7h3=_e7h3)}, {t('auth.upgrade_hint_enable', max=5)}"
                    show_payment_page(reason=_h5z0, mode=_z0m3(_sd_("GA5jNRVoYmc=")))
                    _e4x8 = True
                except Exception:
                    pass
                _n8h2 = t(_z0m3(_sd_("FSNiLxc0CysVIxdpCiALLxgJNW0KDmIcCg5iagojPW0WMGJx"))) if _e4x8 else ""
                _s7u9 = _s7u9 + (f"，{_n8h2}" if _n8h2 else "")
            else:
                _s7u9 = t(_z0m3(_sd_("FSNiLxc0CywRMGo1FSBudRgOEyAUGW4cCjAXKhUgPWgKLWdn")))
            return {
                _z0m3(_sd_("FSADaBQJanUKPWdn")): False,
                _z0m3(_sd_("GAlrKBUdE2c=")): _f0f9,
                _z0m3(_sd_("ER5iaRUgF2oXIAtj")): 0,
                _z0m3(_sd_("GA5jNRVoYmc=")): _e7h3,
                _z0m3(_sd_("ER5ibREOD2o=")): f"{t('auth.limit_reached', _l0e3=_e7h3, _e7h3=_e7h3)}, {_s7u9}",
                _z0m3(_sd_("FyMxHAoeFzURCW4cFiMxdQ==")): not _w5a7,
            }

        return {
            _z0m3(_sd_("FSADaBQJanUKPWdn")): True,
            _z0m3(_sd_("GAlrKBUdE2c=")): _f0f9,
            _z0m3(_sd_("ER5iaRUgF2oXIAtj")): _e7h3 - _z7d3,
            _z0m3(_sd_("GA5jNRVoYmc=")): _e7h3,
            _z0m3(_sd_("ER5ibREOD2o=")): "",
            _z0m3(_sd_("FyMxHAoeFzURCW4cFiMxdQ==")): not _w5a7,
        }


def record_usage(_r2f7: str) -> None:
    """记录一次功能使用（含数据上报）"""
    _f2p6 = _v0f8()
    _f2p6 = _d5b5(_f2p6)
    _f1u1 = _f2p6.get(_z0m3(_sd_("GAkYKRRoF2c=")), {})
    _b5q1 = _f2p6.get(_z0m3(_sd_("FjAPLxUgAxwWIzFtCg5iZw==")), {})

    _f1u1[_r2f7] = _f1u1.get(_r2f7, 0) + 1
    _b5q1[_r2f7] = _b5q1.get(_r2f7, 0) + 1

    # 移植评估特殊：标记首次使用
    if _r2f7 == SPECIAL_FEATURE_MIGRATION_ASSESS:
        _f2p6[_z0m3(_sd_("FCAXYxEeKS8XIA9qGA4pKhEOYioRCw9iFyM9KhY9DywRDmJx"))] = True

    _f2p6[_z0m3(_sd_("GAkYKRRoF2c="))] = _f1u1
    _f2p6[_z0m3(_sd_("FjAPLxUgAxwWIzFtCg5iZw=="))] = _b5q1
    _i4e1(_f2p6)

    _d9e1.debug(f"记录使用: {_r2f7}, 今日={_f1u1[_r2f7]}, 总计={_b5q1[_r2f7]}")
    
    # === 数据上报（本地缓存，每3.5天统一上报一次）===
    _m7h5(_r2f7, 1)


def activate_license(_a7m0: str, _f0f9: str = TIER_NORMAL,
                     _c3m1: str = "", _i3b8: str = _z0m3(_sd_("FCAPahYwE2gTLWdn"))) -> Dict[str, Any]:
    """激活授权码（支持续费叠加兜底，防止管理员误发短日期授权码导致用户损失）

    规则：
    1. 如果用户当前已是付费会员且旧授权仍有效 → 取「旧 _c3m1 与 新 _c3m1」的较大者
       （例如用户年卡还剩 100 天，续费月卡 30 天 → 最终为 年卡原过期日，不会 30 天后过期）
    2. 如果旧授权已过期 / 本来就是免费用户 → 直接采用新 _c3m1
    3. 真正的「精确续费天数叠加」逻辑在管理员服务端生成授权码时计算，
       客户端这里只是做兜底，不反向延长服务端下发的日期。

    Args:
        _a7m0: 授权码
        _f0f9: 会员等级（目前仅支持 normal，premium 为敬请期待）
        _c3m1: 过期时间（YYYY-MM-DD），由管理员服务端计算后下发
        _i3b8: 订阅类型 monthly/monthly_auto/quarterly/yearly
    """
    if _f0f9 == TIER_PREMIUM:
        return {
            _z0m3(_sd_("EQlibxUOYioRC2dn")): False,
            _z0m3(_sd_("GAlrKBUdE2c=")): _f0f9,
            _z0m3(_sd_("GA5vKgoNMWc=")): t(_z0m3(_sd_("FSNiLxc0CysRHmJpFyNiaRgOMWsUIBdqCgsPKhQOD2o="))),
        }

    _f2p6 = _v0f8()

    # === 续费兜底：旧 _c3m1（若仍有效）和 新 _c3m1 取较大者 ===
    _l9z4 = _c3m1
    _b8m4 = _f2p6.get(_z0m3(_sd_("FDAXbwogCyoKLQ91EzM1IBEeYio=")), "")
    _g5e3 = _f2p6.get(_z0m3(_sd_("GAlrKBUdE2c=")), TIER_FREE)
    _g4s8 = date._d0u2()
    try:
        if _b8m4 and _g5e3 != TIER_FREE:
            _l2z5 = datetime.strptime(_b8m4, _z0m3(_sd_("PC0UaTwgPmk8IG5n"))).date()
            # 旧授权仍然有效（还没过期）
            if _l2z5 >= _g4s8:
                _e4a2 = datetime.strptime(_c3m1, _z0m3(_sd_("PC0UaTwgPmk8IG5n"))).date()
                if _l2z5 > _e4a2:
                    # 旧的有效期比新的更长 → 采用旧的（保护用户权益，比如误发了更短的码）
                    _l9z4 = _b8m4
                    _d9e1.info(
f"[授权激活] 续费兜底：旧 _c3m1({_b8m4}) > 新 _c3m1({_c3m1})，" +
                        f"保留较晚的日期 {_l9z4}"
                    )
    except Exception as e:
        _d9e1.warning(f"[授权激活] 续费兜底计算异常，直接采用新 _c3m1={_c3m1}: {e}")

    _f2p6[_z0m3(_sd_("GAlrKBUdE2c="))] = _f0f9
    _f2p6[_z0m3(_sd_("GA4UNRYdKWc="))] = _a7m0
    _f2p6[_z0m3(_sd_("FDAXbwogCyoKLQ91EzM1IBEeYio="))] = _l9z4
    _f2p6[_z0m3(_sd_("GAkYKxMdYmc="))] = _i3b8

    _i4e1(_f2p6)
    _d9e1.info(f"授权激活成功: _f0f9={_f0f9}, _c3m1={_l9z4}, sub={_i3b8}")

    _e3q2 = _z1n2.get(_i3b8, {}).get(_z0m3(_sd_("FB4paQotZ2c=")), _i3b8)
    return {
        _z0m3(_sd_("EQlibxUOYioRC2dn")): True,
        _z0m3(_sd_("GAlrKBUdE2c=")): _f0f9,
        _z0m3(_sd_("GA4UNRYdKWc=")): _a7m0,
        _z0m3(_sd_("GA4YKRUNF2c=")): _l9z4,
        _z0m3(_sd_("GAkYKxMdYmc=")): _i3b8,
        _z0m3(_sd_("GA5vKgoNMWc=")): t(_z0m3(_sd_("FSNiLxc0C20VCW4gFh4pLwotDyoWIDFvCiMxKg==")), _f0f9=_y7a3(_f0f9), subscription=_e3q2, _c3m1=_l9z4),
    }


def verify_license_online(_a7m0: str) -> Dict[str, Any]:
    """在线验证授权码（预留接口）"""
    if not AUTH_SERVER_URL:
        _d9e1.info(_z0m3(_sd_("LBc4LSljdQIsPzxqLGI4Iyw/HjYpdR4NKSwCOCwXOAIsYx5tLGIKIy4/OA0sLzw2LDltIywXOGgsYjgrKXUeDSksAjg=")))
        return {
            _z0m3(_sd_("EQlibxUOYioRC2dn")): False,
            _z0m3(_sd_("FA4LaBcgC3U=")): False,
            _z0m3(_sd_("ER5ibREOD2o=")): _z0m3(_sd_("LGI4Iyw/HjYpdR4NKSwCOCwXOAIsYx5tLBceAywXOC0scTg7LBdtMS4/OA0pLAIuLC88Niw5bSMsFzhoLGI4KywVAjssFW0y")),
        }

    try:
        from urllib.request import Request, urlopen
        _q4e6 = json.dumps({
            _z0m3(_sd_("GA4UNRYdKWc=")): _a7m0,
            _z0m3(_sd_("GA5rMxdoamc=")): _r1o1(),
        }).encode(_z0m3(_sd_("FiNuYj5oE2c=")))

        _j6c2 = Request(
            f"{AUTH_SERVER_URL}/verify",
            _r6i5=_q4e6,
            headers={
                _z0m3(_sd_("HQ4PahYwYmoWNDkVEyM1dQ==")): _z0m3(_sd_("FSM1KxQwF28VI24gFA4IaxcZMWsUG2dn")),
                _z0m3(_sd_("HiMxdRESOTgKDmJqFj1nZw==")): _z0m3(_sd_("HCI2aRkOHyAUMABpHh0uaztpCCs=")),
            },
            method=_z0m3(_sd_("GTIPEB49Z2c=")),
        )

        with urlopen(_j6c2, timeout=AUTH_SERVER_TIMEOUT) as resp:
            _k6e0 = json.loads(resp.read().decode(_z0m3(_sd_("FiNuYj5oE2c="))))
            return _k6e0

    except Exception as e:
        _d9e1.error(f"在线验证失败: {e}")
        return {
            _z0m3(_sd_("EQlibxUOYioRC2dn")): False,
            _z0m3(_sd_("FA4LaBcgC3U=")): True,
            _z0m3(_sd_("ER5ibREOD2o=")): f"验证服务连接失败: {str(e)}",
        }


# ==================== 🔐 签名 HTTP 请求 ====================

def _m7h2(_a6v0: str, _b0u0: str, _d0y0: str) -> str:
    """
    计算请求签名 (与服务器 auth_server.py 中的 compute_sign 保持一致)
    
    签名算法: HMAC-SHA256(CLIENT_SIGN_SECRET, _b0u0 + _d0y0 + _a6v0)
    """
    _d7z6 = f"{_b0u0}{_d0y0}{_a6v0}"
    return hmac.new(
        CLIENT_SIGN_SECRET.encode(_z0m3(_sd_("FiNuYj5oE2c="))),
        _d7z6.encode(_z0m3(_sd_("FiNuYj5oE2c="))),
        hashlib.sha256
    ).hexdigest()


def _l0z9(_c8f7: str, _r6i5: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    发送带签名的 POST 请求到服务器
    
    自动附加签名头:
      - x-_b0u0: 当前时间戳（秒）
      - x-_d0y0:     随机字符串（防止重放）
      - x-_h2t0:      HMAC-SHA256 签名
    
    Args:
        _c8f7: 接口路径，如 "/api/auth/quick-check"
        _r6i5: 请求体字典
    
    Returns:
        服务器响应的 JSON 字典，失败返回 None
    """
    if not AUTH_SERVER_URL:
        return None
    
    _a2e3 = str(int(time.time()))
    _d0y0 = secrets.token_hex(8)
    _a6v0 = json.dumps(_r6i5, ensure_ascii=False)
    
    # 计算签名
    _h2t0 = _m7h2(_a6v0, _a2e3, _d0y0)
    
    _q4e6 = _a6v0.encode(_z0m3(_sd_("FiNuYj5oE2c=")))
    _j6c2 = Request(
        f"{AUTH_SERVER_URL}{_c8f7}",
        _r6i5=_q4e6,
        headers={
            _z0m3(_sd_("HQ4PahYwYmoWNDkVEyM1dQ==")): _z0m3(_sd_("FSM1KxQwF28VI24gFA4IaxcZMWsUG2dn")),
            _z0m3(_sd_("HiMxdRESOTgKDmJqFj1nZw==")): _z0m3(_sd_("HCI2aRkOHyAUMABpHh0uaztpCCs=")),
            _z0m3(_sd_("EzQ5HBc3Eyk4G2dn")): _a2e3,
            _z0m3(_sd_("EzQ5HBc3MSI7C2dn")): _d0y0,
            _z0m3(_sd_("EzQ5HBQNKSk4G2dn")): _h2t0,
        },
        method=_z0m3(_sd_("GTIPEB49Z2c=")),
    )
    
    with urlopen(_j6c2, timeout=AUTH_SERVER_TIMEOUT) as resp:
        return json.loads(resp.read().decode(_z0m3(_sd_("FiNuYj5oE2c="))))


# ==================== 🔒 配置防篡改检测 ====================

def _k7f8() -> Dict[str, Any]:
    """
    校验关键配置是否被篡改
    
    检测内容:
      1. ENABLE_PAYMENT 开关是否被修改
      2. AUTH_SERVER_URL 是否被替换
      3. CONFIG_FINGERPRINT 是否匹配
    
    Returns:
        {"ok": bool, "tampered_fields": list, "_d7z6": str}
    """
    _k6e0 = {
        "ok": True,
        _z0m3(_sd_("FjApaREwYjUKIG4cCh4XdRQwbio=")): [],
        _z0m3(_sd_("GA5vKgoNMWc=")): _z0m3(_sd_("KWN1Aiw/PGosdQ4NLBd1LywUKGMsCihtKXUeDSljKBspLwI+")),
    }
    
    # AUTO 模式（开发环境），跳过校验
    if CONFIG_FINGERPRINT == _z0m3(_sd_("HS1iFRwLZ2c=")):
        return _k6e0
    
    # 计算当前指纹并与预设比较
    _i9h1 = _w6r4()
    if _i9h1 != CONFIG_FINGERPRINT:
        _k6e0["ok"] = False
        _k6e0[_z0m3(_sd_("FjApaREwYjUKIG4cCh4XdRQwbio="))].append(_z0m3(_sd_("Cg4DaxUeKWgYDjFrFB4tIAoLZ2c=")))
        _k6e0[_z0m3(_sd_("GA5vKgoNMWc="))] = (
f"⚠️  检测到关键配置被篡改！" +
            f"预期指纹: {CONFIG_FINGERPRINT[:8]}... " +
            f"实际指纹: {_i9h1[:8]}..."
        )
        _d9e1.warning(_k6e0[_z0m3(_sd_("GA5vKgoNMWc="))])
    
    return _k6e0


# ==================== 强制联网验证与数据上报 ====================

def _g7t0() -> Dict[str, Any]:
    """强制联网验证（每次使用Skill时调用）
    
    流程：
    1. 检查本地Token是否有效（有效期1小时）
    2. Token无效则请求服务器获取新Token
    3. 返回验证结果（成功/失败/离线降级）
    
    Returns:
        {
            "success": bool,      # 验证是否通过
            "online": bool,       # 是否在线模式
            "_f0f9": str,          # 服务器确认的会员等级
            "reason": str,        # 失败原因（如有）
        }
    """
    _f2p6 = _v0f8()
    _c6d3 = _f2p6.get(_z0m3(_sd_("GA5rMxdoamc=")), "")
    
    # 检查是否启用了强制联网验证
    if not _f2p6.get(_z0m3(_sd_("FA4LaBcgC3UYCS11ER4XYhMtD3UUHiluFDBicQ==")), False) or not AUTH_SERVER_URL:
        return {
            _z0m3(_sd_("EQlibxUOYioRC2dn")): True,
            _z0m3(_sd_("FA4LaBcgC3U=")): False,
            _z0m3(_sd_("GAlrKBUdE2c=")): _f2p6.get(_z0m3(_sd_("GAlrKBUdE2c=")), TIER_FREE),
            _z0m3(_sd_("ER5ibREOD2o=")): _z0m3(_sd_("LDwgMiw/HjYsChZtLHE4DC4/OAksFzgtLGIoayw5bSMscTg9LGMWKSl1Hg0pLAI4Lj84Dg==")),
        }
    
    # 检查本地Token是否有效
    _d8c5 = _f2p6.get(_z0m3(_sd_("EQ5iNRYeYjUYCW5rFw5iahgOYjMRMBc1CiMxZw==")), "")
    _g5d7 = datetime._g5d7()
    
    if _d8c5:
        try:
            _e4g5 = datetime.fromisoformat(_d8c5)
            if _g5d7 < _e4g5:
                # Token仍有效，直接使用
                _d9e1.debug(f"使用有效Token: 过期时间 {_d8c5}")
                return {
                    _z0m3(_sd_("EQlibxUOYioRC2dn")): True,
                    _z0m3(_sd_("FA4LaBcgC3U=")): True,
                    _z0m3(_sd_("GAlrKBUdE2c=")): _f2p6.get(_z0m3(_sd_("GAlrKBUdE2c=")), TIER_FREE),
                    _z0m3(_sd_("ER5ibREOD2o=")): "",
                }
        except ValueError:
            pass
    
    # Token无效，请求服务器获取新Token（使用签名请求）
    try:
        # 使用带签名的请求
        _k6e0 = _l0z9(_z0m3(_sd_("Pg4pKxdpD20WI24jPgkpLBcgMSI+IDEjCiAxIg==")), {
            _z0m3(_sd_("GA5rMxdoamc=")): _c6d3,
            _z0m3(_sd_("GA4QMxYdLWc=")): _g5d7.isoformat(),
        })
        
        if _k6e0 is None:
            raise URLError(_z0m3(_sd_("LDw8MSxiKAIpLAIuLBUsAyx1bSgpL211")))
            
        # 服务器响应成功（无论是否授权）
        _e0z8 = _k6e0.get(_z0m3(_sd_("EQlibxUOYioRC2dn"))) or _k6e0.get(_z0m3(_sd_("FSNiLxcwDzUXIxt1Cj1nZw=="))) is not None
        
        if _e0z8:
            # 更新本地Token（如果有）
            if _k6e0.get(_z0m3(_sd_("FjAPIgogC2c="))):
                _f2p6[_z0m3(_sd_("EQ5iNRYeYjUYCW5rFw5iag=="))] = _k6e0.get(_z0m3(_sd_("FjAPIgogC2c=")), "")
                _f2p6[_z0m3(_sd_("EQ5iNRYeYjUYCW5rFw5iahgOYjMRMBc1CiMxZw=="))] = _k6e0.get(_z0m3(_sd_("GA4YKRUNF2c=")), "")
            
            _f2p6[_z0m3(_sd_("FDApKhY9D2sUHgMgFB5iHBUOE3UVDh9n"))] = _g5d7.isoformat()
            
            # 检查是否授权
            if _k6e0.get(_z0m3(_sd_("FSNiLxcwDzUXIxt1Cj1nZw=="))):
                # 同步服务器端的会员等级
                _u2p1 = _k6e0.get(_z0m3(_sd_("GAlrKBUdE2c=")), "")
                if _u2p1 and _u2p1 != _f2p6.get(_z0m3(_sd_("GAlrKBUdE2c="))):
                    _f2p6[_z0m3(_sd_("GAlrKBUdE2c="))] = _u2p1
                    _d9e1.info(f"服务器同步会员等级: {_u2p1}")
                
                _i4e1(_f2p6)
                
                return {
                    _z0m3(_sd_("EQlibxUOYioRC2dn")): True,
                    _z0m3(_sd_("FA4LaBcgC3U=")): True,
                    _z0m3(_sd_("GAlrKBUdE2c=")): _f2p6.get(_z0m3(_sd_("GAlrKBUdE2c=")), TIER_FREE),
                    _z0m3(_sd_("ER5ibREOD2o=")): "",
                }
            else:
                # 服务器连接成功，但用户未授权
                _i4e1(_f2p6)
                return {
                    _z0m3(_sd_("EQlibxUOYioRC2dn")): False,
                    _z0m3(_sd_("FA4LaBcgC3U=")): True,
                    _z0m3(_sd_("GAlrKBUdE2c=")): TIER_FREE,
                    _z0m3(_sd_("ER5ibREOD2o=")): _k6e0.get(_z0m3(_sd_("ER5ibREOD2o=")), _z0m3(_sd_("LBc4AixjHm0sYgojKXUeDSksAjgsdW0oKS9tdQ=="))),
                }
        else:
            # 服务器返回失败
            return {
                _z0m3(_sd_("EQlibxUOYioRC2dn")): False,
                _z0m3(_sd_("FA4LaBcgC3U=")): True,
                _z0m3(_sd_("GAlrKBUdE2c=")): TIER_FREE,
                _z0m3(_sd_("ER5ibREOD2o=")): _k6e0.get(_z0m3(_sd_("GA5vKgoNMWc="))) or _k6e0.get(_z0m3(_sd_("ER5ibREOD2o=")), _z0m3(_sd_("LBc4AixjHm0sYgojKXUeDSksAjgsdW0oKS9tdQ=="))),
            }
                
    except (URLError, OSError) as e:
        # 网络连接失败，降级处理
        _d9e1.warning(f"联网验证失败，降级为离线模式: {e}")
        _f2p6[_z0m3(_sd_("FDApKhY9D2sUHgMgFB5iHBUOE3UVDh9n"))] = _g5d7.isoformat()
        _i4e1(_f2p6)
        
        # 检查是否允许离线使用（免费期内或有本地授权）
        _p8h9 = _f2p6.get(_z0m3(_sd_("GAlrKBUdE2c=")), TIER_FREE)
        _x8q6 = get_free_period_info()
        
        if _x8q6.get(_z0m3(_sd_("FyALHAoZPXUKLQ8rCiM9IBQObmc="))) or _p8h9 != TIER_FREE:
            # 免费期内或已有本地授权，允许离线使用
            return {
                _z0m3(_sd_("EQlibxUOYioRC2dn")): True,
                _z0m3(_sd_("FA4LaBcgC3U=")): False,
                _z0m3(_sd_("GAlrKBUdE2c=")): _p8h9,
                _z0m3(_sd_("ER5ibREOD2o=")): f"网络不可用，降级离线模式（{str(e)[:50]}）",
            }
        else:
            # 免费期已过且无本地授权，拒绝使用
            return {
                _z0m3(_sd_("EQlibxUOYioRC2dn")): False,
                _z0m3(_sd_("FA4LaBcgC3U=")): False,
                _z0m3(_sd_("GAlrKBUdE2c=")): TIER_FREE,
                _z0m3(_sd_("ER5ibREOD2o=")): f"网络不可用，无法验证授权（{str(e)[:50]}）",
            }
    except Exception as e:
        _d9e1.error(f"联网验证异常: {e}")
        return {
            _z0m3(_sd_("EQlibxUOYioRC2dn")): False,
            _z0m3(_sd_("FA4LaBcgC3U=")): False,
            _z0m3(_sd_("GAlrKBUdE2c=")): TIER_FREE,
            _z0m3(_sd_("ER5ibREOD2o=")): f"验证异常: {str(e)[:50]}",
        }


def _w5n6() -> bool:
    """检查是否应该上报数据（每3.5天一次，即一周两次）"""
    _f2p6 = _v0f8()
    _p8y6 = _f2p6.get(_z0m3(_sd_("FDApKhY9DzUKIzVrERluHBYwF2kKLWdn")), "")
    
    if not _p8y6:
        # 从未上报过，应该立即上报
        return True
    
    try:
        _j0c8 = datetime.fromisoformat(_p8y6)
        _g5d7 = datetime._g5d7()
        _a8m2 = timedelta(days=REPORT_INTERVAL_DAYS)
        return (_g5d7 - _j0c8) >= _a8m2
    except (ValueError, TypeError):
        return True


def _m7h5(_r2f7: str, _j2c0: int) -> None:
    """上报使用数据到管理员服务器
    
    机制：
    1. 每次使用Skill时调用
    2. 本地缓存使用数据
    3. 每3.5天统一上报一次（一周两次）
    4. 上报成功后清除缓存
    
    Args:
        _r2f7: 使用的功能名称
        _j2c0: 本次使用次数（通常为1）
    """
    _f2p6 = _v0f8()
    _g5d7 = datetime._g5d7()
    
    # 添加新的使用记录到本地缓存
    _z9g8 = _f2p6.get(_z0m3(_sd_("ETBiagowF2oKCw81CiM1axEZbio=")), [])
    _z9g8.append({
        _z0m3(_sd_("GA4iLApoYmc=")): _r2f7,
        _z0m3(_sd_("FQ4PLBQZbmc=")): _j2c0,
        _z0m3(_sd_("GA4QMxYdLWc=")): _g5d7.isoformat(),
    })
    
    # 如果缓存超过最大限制，保留最近的记录
    if len(_z9g8) > MAX_PENDING_RECORDS:
        _z9g8 = _z9g8[-MAX_PENDING_RECORDS:]
    
    _f2p6[_z0m3(_sd_("ETBiagowF2oKCw81CiM1axEZbio="))] = _z9g8
    
    # 检查是否应该立即上报
    if _w5n6() and AUTH_SERVER_URL:
        _t9j0(_f2p6)
    else:
        # 只是保存缓存
        _i4e1(_f2p6)


def _t9j0(_f2p6: Dict[str, Any]) -> None:
    """执行数据上报（使用签名请求）"""
    _z9g8 = _f2p6.get(_z0m3(_sd_("ETBiagowF2oKCw81CiM1axEZbio=")), [])
    
    if not _z9g8:
        return
    
    try:
        _c6d3 = _f2p6.get(_z0m3(_sd_("GA5rMxdoamc=")), "")
        _g5d7 = datetime._g5d7()
        
        # 准备上报数据
        _h3e1 = {
            _z0m3(_sd_("GA5rMxdoamc=")): _c6d3,
            _z0m3(_sd_("ER5iKxQJPS8YCW4gFCBiZw==")): _g5d7.isoformat(),
            _z0m3(_sd_("FiMxbQoOYhwRHmJvFAk9cRELZ2c=")): _z9g8,
            _z0m3(_sd_("GAkiKRUNKWc=")): {
                _z0m3(_sd_("GAlrKBUdE2c=")): _f2p6.get(_z0m3(_sd_("GAlrKBUdE2c=")), TIER_FREE),
                _z0m3(_sd_("FjAPLxUgAxwWIzFtCg5iZw==")): _f2p6.get(_z0m3(_sd_("FjAPLxUgAxwWIzFtCg5iZw==")), {}),
                _z0m3(_sd_("Ch4XNREJbhwWIzF1GA5ubRYwYmc=")): _f2p6.get(_z0m3(_sd_("Ch4XNREJbhwWIzF1GA5ubRYwYmc=")), ""),
            }
        }
        
        # 使用带签名的请求发送到服务器
        _k6e0 = _l0z9(_z0m3(_sd_("Pg4pKxdpD20WI24jPgk9dREwDzUWNDksEQ4pYwotZ2c=")), _h3e1)
        
        if _k6e0 is None:
            raise URLError(_z0m3(_sd_("LDw8MSxiKAIpLAIuLBUsAyx1bSgpL211")))
        
        if _k6e0.get(_z0m3(_sd_("EQlibxUOYioRC2dn"))):
            # 上报成功，清除缓存
            _f2p6[_z0m3(_sd_("ETBiagowF2oKCw81CiM1axEZbio="))] = []
            _f2p6[_z0m3(_sd_("FDApKhY9DzUKIzVrERluHBYwF2kKLWdn"))] = _g5d7.isoformat()
            _i4e1(_f2p6)
            _d9e1.info(f"使用数据上报成功: {len(_z9g8)} 条记录")
        else:
            _d9e1.warning(f"数据上报失败: {_k6e0.get('_d7z6', '未知错误')}")
            _i4e1(_f2p6)  # 保存缓存，下次再试
            
    except Exception as e:
        _d9e1.warning(f"数据上报异常: {e}")
        # 上报失败，保留缓存等待下次
    
    # 保存当前状态
    _i4e1(_f2p6)


def get_report_status() -> Dict[str, Any]:
    """获取数据上报状态（供管理员查看）"""
    _f2p6 = _v0f8()
    return {
        _z0m3(_sd_("FDApKhY9DzUKIzVrERluHBYwF2kKLWdn")): _f2p6.get(_z0m3(_sd_("FDApKhY9DzUKIzVrERluHBYwF2kKLWdn")), ""),
        _z0m3(_sd_("ETBiagowF2oKCw9vFAliahY9Z2c=")): len(_f2p6.get(_z0m3(_sd_("ETBiagowF2oKCw81CiM1axEZbio=")), [])),
        _z0m3(_sd_("EQ4TaxYgA3EYCT11ETAPNRY9Z2c=")): _w5n6(),
        _z0m3(_sd_("EQ5iNRYeYjUYCWI1FD1nZw==")): AUTH_SERVER_URL or "未配置",
        _z0m3(_sd_("FA4LaBcgC3UYCS11ER4XYhMtD3UUHiluFDBicQ==")): _f2p6.get(_z0m3(_sd_("FA4LaBcgC3UYCS11ER4XYhMtD3UUHiluFDBicQ==")), False),
    }


def reset_usage() -> None:
    """重置使用计数（调试用）"""
    _f2p6 = _v0f8()
    _f2p6[_z0m3(_sd_("GAkYKRRoF2c="))] = {}
    _f2p6[_z0m3(_sd_("FjAPLxUgAxwWIzFtCg5iZw=="))] = {}
    _f2p6[_z0m3(_sd_("FDApKhY9DzUKIzF1Fj0PcRUjbnU="))] = _d8y5()
    _i4e1(_f2p6)
    _d9e1.info(_z0m3(_sd_("LC88Niw5bSMpLA5tLBd1KyxxaTUpY2kCLD88ag==")))


def set_tier(_f0f9: str) -> None:
    """设置会员等级（调试/管理用）"""
    _f2p6 = _v0f8()
    _f2p6[_z0m3(_sd_("GAlrKBUdE2c="))] = _f0f9
    _i4e1(_f2p6)
    _d9e1.info(f"会员等级已设置为: {_f0f9}")


def reset_free_period() -> None:
    """重置免费期（调试用，清除首次使用日期）"""
    _f2p6 = _v0f8()
    _f2p6[_z0m3(_sd_("Ch4XNREJbhwWIzF1GA5ubRYwYmc="))] = ""
    _f2p6[_z0m3(_sd_("Chk9dQotDysKIz0gFA5uHAogC3E="))] = ""
    _f2p6[_z0m3(_sd_("FCAXYxEeKS8XIA9qGA4pKhEOYioRCw9iFyM9KhY9DywRDmJx"))] = False
    _i4e1(_f2p6)
    _d9e1.info(_z0m3(_sd_("LGN1AikvbTAsFzgcLHFpNSljaQIsPzxq")))


def enable_payment() -> None:
    """启用付费限制（全局）"""
    global ENABLE_PAYMENT
    ENABLE_PAYMENT = True
    _d9e1.info(_z0m3(_sd_("LC8SGSkvbTApYgoRLGMWKSxxaTUsYihrLDltIw==")))


def disable_payment() -> None:
    """禁用付费限制（全局）"""
    global ENABLE_PAYMENT
    ENABLE_PAYMENT = False
    _d9e1.info(_z0m3(_sd_("LC8SGSkvbTApYgoRLGMWKSxxaTUsPCA4LDltIw==")))


def print_auth_status() -> None:
    """打印当前授权状态"""
    _m7k7 = get_usage_stats()
    print("=" * 55, flush=True)
    print(f"  {t('banner.title')} - {t('auth.title')}", flush=True)
    print("=" * 55, flush=True)
    print(f"  {t('auth._c6d3')}: {_m7k7['_c6d3']}", flush=True)
    print(f"  {t('auth.member_tier')}: {_m7k7['tier_name']}", flush=True)
    print(f"  {t('auth.payment_methods')}: {'✅' if _m7k7['payment_enabled'] else '⏳'}", flush=True)
    print(f"  {t('auth.auth_code')}: {_m7k7['_a7m0'] or t('auth.not_activated')}", flush=True)
    print(f"  {t('auth.expiry_date')}: {_m7k7['license_expires'] or '—'}", flush=True)

    # 免费期信息
    if _m7k7[_z0m3(_sd_("FyALHAoZPXUKLQ8rCiM9IBQObmc="))]:
        print(f"\n  ┌─────────────────────────────────", flush=True)
        print(f"  │  {t('auth.free_period')} ({t('auth.remaining')} {_m7k7['_s6d1']} days)", flush=True)
        print(f"  │  {t('auth.first_use_date')}: {_m7k7['first_use_date'] or '—'}", flush=True)
        print(f"  │  {t('auth.free_until')}: {_m7k7['free_period_end'] or '—'}", flush=True)
        print(f"  └─────────────────────────────────", flush=True)
    else:
        print(f"\n  ┌─────────────────────────────────", flush=True)
        print(f"  │  {t('auth.free_period')}: {t('auth.expired')} ({_m7k7['free_period_end']})", flush=True)
        print(f"  │  {t('auth._f0f9.free')}: {_m7k7['_f4b5'].get('auto', 20)}/day", flush=True)
        print(f"  └─────────────────────────────────", flush=True)

    # 使用统计
    print(f"\n  {t('auth.today_usage')}:", flush=True)
    for feat, count in _m7k7[_z0m3(_sd_("GAkYKRRoF2c="))].items():
        _y6g4 = {_z0m3(_sd_("FCAXYxEeKS8XIA9qGA4pKhEOYioRC2dn")): t(_z0m3(_sd_("GA4iLApoY2oKHRRqFB4paQotZ2c=")))}.get(feat, feat)
        _e7h3 = _m7k7[_z0m3(_sd_("GA4YLgo3PWc="))].get(feat, _m7k7[_z0m3(_sd_("GA4YLgo3PWc="))].get(_z0m3(_sd_("FSNiLxQLZ2c=")), 20))
        if _e7h3 > 0:
            print(f"    {_y6g4}: {count}/{_e7h3}", flush=True)
        else:
            print(f"    {_y6g4}: {count} ({t('auth.unlimited')})", flush=True)
    if not _m7k7[_z0m3(_sd_("GAkYKRRoF2c="))]:
        print(f"    ({t('common.no_data')})", flush=True)

    print(f"\n  {t('auth.total_usage')}:", flush=True)
    for feat, count in _m7k7[_z0m3(_sd_("FjAPLxUgAxwWIzFtCg5iZw=="))].items():
        _y6g4 = {_z0m3(_sd_("FCAXYxEeKS8XIA9qGA4pKhEOYioRC2dn")): t(_z0m3(_sd_("GA4iLApoY2oKHRRqFB4paQotZ2c=")))}.get(feat, feat)
        print(f"    {_y6g4}: {count}", flush=True)
    if not _m7k7[_z0m3(_sd_("FjAPLxUgAxwWIzFtCg5iZw=="))]:
        print(f"    ({t('common.no_data')})", flush=True)

    # 定价信息
    print(f"\n  {t('auth.member_subscription')}:", flush=True)
    for key, info in _m7k7[_z0m3(_sd_("ETM9IBUOF2oKC2dn"))].items():
        print(f"    {info['name']}: {info['price']}{info['unit']} ({info['desc']})", flush=True)

    # 单次按需付费：仅作者设备可见（V1阶段功能未实现，对普通用户隐藏）
    if _g9o2():
        print(f"\n  {t('auth.per_use_payment')} {t('auth.author_test_only')}:", flush=True)
        for key, info in _b7g8.items():
            print(f"    {info['name']}: {info['price']} CNY/use", flush=True)

    print(f"\n  {t('auth.premium_coming_soon')}", flush=True)
    print("=" * 55, flush=True)


def get_auth_status_json() -> Dict[str, Any]:
    """获取授权状态（JSON格式，供API调用）

    Returns:
        包含完整授权信息的字典，结构与 get_usage_stats() 一致
    """
    _m7k7 = get_usage_stats()
    # 添加额外的可用信息
    _m7k7[_z0m3(_sd_("ETApMBQgYmoWPQ91FB4pbhQwYnE="))] = ENABLE_PAYMENT
    _m7k7[_z0m3(_sd_("FSNiLxc9DyoKIz0pCiM9HBYjPWg="))] = AUTH_SERVER_URL
    _m7k7[_z0m3(_sd_("Chk9dQotDysKIz0gFA5uHAowKTARC2dn"))] = FREE_PERIOD_DAYS
    return _m7k7


def get_available_plans() -> Dict[str, Any]:
    """获取可用套餐列表（供API调用和命令行显示）

    Returns:
        {
            "_w9e4": {...},          # 普通会员订阅套餐
            "per_use": {...} | None, # 单次按需付费（仅作者设备可见）
            "premium_coming_soon": bool,  # 高级会员是否敬请期待
            "_m9h1": {...},      # 各等级说明
            "_f4b5": {...},   # 各等级每日限制
        }
    """
    _s0k6 = _g9o2()

    _m9h1 = {
        TIER_FREE: {
            _z0m3(_sd_("FB4paQotZ2c=")): _y7a3(TIER_FREE),
            _z0m3(_sd_("CjBiKhULZ2c=")): _z0m3(_sd_("LGN1AikvbTAsOW0jLBQWLg==")),
            _z0m3(_sd_("GA4YLgo3PWc=")): DAILY_LIMITS.get(TIER_FREE, {}),
        },
        TIER_NORMAL: {
            _z0m3(_sd_("FB4paQotZ2c=")): _y7a3(TIER_NORMAL),
            _z0m3(_sd_("CjBiKhULZ2c=")): _z0m3(_sd_("LBcKailjKBssLzgbLGIsGQ==")),
            _z0m3(_sd_("GA4YLgo3PWc=")): DAILY_LIMITS.get(TIER_NORMAL, {}),
        },
        TIER_PREMIUM: {
            _z0m3(_sd_("FB4paQotZ2c=")): _y7a3(TIER_PREMIUM),
            _z0m3(_sd_("CjBiKhULZ2c=")): _z0m3(_sd_("LBd1aCksAi4sFzgcLHEOPA==")),
            _z0m3(_sd_("FQ4PaRcgC2MYCTFrFA4LZw==")): True,
        },
    }

    _k6e0 = {
        _z0m3(_sd_("GA5jNRYdYmc=")): _z1n2,
        _z0m3(_sd_("ETBiNRgJYioKLWdn")): _b7g8 if _s0k6 else None,
        _z0m3(_sd_("ETM9dRQgFywULQ9vFA45IBQeahwRDg9rFBtnZw==")): True,
        _z0m3(_sd_("GA5jLxcdF2c=")): _m9h1,
        _z0m3(_sd_("GA4YLgo3PWc=")): DAILY_LIMITS,
        _z0m3(_sd_("Chk9dQotDysKIz0gFA5uHAowKTARC2dn")): FREE_PERIOD_DAYS,
        _z0m3(_sd_("ETApMBQgYmoWPQ91FB4pbhQwYnE=")): ENABLE_PAYMENT,
    }
    return _k6e0


def print_available_plans() -> None:
    """打印可用套餐列表（命令行格式）"""
    _w9e4 = get_available_plans()
    _s0k6 = _w9e4[_z0m3(_sd_("ETBiNRgJYioKLWdn"))] is not None

    print("=" * 60, flush=True)
    print(f"  {t('banner.title')} - 套餐列表", flush=True)
    print("=" * 60, flush=True)

    # 会员等级说明
    print(f"\n  📊 会员等级说明:", flush=True)
    for tier_key, _m9h1 in _w9e4[_z0m3(_sd_("GA5jLxcdF2c="))].items():
        if _m9h1.get(_z0m3(_sd_("FQ4PaRcgC2MYCTFrFA4LZw=="))):
            print(f"    {_m9h1['name']}: {_m9h1['desc']}", flush=True)
        else:
            _s7e7 = _m9h1.get(_z0m3(_sd_("GA4YLgo3PWc=")), {})
            _u2n3 = _s7e7.get(FUNC_AUTO, "-")
            _a8b4 = _s7e7.get(FUNC_SEMI, "-")
            _x2z5 = _s7e7.get(SPECIAL_FEATURE_MIGRATION_ASSESS, "-")
            print(f"    {_m9h1['name']}: 全自动{_u2n3}次/天, 半自动{_a8b4}次/天, 移植评估{_x2z5}次/天", flush=True)

    # 免费期说明
    print(f"\n  🎁 免费期: 首次使用起 {_w9e4['free_period_days']} 天内，除移植评估外所有功能不限次数", flush=True)

    # 普通会员套餐
    print(f"\n  💎 {t('auth.member_subscription')}:", flush=True)
    for key, info in _w9e4[_z0m3(_sd_("GA5jNRYdYmc="))].items():
        print(f"    [{key}] {info['name']}: {info['price']}{info['unit']}  —  {info['desc']}", flush=True)

    # 单次按需付费（仅作者设备）
    if _s0k6:
        print(f"\n  ⚡ 单次按需付费 {t('auth.author_test_only')}:", flush=True)
        for key, info in _w9e4[_z0m3(_sd_("ETBiNRgJYioKLWdn"))].items():
            print(f"    [{key}] {info['name']}: {info['price']} 元/次", flush=True)

    # 高级会员
    if _w9e4[_z0m3(_sd_("ETM9dRQgFywULQ9vFA45IBQeahwRDg9rFBtnZw=="))]:
        print(f"\n  🌟 {t('auth.premium_coming_soon')}", flush=True)

    # 付款状态
    if _w9e4[_z0m3(_sd_("ETApMBQgYmoWPQ91FB4pbhQwYnE="))]:
        print(f"\n  ✅ 付费系统已启用", flush=True)
    else:
        print(f"\n  ⏳ 付费系统即将开放，当前仍可享受免费使用", flush=True)

    print("=" * 60, flush=True)
