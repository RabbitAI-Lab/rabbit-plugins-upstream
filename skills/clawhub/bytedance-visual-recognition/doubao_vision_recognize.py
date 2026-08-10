#!/usr/bin/env python3
"""
Doubao Vision Recognize v4.2.0
================================
图片/视频 → 文字/代码
  img-to-text     Doubao*6→GLM-4.6V→GLM-4.1V
  video-to-text   Doubao*6→GLM-4.6V→GLM-4.1V
  img-to-code     Doubao*5→GLM-4.6V→GLM-4.1V
  video-to-code   Doubao*5 (GLM不支持视频转代码)

后端: Doubao Responses API + Zhipu Chat Completions API
"""

import base64
import hashlib
import hmac
import json
import os
import shutil
import ssl
import sys
import time
import unicodedata
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# 默认配置（首次运行自动生成 config.json）
_CONFIG_DEFAULTS = {
    "provider_mode":            0,
    "temp_retention_days":      7,
    "ark_api_key":              "",
    "doubao_vision_21p_id":     "",
    "doubao_vision_21t_id":     "",
    "doubao_vision_20p_id":     "",
    "doubao_vision_20c_id":     "",
    "doubao_vision_20l_id":     "",
    "doubao_vision_20m_id":     "",
    "volcengine_access_key":    "",
    "volcengine_secret_key":    "",
    "zhipu_api_key":            "",
    "privacy_notice_shown":     False,
}

_CONFIG_DESCRIPTIONS = {
    "provider_mode":            "0=默认 1=仅智谱 2=仅豆包",
    "temp_retention_days":      "Temp 缓存保留天数（1-3650）",
    "ark_api_key":              "火山方舟 API Key",
    "doubao_vision_21p_id":     "Doubao-Seed-2.1-Pro 接入点 ID",
    "doubao_vision_21t_id":     "Doubao-Seed-2.1-Turbo 接入点 ID",
    "doubao_vision_20p_id":     "Doubao-Seed-2.0-Pro 接入点 ID",
    "doubao_vision_20c_id":     "Doubao-Seed-2.0-Code 接入点 ID",
    "doubao_vision_20l_id":     "Doubao-Seed-2.0-Lite 接入点 ID",
    "doubao_vision_20m_id":     "Doubao-Seed-2.0-Mini 接入点 ID",
    "volcengine_access_key":    "火山 IAM Access Key（可选）",
    "volcengine_secret_key":    "火山 IAM Secret Key（可选）",
    "zhipu_api_key":            "智谱 API Key（免费模型）",
    "privacy_notice_shown":     "隐私声明已确认（首次运行自动设置）",
}

_PATH = Path(__file__).resolve().parent
_CONFIG_PATH = _PATH / "config.json"

# 首次运行：自动生成 config.json
if not _CONFIG_PATH.exists():
    meta = {"_comment": "ByteDance Visual Recognition 配置文件 — 填好对应值即可，留空表示不启用。"}
    config = dict(meta, **_CONFIG_DEFAULTS)
    with open(_CONFIG_PATH, "w", encoding="utf-8", newline="\n") as _f:
        json.dump(config, _f, ensure_ascii=False, indent=2)
        _f.write("\n")

# 加载配置
_cfg = {}
if _CONFIG_PATH.exists():
    try:
        with open(_CONFIG_PATH, "r", encoding="utf-8") as _f:
            _cfg = json.load(_f)
    except Exception:
        pass

# 兼容旧版 .env → json 自动迁移
API_URL = "https://ark.cn-beijing.volces.com/api/v3/responses"
ARK_API_KEY = _cfg.get("ark_api_key", "")
IAM_AK = _cfg.get("volcengine_access_key", "")
IAM_SK = _cfg.get("volcengine_secret_key", "")
ZHIPU_API_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
ZHIPU_API_KEY = _cfg.get("zhipu_api_key", "")
_PROVIDER_MODE = _cfg.get("provider_mode", 0)
_TEMP_RETENTION = max(1, min(3650, _cfg.get("temp_retention_days", 7)))
SYNC_INTERVAL = 30 * 60


def _show_privacy_notice():
    """首次运行显示隐私声明并记录确认"""
    if not _cfg.get("privacy_notice_shown", False):
        print("\n".join([
            "",
            "╔══════════════════ 隐私与数据声明 ═══════════════════════════╗",
            "║ • 选中的图片/视频和 prompt 将 base64 编码后发送至云端 API   ║",
            "║   （火山方舟 Doubao / 智谱 GLM）                            ║",
            "║ • API Key 明文存储在 config.json 中                         ║",
            "║ • 媒体文件缓存至 Temp/，默认保留 7 天                         ║",
            "║ • 识别历史在 vision_history.json，追问上下文在 .last_response ║",
            "║ • 继续使用即表示已阅读并接受以上数据行为                      ║",
            "╚══════════════════════════════════════════════════════════════╝",
            "",
        ]))
        _cfg["privacy_notice_shown"] = True
        try:
            with open(_CONFIG_PATH, "r", encoding="utf-8") as _f:
                data = json.load(_f)
            data["privacy_notice_shown"] = True
            with open(_CONFIG_PATH, "w", encoding="utf-8", newline="\n") as _f:
                json.dump(data, _f, ensure_ascii=False, indent=2)
                _f.write("\n")
        except Exception:
            pass
SYNC_INTERVAL = 30 * 60
RETENTION_DAYS = 7
TIMEOUT = 300
MAX_IMG = 15 * 1024 * 1024
MAX_VID = 50 * 1024 * 1024
MAX_PAYLOAD = 64 * 1024 * 1024
DAILY_LIMIT = 1_800_000

# 按模式控制思考深度: text 模式轻思考(low)节省Token，code 模式均衡(medium)保证质量
_REASONING_EFFORT = {
    "img-to-text": "low",
    "video-to-text": "low",
    "img-to-code": "medium",
    "video-to-code": "medium",
}

BASE_DIR = Path(__file__).resolve().parent
HISTORY_FILE = Path(os.environ.get("VISION_HISTORY_FILE", str(BASE_DIR / "vision_history.json")))
TEMP_DIR = Path(os.environ.get("VISION_TEMP_DIR", str(BASE_DIR / "Temp")))
def _today_dir() -> Path:
    """返回今天的缓存子目录（Temp/YYYYMMDD）"""
    d = TEMP_DIR / datetime.now().strftime("%Y%m%d")
    d.mkdir(parents=True, exist_ok=True)
    return d
LAST_RESP_FILE = BASE_DIR / ".last_response"
ssl_ctx = ssl.create_default_context()

_MODELS = {
    "21PRO":  {"name": "Doubao-Seed-2.1-Pro",   "id": _cfg.get("doubao_vision_21p_id", ""),  "env": "doubao_vision_21p_id", "provider": "doubao"},
    "21TURBO":{"name": "Doubao-Seed-2.1-Turbo", "id": _cfg.get("doubao_vision_21t_id", ""),  "env": "doubao_vision_21t_id", "provider": "doubao"},
    "20PRO":  {"name": "Doubao-Seed-2.0-Pro",   "id": _cfg.get("doubao_vision_20p_id", ""),  "env": "doubao_vision_20p_id", "provider": "doubao"},
    "20CODE": {"name": "Doubao-Seed-2.0-Code",  "id": _cfg.get("doubao_vision_20c_id", ""),  "env": "doubao_vision_20c_id", "provider": "doubao"},
    "20LITE": {"name": "Doubao-Seed-2.0-Lite",  "id": _cfg.get("doubao_vision_20l_id", ""),  "env": "doubao_vision_20l_id", "provider": "doubao"},
    "20MINI": {"name": "Doubao-Seed-2.0-Mini",  "id": _cfg.get("doubao_vision_20m_id", ""),  "env": "doubao_vision_20m_id", "provider": "doubao"},
    "GLM46V": {"name": "GLM-4.6V-Flash",        "id": "glm-4.6v-flash" if ZHIPU_API_KEY else "",  "env": "ZHIPU_API_KEY",       "provider": "zhipu", "retries": 10},
    "GLM41V": {"name": "GLM-4.1V-Thinking-Flash","id": "glm-4.1v-thinking-flash" if ZHIPU_API_KEY else "", "env": "ZHIPU_API_KEY", "provider": "zhipu", "retries": 5},
}

def _validate_models():
    """延迟校验：任意配置一个模型 ID 即可运行。_select_model 会跳过空 ID。"""
    if not any(m["id"] for m in _MODELS.values()):
        raise RuntimeError("未配置任何模型，请在 config.json 中至少填入一个 API Key（如 doubao_vision_21p_id 或 zhipu_api_key）。")

_MAX_NAME_W = max(len(m["name"]) for m in _MODELS.values())


def _pad_name(name: str) -> str:
    return name + ' ' * (_MAX_NAME_W - len(name))


_MODES = {
    "img-to-text":   {"label": "图片→文字", "chain": ["21PRO", "21TURBO", "20PRO", "20CODE", "20LITE", "20MINI", "GLM46V", "GLM41V"]},
    "video-to-text": {"label": "视频→文字", "chain": ["21PRO", "21TURBO", "20PRO", "20CODE", "20LITE", "20MINI", "GLM46V", "GLM41V"]},
    "img-to-code":   {"label": "图片→代码", "chain": ["21PRO", "21TURBO", "20CODE", "20PRO", "20LITE", "GLM46V", "GLM41V"]},
    "video-to-code": {"label": "视频→代码", "chain": ["21PRO", "21TURBO", "20CODE", "20PRO", "20LITE"]},
}

_MODE_MAP = {
    ("image", "text"): "img-to-text",
    ("video", "text"): "video-to-text",
    ("image", "code"): "img-to-code",
    ("video", "code"): "video-to-code",
}

_MEDIA_EXT = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif", ".tiff",
              ".mp4", ".mov", ".webm", ".avi", ".mkv", ".flv", ".wmv"}

SP_VISION = """你是一个专业的视觉识别和分析助手。请仔细观察用户提供的图片/视频内容，按以下规则完成分析：

【通用规则】(优先级从高到低)
1. 完整性规则: 需对内容进行完整分析，覆盖图形、文字、表格、场景等所有视觉元素维度，不能遗漏关键内容。
2. 匹配性规则: 分析结果需完全匹配用户指令的具体需求，用户未提及的冗余内容无需反馈。
3. 格式化规则: 若提取文字或表格，整理后须用 Markdown 格式输出；表格须转成标准 Markdown 表格格式；公式须转成标准 LaTeX 格式。
4. 默认规则: 用户若无特殊指令需求，分析结果以"场景描述"为核心，按用户日常阅读习惯整理成简洁的自然语言文本。

【后置检查】
1. 确认结果中没有用户未提及的冗余内容。
2. 确认所有需 Markdown 格式的内容格式正确。
3. 确认内容描述与实际显示一致，未出现主观臆断。"""

SP_VIDEO = """你是一个专业的视频内容分析助手。请仔细观察用户提供的视频内容，按以下规则完成分析：

【通用规则】(优先级从高到低)
1. 完整性规则: 需对视频内容进行完整分析，先梳理视频的完整叙事逻辑或操作流程，再按"核心内容-关键细节-总结归纳"的优先级整理结果。
2. 匹配性规则: 分析结果需完全匹配用户指令的具体需求。
3. 时间戳规则: 若视频中存在明确的时间节点或操作步骤，需为这些节点补充精确到秒的时间戳标记。
4. 默认规则: 用户若无特殊指令，分析结果以不超过300字的通俗易懂的自然语言文本输出。

【后置检查】
1. 确认结果中没有用户未提及的冗余内容。
2. 确认所有需时间戳标记的地方都已补充精确时间。
3. 确认分析结果格式布局符合日常阅读习惯。"""

SP_IMG_CODE = """你是一个专业的 UI 设计稿转代码助手。请仔细观察用户提供的图片，按以下规则生成代码：

【通用规则】(优先级从高到低)
1. 完整性规则: 需完整复刻图片中的 UI 布局、细节样式、交互元素视觉效果，不能遗漏任何关键视觉元素。
2. 匹配性规则: 生成的代码技术栈，需完全匹配用户指令中指定的技术栈。
3. 格式化规则: 代码需遵循统一规范，使用语义化 HTML 标签，CSS 类名采用 BEM 风格，代码结构清晰，关键部分需要添加注释说明。
4. 响应式规则: 代码需同时适配桌面端和移动端，在不同设备尺寸下保持视觉效果一致。
5. 默认规则: 用户若无特殊指令需求，技术栈默认使用 HTML+TailwindCSS，无需额外补充无用的 JS 代码。

【后置检查】
1. 确认代码的技术栈完全匹配用户指令的要求。
2. 确认代码中没有用户指令未提及的冗余内容。
3. 确认代码中所有需要图片的地方都使用了合理的占位图。
4. 确认代码的格式布局符合行业标准，没有语法错误。
5. 确认代码的复刻效果与原图的视觉效果高度匹配。"""

SP_VIDEO_CODE = """你是一个专业的视频转代码助手。请仔细观察用户提供的视频内容（可能是UI演示、网页录屏、应用操作录屏等），按以下规则生成代码：

【通用规则】(优先级从高到低)
1. 完整性规则: 需完整复刻视频中展示的 UI 布局、页面结构、交互流程和视觉样式，不能遗漏任何关键界面元素。
2. 匹配性规则: 生成的代码技术栈需完全匹配用户指令中指定的技术栈。
3. 格式化规则: 代码需遵循统一规范，使用语义化 HTML 标签，CSS 类名采用 BEM 风格，代码结构清晰，关键部分添加注释说明。
4. 响应式规则: 代码需同时适配桌面端和移动端，在不同设备尺寸下保持视觉效果一致。
5. 默认规则: 用户若无特殊指令需求，技术栈默认使用 HTML+TailwindCSS，无需额外补充无用的 JS 代码。

【后置检查】
1. 确认代码的技术栈完全匹配用户指令的要求。
2. 确认代码中没有用户指令未提及的冗余内容。
3. 确认代码中所有需要图片的地方都使用了合理的占位图。
4. 确认代码的格式布局符合行业标准，没有语法错误。
5. 确认代码的复刻效果与视频中展示的视觉效果高度匹配。"""

_SP_MAP = {
    "img-to-text": SP_VISION,
    "video-to-text": SP_VIDEO,
    "img-to-code": SP_IMG_CODE,
    "video-to-code": SP_VIDEO_CODE,
}


class ConsoleSyncer:
    """火山方舟控制台用量同步器 — 使用 IAM HMAC-SHA256 签名调用 GetInferenceUsage API"""
    def __init__(self):
        self._ak = IAM_AK
        self._sk = IAM_SK
        self._enabled = bool(self._ak and self._sk)
        self._last_sync = 0

    @property
    def enabled(self):
        return self._enabled

    def _sign(self, key: bytes, msg: str) -> bytes:
        return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

    def _build_auth(self, action: str, payload_str: str):
        svc, region, host = "ark", "cn-beijing", "open.volcengineapi.com"
        now = datetime.now(timezone.utc)
        ds = now.strftime("%Y%m%d")
        xd = now.strftime("%Y%m%dT%H%M%SZ")
        q = f"Action={action}&Version=2024-01-01"
        csha = hashlib.sha256(payload_str.encode("utf-8")).hexdigest()
        ch = f"content-type:application/json; charset=UTF-8\nhost:{host}\nx-content-sha256:{csha}\nx-date:{xd}\n"
        sh = "content-type;host;x-content-sha256;x-date"
        cr = f"POST\n/\n{q}\n{ch}\n{sh}\n{csha}"
        cs = f"{ds}/{region}/{svc}/request"
        sts = f"HMAC-SHA256\n{xd}\n{cs}\n{hashlib.sha256(cr.encode('utf-8')).hexdigest()}"
        kd = self._sign(self._sk.encode("utf-8"), ds)
        kr = self._sign(kd, region)
        ks = self._sign(kr, svc)
        ksg = self._sign(ks, "request")
        sig = hmac.new(ksg, sts.encode("utf-8"), hashlib.sha256).hexdigest()
        auth = f"HMAC-SHA256 Credential={self._ak}/{cs}, SignedHeaders={sh}, Signature={sig}"
        return {"Authorization": auth, "Content-Type": "application/json; charset=UTF-8",
                "Host": host, "X-Date": xd, "X-Content-Sha256": csha}, q

    def _post(self, url, headers, data, timeout=30):
        req = urllib.request.Request(url, data=data, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=ssl_ctx) as r:
                return r.status, json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            b = e.read().decode("utf-8", errors="replace")
            return e.code, json.loads(b) if b else {}

    def query_today(self):
        if not self._enabled:
            return {}
        try:
            today = datetime.now().strftime("%Y-%m-%d")
            yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
            ids = [m["id"] for m in _MODELS.values() if m.get("provider", "doubao") == "doubao"]
            payload = {"QueryInterval": "Hour", "StartTime": yesterday, "EndTime": today,
                       "Filters": [{"Key": "ModelEndpoint", "Values": ids}]}
            ps = json.dumps(payload)
            hdrs, q = self._build_auth("GetInferenceUsage", ps)
            st, res = self._post(f"https://open.volcengineapi.com/?{q}", hdrs, ps.encode("utf-8"))
            if st != 200 or "Result" not in res:
                return {}
            fields = [f["Name"] for f in res["Result"].get("Fields", [])]
            data = res["Result"].get("Data", [])
            if "ModelEndpoint" not in fields or "TotalTokens" not in fields:
                return {}
            ei, ti = fields.index("ModelEndpoint"), fields.index("TotalTokens")
            nmap = {m["id"]: m["name"] for m in _MODELS.values()}
            counts: Dict[str, int] = {}
            for row in data:
                name = nmap.get(str(row[ei]) if ei < len(row) else "")
                if name:
                    counts[name] = counts.get(name, 0) + int(row[ti] or 0)
            return counts
        except Exception:
            return {}

    def sync_to_local(self, hm: "HistoryManager"):
        if not self._enabled or (time.time() - self._last_sync) < SYNC_INTERVAL:
            return {}
        self._last_sync = time.time()
        pc = self.query_today()
        if not pc or sum(pc.values()) == 0:
            return {}
        return hm.sync_from_console(pc)


class HistoryManager:
    """本地调用历史与 Token 用量管理器 — JSON 文件持久化，7天自动清理"""
    def __init__(self, path: Path):
        self.path = path
        self.data = self._load()
        self._clean()

    def _load(self) -> Dict:
        if not self.path.exists():
            return {"history": [], "daily_tokens": {}}
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                d = json.load(f)
                d.setdefault("history", [])
                d.setdefault("daily_tokens", {})
                return d
        except (json.JSONDecodeError, IOError):
            return {"history": [], "daily_tokens": {}}

    def _save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".json.tmp")
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
        tmp.replace(self.path)

    def _clean(self):
        cutoff = datetime.now() - timedelta(days=RETENTION_DAYS)
        cts, cds = cutoff.timestamp(), cutoff.strftime("%Y-%m-%d")
        self.data["history"] = [r for r in self.data["history"] if r.get("timestamp", 0) >= cts]
        self.data["daily_tokens"] = {d: c for d, c in self.data["daily_tokens"].items() if d >= cds}

    @staticmethod
    def _today():
        return datetime.now().strftime("%Y-%m-%d")

    def get_daily(self, name: str) -> int:
        return self.data.setdefault("daily_tokens", {}).setdefault(self._today(), {}).get(name, 0)

    def add_tokens(self, name: str, tokens: int) -> int:
        self._clean()
        c = self.data.setdefault("daily_tokens", {}).setdefault(self._today(), {})
        c[name] = c.get(name, 0) + tokens
        self._save()
        return c[name]

    def add_record(self, rec: Dict):
        self._clean()
        self.data.setdefault("history", []).append(rec)
        self._save()

    def get_status(self) -> Dict:
        today = self._today()
        models = []
        for m in _MODELS.values():
            configured = bool(m["id"]) and m["id"].strip() != "*"
            unlimited = m.get("provider") == "zhipu"
            models.append({
                "name": m["name"],
                "tokens": self.get_daily(m["name"]) if configured else 0,
                "limit": DAILY_LIMIT if not unlimited else -1,
                "configured": configured,
                "unlimited": unlimited,
            })
        return {
            "date": today,
            "total_history": len(self.data.get("history", [])),
            "models": models,
        }

    def sync_from_console(self, console: Dict[str, int]) -> Dict[str, str]:
        lc = self.data.setdefault("daily_tokens", {}).setdefault(self._today(), {})
        result = {}
        for name, cv in console.items():
            lv = lc.get(name, 0)
            if cv > lv:
                lc[name] = cv
                result[name] = "synced"
            else:
                result[name] = "kept_local"
        self._save()
        return result

    def get_history(self) -> List[Dict]:
        return self.data.get("history", [])


class DoubaoVisionRecognizer:
    """核心识别引擎 — 封装模型选择、媒体编码、API调用、结果提取"""
    def __init__(self):
        _validate_models()
        _show_privacy_notice()
        self.api_key = ARK_API_KEY
        self.history = HistoryManager(HISTORY_FILE)
        self._console = ConsoleSyncer()

    def _auto_sync(self):
        if self._console.enabled:
            self._console.sync_to_local(self.history)
        self._cleanup_temp()

    def _cleanup_temp(self):
        """清理 Temp 下超过 TEMP_RETENTION_DAYS 天的日期子目录"""
        try:
            if not TEMP_DIR.exists():
                return
            cutoff = (datetime.now() - timedelta(days=_TEMP_RETENTION)).strftime("%Y%m%d")
            for d in TEMP_DIR.iterdir():
                if d.is_dir() and len(d.name) == 8 and d.name.isdigit() and d.name < cutoff:
                    shutil.rmtree(d, ignore_errors=True)
        except Exception:
            pass

    def _post(self, url, headers, data, timeout=TIMEOUT):
        req = urllib.request.Request(url, data=data, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=ssl_ctx) as r:
                return r.status, r.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            return e.code, e.read().decode("utf-8", errors="replace")

    def _select_model(self, mode_key: str) -> Optional[Dict]:
        """按模式降级链选择首个未超限的模型（按 PROVIDER_MODE 过滤供应商）"""
        for mk in _MODES[mode_key]["chain"]:
            spec = _MODELS[mk]
            if not spec["id"]:
                continue
            # 供应商过滤：1=仅智谱 2=仅豆包
            if _PROVIDER_MODE == 1 and spec["provider"] == "doubao":
                continue
            if _PROVIDER_MODE == 2 and spec["provider"] == "zhipu":
                continue
            if self.history.get_daily(spec["name"]) < DAILY_LIMIT:
                return {"key": mk, "name": spec["name"], "id": spec["id"], "provider": spec["provider"],
                        "retries": spec.get("retries", 0)}
        return None

    def _encode_media(self, file_path: str, input_type: str) -> Tuple[str, str, str]:
        """读取文件→Base64编码→生成data URI"""
        src = Path(file_path)
        if not src.is_file():
            raise FileNotFoundError(f"文件不存在: {file_path}")
        ext = src.suffix.lower()
        raw = src.read_bytes()
        if input_type == "image":
            max_b, media = MAX_IMG, "image"
        elif input_type == "video":
            max_b, media = MAX_VID, "video"
        else:
            raise ValueError("必须指定输入类型: --image 或 --video")
        if len(raw) > max_b:
            raise ValueError(f"文件过大 ({len(raw)/1024/1024:.1f} MB)，最大 {max_b/1024/1024:.0f} MB")
        td = _today_dir()
        tmp = td / f"v_{hashlib.md5(str(src).encode()).hexdigest()[:12]}{ext}"
        shutil.copy2(src, tmp)
        fmt = ext.lstrip(".")
        if fmt == "jpg":
            fmt = "jpeg"
        elif fmt not in ("png", "jpeg", "webp", "bmp", "gif", "tiff", "mp4", "mov", "webm"):
            fmt = "png" if media == "image" else "mp4"
        b64 = base64.b64encode(raw).decode("ascii")
        payload_est = len(b64) + 2048
        if payload_est > MAX_PAYLOAD:
            raise ValueError(f"请求体过大 ({payload_est/1024/1024:.1f} MB)，API 上限 64 MB，请压缩文件后重试")
        return f"data:{media}/{fmt};base64,{b64}", str(tmp), media

    def _build_blocks(self, media: str, data_uri: str, prompt: str, output_type: str) -> List[Dict]:
        """构建多模态 API 的 content blocks — text模式用low细节省Token，code模式用high保证精度"""
        blocks = []
        if media == "image":
            detail = "low" if output_type == "text" else "high"
            blocks.append({"type": "input_image", "image_url": data_uri, "detail": detail})
        else:
            blocks.append({"type": "input_video", "video_url": data_uri, "fps": 1.0})
        blocks.append({"type": "input_text", "text": prompt})
        return blocks

    # ── GLM / 智谱 API 后端 ────────────────────────────────────────

    def _build_zhipu_blocks(self, media: str, data_uri: str, prompt: str, sp: str) -> List[Dict]:
        """构建智谱 Chat Completions API 的 content blocks"""
        blocks = []
        if media == "image":
            blocks.append({"type": "image_url", "image_url": {"url": data_uri}})
        else:
            blocks.append({"type": "video_url", "video_url": {"url": data_uri}})
        blocks.append({"type": "text", "text": sp + "\n" + prompt})
        return blocks

    def _zhipu_call(self, model_info: Dict, messages: List[Dict],
                     retries: int = 5, interval: float = 1.0) -> Tuple[Optional[Dict], str]:
        """调用智谱 API，自动重试处理 429/502/503"""
        headers = {"Authorization": f"Bearer {ZHIPU_API_KEY}",
                   "Content-Type": "application/json"}
        payload = {"model": model_info["id"], "messages": messages,
                   "thinking": {"type": "enabled"}, "stream": False}
        last_error = ""
        for attempt in range(retries + 1):
            if attempt > 0:
                print(f"   ⚠️ 重试 {attempt}/{retries} (1s后)...")
                time.sleep(interval)
            try:
                st, body = self._post(ZHIPU_API_URL, headers, json.dumps(payload).encode("utf-8"))
                if st == 200:
                    return json.loads(body), ""
                elif st in (429, 502, 503):
                    last_error = f"HTTP {st}"
                    continue
                else:
                    return None, f"智谱 API 请求失败 (HTTP {st}): {body[:300]}"
            except Exception as e:
                last_error = f"{type(e).__name__}: {e}"
                continue
        return None, f"智谱 API 重试{retries}次后仍失败: {last_error}"

    @staticmethod
    def _extract_zhipu_text(res: Dict) -> str:
        """从智谱 API 响应中提取文本"""
        for c in res.get("choices", []):
            msg = c.get("message", {})
            if msg.get("role") == "assistant":
                return msg.get("content", "")
        return ""

    @staticmethod
    def _extract_zhipu_tokens(res: Dict) -> Dict:
        """从智谱 API 响应中提取 Token 用量"""
        u = res.get("usage", {})
        return {
            "input_tokens": u.get("prompt_tokens", 0),
            "output_tokens": u.get("completion_tokens", 0),
            "total_tokens": u.get("total_tokens", 0),
            "reasoning_tokens": u.get("completion_tokens_details", {}).get("reasoning_tokens", 0),
            "cached_tokens": u.get("prompt_tokens_details", {}).get("cached_tokens", 0),
        }

    # ── 通用方法 ────────────────────────────────────────────────────

    def _resolve_prompt(self, mode_key: str, user_prompt: str) -> str:
        """组装最终提示词: 系统预设 + 用户指令"""
        sp = _SP_MAP.get(mode_key, SP_VISION)
        if not user_prompt or not user_prompt.strip():
            if mode_key.endswith("-to-text"):
                return sp + "\n请详细描述该内容。"
            return sp + "\n请根据内容生成对应的前端代码（HTML+TailwindCSS）。"
        return sp + f"\n\n用户指令: {user_prompt}"

    def _extract_tokens(self, res: Dict) -> Dict:
        u = res.get("usage", {})
        return {
            "input_tokens": u.get("input_tokens", 0),
            "output_tokens": u.get("output_tokens", 0),
            "total_tokens": u.get("total_tokens", 0),
            "reasoning_tokens": u.get("output_tokens_details", {}).get("reasoning_tokens", 0),
            "cached_tokens": u.get("input_tokens_details", {}).get("cached_tokens", 0),
        }

    def _extract_text(self, res: Dict) -> str:
        for o in res.get("output", []):
            if o.get("type") == "message":
                for c in o.get("content", []):
                    if c.get("type") == "output_text":
                        return c.get("text", "")
        return ""

    def process(self, file_path: str, input_type: str, output_type: str, prompt: str = "") -> Dict:
        """主处理流程: 编码→遍历降级链→调用API(Doubao/GLM)→成功后记录"""
        self._cleanup_temp()
        mode = _MODE_MAP.get((input_type, output_type))
        if not mode:
            return {"success": False, "error": "无效参数组合，需 --image/--video + --text/--code"}
        if not file_path or not Path(file_path).is_file():
            return {"success": False, "error": "请提供图片/视频文件路径。"}
        try:
            data_uri, tmp_path, media = self._encode_media(file_path, input_type)
        except (FileNotFoundError, ValueError) as e:
            return {"success": False, "error": str(e)}
        md = _MODES[mode]
        full_prompt = self._resolve_prompt(mode, prompt)
        sp = _SP_MAP.get(mode, SP_VISION)

        print(f"\n🔍 {md['label']}")
        print(f"   文件: {Path(file_path).name} ({media})")
        if prompt:
            print(f"   指令: {prompt[:80]}...")

        last_error = ""
        for mk in _MODES[mode]["chain"]:
            spec = _MODELS[mk]
            if not spec["id"] or spec["id"].strip() == "*":
                continue
            if _PROVIDER_MODE == 2 and spec["provider"] == "zhipu":
                continue
            if self.history.get_daily(spec["name"]) >= DAILY_LIMIT:
                continue
            model = {"key": mk, "name": spec["name"], "id": spec["id"],
                     "provider": spec["provider"], "retries": spec.get("retries", 0)}
            provider = model["provider"]
            print(f"   → {model['name']} ({provider})")

            if provider == "zhipu":
                blocks = self._build_zhipu_blocks(media, data_uri, full_prompt, sp)
                messages = [{"role": "user", "content": blocks}]
                result, error = self._zhipu_call(model, messages, retries=model["retries"])
                if result is None:
                    print(f"   ✗ {model['name']}: {error[:80]}")
                    last_error = error
                    continue
                tokens = self._extract_zhipu_tokens(result)
                text = self._extract_zhipu_text(result)
                resp_id = result.get("id", "")
                self._save_glm_context(resp_id, model["id"], input_type, file_path,
                                        messages, text, mode)
            else:
                thinking_cfg = {"type": "enabled", "reasoning_effort": _REASONING_EFFORT[mode]}
                doubao_blocks = self._build_blocks(media, data_uri, full_prompt, output_type)
                headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
                payload = {"model": model["id"], "input": [{"role": "user", "content": doubao_blocks}],
                           "thinking": thinking_cfg, "caching": {"type": "enabled"}}
                try:
                    st, body = self._post(API_URL, headers, json.dumps(payload).encode("utf-8"))
                except Exception as e:
                    print(f"   ✗ {model['name']}: {e}")
                    last_error = f"{type(e).__name__}: {e}"
                    continue
                if st != 200:
                    last_error = f"HTTP {st}"
                    print(f"   ✗ {model['name']}: HTTP {st}")
                    continue
                result = json.loads(body)
                tokens = self._extract_tokens(result)
                text = self._extract_text(result)
                resp_id = result.get("id", "")
                self._save_last_resp(resp_id, model["id"], input_type, file_path, provider)

            new_total = self.history.add_tokens(model["name"], tokens["total_tokens"])
            ts = time.time()
            self.history.add_record({
                "timestamp": ts, "datetime": datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S"),
                "mode": mode, "model": model["name"], "model_id": model["id"],
                "provider": provider,
                "file": file_path, "prompt": prompt or "(auto)",
                "input_tokens": tokens["input_tokens"], "output_tokens": tokens["output_tokens"],
                "total_tokens": tokens["total_tokens"], "reasoning_tokens": tokens["reasoning_tokens"],
                "cached_tokens": tokens["cached_tokens"], "response": text[:500],
            })
            limit = -1 if provider == "zhipu" else DAILY_LIMIT
            remaining = -1 if provider == "zhipu" else DAILY_LIMIT - new_total
            return {
                "success": True, "mode": mode, "model": model["name"],
                "file": file_path, "prompt": prompt or "(auto)", "tokens": tokens,
                "total_today": new_total, "limit": limit,
                "remaining": remaining, "response": text, "resp_id": resp_id,
            }

        return {"success": False,
                "error": f"模式 {md['label']} 全部模型失败: {last_error or '无可用模型'}"}

    def _save_last_resp(self, resp_id: str, model_id: str, input_type: str, file_path: str,
                         provider: str = "doubao"):
        """保存最近一次响应的上下文，用于追问"""
        try:
            data = {"resp_id": resp_id, "model_id": model_id,
                    "input_type": input_type, "file": file_path,
                    "provider": provider, "ts": time.time()}
            tmp = LAST_RESP_FILE.with_suffix(".json.tmp")
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            tmp.replace(LAST_RESP_FILE)
        except Exception:
            pass

    def _save_glm_context(self, resp_id: str, model_id: str, input_type: str,
                           file_path: str, messages: List[Dict], assistant_text: str,
                           mode: str):
        """保存 GLM 多轮对话上下文（消息历史 + 最后回复），用于追问"""
        try:
            data = {"resp_id": resp_id, "model_id": model_id,
                    "input_type": input_type, "file": file_path,
                    "provider": "zhipu", "mode": mode,
                    "messages": messages,
                    "last_text": assistant_text,
                    "ts": time.time()}
            tmp = LAST_RESP_FILE.with_suffix(".json.tmp")
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            tmp.replace(LAST_RESP_FILE)
        except Exception:
            pass

    def _load_last_resp(self) -> Optional[Dict]:
        try:
            if LAST_RESP_FILE.exists():
                with open(LAST_RESP_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
        except Exception:
            pass
        return None

    def follow_up(self, output_type: str, prompt: str) -> Dict:
        """追问功能: Doubao用previous_response_id，GLM用消息历史"""
        last = self._load_last_resp()
        if not last or not last.get("resp_id"):
            return {"success": False, "error": "没有可追问的记录，请先使用 rec 命令识别文件"}
        input_type = last.get("input_type", "image")
        mode = _MODE_MAP.get((input_type, output_type))
        if not mode:
            return {"success": False, "error": "无效输出类型，需 --text 或 --code"}
        md = _MODES[mode]
        provider = last.get("provider", "doubao")
        orig_model_id = last.get("model_id", "")
        orig_model_name = ""
        retries = 0
        for spec in _MODELS.values():
            if spec["id"] == orig_model_id:
                orig_model_name = spec["name"]
                retries = spec.get("retries", 0)
                break
        if not orig_model_name:
            orig_model_name = orig_model_id
        sp = _SP_MAP.get(mode, SP_VISION)

        fn = Path(last.get("file", "")).name
        print(f"\n💬 追问 [{md['label']}]")
        print(f"   模型: {orig_model_name} ({provider})")
        print(f"   上次: {fn} ({input_type})")
        print(f"   指令: {prompt[:80]}...")

        if provider == "zhipu":
            # GLM: 用消息历史维持多轮对话
            history_msgs = list(last.get("messages", []))
            history_msgs.append({"role": "assistant", "content": last.get("last_text", "")})
            history_msgs.append({"role": "user", "content": sp + "\n" + prompt})
            result, error = self._zhipu_call({"id": orig_model_id, "name": orig_model_name},
                                             history_msgs, retries=retries)
            if result is None:
                return {"success": False, "error": error, "model": orig_model_name}
            tokens = self._extract_zhipu_tokens(result)
            text = self._extract_zhipu_text(result)
            new_resp_id = result.get("id", "")
            api_err = ""
            self._save_glm_context(new_resp_id, orig_model_id, input_type,
                                    last.get("file", ""), history_msgs, text, mode)
        else:
            # Doubao: previous_response_id + 缓存
            if self.history.get_daily(orig_model_name) >= DAILY_LIMIT:
                return {"success": False, "error": f"原始模型 {orig_model_name} 今日已超限，请明天再试或用 rec 重新开始"}
            thinking_cfg = {"type": "enabled", "reasoning_effort": _REASONING_EFFORT[mode]}
            headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
            payload = {
                "model": orig_model_id,
                "previous_response_id": last["resp_id"],
                "input": [
                    {"role": "system", "content": [{"type": "input_text", "text": sp}]},
                    {"role": "user", "content": [{"type": "input_text", "text": prompt}]},
                ],
                "thinking": thinking_cfg,
                "caching": {"type": "enabled"},
            }
            try:
                st, body = self._post(API_URL, headers, json.dumps(payload).encode("utf-8"))
            except Exception as e:
                return {"success": False, "error": f"API 调用失败: {type(e).__name__}: {e}",
                        "model": orig_model_name}
            if st != 200:
                try:
                    detail = json.loads(body)
                except Exception:
                    detail = body[:500]
                return {"success": False, "error": f"API 请求失败 (HTTP {st})",
                        "model": orig_model_name, "detail": str(detail)[:500]}
            result = json.loads(body)
            tokens = self._extract_tokens(result)
            text = self._extract_text(result)
            new_resp_id = result.get("id", "")
            api_err = ""
            self._save_last_resp(new_resp_id, orig_model_id, input_type,
                                  last.get("file", ""), provider)

        new_total = self.history.add_tokens(orig_model_name, tokens["total_tokens"])
        ts = time.time()
        self.history.add_record({
            "timestamp": ts, "datetime": datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S"),
            "mode": mode, "model": orig_model_name, "model_id": orig_model_id,
            "provider": provider,
            "file": last.get("file", ""), "prompt": prompt,
            "input_tokens": tokens["input_tokens"], "output_tokens": tokens["output_tokens"],
            "total_tokens": tokens["total_tokens"], "reasoning_tokens": tokens["reasoning_tokens"],
            "cached_tokens": tokens["cached_tokens"], "response": text[:500],
            "follow_up": True, "prev_resp_id": last["resp_id"],
        })
        limit = -1 if provider == "zhipu" else DAILY_LIMIT
        remaining = -1 if provider == "zhipu" else DAILY_LIMIT - new_total
        return {
            "success": True, "mode": mode, "model": orig_model_name,
            "file": last.get("file", ""), "prompt": prompt, "tokens": tokens,
            "total_today": new_total, "limit": limit,
            "remaining": remaining, "response": text, "resp_id": new_resp_id,
        }

    def get_status(self):
        return self.history.get_status()

    def get_history(self):
        return self.history.get_history()

    def sync_console(self):
        if not self._console.enabled:
            return {"error": "IAM 密钥未配置"}
        self._console._last_sync = 0
        return self._console.sync_to_local(self.history)


def _fmt_wan(val: int) -> str:
    w = val / 10_000
    return f"{w:.0f}W" if w == int(w) else f"{w:.2f}W"


def _parse_flags(args: List[str]) -> Tuple[List[str], Dict[str, str]]:
    flags: Dict[str, str] = {}
    rest: List[str] = []
    i = 0
    while i < len(args):
        if args[i] in ("--prompt", "-p") and i + 1 < len(args):
            flags["prompt"] = args[i + 1]; i += 2
        elif args[i] == "--video":
            flags["input_type"] = "video"; i += 1
        elif args[i] == "--image":
            flags["input_type"] = "image"; i += 1
        elif args[i] == "--text":
            flags["output_type"] = "text"; i += 1
        elif args[i] == "--code":
            flags["output_type"] = "code"; i += 1
        elif args[i] == "--batch":
            flags["batch"] = "true"; i += 1
        else:
            rest.append(args[i]); i += 1
    return rest, flags


def _display_width(text: str) -> int:
    """计算字符串在终端中的显示宽度（CJK + emoji 计 2 列）"""
    w = 0
    for ch in text:
        w += 2 if unicodedata.east_asian_width(ch) in ('W', 'F') else 1
    return w


def _center_text(text: str, width: int) -> str:
    """居中字符串，按显示宽度对齐"""
    dw = _display_width(text)
    left = (width - dw) // 2
    right = width - dw - left
    return ' ' * left + text + ' ' * right


def _print_usage():
    W = 60  # box inner width
    hr = '═' * W
    title1 = _center_text('ByteDance Visual Recognition v4.2.0', W)
    title2 = _center_text('火山方舟 豆包多模态视觉识别 + 代码生成', W)
    print(f"""
╔{hr}╗
║{title1}║
║{title2}║
╚{hr}╝

【命令】
  rec <文件/目录> [参数]    识别或批量处理
  ask [参数]                追问上次识别结果(无需重新上传文件)
  status                    查看状态/用量
  sync                      手动控制台同步
  history                   7天调用历史

【参数 - rec】
  --image          输入为图片
  --video          输入为视频
  --text           输出为文字
  --code           输出为代码
  --prompt, -p     一级提示词(可选)
  --batch          批量处理目录下所有媒体文件

【参数 - ask】
  --text           输出为文字
  --code           输出为代码
  --prompt, -p     追问内容

【模型选择】
  每模型每天 180W tokens超过自动降级，不支持指定模型
  img-to-text    图片→文字  Doubao*6 → GLM-4.6V-Flash → GLM-4.1V-Thinking
  video-to-text  视频→文字  Doubao*6 → GLM-4.6V-Flash → GLM-4.1V-Thinking
  img-to-code    图片→代码  Doubao*5 → GLM-4.6V-Flash → GLM-4.1V-Thinking
  video-to-code  视频→代码  Doubao*5 (GLM 不支持视频转代码)

  当所有豆包模型不可用时，自动切换 GLM 免费模型。

【示例】
  rec photo.jpg --image --text
  rec photo.jpg --image --code
  rec video.mp4 --video --text
  rec video.mp4 --video --code
  rec photo.jpg --image --text --prompt "提取所有文字"
  rec ./images/ --batch --image --text

  # 追问(基于上次rec的结果，无需重新上传) 例：
  ask --text --prompt "图片的详细内容是？"
  ask --code --prompt "将图片转代码"
  ask --code --prompt "用React实现"
""")


def _print_status_header(vr: DoubaoVisionRecognizer):
    vr._auto_sync()
    st = vr.get_status()
    print(f"\n📊 {st['date']}")
    total_w = 56
    for m in st["models"]:
        if not m["configured"]:
            amount = "-W/-W"
        elif m["unlimited"]:
            amount = _fmt_wan(m["tokens"])
        else:
            amount = f"{_fmt_wan(m['tokens'])}/{_fmt_wan(m['limit'])}"
        icon = "🔴" if (not m["configured"]) else ("🔴" if m["tokens"] >= (10_000_000 if m["unlimited"] else m["limit"]) else "🟢")
        prefix = f"   {icon} {m['name']}"
        print(f"{prefix}{' ' * (total_w - _display_width(prefix) - len(amount))}{amount}")


def _print_result(result: Dict):
    if result["success"]:
        label = _MODES.get(result.get("mode", ""), {}).get("label", result.get("mode", ""))
        print(f"\n✅ 成功! [{label}]")
        print(f"   模型:    {result['model']}")
        t = result["tokens"]
        print(f"   Token:   输入 {t['input_tokens']} | 输出 {t['output_tokens']} | 推理 {t['reasoning_tokens']}")
        print(f"   本次:    {t['total_tokens']}")
        if result.get("limit", DAILY_LIMIT) < 0:
            print(f"   今日:    {_fmt_wan(result['total_today'])}")
        else:
            print(f"   今日:    {_fmt_wan(result['total_today'])} / {_fmt_wan(result['limit'])}")
            print(f"   剩余:    {_fmt_wan(result['remaining'])}")
        print(f"\n{'─' * 56}")
        print(f"📝 结果:\n{result['response']}")
    else:
        print(f"\n❌ 失败: {result.get('error', '未知错误')}")
        if "detail" in result:
            print(f"   详情: {result['detail']}")


def _cmd_status():
    vr = DoubaoVisionRecognizer()
    st = vr.get_status()
    print(f"\n📊 今日状态 ({st['date']})")
    print(f"   识别记录总数: {st['total_history']}")
    print(f"   {'─' * 56}")
    total_w = 56
    for m in st["models"]:
        if not m["configured"]:
            amount = "-W/-W"
        elif m["unlimited"]:
            amount = _fmt_wan(m["tokens"])
        else:
            amount = f"{_fmt_wan(m['tokens'])}/{_fmt_wan(m['limit'])}"
        icon = "🔴" if (not m["configured"]) else ("🔴" if m["tokens"] >= (10_000_000 if m["unlimited"] else m["limit"]) else "🟢")
        extra = "" if not (m["configured"] and not m["unlimited"]) else f" (剩余: {_fmt_wan(m['limit'] - m['tokens'])})"
        prefix = f"   {icon} {m['name']}"
        print(f"{prefix}{' ' * (total_w - _display_width(prefix) - len(amount) - len(extra))}{amount}{extra}")
    tu = sum(m["tokens"] for m in st["models"] if m["configured"])
    tl = sum(m["limit"] for m in st["models"] if m["configured"] and not m["unlimited"])
    print(f"   {'─' * 56}")
    print(f"   可配模型总计: {_fmt_wan(tu)} / {'∞W' if any(m['unlimited'] for m in st['models'] if m['configured']) else _fmt_wan(tl) + ' tokens'}")
    print(f"\n📋 模式:")
    for mk, md in _MODES.items():
        chain = " -> ".join(_MODELS[k]["name"] for k in md["chain"])
        print(f"   {mk:14s} {md['label']:8s} {chain}")


def _cmd_sync():
    vr = DoubaoVisionRecognizer()
    if not vr._console.enabled:
        print("❌ IAM 密钥未配置")
        return
    print("\n🔄 控制台用量同步中...")
    before = {m["name"]: m["tokens"] for m in vr.get_status()["models"]}
    result = vr.sync_console()
    if not result:
        print("⚠️ 控制台返回无数据，保持本地计数")
        return
    print("\n   对比 (本地 -> 控制台):")
    after = vr.get_status()
    for m in after["models"]:
        action = result.get(m["name"], "?")
        icon = "🔄" if action == "synced" else "📌"
        print(f"   {icon} {m['name']:<24s} {_fmt_wan(before.get(m['name'], 0))} -> {_fmt_wan(m['tokens'])} ({action})")


def _cmd_history():
    vr = DoubaoVisionRecognizer()
    records = vr.get_history()
    print(f"\n📋 历史记录 (共 {len(records)} 条, 保留 {RETENTION_DAYS} 天)")
    print(f"   {'─' * 64}")
    for r in records[-20:]:
        print(f"   🔍 {r.get('datetime', '?')} | {r.get('mode', '?')} | {r.get('model', '?')}")
        fn = Path(r.get('file', '')).name if r.get('file') else '(无文件)'
        print(f"      文件: {fn}")
        print(f"      Token: 入{r.get('input_tokens', 0)} 出{r.get('output_tokens', 0)} 推理{r.get('reasoning_tokens', 0)}")


def _cmd_batch(args: List[str], flags: Dict[str, str]):
    if not args:
        print("❌ 请提供目录路径")
        return
    dp = Path(args[0])
    if not dp.is_dir():
        print(f"❌ 目录不存在: {dp}")
        return
    td = _today_dir()
    bd = td / f"batch_{dp.name}_{hashlib.md5(str(dp).encode()).hexdigest()[:12]}"
    if bd.exists():
        shutil.rmtree(bd)
    bd.mkdir(parents=True, exist_ok=True)
    # 仅复制支持的媒体文件，不复制整个目录
    files = sorted(f for f in dp.iterdir() if f.is_file() and f.suffix.lower() in _MEDIA_EXT)
    if not files:
        print(f"❌ 目录中没有支持的媒体文件: {dp}")
        return
    for f in files:
        shutil.copy2(f, bd / f.name)
    print(f"📁 已复制 {len(files)} 个媒体文件到 Temp: {bd}")
    input_type = flags.get("input_type", "")
    output_type = flags.get("output_type", "")
    prompt = flags.get("prompt", "")
    vr = DoubaoVisionRecognizer()
    _print_status_header(vr)
    mode_label = f"{input_type}->{output_type}" if input_type else output_type
    print(f"\n📁 批量处理: {len(files)} 个文件 (模式: {mode_label})")
    ok, fail, total = 0, 0, 0
    for i, f in enumerate(files, 1):
        print(f"\n[{i}/{len(files)}] {f.name}")
        result = vr.process(str(f), input_type=input_type, output_type=output_type, prompt=prompt)
        if result["success"]:
            ok += 1
            total += result["tokens"]["total_tokens"]
            print(f"   ✅ {result['model']} | tokens: {result['tokens']['total_tokens']}")
            rp = result.get("response", "")[:120]
            if rp:
                print(f"   💬 {rp}...")
        else:
            fail += 1
            print(f"   ❌ {result.get('error', '未知错误')}")
            if "超限" in result.get("error", ""):
                print("   ⚠️ 全部模型超限，停止批量处理")
                break
    print(f"\n{'─' * 56}")
    print(f"📊 批量完成: 成功 {ok}, 失败 {fail}")
    print(f"   Token 消耗: {total}")


def main():
    if len(sys.argv) < 2:
        _print_usage()
        return
    arg1 = sys.argv[1]
    if arg1 in ("--help", "-h"):
        _print_usage()
        return
    sub = arg1.lower()
    if sub == "status":
        _cmd_status()
    elif sub == "sync":
        _cmd_sync()
    elif sub == "history":
        _cmd_history()
    elif sub == "rec":
        rest, flags = _parse_flags(sys.argv[2:])
        if not rest:
            print("❌ 请提供文件或目录路径")
            print("   用法: rec <路径> --image|--video --text|--code [--prompt \"...\"] [--batch]")
            return
        it = flags.get("input_type", "")
        ot = flags.get("output_type", "")
        if not it:
            print("❌ 必须指定输入类型: --image 或 --video")
            return
        if not ot:
            print("❌ 必须指定输出类型: --text 或 --code")
            return
        target = rest[0]
        if flags.get("batch") == "true":
            _cmd_batch([target], flags)
            return
        vr = DoubaoVisionRecognizer()
        _print_status_header(vr)
        _print_result(vr.process(target, input_type=it, output_type=ot, prompt=flags.get("prompt", "")))
    elif sub == "ask":
        rest, flags = _parse_flags(sys.argv[2:])
        ot = flags.get("output_type", "")
        prompt = flags.get("prompt", "")
        if not ot:
            print("❌ 必须指定输出类型: --text 或 --code")
            return
        if not prompt:
            print("❌ 追问必须提供 --prompt 内容")
            print("   用法: ask --text|--code --prompt \"追问内容\"")
            return
        vr = DoubaoVisionRecognizer()
        _print_status_header(vr)
        _print_result(vr.follow_up(output_type=ot, prompt=prompt))
    else:
        print(f"❌ 未知命令: {arg1}")
        print("   可用命令: rec, ask, status, sync, history")
        print("   使用 --help 查看帮助")


if __name__ == "__main__":
    main()
