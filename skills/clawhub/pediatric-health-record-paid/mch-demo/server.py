#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mch-demo (Python 版) — 微信 Agent Pay / X402 协议商户服务端

实现 SkillHub「payskill帮助」要求的付费 skill 服务端：
  POST /api/resource   首次请求返回 402(要求支付)；支付后带 X-Out-Trade-No 重试返回付费内容
  POST /api/pay/notify   微信支付结果回调（可选）
  POST /api/refund/notify 退款结果回调（可选）
  GET  /health          健康检查

依赖：requests, cryptography  （pip install -r requirements.txt）

配置：复制 .env.example 为 .env 并填好；或导出同名环境变量。
     设 MOCK=1（或缺失微信/ SkillHub 密钥）时进入本地 mock 模式：
       跳过真实微信/SkillHub 调用，直接返回演示 payment_code，
       且查单立即返回 SUCCESS —— 用于先跑通 402→重试→200 结构。

真实模式需要：
  微信支付：MCH_ID APP_ID SERIAL_NO PRIVATE_KEY_PATH MCH_APIV3_KEY
  SkillHub：SKILLHUB_DEVELOPER_ID SKILLHUB_PUB_KEY_ID SKILLHUB_PRIVATE_KEY
            SKILL_ID SKILL_VERSION
  回调：    PAY_NOTIFY_URL REFUND_NOTIFY_URL（公网 https）
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

import requests
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.x509 import load_pem_x509_certificate


def _load_dotenv(path=".env"):
    """健壮加载 .env，支持无引号多行 PEM 私钥（如 SkillHub 私钥）。
    原生 python-dotenv 对无引号多行值解析失败，这里手动处理：
    遇到 KEY= 且值以 -----BEGIN 开头、不含 -----END 时进入多行收集，
    直到遇到含 -----END 的行结束。"""
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
    """加载 SkillHub 开发者私钥。

    优先从文件读取（容器部署时通过挂载注入，避免把多行 PEM 写进 .env
    导致 docker compose 的 go-dotenv 解析失败）；文件不存在时回退到
    环境变量 SKILLHUB_PRIVATE_KEY（本地直跑可用，自定义 _load_dotenv 支持多行）。
    """
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
    """调微信 Native 下单，返回 code_url。"""
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
    """查单，返回 trade_state。

    关键点：微信支付 v3「查询订单」接口要求 mchid 作为**查询参数** (?mchid=)，
    且签名串的 canonical URI 必须包含该查询串（与 POST 下单不同）。
    仅把 mchid 放 Authorization 头里 → 400 PARAM_ERROR 商户号格式错误；
    拼了 ?mchid 但签名没覆盖查询串 → 401 签名错误。两者都修好才通。
    """
    path = f"/v3/pay/transactions/out-trade-no/{out_trade_no}?mchid={ENV['MCH_ID']}"
    headers = {
        "Authorization": _wx_authorization("GET", path, ""),
        "Accept": "application/json",
    }
    r = requests.get(WX_BASE + path, headers=headers, timeout=20)
    r.raise_for_status()
    return r.json().get("trade_state", "")


# ---------------- 微信支付回调：验签 + 解密 ----------------
# 回调验签需要用「微信支付平台证书」公钥（而非商户自己的私钥）。
# 平台证书通过 /v3/certificates 拉取（响应本身用 APIv3 密钥加密），按 serial_no 缓存。
_wx_certs = {}  # serial_no -> cryptography 公钥对象
_wx_certs_lock = threading.Lock()


def _aead_decrypt(ciphertext_b64: str, nonce: str, associated_data: str, key_str: str) -> bytes:
    """AEAD_AES_256_GCM 解密（微信支付 v3 回调 / 证书下载均用此算法）。"""
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
    """拉取并缓存微信支付平台证书（用于回调验签）。"""
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
    """微信支付公钥模式：从商户平台下载的「微信支付公钥」(PEM) + 公钥ID 加载，
    并登记到 _wx_certs（与平台证书共用查找表）。公钥ID 即回调头里的 Wechatpay-Serial。
    公钥文件可能是裸公钥(PKCS#8)或 X.509 证书，两者都支持。"""
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
    """用平台证书公钥验签：明文 = timestamp\\nnonce\\nbody\\n。失败抛 InvalidSignature。"""
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
    """验签 + 解密微信支付回调，返回解密后的业务 JSON（dict）。
    任何一步失败都会抛异常，调用方据此拒绝确认。"""
    ts = headers.get("Wechatpay-Timestamp", "")
    nonce = headers.get("Wechatpay-Nonce", "")
    serial = headers.get("Wechatpay-Serial", "")
    sig = headers.get("Wechatpay-Signature", "")
    if not (ts and nonce and serial and sig):
        raise RuntimeError("回调缺少验签头（Wechatpay-Timestamp/Nonce/Serial/Signature）")
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
    """调 SkillHub AI 预下单，返回 payment_code（L1 信封 JSON 字符串）。"""
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
    # 优先取接口返回的 payment_code；否则用本机生成的 L1 信封
    return data.get("payment_code") or json.dumps(l1)


# ---------------- 儿童健康档案生成（真实业务逻辑）----------------

# 国家免疫规划 0–3 岁疫苗：名称 -> 推荐接种月龄列表
_NATIONAL_SCHEDULE = {
    "卡介苗(BCG)": [0],
    "乙肝疫苗(HepB)": [0, 1, 6],
    "脊灰疫苗(IPV/OPV)": [2, 3, 4],
    "百白破(DTP)": [3, 4, 5, 18],
    "麻腮风(MMR)": [8, 18],
    "乙脑减毒(JE)": [8, 24],
    "A群流脑(MPSV-A)": [6, 9],
    "甲肝(HepA)": [18],
}
# 常见非规划（自费）疫苗
_EXTRA_SCHEDULE = {
    "13价肺炎(PCV13)": [2, 4, 6, 12],
    "轮状病毒(RV)": [2, 4, 6],
    "Hib": [2, 4, 6, 18],
    "流感(Influenza)": ["每年"],
    "手足口(EV71)": [6, 7],
    "水痘(Varicella)": [12, 48],
}

# WHO 2006 儿童生长标准近似参考（月龄 -> 中位数 M / 变异系数 S）
_WHO_AGES = [0, 1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 24, 30, 36]
_WHO = {
    "M": {
        "weight": {"boy":  [3.3,4.5,5.6,6.4,7.0,7.5,7.9,8.6,9.2,9.6,10.3,10.9,12.2,13.3,14.3],
                   "girl": [3.2,4.2,5.1,5.8,6.4,6.9,7.3,7.9,8.5,8.9,9.6,10.2,11.5,12.6,13.6]},
        "height": {"boy":  [49.9,54.7,58.4,61.4,63.9,65.9,67.6,70.6,73.3,75.7,79.7,82.3,87.1,91.7,96.1],
                   "girl": [49.1,53.7,57.1,59.8,62.1,64.0,65.7,68.5,71.1,73.4,77.2,79.8,84.5,88.9,93.4]},
        "hc":     {"boy":  [34.5,37.6,39.6,41.0,42.1,43.0,43.7,45.0,45.9,46.5,47.3,47.8,48.3,48.9,49.4],
                   "girl": [33.9,36.8,38.6,39.9,41.0,41.9,42.6,43.8,44.7,45.3,46.1,46.6,47.1,47.7,48.2]},
    },
    "S": {
        "weight": {"boy":  [0.38,0.50,0.56,0.60,0.64,0.67,0.69,0.74,0.79,0.84,0.91,0.98,1.12,1.26,1.39],
                   "girl": [0.36,0.46,0.52,0.55,0.59,0.62,0.64,0.69,0.74,0.79,0.85,0.92,1.05,1.18,1.29]},
        "height": {"boy":  [1.89,2.26,2.42,2.50,2.55,2.59,2.62,2.66,2.70,2.74,2.80,2.85,2.93,3.01,3.09],
                   "girl": [1.86,2.14,2.29,2.36,2.40,2.44,2.47,2.51,2.55,2.60,2.66,2.70,2.78,2.86,2.94]},
        "hc":     {"boy":  [1.24,1.26,1.26,1.25,1.24,1.23,1.22,1.20,1.19,1.18,1.17,1.16,1.15,1.14,1.13],
                   "girl": [1.18,1.20,1.20,1.19,1.18,1.17,1.16,1.15,1.14,1.13,1.12,1.11,1.10,1.09,1.08]},
    },
}


def _norm_cdf(z: float) -> float:
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def _who_pct(sex, metric, age_months, value):
    """返回 (z, pct, label)。age_months 可小数，对 M/S 线性插值。"""
    if value is None or value <= 0:
        return None, None, "未提供"
    ages, Ms, Ss = _WHO_AGES, _WHO["M"][metric][sex], _WHO["S"][metric][sex]
    if age_months <= ages[0]:
        i, t = 0, 0.0
    elif age_months >= ages[-1]:
        i, t = len(ages) - 2, 1.0
    else:
        for i in range(len(ages) - 1):
            if ages[i] <= age_months <= ages[i + 1]:
                t = (age_months - ages[i]) / (ages[i + 1] - ages[i])
                break
        else:
            i, t = 0, 0.0
    M = Ms[i] + (Ms[i + 1] - Ms[i]) * t
    S = Ss[i] + (Ss[i + 1] - Ss[i]) * t
    z = (value - M) / S
    pct = _norm_cdf(z) * 100
    if z < -2:
        label = "偏低 ⚠️"
    elif z < -1:
        label = "偏下"
    elif z <= 1:
        label = "正常(中等)"
    elif z <= 2:
        label = "偏上"
    else:
        label = "偏高 ⚠️"
    return round(z, 2), round(pct, 1), label


def _age_info(birth: str):
    """返回 (total_months_float, years, months, display)。"""
    try:
        b = _dt.datetime.strptime(birth, "%Y-%m-%d").date()
    except Exception:
        return None, None, None, "出生日期格式有误"
    today = _dt.date.today()
    months = (today.year - b.year) * 12 + (today.month - b.month) + (today.day - b.day) / 30.44
    y = int(months // 12)
    m = int(round(months - y * 12))
    if m == 12:
        y, m = y + 1, 0
    disp = f"{y}岁{m}月" if y > 0 else f"{m}月龄"
    return months, y, m, disp


def _sex_key(gender):
    g = (gender or "").lower()
    if g in ("m", "男", "男孩", "boy"):
        return "boy"
    return "girl"


def _milestones(age_months):
    items = [
        (1, "俯卧可短暂抬头"),
        (3, "俯卧抬头 45°、开始翻身"),
        (6, "独坐片刻、认人、抓握积木"),
        (8, "独坐稳、腹部贴地爬行"),
        (12, "扶站/独走几步、无意识叫爸妈"),
        (18, "独走稳、说单字、指认身体部位"),
        (24, "跑、说 2 字短语、模仿家务"),
        (36, "双脚跳、说短句、能数数/辨色"),
    ]
    out = [f"- ✓ {mo}月：{desc}" for mo, desc in items
           if age_months is not None and age_months >= mo]
    return "\n".join(out) if out else "- 暂无该年龄段里程碑记录（请在 child 中提供出生日期）"


def _feeding_guide(age_months):
    if age_months is None:
        return "请提供出生日期以获得月龄喂养建议。"
    if age_months < 6:
        return "0–6月：纯母乳或配方奶喂养，按需哺乳；生后数天起补充维生素 D 400 IU/日。"
    if age_months < 12:
        return "6–12月：添加辅食（铁强化米粉→肉泥菜泥果泥），继续母乳；质地由泥糊过渡到碎末；禁蜂蜜、整粒坚果。"
    if age_months < 24:
        return "12–24月：三餐三点，食物多样化，学习自主进食；每日奶量约 400–500 ml；少盐少糖。"
    return "24–36月：家庭均衡膳食，规律三餐，培养自主进食与口腔卫生习惯。"


def _vaccine_checklist(provided, age_months, schedule):
    provided_names = {(v.get("name") or "").replace(" ", "") for v in (provided or [])}
    lines = []
    for name, months in schedule.items():
        short = name.split("(")[0]
        due = [mo for mo in months if isinstance(mo, int)
               and (age_months is None or mo <= (age_months or 0))]
        if not due:
            continue
        got = any(short in pn or name.split("(")[0] in pn for pn in provided_names)
        if age_months is not None and max(due) <= (age_months or 0):
            status = "✅ 已种" if got else "⏳ 待种"
        else:
            status = "✅ 已种" if got else "🔜 未到"
        lines.append(f"- {name}（推荐 {', '.join(map(str, months))} 月）：{status}")
    return "\n".join(lines) if lines else "- 无"


def build_record(data: dict) -> str:
    """依据 child 数据生成结构化儿科健康档案（Markdown）。"""
    child = data.get("child") or {}
    query = (data.get("query") or "").strip()
    name = child.get("name") or "宝宝"
    gender = child.get("gender") or "男"
    birth = child.get("birth_date") or ""
    today = _dt.date.today().isoformat()
    age_months, y, m, age_disp = _age_info(birth)

    L = []
    L.append(f"# 儿科健康档案：{name}")
    L.append("")
    L.append("> 由「儿科健康档案建立器」依据你提供的数据自动生成")
    L.append("")
    L.append("## 一、基本信息")
    L.append(f"- 姓名：{name}")
    L.append(f"- 性别：{gender}")
    L.append(f"- 出生日期：{birth or '（未提供）'}")
    L.append(f"- 当前年龄：{age_disp}")
    L.append(f"- 建档日期：{today}")
    L.append("")

    L.append("## 二、生长发育评估（WHO 2006 参考）")
    growth = child.get("growth") or []
    if growth:
        L.append("| 测量月龄 | 体重(kg) | 体重百分位 | 身长/身高(cm) | 身高百分位 | 头围(cm) | 头围百分位 |")
        L.append("|---|---|---|---|---|---|---|")
        for g in growth:
            am = g.get("age_months")
            if am is None and g.get("date") and birth:
                try:
                    d = _dt.datetime.strptime(g["date"], "%Y-%m-%d").date()
                    b = _dt.datetime.strptime(birth, "%Y-%m-%d").date()
                    am = (d.year - b.year) * 12 + (d.month - b.month) + (d.day - b.day) / 30.44
                except Exception:
                    am = None
            sex = _sex_key(gender)
            w, h, hc = g.get("weight_kg"), g.get("height_cm"), g.get("head_cm")
            wz, wp, wl = _who_pct(sex, "weight", am, w)
            hz, hp, hl = _who_pct(sex, "height", am, h)
            cz, cp, cl = _who_pct(sex, "hc", am, hc)
            L.append(
                f"| {('%.1f' % am) if am is not None else '?'} "
                f"| {w if w else '—'} | {('P%.0f %s' % (wp, wl)) if wp is not None else '—'} "
                f"| {h if h else '—'} | {('P%.0f %s' % (hp, hl)) if hp is not None else '—'} "
                f"| {hc if hc else '—'} | {('P%.0f %s' % (cp, cl)) if cp is not None else '—'} |"
            )
        L.append("")
        L.append("> 百分位说明：P50 约为中位数；P3–P97 为正常区间；超出建议儿保科评估。")
    else:
        L.append("- 尚未提供生长测量数据。请在 `child.growth` 中提供至少一次体重/身长，例如 "
                 "`{\"age_months\":6,\"weight_kg\":7.9,\"height_cm\":67.6,\"head_cm\":43.7}` 以生成生长曲线评估。")
    L.append("")

    L.append("## 三、疫苗接种记录")
    provided = child.get("vaccines") or []
    if provided:
        L.append("**已记录接种：**")
        for v in provided:
            L.append(f"- {v.get('name')}｜{v.get('date') or '日期未填'}｜{v.get('dose') or ''}")
        L.append("")
    L.append("**国家免疫规划（0–3 岁）核对：**")
    L.append(_vaccine_checklist(provided, age_months, _NATIONAL_SCHEDULE))
    L.append("")
    L.append("**常见非规划（自费）核对：**")
    L.append(_vaccine_checklist(provided, age_months, _EXTRA_SCHEDULE))
    L.append("")

    L.append("## 四、喂养与营养")
    L.append(_feeding_guide(age_months))
    fn = child.get("feeding")
    if fn:
        L.append(f"\n备注：{fn}")
    L.append("")

    L.append("## 五、发育筛查（年龄相关里程碑）")
    L.append(_milestones(age_months))
    sn = child.get("screening")
    if sn:
        L.append(f"\n备注：{sn}")
    L.append("")

    L.append("## 六、既往史 / 过敏 / 注意事项")
    L.append(f"- 过敏史：{child.get('allergy') or '无记录'}")
    L.append(f"- 既往疾病：{child.get('illness') or '无记录'}")
    L.append(f"- 其他备注：{child.get('notes') or (query if query else '无')}")
    L.append("")

    L.append("## 七、保健建议（通用）")
    L.append("- 定期儿童保健体检：1 岁内每 3 月一次，1–3 岁每半年一次。")
    L.append("- 坚持维生素 D 补充至 2–3 岁；保证户外活动。")
    L.append("- 生长曲线持续偏离 P3/P97 或里程碑明显落后，请及时儿保/专科就诊。")
    L.append("")
    L.append("---")
    L.append("**免责声明**：本档案由 AI 依据你提供的数据自动生成，生长曲线基于 WHO 2006 参考中位数近似计算，"
             "仅供健康记录参考，**不能替代儿科医生的专业评估与诊断**。")
    return "\n".join(L)


def execute_business(data: dict) -> str:
    """真实业务：依据 child 数据生成结构化儿科健康档案（Markdown）。"""
    return build_record(data)


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
        """微信支付结果回调：验签 + 解密，仅成功时确认（200）。
        MOCK 模式跳过验签（演示用）。验证失败一律不确认，返回 500 让微信重试，
        伪造回调无法拿到任何确认。"""
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
        query = (data.get("query") or "").strip() or "为宝宝建立健康档案"

        if path == "/api/pay/notify" or path == "/api/refund/notify":
            self._handle_wx_notify(path, raw)
            return
        if path != "/api/resource":
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
        amount_fen = 299  # 与 SKILL.md 的 pricing.amount_fen 一致（2.99 元/次）
        description = "儿科健康档案建立器"
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
    print(f"微信 Agent Pay 商户 Demo 启动，监听端口: {port}  [MOCK={'是' if MOCK else '否'}]")
    if MOCK:
        print("⚠️ MOCK 模式：未配置微信/SkillHub 密钥，跳过真实预下单，仅用于本地结构联调。")
    else:
        # 公钥模式：加载商户平台下载的「微信支付公钥」(优先)
        try:
            _load_wx_pub_key()
            if _wx_certs:
                print(f"✅ 已加载 {len(_wx_certs)} 个回调验签公钥（微信支付公钥模式）")
        except Exception as e:
            print(f"⚠️ 微信支付公钥加载失败：{e}")
        # 兼容：尝试预拉平台证书（公钥模式下会 404，属正常，仅作兜底）
        try:
            _wx_get_certs()
            print(f"✅ 已额外加载 {len(_wx_certs)} 张微信支付平台证书，可用于回调验签")
        except Exception as e:
            print(f"ℹ️ 平台证书预拉取不可用（公钥模式常见，已忽略）：{e}")
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()


if __name__ == "__main__":
    main()
