#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
redact.py - 素材净化模块。

会话原始记录里可能夹带 API key、token、手机号、邮箱、本机路径。
本模块在会话文本离开原始记录、写入 transcript.md 之前，把这些内容替换为占位符，
使下游的文章与卡片数据不含可识别的凭据或隐私信息。

设计原则：
1. 只做替换，不联网、不落盘、不记录原始值。
2. 规则保守：宁可漏掉长串编号，也不要把正文数字改成占位符。
3. 每次替换返回计数，便于调用方在日志里说明「净化了多少处」。

用法（本模块只作为库被 extract_session.py 调用，没有命令行入口、
不接受任何文件路径参数，因此不存在独立的文件读取面）：
    scrub(text)                      -> (净化后文本, 替换计数)
    scrub(text, redact_paths=False)  -> 保留本机路径原文
"""

import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

# 凭据类：常见云厂商与服务商的密钥格式
CREDENTIAL_PATTERNS = (
    ("openai_like_key", re.compile(r"\b(?:sk|rk|pk)-[A-Za-z0-9_\-]{16,}\b")),
    ("github_token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),
    ("aws_access_key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("aliyun_access_key", re.compile(r"\bLTAI[0-9A-Za-z]{12,}\b")),
    ("jwt", re.compile(r"\beyJ[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{8,}\b")),
    ("private_key_block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?-----END [A-Z ]*PRIVATE KEY-----")),
)

# 键值对形式：app_secret=xxx / "api_key": "xxx"
KV_PATTERN = re.compile(
    r"(?i)\b(app[_-]?secret|app[_-]?id|api[_-]?key|access[_-]?token|client[_-]?secret|"
    r"secret[_-]?key|password|passwd|pwd)\b(\s*[:=]\s*)(['\"]?)([A-Za-z0-9_\-\.]{8,})\3"
)

# 个人标识
PHONE_PATTERN = re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")
EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b")

# 本机路径：只匹配 ASCII 路径字符，避免吞掉后面的中文正文
# 1) 带空格的常见安装路径（Program Files / Applications）单独处理
SPACY_PATH_PATTERN = re.compile(
    r"[A-Za-z]:\\Program Files(?: \(x86\))?\\[A-Za-z0-9_\-.\\ ]{0,120}"
    r"|/Applications/[A-Za-z0-9_\-. /]{0,120}"
)
# 2) 普通盘符路径（反斜杠或正斜杠写法都要覆盖）
WIN_PATH_PATTERN = re.compile(r"\b[A-Za-z]:[\\/][A-Za-z0-9_\-.\\/]+")
# 3) 家目录简写 ~/xxx
TILDE_PATH_PATTERN = re.compile(r"(?<![\w~])~[\\/][A-Za-z0-9_\-.\\/]+")
# 4) macOS / Linux 用户目录
POSIX_PATH_PATTERN = re.compile(r"/(?:Users|home)/[A-Za-z0-9_\-.]+(?:/[A-Za-z0-9_\-.]+)*")

# 内网 / 公网 IP（四段点分十进制）
IP_PATTERN = re.compile(r"(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])")

PLACEHOLDERS = {
    "openai_like_key": "<REDACTED_API_KEY>",
    "github_token": "<REDACTED_GITHUB_TOKEN>",
    "aws_access_key": "<REDACTED_AWS_KEY>",
    "aliyun_access_key": "<REDACTED_ACCESS_KEY>",
    "jwt": "<REDACTED_JWT>",
    "private_key_block": "<REDACTED_PRIVATE_KEY>",
}


def _valid_ip(text):
    """过滤掉 1.2.3.400 这类伪 IP，降低误伤版本号/编号的概率。"""
    parts = text.split(".")
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(p) <= 255 for p in parts)
    except ValueError:
        return False


def scrub(text, redact_paths=True):
    """返回 (净化后文本, 替换计数)。redact_paths=False 时保留路径原文。"""
    if not isinstance(text, str) or not text:
        return text, 0

    hits = 0
    out = text

    for name, pattern in CREDENTIAL_PATTERNS:
        out, n = pattern.subn(PLACEHOLDERS[name], out)
        hits += n

    def _kv_repl(m):
        return "%s%s%s<REDACTED>%s" % (m.group(1), m.group(2), m.group(3), m.group(3))

    out, n = KV_PATTERN.subn(_kv_repl, out)
    hits += n

    out, n = PHONE_PATTERN.subn("<REDACTED_PHONE>", out)
    hits += n
    out, n = EMAIL_PATTERN.subn("<REDACTED_EMAIL>", out)
    hits += n

    def _ip_repl(m):
        return "<REDACTED_IP>" if _valid_ip(m.group(0)) else m.group(0)

    out, n = IP_PATTERN.subn(_ip_repl, out)
    hits += n

    if redact_paths:
        out, n = SPACY_PATH_PATTERN.subn("<LOCAL_PATH>", out)
        hits += n
        out, n = WIN_PATH_PATTERN.subn("<LOCAL_PATH>", out)
        hits += n
        out, n = TILDE_PATH_PATTERN.subn("<LOCAL_PATH>", out)
        hits += n
        out, n = POSIX_PATH_PATTERN.subn("<LOCAL_PATH>", out)
        hits += n

    return out, hits
