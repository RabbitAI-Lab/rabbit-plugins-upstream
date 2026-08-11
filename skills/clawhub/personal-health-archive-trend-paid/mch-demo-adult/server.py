#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mch-demo-adult (Python 版) — 微信 Agent Pay / X402 协议商户服务端（成人健康档案与趋势分析）

实现 SkillHub「payskill帮助」要求的付费 skill 服务端：
  POST /api/resource   首次请求返回 402(要求支付)；支付后带 X-Out-Trade-No 重试返回付费内容
  POST /api/pay/notify   微信支付结果回调（可选）
  POST /api/refund/notify 退款结果回调（可选）
  GET  /health          健康检查

本服务为「成人健康档案与趋势分析」付费 Skill 的后端：买家传入成人基本信息 + 多个时间点的
体检/检验/住院报告（结构化 values 或粘贴 text），付费后服务端实时生成结构化成人健康档案
（各系统指标 + 异常标注 + 跨年度趋势分析）作为付费内容返回。

依赖：requests, cryptography  （pip install -r requirements.txt）
配置：复制 .env.example 为 .env 并填好；或导出同名环境变量。
     设 MOCK=1（或缺失微信/ SkillHub 密钥）时进入本地 mock 模式。
"""

import os
import time
import json
import base64
import uuid
import secrets
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse
import math
import datetime as _dt
import re

import requests
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.x509 import load_pem_x509_certificate


def _load_dotenv(path=".env"):
    """健壮加载 .env，支持无引号多行 PEM 私钥。"""
    try:
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return
    env = {}
    key = None
    buf = None
    for raw in lines:
        line = raw.rstrip("\n")
        s = line.strip()
        if not s or s.startswith("#"):
            if key is not None:
                buf += "\n"
            continue
        if "=" in line and key is None:
            k, _, v = line.partition("=")
            k, v = k.strip(), v.strip()
            if v.startswith("-----BEGIN") and "-----END" not in v:
                key, buf = k, v
            elif v.endswith("\\"):
                key, buf = k, v[:-1]
            else:
                env[k] = v
        elif key is not None:
            buf += "\n" + s
            if "-----END" in s:
                env[key], key, buf = buf, None, None
            elif s.endswith("\\"):
                buf = buf[:-1]
    for k, v in env.items():
        os.environ.setdefault(k, v)


_load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

# ---------------- 配置 ----------------
ENV = {k: os.environ.get(k, "") for k in [
    "MCH_ID", "APP_ID", "SERIAL_NO", "PRIVATE_KEY_PATH", "MCH_APIV3_KEY",
    "PAY_NOTIFY_URL", "REFUND_NOTIFY_URL",
    "SKILLHUB_DEVELOPER_ID", "SKILLHUB_PUB_KEY_ID", "SKILLHUB_PRIVATE_KEY",
    "SKILLHUB_PRIVATE_KEY_FILE",
    "WX_PUB_KEY_FILE", "WX_PUB_KEY_ID",
    "SKILL_ID", "SKILL_VERSION", "PORT",
]}
MOCK = os.environ.get("MOCK", "").lower() in ("1", "true", "yes") or not (
    ENV["MCH_ID"] and ENV["SKILLHUB_DEVELOPER_ID"]
    and (ENV["SKILLHUB_PRIVATE_KEY"] or ENV["SKILLHUB_PRIVATE_KEY_FILE"])
)

WX_BASE = "https://api.mch.weixin.qq.com"
PREORDER_URL = "https://payapp.weixin.qq.com/palmpayminiapp/clawagentpay/preorder"
PREORDER_PATH = "/palmpayminiapp/clawagentpay/preorder"

_lock = threading.Lock()
_orders = {}  # out_trade_no -> {"paid": bool, "content": str}


# ---------------- 密钥加载 ----------------
def _load_wx_key():
    p = ENV["PRIVATE_KEY_PATH"]
    if not p or not os.path.exists(p):
        raise RuntimeError(f"微信支付私钥文件不存在: {p}")
    with open(p, "rb") as f:
        return load_pem_private_key(f.read(), password=None)


def _load_sh_key():
    fp = ENV.get("SKILLHUB_PRIVATE_KEY_FILE", "")
    if fp and os.path.exists(fp):
        with open(fp, "rb") as f:
            pem = f.read().decode("utf-8")
    else:
        pem = ENV.get("SKILLHUB_PRIVATE_KEY", "")
    if not pem:
        raise RuntimeError("缺少 SKILLHUB_PRIVATE_KEY（或 SKILLHUB_PRIVATE_KEY_FILE）")
    return load_pem_private_key(pem.encode(), password=None)


def _sign(key, msg: str) -> str:
    sig = key.sign(msg.encode("utf-8"), asym_padding.PKCS1v15(), hashes.SHA256())
    return base64.b64encode(sig).decode("ascii")


def _nonce(n=32) -> str:
    return secrets.token_hex(n // 2)


# ---------------- 微信支付 v3 签名 ----------------
def _wx_authorization(method: str, path: str, body: str) -> str:
    ts = str(int(time.time()))
    nonce = _nonce()
    sign_str = f"{method}\n{path}\n{ts}\n{nonce}\n{body}\n"
    sig = _sign(_load_wx_key(), sign_str)
    return (f'WECHATPAY2-SHA256-RSA2048 mchid="{ENV["MCH_ID"]}",'
            f'nonce_str="{nonce}",signature="{sig}",timestamp="{ts}",'
            f'serial_no="{ENV["SERIAL_NO"]}"')


def _wx_native_order(description: str, out_trade_no: str, amount_fen: int) -> str:
    path = "/v3/pay/transactions/native"
    body = json.dumps({
        "mchid": ENV["MCH_ID"],
        "appid": ENV["APP_ID"],
        "description": description,
        "out_trade_no": out_trade_no,
        "notify_url": ENV["PAY_NOTIFY_URL"],
        "amount": {"total": amount_fen, "currency": "CNY"},
    })
    headers = {
        "Authorization": _wx_authorization("POST", path, body),
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    r = requests.post(WX_BASE + path, data=body.encode(), headers=headers, timeout=20)
    r.raise_for_status()
    return r.json().get("code_url", "")


def _wx_query_order(out_trade_no: str) -> str:
    path = f"/v3/pay/transactions/out-trade-no/{out_trade_no}?mchid={ENV['MCH_ID']}"
    headers = {
        "Authorization": _wx_authorization("GET", path, ""),
        "Accept": "application/json",
    }
    r = requests.get(WX_BASE + path, headers=headers, timeout=20)
    r.raise_for_status()
    return r.json().get("trade_state", "")


# ---------------- 微信支付回调：验签 + 解密 ----------------
_wx_certs = {}
_wx_certs_lock = threading.Lock()


def _aead_decrypt(ciphertext_b64: str, nonce: str, associated_data: str, key_str: str) -> bytes:
    key = key_str.encode("utf-8")
    if len(key) > 32:
        key = key[:32]
    if len(key) < 32:
        key = key.ljust(32, b"\0")
    aead = AESGCM(key)
    ct = base64.b64decode(ciphertext_b64)
    aad = associated_data.encode("utf-8") if associated_data else b""
    return aead.decrypt(nonce.encode("utf-8"), ct, aad)


def _wx_get_certs():
    if not ENV["MCH_APIV3_KEY"]:
        raise RuntimeError("缺少 MCH_APIV3_KEY，无法下载平台证书")
    path = "/v3/certificates"
    headers = {
        "Authorization": _wx_authorization("GET", path, ""),
        "Accept": "application/json",
    }
    r = requests.get(WX_BASE + path, headers=headers, timeout=20)
    r.raise_for_status()
    count = 0
    for item in r.json().get("data", []):
        serial = item.get("serial_no", "")
        enc = item.get("encrypt_certificate", {})
        pem = _aead_decrypt(
            enc.get("ciphertext", ""), enc.get("nonce", ""),
            enc.get("associated_data", "") or "", ENV["MCH_APIV3_KEY"],
        )
        cert = load_pem_x509_certificate(pem)
        with _wx_certs_lock:
            _wx_certs[serial] = cert.public_key()
        count += 1
    if count == 0:
        raise RuntimeError("平台证书为空，请检查 MCH_APIV3_KEY 是否正确")


def _load_wx_pub_key():
    fp = ENV.get("WX_PUB_KEY_FILE", "")
    serial = ENV.get("WX_PUB_KEY_ID", "")
    if not fp or not serial or not os.path.exists(fp):
        return
    with open(fp, "rb") as f:
        data = f.read()
    try:
        pub = load_pem_public_key(data)
    except Exception:
        pub = load_pem_x509_certificate(data).public_key()
    with _wx_certs_lock:
        _wx_certs[serial] = pub


def _verify_wx_signature(timestamp: str, nonce: str, body_bytes: bytes,
                         serial: str, sig_b64: str):
    pub = _wx_certs.get(serial)
    if pub is None:
        _wx_get_certs()
        pub = _wx_certs.get(serial)
    if pub is None:
        raise RuntimeError(f"找不到序列号 {serial} 的平台证书")
    msg = f"{timestamp}\n{nonce}\n{body_bytes.decode('utf-8')}\n".encode("utf-8")
    pub.verify(
        base64.b64decode(sig_b64),
        msg,
        asym_padding.PKCS1v15(),
        hashes.SHA256(),
    )


def _process_wx_notify(raw_body: bytes, headers) -> dict:
    ts = headers.get("Wechatpay-Timestamp", "")
    nonce = headers.get("Wechatpay-Nonce", "")
    serial = headers.get("Wechatpay-Serial", "")
    sig = headers.get("Wechatpay-Signature", "")
    if not (ts and nonce and serial and sig):
        raise RuntimeError("回调缺少验签头")
    _verify_wx_signature(ts, nonce, raw_body, serial, sig)
    payload = json.loads(raw_body)
    res = payload.get("resource", {})
    plain = _aead_decrypt(
        res.get("ciphertext", ""), res.get("nonce", ""),
        res.get("associated_data", "") or "", ENV["MCH_APIV3_KEY"],
    )
    return json.loads(plain)


# ---------------- SkillHub AI 预下单签名 ----------------
def _sh_preorder(code_url: str, out_trade_no: str) -> str:
    ts = str(int(time.time()))
    expires = str(int(time.time()) + 900)
    nonce = _nonce()
    l2 = {
        "skill_info": {"skill_id": ENV["SKILL_ID"], "skill_version": ENV["SKILL_VERSION"]},
        "pay_type": "SKILL_PAY",
        "pay_mode": "AUTH_AND_PAY",
        "pay_items": [{
            "product_id": "SP" + out_trade_no[-12:],
            "pay_data": {"type": "code_url", "value": code_url},
        }],
        "expires_at": expires,
    }
    payment_required = base64.b64encode(json.dumps(l2).encode()).decode()
    l1 = {
        "signature_type": "SKILLHUB-SHA256-RSA2048",
        "developer_platform": "SKILLHUB",
        "developer_id": ENV["SKILLHUB_DEVELOPER_ID"],
        "pub_key_id": ENV["SKILLHUB_PUB_KEY_ID"],
        "nonce_str": nonce,
        "timestamp": ts,
        "signature": "",
        "payment_required": payment_required,
    }
    sign_str = f"POST\n{PREORDER_PATH}\n{ts}\n{nonce}\n{payment_required}\n"
    l1["signature"] = _sign(_load_sh_key(), sign_str)
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    r = requests.post(PREORDER_URL, data=json.dumps(l1).encode(), headers=headers, timeout=20)
    r.raise_for_status()
    data = r.json()
    return data.get("payment_code") or json.dumps(l1)


# ---------------- 成人健康档案生成（真实业务逻辑）----------------

# 参考区间（公开医学知识）：low, high, unit；None 表示无该侧边界。
# 性别差异通过 _adult_range 覆盖。
_ADULT_REF = {
    "wbc": (3.5, 9.5, "10⁹/L"),
    "rbc": (3.5, 5.0, "10¹²/L"),
    "hgb": (130, 175, "g/L"),
    "plt": (125, 350, "10⁹/L"),
    "ne%": (40, 75, "%"),
    "ly%": (20, 50, "%"),
    "mo%": (3, 10, "%"),
    "eo%": (0.4, 8, "%"),
    "hs-crp": (0, 10, "mg/L"),
    "crp": (0, 10, "mg/L"),
    "pct": (0, 0.5, "ng/mL"),
    "esr": (0, 15, "mm/h"),
    "alt": (9, 50, "U/L"),
    "ast": (15, 40, "U/L"),
    "ggt": (10, 60, "U/L"),
    "alp": (38, 126, "U/L"),
    "tbil": (5, 21, "μmol/L"),
    "dbil": (0, 6.8, "μmol/L"),
    "alb": (40, 55, "g/L"),
    "tp": (65, 85, "g/L"),
    "bun": (2.9, 8.2, "mmol/L"),
    "cr": (44, 106, "μmol/L"),
    "ua": (208, 428, "μmol/L"),
    "egfr": (90, None, "mL/min/1.73m²"),
    "glu": (3.9, 6.1, "mmol/L"),
    "hba1c": (4.0, 6.0, "%"),
    "tc": (None, 5.2, "mmol/L"),
    "tg": (None, 1.7, "mmol/L"),
    "ldl-c": (None, 3.4, "mmol/L"),
    "hdl-c": (1.0, None, "mmol/L"),
    "na": (137, 147, "mmol/L"),
    "k": (3.5, 5.3, "mmol/L"),
    "cl": (99, 110, "mmol/L"),
    "ca": (2.11, 2.52, "mmol/L"),
    "ck": (24, 194, "U/L"),
    "ck-mb": (0, 5, "ng/mL"),
    "ctni": (0, 0.04, "ng/mL"),
    "bnp": (None, 100, "pg/mL"),
    "nt-probnp": (None, 125, "pg/mL"),
    "pt": (11, 14, "s"),
    "inr": (0.8, 1.2, ""),
    "d-dimer": (0, 0.5, "μg/mL"),
    "tsh": (0.27, 4.2, "mIU/L"),
    "ft3": (3.1, 6.8, "pmol/L"),
    "ft4": (12, 22, "pmol/L"),
    "cea": (0, 5, "ng/mL"),
    "cyfra21-1": (0, 3.3, "ng/mL"),
    "nse": (0, 16.3, "ng/mL"),
    "scc": (0, 1.5, "ng/mL"),
    "ca125": (0, 35, "U/mL"),
    "ca199": (0, 37, "U/mL"),
}

_ALIASES = {
    "白细胞": "wbc", "白血球": "wbc", "wbc": "wbc",
    "红细胞": "rbc", "rbc": "rbc",
    "血红蛋白": "hgb", "血色素": "hgb", "hgb": "hgb", "hb": "hgb",
    "血小板": "plt", "plt": "plt",
    "中性粒细胞": "ne%", "中性粒": "ne%", "ne%": "ne%", "ne": "ne%",
    "淋巴细胞": "ly%", "淋巴": "ly%", "ly%": "ly%", "ly": "ly%",
    "单核细胞": "mo%", "mo%": "mo%",
    "嗜酸粒细胞": "eo%", "eo%": "eo%",
    "超敏c反应蛋白": "hs-crp", "超敏c反应": "hs-crp", "hs-crp": "hs-crp",
    "c反应蛋白": "crp", "crp": "crp",
    "降钙素原": "pct", "pct": "pct",
    "血沉": "esr", "esr": "esr",
    "谷丙转氨酶": "alt", "丙氨酸氨基转移酶": "alt", "alt": "alt",
    "谷草转氨酶": "ast", "天门冬氨酸氨基转移酶": "ast", "ast": "ast",
    "谷氨酰转移酶": "ggt", "γ-谷氨酰转移酶": "ggt", "ggt": "ggt",
    "碱性磷酸酶": "alp", "alp": "alp",
    "总胆红素": "tbil", "tbil": "tbil",
    "直接胆红素": "dbil", "dbil": "dbil",
    "白蛋白": "alb", "alb": "alb",
    "总蛋白": "tp", "tp": "tp",
    "尿素氮": "bun", "bun": "bun",
    "肌酐": "cr", "血肌酐": "cr", "cr": "cr",
    "尿酸": "ua", "ua": "ua",
    "egfr": "egfr", "肾小球滤过率": "egfr",
    "空腹血糖": "glu", "血糖": "glu", "glu": "glu",
    "糖化血红蛋白": "hba1c", "hba1c": "hba1c",
    "总胆固醇": "tc", "胆固醇": "tc", "tc": "tc",
    "甘油三酯": "tg", "甘油三脂": "tg", "tg": "tg",
    "低密度脂蛋白": "ldl-c", "低密度": "ldl-c", "ldl": "ldl-c", "ldl-c": "ldl-c", "ldl_c": "ldl-c",
    "高密度脂蛋白": "hdl-c", "高密度": "hdl-c", "hdl": "hdl-c", "hdl-c": "hdl-c", "hdl_c": "hdl-c",
    "钠": "na", "na": "na",
    "钾": "k", "k": "k",
    "氯": "cl", "cl": "cl",
    "钙": "ca", "ca": "ca",
    "肌酸激酶": "ck", "ck": "ck",
    "肌酸激酶同工酶": "ck-mb", "ck-mb": "ck-mb",
    "肌钙蛋白": "ctni", "肌钙蛋白i": "ctni", "ctni": "ctni",
    "bnp": "bnp",
    "nt-probnp": "nt-probnp", "nt-probnp": "nt-probnp",
    "凝血酶原时间": "pt", "pt": "pt",
    "inr": "inr",
    "d-二聚体": "d-dimer", "d二聚体": "d-dimer", "d-dimer": "d-dimer",
    "促甲状腺激素": "tsh", "tsh": "tsh",
    "游离t3": "ft3", "ft3": "ft3",
    "游离t4": "ft4", "ft4": "ft4",
    "癌胚抗原": "cea", "cea": "cea",
    "细胞角蛋白19片段": "cyfra21-1", "cyfra21-1": "cyfra21-1",
    "神经元特异性烯醇化酶": "nse", "nse": "nse",
    "鳞状细胞癌抗原": "scc", "scc": "scc",
    "ca125": "ca125",
    "ca199": "ca199", "ca19-9": "ca199",
}

# 指标 -> 所属系统
_SYS = {
    "wbc": "血常规", "rbc": "血常规", "hgb": "血常规", "plt": "血常规",
    "ne%": "血常规", "ly%": "血常规", "mo%": "血常规", "eo%": "血常规",
    "hs-crp": "炎症/感染", "crp": "炎症/感染", "pct": "炎症/感染", "esr": "炎症/感染",
    "alt": "肝功能", "ast": "肝功能", "ggt": "肝功能", "alp": "肝功能",
    "tbil": "肝功能", "dbil": "肝功能", "alb": "肝功能", "tp": "肝功能",
    "bun": "肾功能", "cr": "肾功能", "ua": "肾功能", "egfr": "肾功能",
    "glu": "血糖/血脂", "hba1c": "血糖/血脂", "tc": "血糖/血脂", "tg": "血糖/血脂",
    "ldl-c": "血糖/血脂", "hdl-c": "血糖/血脂",
    "na": "电解质", "k": "电解质", "cl": "电解质", "ca": "电解质",
    "ck": "心肌标志物", "ck-mb": "心肌标志物", "ctni": "心肌标志物",
    "bnp": "心肌标志物", "nt-probnp": "心肌标志物",
    "pt": "凝血", "inr": "凝血", "d-dimer": "凝血",
    "tsh": "甲状腺", "ft3": "甲状腺", "ft4": "甲状腺",
    "cea": "肿瘤标志物", "cyfra21-1": "肿瘤标志物", "nse": "肿瘤标志物",
    "scc": "肿瘤标志物", "ca125": "肿瘤标志物", "ca199": "肿瘤标志物",
}

# 数值越高越差（用于趋势"恶化/改善"判定）；其余默认为越高越差
_HIGHER_BETTER = {"hdl-c", "egfr"}


def _sex_key(gender):
    g = (gender or "").lower()
    if g in ("m", "男", "boy", "男性"):
        return "boy"
    return "girl"


def _norm_key(name):
    if not name:
        return None
    n = name.strip().lower().replace(" ", "")
    if n in _ALIASES:
        return _ALIASES[n]
    # 去掉常见前缀/单位后再试
    n2 = re.sub(r"[\(（].*?[\)）]", "", n)
    return _ALIASES.get(n2)


def _adult_range(key, sex):
    if key not in _ADULT_REF:
        return None
    low, high, unit = _ADULT_REF[key]
    s = _sex_key(sex)
    if key == "hgb":
        return (130, 175, unit) if s == "boy" else (115, 150, unit)
    if key == "alt":
        return (9, 50, unit) if s == "boy" else (7, 40, unit)
    if key == "ast":
        return (15, 40, unit) if s == "boy" else (13, 35, unit)
    if key == "cr":
        return (44, 106, unit) if s == "boy" else (44, 97, unit)
    if key == "esr":
        return (0, 15, unit) if s == "boy" else (0, 20, unit)
    if key == "rbc":
        return (3.5, 5.0, unit) if s == "boy" else (3.8, 5.1, unit)
    return (low, high, unit)


def _to_float(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    m = re.search(r"-?\d+\.?\d*", str(v))
    return float(m.group()) if m else None


def _flag(key, value, sex):
    r = _adult_range(key, sex)
    if not r:
        return "—", "未收录"
    low, high, unit = r
    if value is None:
        return "—", "未提供"
    bad_high = high is not None and value > high
    bad_low = low is not None and value < low
    if bad_high and bad_low:
        return "—", "异常"
    if bad_high:
        return "↑", "偏高 ⚠️"
    if bad_low:
        return "↓", "偏低 ⚠️"
    return "✓", "正常"


def _parse_values(report):
    """从 report 的 values（dict）或 text（字符串）抽取 {key: float}。"""
    out = {}
    if isinstance(report, dict):
        vals = report.get("values")
        if isinstance(vals, dict):
            for k, v in vals.items():
                key = _norm_key(k)
                if key:
                    fv = _to_float(v)
                    if fv is not None:
                        out[key] = fv
        text = report.get("text")
    else:
        text = report
    if isinstance(text, str) and text.strip():
        for alias in _ALIASES:
            # 中文别名 / 英文别名，后跟可选冒号与数值
            for pat in (re.escape(alias) + r"\s*[:：]?\s*([0-9]+\.?[0-9]*)",):
                m = re.search(pat, text)
                if m:
                    key = _ALIASES[alias]
                    if key not in out:
                        out[key] = float(m.group(1))
    return out


def build_adult_record(data: dict) -> str:
    """依据 profile + reports 生成结构化成人健康档案（Markdown）。"""
    profile = data.get("profile") or {}
    reports = data.get("reports") or []
    query = (data.get("query") or "").strip()
    name = profile.get("name") or "用户"
    gender = profile.get("gender") or "男"
    birth = profile.get("birth_date") or ""
    h = _to_float(profile.get("height_cm"))
    w = _to_float(profile.get("weight_kg"))
    today = _dt.date.today().isoformat()

    sex = _sex_key(gender)
    bmi = None
    bmi_flag = "—"
    if h and w and h > 0:
        bmi = w / ((h / 100) ** 2)
        if bmi < 18.5:
            bmi_flag = "偏瘦 ↓"
        elif bmi <= 24:
            bmi_flag = "正常 ✓"
        elif bmi <= 28:
            bmi_flag = "超重 ↑"
        else:
            bmi_flag = "肥胖 ⚠️"

    # 按日期排序报告
    def _sort_key(r):
        d = (r.get("date") if isinstance(r, dict) else "") or ""
        return d
    reports = sorted(reports, key=_sort_key)
    parsed = []  # (date, type, {key: val})
    for r in reports:
        if not isinstance(r, dict):
            continue
        parsed.append((r.get("date", ""), r.get("type", "体检"), _parse_values(r)))

    L = []
    L.append(f"# 成人健康档案与趋势分析：{name}")
    L.append("")
    L.append("> 由「成人健康档案与趋势分析」付费服务依据你提供的数据自动生成")
    L.append("")
    L.append("## 一、基本信息")
    L.append(f"- 姓名：{name}")
    L.append(f"- 性别：{gender}")
    L.append(f"- 出生日期：{birth or '（未提供）'}")
    L.append(f"- 身高：{h if h else '—'} cm｜体重：{w if w else '—'} kg｜BMI：{('%.1f' % bmi) if bmi else '—'}（{bmi_flag}）")
    L.append(f"- 建档日期：{today}")
    L.append(f"- 报告覆盖时间点：{len(parsed)} 个（{parsed[0][0] if parsed else '—'} ～ {parsed[-1][0] if parsed else '—'}）")
    L.append("")

    # 二、各系统指标与异常标注
    L.append("## 二、各系统指标与异常标注")
    if not parsed:
        L.append("- 尚未提供任何报告数据。请在 `reports` 中提供至少一个时间点的 `values`（如 `{\"date\":\"2024-07-20\",\"values\":{\"TC\":6.1,\"LDL-C\":4.2,\"ALT\":36}}`）以生成档案。")
    else:
        # 系统顺序
        sys_order = ["血常规", "炎症/感染", "肝功能", "肾功能", "血糖/血脂",
                     "电解质", "心肌标志物", "凝血", "甲状腺", "肿瘤标志物"]
        seen_sys = []
        for p in parsed:
            for k in p[2]:
                s = _SYS.get(k)
                if s and s not in seen_sys:
                    seen_sys.append(s)
        sys_order = [s for s in sys_order if s in seen_sys] + [s for s in seen_sys if s not in sys_order]
        for sysname in sys_order:
            L.append(f"### {sysname}")
            for (date, rtype, vals) in parsed:
                keys = [k for k in vals if _SYS.get(k) == sysname]
                if not keys:
                    continue
                L.append(f"**{date}（{rtype}）**")
                L.append("| 指标 | 结果 | 单位 | 参考范围 | 判定 |")
                L.append("|---|---|---|---|---|")
                for k in keys:
                    v = vals[k]
                    low, high, unit = _adult_range(k, sex) or (None, None, "")
                    rng = f"{low if low is not None else '—'}–{high if high is not None else '—'}"
                    arrow, verdict = _flag(k, v, sex)
                    L.append(f"| {k.upper()} | {v} | {unit} | {rng} | {arrow} {verdict} |")
                L.append("")
    L.append("")

    # 三、异常项汇总
    L.append("## 三、异常项汇总")
    abnorm = []
    for (date, rtype, vals) in parsed:
        for k, v in vals.items():
            arrow, verdict = _flag(k, v, sex)
            if "⚠️" in verdict or verdict == "异常":
                abnorm.append((date, k.upper(), v, verdict))
    if not abnorm:
        L.append("- 本次所有已识别指标均在参考范围内。")
    else:
        L.append("| 时间 | 指标 | 结果 | 判定 |")
        L.append("|---|---|---|---|")
        for date, k, v, verdict in abnorm:
            L.append(f"| {date} | {k} | {v} | {verdict} |")
    L.append("")

    # 四、跨年度趋势分析
    L.append("## 四、跨年度趋势分析")
    trend = {}  # key -> [(date, value)]
    for (date, rtype, vals) in parsed:
        for k, v in vals.items():
            trend.setdefault(k, []).append((date, v))
    multi = {k: v for k, v in trend.items() if len(v) >= 2}
    if not multi:
        L.append("- 当前仅 1 个时间点，暂无法做趋势对比。补充更早/更晚的报告即可自动生成跨年度趋势。")
    else:
        L.append("| 指标 | " + " | ".join(d for d, _ in next(iter(multi.values()))) +
                 " | 趋势 |")
        L.append("|---" * (len(next(iter(multi.values()))) + 2) + "|")
        for k, series in multi.items():
            first_v = series[0][1]
            last_v = series[-1][1]
            delta = last_v - first_v
            higher_worse = k not in _HIGHER_BETTER
            if abs(delta) < 1e-9:
                trend_txt = "→ 平稳"
            elif delta > 0:
                trend_txt = "↑ 升高" + (" ⚠️" if higher_worse else " ✓改善")
            else:
                trend_txt = "↓ 下降" + (" ✓改善" if higher_worse else " ⚠️")
            L.append(f"| {k.upper()} | " + " | ".join(str(v) for _, v in series) +
                     f" | {trend_txt} |")
        L.append("")
        L.append("> 趋势判定：对多数指标「升高=恶化、下降=改善」；HDL-C、eGFR 相反。仅基于你提供的数据，不替代医生判断。")
    L.append("")

    # 五、保健建议（通用，基于异常项）
    L.append("## 五、保健建议（通用）")
    sugg = set()
    abkeys = {k for _, k, _, _ in abnorm}  # 大写键，如 LDL-C / GGT
    if any(x in abkeys for x in ("LDL-C", "TC", "TG")):
        sugg.add("- 血脂异常：低脂饮食、规律有氧运动，心血管内科评估是否需要他汀类干预。")
    if any(x in abkeys for x in ("GGT", "ALT", "AST")):
        sugg.add("- 肝酶异常：排查脂肪肝/饮酒/药物因素，复查肝功能与肝胆超声。")
    if "HGB" in abkeys:
        sugg.add("- 血红蛋白异常：结合铁代谢等进一步评估贫血或红细胞增多。")
    if any(x in abkeys for x in ("GLU", "HBA1C")):
        sugg.add("- 血糖异常：内分泌科评估糖代谢状态，必要时 OGTT。")
    if bmi and bmi > 24:
        sugg.add(f"- 体重管理：当前 BMI {bmi:.1f}（{bmi_flag}），建议控制体重。")
    if not sugg:
        sugg.add("- 目前指标总体平稳，保持规律体检（建议每年 1 次）与健康生活方式。")
    for s in sugg:
        L.append(s)
    L.append("")
    L.append("---")
    L.append("**免责声明**：本档案由 AI 依据你提供的数据自动生成，参考区间为通用成人范围（不同实验室略有差异，以报告单为准），"
             "仅供健康记录与趋势参考，**不能替代医生的专业评估与诊断**。异常指标请遵医嘱复查。")
    return "\n".join(L)


def execute_business(data: dict) -> str:
    """付费校验通过后的返回内容。

    依据 v7 SKILL.md：健康资料仅在用户本地（Agent）处理，付费端点仅做
    X402 计费校验、不接收也不消费健康资料。因此付费成功后返回的是
    「已解锁」确认，真正的档案由 Agent 在本地生成并交付。
    """
    # 兼容性：若请求体误带健康资料（旧式调用），仍可在服务端生成档案。
    if data.get("profile") or data.get("reports"):
        return build_adult_record(data)
    skill = data.get("skill") or "personal-health-archive-trend"
    return (
        "✅ 已解锁 Personal Health Archive Trend（成人健康档案趋势分析）。\n\n"
        "本次付费校验已完成。请在本机（Agent）根据您主动提供的体检/住院报告，"
        "按本地工作流生成结构化健康档案（主档、异常标注、跨年度趋势对比）。\n"
        "您的健康资料全程仅在本地处理，未上传至任何外部服务器。\n"
        f"（skill={skill}）"
    )


# ---------------- HTTP 处理 ----------------
class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body_obj=None, headers=None):
        payload = json.dumps(body_obj).encode("utf-8") if body_obj is not None else b""
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        if payload:
            self.wfile.write(payload)

    def do_GET(self):
        if urlparse(self.path).path == "/health":
            body = b"ok"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        self._send(404, {"error": "not found"})

    def _handle_wx_notify(self, path, raw):
        if MOCK:
            self._send(200, {"code": "SUCCESS", "message": "成功"})
            return
        try:
            dec = _process_wx_notify(raw, self.headers)
        except Exception as e:
            print(f"[notify] ❌ 验签/解密失败（{path}）：{e}")
            self._send(500, {"code": "FAIL", "message": "verify or decrypt failed"})
            return
        otn = dec.get("out_trade_no") or dec.get("out_refund_no") or ""
        state = dec.get("trade_state") or dec.get("refund_status") or ""
        with _lock:
            rec = _orders.setdefault(otn, {"paid": False, "content": None})
            if state in ("SUCCESS", "REFUND_SUCCESS"):
                rec["paid"] = True
            rec["wx_notify"] = dec
        print(f"[notify] ✅ {path} out_trade_no={otn} state={state} 已确认收讫")
        self._send(200, {"code": "SUCCESS", "message": "成功"})

    def do_POST(self):
        path = urlparse(self.path).path
        length = int(self.headers.get("Content-Length", 0) or 0)
        raw = self.rfile.read(length) if length else b"{}"
        try:
            data = json.loads(raw or b"{}")
        except Exception:
            data = {}
        query = (data.get("query") or "").strip() or "成人健康档案"

        if path in ("/api/pay/notify", "/api/refund/notify",
                    "/api/adult/pay/notify", "/api/adult/refund/notify"):
            self._handle_wx_notify(path, raw)
            return
        if path not in ("/api/resource", "/api/adult/resource"):
            self._send(404, {"error": "not found"})
            return

        out_trade_no = self.headers.get("X-Out-Trade-No", "")

        # —— 重试：支付后查单履约 ——
        if out_trade_no:
            if MOCK:
                paid = True
            else:
                try:
                    paid = _wx_query_order(out_trade_no) == "SUCCESS"
                except Exception as e:
                    self._send(402, {"code": "NOT_PAID", "message": f"查单失败: {e}"})
                    return
            if not paid:
                self._send(402, {"code": "NOT_PAID", "message": "订单未支付"})
                return
            with _lock:
                rec = _orders.get(out_trade_no, {})
                content = rec.get("content") or execute_business(data)
            self._send(200, {"code": "SUCCESS", "content": content})
            return

        # —— 首次：下单 + 预下单，返回 402 ——
        out_trade_no = "WX402_" + str(int(time.time()))[-14:] + secrets.token_hex(6)
        amount_fen = 599  # 与付费版 SKILL.md 的 pricing.amount_fen 一致（5.99 元/次）
        description = "成人健康档案与趋势分析"
        if MOCK:
            code_url = "weixin://wxpay/mock/bizpayurl"
            payment_code = json.dumps({"mock": True, "out_trade_no": out_trade_no})
        else:
            try:
                code_url = _wx_native_order(description, out_trade_no, amount_fen)
                payment_code = _sh_preorder(code_url, out_trade_no)
            except Exception as e:
                self._send(500, {"code": "FULFILL_AND_REFUND_FAILED",
                                 "message": f"预下单失败: {e}"})
                return
        with _lock:
            _orders[out_trade_no] = {"paid": False, "content": execute_business(data)}
        body = {
            "code": "PAYMENT_REQUIRED",
            "message": "需要支付后才能获取内容",
            "WeixinPay": {
                "WeixinPay-Required": payment_code,
                "prompt": "本次使用微信支付，请将 WeixinPay-Required 的值作为 paymentCode 交给 weixinpay_pay，以向用户申请支付授权。",
            },
            "out_trade_no": out_trade_no,
            "amount": f"{amount_fen/100:.2f}",
            "currency": "CNY",
            "description": f"AI付费查询: {description}",
        }
        headers = {
            "WeixinPay-Required": payment_code,
            "X-Out-Trade-No": out_trade_no,
        }
        self._send(402, body, headers)

    def log_message(self, *args):
        pass


def main():
    port = int(ENV["PORT"] or "8080")
    print(f"成人健康档案 X402 商户 Demo 启动，监听端口: {port}  [MOCK={'是' if MOCK else '否'}]")
    if MOCK:
        print("⚠️ MOCK 模式：未配置微信/SkillHub 密钥，跳过真实预下单，仅用于本地结构联调。")
    else:
        try:
            _load_wx_pub_key()
            if _wx_certs:
                print(f"✅ 已加载 {len(_wx_certs)} 个回调验签公钥（微信支付公钥模式）")
        except Exception as e:
            print(f"⚠️ 微信支付公钥加载失败：{e}")
        try:
            _wx_get_certs()
            print(f"✅ 已额外加载 {len(_wx_certs)} 张微信支付平台证书，可用于回调验签")
        except Exception as e:
            print(f"ℹ️ 平台证书预拉取不可用（公钥模式常见，已忽略）：{e}")
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()


if __name__ == "__main__":
    main()
