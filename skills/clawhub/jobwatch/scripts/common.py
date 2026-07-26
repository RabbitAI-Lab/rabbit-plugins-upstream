"""JobWatcher shared helpers: env, HTTP (stdlib only), state, logging."""
import json
import os
import time
import uuid
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent


def _resolve_home():
    """运行数据主目录。

    优先 env JOBWATCH_HOME；否则：若本 skill 安装在 <workspace>/skills/jobwatch/
    下，数据放 <workspace>/jobwatch/（skill 目录保持只读、可随时升级重装）；
    若是独立工作区形态（template/作业实例），数据就在工作区根目录。
    """
    env = os.environ.get("JOBWATCH_HOME")
    if env:
        return Path(env).expanduser()
    parts = SKILL_DIR.parts
    if "skills" in parts:
        ws = Path(*parts[: parts.index("skills")])
        return ws / "jobwatch"
    return SKILL_DIR


ROOT = _resolve_home()


def _load_config():
    """HOME/config.json（用户态，入职时生成/修改）→ 缺省回退 skill 自带默认值。"""
    user_cfg = ROOT / "config.json"
    if user_cfg.exists():
        return json.loads(user_cfg.read_text())
    default = SKILL_DIR / "config.default.json"
    if default.exists():
        ROOT.mkdir(parents=True, exist_ok=True)
        user_cfg.write_text(default.read_text())  # 首跑落地一份供用户/入职流程修改
        return json.loads(user_cfg.read_text())
    return json.loads((SKILL_DIR / "config.json").read_text())


CONFIG = _load_config()
STATE_FILE = ROOT / "state" / "seen_jobs.json"
QUEUE_FILE = ROOT / "queue" / "p2_digest.jsonl"
RUNS_DIR = ROOT / "runs"

OPENCLAW_DIR = Path(os.environ.get("OPENCLAW_DIR", str(Path.home() / ".openclaw")))


def load_env():
    """Load ROOT/.env into os.environ (existing env wins)."""
    for env_file in (ROOT / ".env", SKILL_DIR / ".env"):
        if env_file.exists():
            _parse_env(env_file)


def _parse_env(env_file):
    for line in env_file.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        os.environ.setdefault(k.strip(), v.strip())


load_env()


def now_iso():
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def http(url, method="GET", headers=None, data=None, json_body=None, timeout=45):
    """Returns (status_code, body_bytes). Raises on network errors."""
    h = {"User-Agent": "JobWatch/1.0 (personal job monitor)"}
    if headers:
        h.update(headers)
    body = data
    if json_body is not None:
        body = json.dumps(json_body).encode()
        h.setdefault("Content-Type", "application/json")
    req = urllib.request.Request(url, data=body, headers=h, method=method)
    import http.client
    for attempt in (1, 2):  # 瞬断（截断/重置/超时）自动重试一次
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            return e.code, e.read()
        except (http.client.IncompleteRead, ConnectionResetError, TimeoutError,
                urllib.error.URLError) as e:
            if attempt == 2:
                raise
            time.sleep(2)


def http_json(url, **kw):
    status, body = http(url, **kw)
    if status >= 300:
        raise RuntimeError(f"HTTP {status} for {url}: {body[:300]!r}")
    return json.loads(body)


def multipart_post(url, fields, file_field, filename, file_bytes,
                   content_type="text/markdown", headers=None, timeout=120):
    """Multipart/form-data POST using stdlib only."""
    boundary = f"----jobwatch{uuid.uuid4().hex}"
    parts = []
    for k, v in (fields or {}).items():
        parts.append(
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n".encode()
        )
    parts.append(
        (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{file_field}\"; "
         f"filename=\"{filename}\"\r\nContent-Type: {content_type}\r\n\r\n").encode()
        + file_bytes + b"\r\n"
    )
    parts.append(f"--{boundary}--\r\n".encode())
    body = b"".join(parts)
    h = {"Content-Type": f"multipart/form-data; boundary={boundary}"}
    if headers:
        h.update(headers)
    return http(url, method="POST", headers=h, data=body, timeout=timeout)


# ---------- credentials ----------
# 最小权限：默认只读 HOME/.env 里用户自己填的 key。复用 OpenClaw / Telegram 宿主
# 配置里的凭证属于跨作用域读取，默认关闭；仅当用户显式 JOBWATCH_ALLOW_HOST_CREDS=1
# 时才启用。见 SKILL.md「隐私与数据流 · ③ 凭证读取」。

def _host_creds_allowed():
    return os.environ.get("JOBWATCH_ALLOW_HOST_CREDS", "").strip() in ("1", "true", "yes")


def _openrouter_key_from_store():
    """OpenClaw 凭证存储兜底：旧版 JSON 文件 → 新版（2026.7.1+）SQLite。
    仅在 JOBWATCH_ALLOW_HOST_CREDS 开启时读取宿主 auth store。"""
    if not _host_creds_allowed():
        return None
    legacy = OPENCLAW_DIR / "agents" / "main" / "agent" / "auth-profiles.json"
    if legacy.exists():
        profiles = json.loads(legacy.read_text()).get("profiles", {})
        key = (profiles.get("openrouter:default") or {}).get("key")
        if key:
            return key
    db = OPENCLAW_DIR / "agents" / "main" / "agent" / "openclaw-agent.sqlite"
    if db.exists():
        try:
            import sqlite3
            con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
            row = con.execute(
                "SELECT store_json FROM auth_profile_store WHERE store_key='primary'"
            ).fetchone()
            con.close()
            if row:
                profiles = json.loads(row[0]).get("profiles", {})
                key = (profiles.get("openrouter:default") or {}).get("key")
                if key:
                    return key
        except Exception:  # noqa: BLE001
            pass
    return None


def openrouter_key():
    k = os.environ.get("OPENROUTER_API_KEY") or _openrouter_key_from_store()
    if k:
        return k
    raise RuntimeError(
        "No OpenRouter API key found. 在 HOME/.env 填 OPENROUTER_API_KEY；"
        "或设 JOBWATCH_ALLOW_HOST_CREDS=1 复用 OpenClaw 已存的 key。")


def telegram_token():
    t = os.environ.get("TELEGRAM_BOT_TOKEN")
    if t:
        return t
    if _host_creds_allowed():  # 复用 openclaw.json 里的 bot token 需显式开启
        p = OPENCLAW_DIR / "openclaw.json"
        if p.exists():
            cfg = json.loads(p.read_text())
            tok = cfg.get("channels", {}).get("telegram", {}).get("botToken")
            if tok:
                return tok
    raise RuntimeError("No Telegram bot token (env TELEGRAM_BOT_TOKEN；或 JOBWATCH_ALLOW_HOST_CREDS=1 复用 openclaw.json)")


def telegram_chat_id():
    cid = os.environ.get("TELEGRAM_CHAT_ID") or CONFIG["telegram"].get("chat_id")
    if cid:
        return cid
    if _host_creds_allowed():  # 复用 openclaw allowFrom 需显式开启
        p = OPENCLAW_DIR / "credentials" / "telegram-default-allowFrom.json"
        if p.exists():
            allow = json.loads(p.read_text()).get("allowFrom", [])
            if allow:
                return str(allow[0])
    raise RuntimeError("No Telegram chat id (env TELEGRAM_CHAT_ID / config.json；或 JOBWATCH_ALLOW_HOST_CREDS=1)")


# ---------- state ----------

def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def save_state(state):
    STATE_FILE.parent.mkdir(exist_ok=True)
    tmp = STATE_FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=1))
    tmp.replace(STATE_FILE)


def append_queue(record):
    QUEUE_FILE.parent.mkdir(exist_ok=True)
    with QUEUE_FILE.open("a") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def log_run(record):
    RUNS_DIR.mkdir(exist_ok=True)
    record.setdefault("ts", now_iso())
    day = datetime.now().strftime("%Y-%m-%d")
    with (RUNS_DIR / f"{day}.jsonl").open("a") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


OUTBOX_FILE = ROOT / "queue" / "outbox.jsonl"
PENDING_FILE = ROOT / "queue" / "pending_judgment.jsonl"
JUDGMENTS_FILE = ROOT / "queue" / "judgments.jsonl"


def judge_mode():
    """agent（默认，零配置：判级交给被唤醒的 agent 本人）| api（OpenAI 兼容端点）"""
    return os.environ.get("JUDGE_MODE") or CONFIG.get("judge", {}).get("mode", "agent")


def notify_mode():
    """agent（默认：消息写 outbox，由 agent 用任意渠道播报）| telegram（直连 bot API）"""
    return os.environ.get("NOTIFY_MODE") or CONFIG.get("notify", {}).get("mode", "agent")


def append_outbox(kind, text, meta=None):
    OUTBOX_FILE.parent.mkdir(exist_ok=True)
    with OUTBOX_FILE.open("a") as f:
        f.write(json.dumps({"ts": now_iso(), "kind": kind, "text": text,
                            "meta": meta or {}}, ensure_ascii=False) + "\n")


def kb_hint():
    """通知消息里的知识库提示行，随 KB 后端自适应。"""
    import os
    backend = os.environ.get("KB_BACKEND") or CONFIG.get("kb", {}).get("backend", "local")
    if backend == "twobrain":
        return f"已入库 2brain，可提问追溯：{CONFIG['twobrain']['ask_url']}"
    return "已入库本地知识库（kb_local/）"


def slug(text, maxlen=48):
    out = "".join(c if c.isalnum() else "-" for c in text.lower())
    while "--" in out:
        out = out.replace("--", "-")
    return out.strip("-")[:maxlen]
