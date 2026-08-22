"""
edge_cloud_dispatch.py - V7 绔簯鍗忓悓鍗忚 v1.0 鐨?Python 绔晶 SDK 鍙傝€冨疄鐜般€?

杩欐槸 references/edge-cloud-protocol.md + edge-cloud-protocol-schema.json 鐨勯涓?
Python 钀藉湴瀹炵幇锛屾彁渚涳細
  - build_request()         鏋勫缓 6 娈佃姹傜粨鏋勶紙8 涓?required 瀛楁锛?
  - validate_request()      鐢?jsonschema + schema 鏂囦欢鏍￠獙
  - check_abstract_data_size()  abstract_data < 10KB 绾︽潫锛圴7 搂4.1锛孍002锛?
  - EdgeCloudClient         绔簯浜ゆ崲瀹㈡埛绔紙PII 鑴辨晱 + 鎴愭湰鐩戞帶 + 5 绾ч檷绾?+ 鐔旀柇锛?
  - 閿欒鐮佹槧灏?E001~E202锛圴7 搂6锛?

璁捐鍝插锛堢户鎵胯嚜 video-editing-skill锛夛細
  - 閲嶆椿绔晶鍋氾紙PII 鑴辨晱 / 澶у皬鎴柇 / 瑙勫垯鏍￠獙閮藉湪绔晶瀹屾垚锛?
  - 鍐崇瓥浜戠鍋氾紙exchange 鎶婃娊璞℃暟鎹彂缁欎簯绔嬁鍐崇瓥锛?
  - JSON 濂戠害鍋氭帴缂濓紙6 娈佃姹傜粨鏋勫氨鏄浜戣竟鐣岋級
  - 瑙勫垯灞傚仛瀹归敊锛坙esson_plan_guard 鍦ㄥ悎鎴愬墠鏍￠獙浜戠杩斿洖锛?

鐢ㄦ硶锛?
    from edge_cloud_dispatch import EdgeCloudClient, build_request

    client = EdgeCloudClient(transport=my_http_transport)
    req = build_request(
        intent="涓洪珮涓€AI閫氳瘑璇剧紪鎺掓暀瀛﹁矾寰?,
        task_type="learning_path_planning",
        context="鏈哄櫒瀛︿範鍏ラ棬妯″潡",
        abstract_data={"segments": [...]},
        decision_type="educational",
        max_tokens=2000,
        max_cost_usd=0.001,
    )
    response = client.exchange(req)
"""
from __future__ import annotations
__version__ = "8.1.0-aipc"  # V8.1-AIPC: 每次工作自动输出本地/云端对比 + 全互动控件完整性门控


# --- UTF-8 stdout/stderr (Windows 涓枃杈撳嚭闃蹭贡鐮? -----------------------------
def _configure_stream_encoding(stream):
    reconfigure = getattr(stream, "reconfigure", None)
    if callable(reconfigure):
        reconfigure(encoding="utf-8")

import sys as _sys
_configure_stream_encoding(_sys.stdout)
_configure_stream_encoding(_sys.stderr)
del _sys
# ----------------------------------------------------------------------------

from log_util import get_logger

log = get_logger("edge_cloud")

import json
import os
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Optional

# 绔晶鑴氭湰鐩綍瑙ｆ瀽
SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
SCHEMA_PATH = SKILL_DIR / "references" / "edge-cloud-protocol-schema.json"

# V7 鍗忚甯搁噺
PROTOCOL_VERSION = "1.0"
DEFAULT_SOURCE = "edge-ai-pc"
ABSTRACT_DATA_MAX_BYTES = 10240  # 10KB锛圴7 搂4.1锛?

# 5 绾ч檷绾ч槇鍊硷紙V7 搂7.2锛?
TIMEOUT_LEVEL_2_THRESHOLD = 3   # 杩炵画 3 娆¤秴鏃?鈫?Level 2
TIMEOUT_LEVEL_3_THRESHOLD = 5   # 杩炵画 5 娆¤秴鏃?鈫?Level 3


# ---------------------------------------------------------------------------
# 閿欒鐮佹槧灏勶紙V7 搂6 閿欒鐮佽〃 E001~E202锛?
# ---------------------------------------------------------------------------

ERROR_CODES: dict[str, str] = {
    "E001": "鍗忚鐗堟湰涓嶅尮閰?,
    "E002": "abstract_data 瓒呰繃 10KB 闄愬埗",
    "E003": "PII 妫€娴嬫湭閫氳繃锛坧ii_detected 涓嶄负 false锛?,
    "E004": "鏁版嵁鍒嗙被闈炴硶鎴栧繀濉瓧娈电己澶?,
    "E101": "浜戠璇锋眰瓒呮椂",
    "E102": "浜戠闄愭祦锛坮ate limit锛?,
    "E103": "浜戠鍐呴儴閿欒锛?xx锛?,
    "E201": "绔晶鎵ц澶辫触",
    "E202": "鎴愭湰鐔旀柇瑙﹀彂锛坈umulative_cost_usd >= monthly_budget锛?,
}


def error_response(
    request_id: str,
    code: str,
    message: str,
    suggestion: str = "",
    retry_after: int = 0,
    degradation_level: int = 1,
) -> dict:
    """鏋勯€?V7 鍗忚閿欒鍝嶅簲銆?""
    return {
        "protocol_version": PROTOCOL_VERSION,
        "request_id": request_id,
        "timestamp": _utc_now_iso(),
        "status": "error",
        "error": {
            "code": code,
            "message": message,
            "suggestion": suggestion or ERROR_CODES.get(code, ""),
            "retry_after_seconds": retry_after,
        },
        "degradation_level": degradation_level,
    }


# ---------------------------------------------------------------------------
# 宸ュ叿鍑芥暟
# ---------------------------------------------------------------------------

def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _serialize_size(obj: Any) -> int:
    """璁＄畻瀵硅薄 JSON 搴忓垪鍖栧悗鐨?UTF-8 瀛楄妭鏁般€?""
    if obj is None:
        return 0
    if isinstance(obj, bytes):
        return len(obj)
    try:
        return len(json.dumps(obj, ensure_ascii=False).encode("utf-8"))
    except (TypeError, ValueError):
        return len(str(obj).encode("utf-8"))


# ---------------------------------------------------------------------------
# 1. 鏋勫缓 6 娈佃姹?
# ---------------------------------------------------------------------------

def build_request(
    intent: str,
    task_type: str,
    context: str,
    abstract_data: dict,
    decision_type: str,
    max_tokens: int,
    max_cost_usd: float,
    *,
    source: str = DEFAULT_SOURCE,
    pii_detected: bool = False,
    data_classification: str = "anonymous",
    save_to_local: bool = True,
) -> dict:
    """鏋勫缓 V7 绔簯鍗忓悓鍗忚 6 娈佃姹傜粨鏋勩€?

    8 涓?required 瀛楁锛坰chema 瀹氫箟锛夛細
        protocol_version / request_id / timestamp / source / intent / abstract / request / callback
    """
    return {
        "protocol_version": PROTOCOL_VERSION,
        "request_id": str(uuid.uuid4()),
        "timestamp": _utc_now_iso(),
        "source": source,
        "intent": intent[:500],
        "abstract": {
            "task_type": task_type,
            "context": context[:200],
            "abstract_data": abstract_data if isinstance(abstract_data, dict) else {},
            "pii_detected": pii_detected,
            "data_classification": data_classification,
        },
        "request": {
            "decision_type": decision_type,
            "max_tokens": max_tokens,
            "max_cost_usd": max_cost_usd,
        },
        "callback": {
            "edge_execution": True,
            "save_to_local": save_to_local,
        },
    }


# ---------------------------------------------------------------------------
# 2. abstract_data 澶у皬妫€鏌ワ紙V7 搂4.1锛孍002锛?
# ---------------------------------------------------------------------------

def check_abstract_data_size(abstract_data: Any) -> tuple[Any, bool, int]:
    """妫€鏌?abstract_data 鏄惁 < 10KB銆?

    Returns:
        (data, truncated, size_bytes)
        - truncated=True 鏃?data 宸茶鎴柇涓哄彧淇濈暀鍓嶈嫢骞?key
    """
    size = _serialize_size(abstract_data)
    if size < ABSTRACT_DATA_MAX_BYTES:
        return abstract_data, False, size

    # 鎴柇锛氬鏋滄槸 dict锛屽彧淇濈暀鍓?N 涓?key 鐩村埌 < 10KB
    if isinstance(abstract_data, dict):
        keys = list(abstract_data.keys())
        truncated: dict = {}
        for k in keys:
            candidate = dict(truncated)
            candidate[k] = abstract_data[k]
            if _serialize_size(candidate) >= ABSTRACT_DATA_MAX_BYTES:
                break
            truncated = candidate
        truncated["_truncated"] = True
        truncated["_original_size_bytes"] = size
        return truncated, True, _serialize_size(truncated)

    # 瀛楃涓?鍏朵粬锛氱洿鎺ユ埅鏂埌瀹夊叏闀垮害
    if isinstance(abstract_data, str):
        safe = abstract_data[: (ABSTRACT_DATA_MAX_BYTES - 100)]
        return safe + "...[truncated]", True, _serialize_size(safe)

    return abstract_data, True, size


# ---------------------------------------------------------------------------
# 3. 璇锋眰鏍￠獙锛坖sonschema + schema 鏂囦欢锛?
# ---------------------------------------------------------------------------

def _load_schema() -> Optional[dict]:
    """鍔犺浇 edge-cloud-protocol-schema.json銆?""
    if not SCHEMA_PATH.exists():
        return None
    try:
        return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _builtin_validate(request: dict) -> list[str]:
    """schema 鏂囦欢涓嶅彲鐢ㄦ椂鐨勫唴缃熀纭€鏍￠獙銆?""
    errors: list[str] = []
    required = [
        "protocol_version", "request_id", "timestamp", "source",
        "intent", "abstract", "request", "callback",
    ]
    for k in required:
        if k not in request:
            errors.append(f"缂哄皯蹇呭～瀛楁锛歿k}")

    if request.get("protocol_version") != PROTOCOL_VERSION:
        errors.append(f"protocol_version 蹇呴』涓?{PROTOCOL_VERSION}")

    abstract = request.get("abstract") or {}
    if not isinstance(abstract, dict):
        errors.append("abstract 蹇呴』涓哄璞?)
    else:
        for k in ("task_type", "context", "abstract_data", "pii_detected", "data_classification"):
            if k not in abstract:
                errors.append(f"abstract 缂哄皯蹇呭～瀛楁锛歿k}")
        if abstract.get("pii_detected") not in (False, True):
            errors.append("pii_detected 蹇呴』涓哄竷灏斿€?)

    req = request.get("request") or {}
    if not isinstance(req, dict):
        errors.append("request 蹇呴』涓哄璞?)
    else:
        for k in ("decision_type", "max_tokens", "max_cost_usd"):
            if k not in req:
                errors.append(f"request 缂哄皯蹇呭～瀛楁锛歿k}")

    cb = request.get("callback") or {}
    if not isinstance(cb, dict):
        errors.append("callback 蹇呴』涓哄璞?)
    elif cb.get("edge_execution") is not True:
        errors.append("callback.edge_execution 蹇呴』涓?true")

    return errors


def validate_request(request: dict) -> tuple[bool, list[str]]:
    """鏍￠獙璇锋眰鏄惁绗﹀悎 V7 鍗忚 schema銆?

    Returns:
        (passed, errors)
    """
    if not isinstance(request, dict):
        return False, ["request 蹇呴』涓?dict 绫诲瀷"]

    schema = _load_schema()
    if schema is None:
        return (len(_builtin_validate(request)) == 0), _builtin_validate(request)

    try:
        import jsonschema
        from jsonschema import Draft202012Validator
        # schema 鏂囦欢鐢?"$defs" + 椤跺眰 "Request" 瀹氫箟
        request_schema = {
            "$schema": schema.get("$schema", "https://json-schema.org/draft/2020-12/schema"),
            **schema.get("Request", {}),
        }
        # 鍚堝苟 $defs锛坖sonschema 闇€瑕侊級
        if "$defs" in schema:
            request_schema["$defs"] = schema["$defs"]
        Draft202012Validator(request_schema).validate(request)
        return True, []
    except ImportError:
        return (len(_builtin_validate(request)) == 0), _builtin_validate(request)
    except Exception as exc:
        return False, [f"schema 鏍￠獙澶辫触锛歿exc}"]


# ---------------------------------------------------------------------------
# 4. EdgeCloudClient锛堢浜戜氦鎹㈠鎴风锛?
# ---------------------------------------------------------------------------

Transport = Callable[[dict], dict]


class EdgeCloudClient:
    """绔簯鍗忓悓鍗忚瀹㈡埛绔€?

    闆嗘垚 4 椤圭渚х‖绾︽潫锛圴7 鏍稿績瑕佹眰锛夛細
      1. PII 鑷姩鑴辨晱锛堣皟鐢?pii_redactor.redact_abstract_data锛?
      2. abstract_data < 10KB 鎴柇锛坈heck_abstract_data_size锛?
      3. 鎴愭湰鐩戞帶涓庣啍鏂紙cost_monitor.CostMonitor锛?
      4. 5 绾ч檷绾х姸鎬佹満锛圴7 搂7.2锛?

    Args:
        transport:  绔簯浼犺緭鍑芥暟 transport(request_dict) -> response_dict銆?
                    娴嬭瘯鏃跺彲娉ㄥ叆 mock锛涚敓浜х幆澧冮粯璁ょ敤 _default_http_transport銆?
        cost_monitor: 鎴愭湰鐩戞帶瀵硅薄锛坉uck-typing锛歳ecord_cost / check_circuit_breaker锛?
        schema_path:  schema 鏂囦欢璺緞锛堥粯璁?references/edge-cloud-protocol-schema.json锛?
        npu_available: NPU 鏄惁鍙敤锛堝奖鍝嶉檷绾?Level 4锛?
        request_timeout: 鍗曟浜戠璇锋眰瓒呮椂绉掓暟
    """

    def __init__(
        self,
        transport: Optional[Transport] = None,
        cost_monitor: Any = None,
        schema_path: Optional[Path] = None,
        npu_available: bool = True,
        request_timeout: float = 30.0,
    ) -> None:
        self.transport: Transport = transport or _default_http_transport
        self.cost_monitor = cost_monitor
        self.schema_path = Path(schema_path) if schema_path else SCHEMA_PATH
        self.npu_available = npu_available
        self.request_timeout = request_timeout

        # 闄嶇骇鐘舵€佹満
        self.consecutive_timeouts: int = 0
        self.degradation_level: int = 1
        self._circuit_breaker_active: bool = False
        # V7-AIPC 鍗囩骇锛氭媶鍒嗕负 connect/read timeout锛圴7.3.2 鏀硅繘2 鍗囩骇鐗堬級锛屽 provider 閫傞厤 + work_summary 鑷姩璁板綍
        self.connect_timeout: float = 5.0
        self.read_timeout: float = request_timeout

        # 鍒濆鍖栨椂鏍规嵁 NPU 鍙敤鎬ц绠楅檷绾х骇鍒?
        prev_level = 1
        self._recompute_degradation_level()
        if self.degradation_level != prev_level:
            self._report_degradation(
                reason="init_npu" if not npu_available else "init",
            )

    # ---- 闄嶇骇鐘舵€佹満 ----

    def _recompute_degradation_level(self) -> None:
        """鏍规嵁杩炵画瓒呮椂鏁?/ NPU 鍙敤鎬?/ 鐔旀柇鐘舵€侀噸绠楅檷绾х骇鍒€?""
        if self._circuit_breaker_active:
            self.degradation_level = 5
            return
        if not self.npu_available:
            self.degradation_level = 4
            return
        if self.consecutive_timeouts >= TIMEOUT_LEVEL_3_THRESHOLD:
            self.degradation_level = 3
            return
        if self.consecutive_timeouts >= TIMEOUT_LEVEL_2_THRESHOLD:
            self.degradation_level = 2
            return
        self.degradation_level = 1

    def _report_degradation(self, reason: str = "", request_id: str = "") -> None:
        """V7.3.2 鏀硅繘5锛氫笂鎶ュ綋鍓?degradation_level 鍒?cost_monitor銆?""
        if self.cost_monitor is None:
            return
        record_fn = getattr(self.cost_monitor, "record_degradation", None)
        if callable(record_fn):
            try:
                record_fn(
                    level=self.degradation_level,
                    source="edge_cloud",
                    reason=reason,
                    request_id=request_id,
                )
            except Exception:
                pass

    def _record_timeout(self) -> None:
        self.consecutive_timeouts += 1
        self._recompute_degradation_level()

    def _record_success(self) -> None:
        self.consecutive_timeouts = 0
        self._recompute_degradation_level()

    def _check_circuit_breaker(self) -> bool:
        """妫€鏌ユ垚鏈啍鏂紙V7 搂11.4锛夈€?""
        if self.cost_monitor is None:
            return False
        # duck-typing锛氫紭鍏堣皟鏂规硶
        fn = getattr(self.cost_monitor, "check_circuit_breaker", None)
        if callable(fn):
            try:
                triggered = bool(fn())
            except Exception:
                triggered = False
        else:
            triggered = False
        if triggered:
            self._circuit_breaker_active = True
            self._recompute_degradation_level()
        return triggered

    # ---- PII 鑴辨晱 ----

    def _apply_pii_redaction(self, request: dict) -> tuple[dict, bool]:
        """瀵?abstract_data 閫掑綊 PII 鑴辨晱锛圴7 zero-upload-privacy 4 绾ц劚鏁忥級銆?""
        abstract = request.get("abstract") or {}
        data = abstract.get("abstract_data")
        try:
            from pii_redactor import redact_abstract_data
            redacted, detected = redact_abstract_data(data)
            abstract["abstract_data"] = redacted
            abstract["pii_detected"] = detected
            request["abstract"] = abstract
            return request, detected
        except ImportError:
            return request, abstract.get("pii_detected", False)

    # ---- 涓讳氦鎹㈡祦绋?----

    def exchange(self, request: dict) -> dict:
        """鎵ц涓€娆＄浜戜氦鎹€?

        娴佺▼锛?
          1. schema 鏍￠獙
          2. PII 鑴辨晱
          3. abstract_data 澶у皬妫€鏌?+ 鎴柇
          4. 鎴愭湰鐔旀柇妫€鏌?
          5. 闄嶇骇 Level 5 鏃剁洿鎺ヨ繑鍥炴湰鍦?fallback
          6. 璋?transport 鍙戣姹?
          7. 璁板綍鎴愭湰 / 鏇存柊闄嶇骇鐘舵€?
        """
        request_id = request.get("request_id", str(uuid.uuid4()))

        # 1. schema 鏍￠獙
        passed, errors = validate_request(request)
        if not passed:
            return error_response(
                request_id, "E004",
                f"璇锋眰 schema 鏍￠獙澶辫触锛歿'; '.join(errors[:5])}",
                degradation_level=self.degradation_level,
            )

        # 2. PII 鑴辨晱
        request, pii_detected = self._apply_pii_redaction(request)
        if pii_detected:
            # V7 瑕佹眰 pii_detected 蹇呴』涓?false 鎵嶅厑璁镐笂浼?
            # 鑴辨晱鍚庡凡鏇挎崲涓烘帺鐮侊紝pii_detected 鍙嶆槧"鏄惁鏇炬娴嬪埌"
            # 涓婁紶瀛楁寮哄埗涓?false锛堝凡鑴辨晱锛?
            request["abstract"]["pii_detected"] = False

        # 3. abstract_data 澶у皬妫€鏌?
        abstract = request.get("abstract", {})
        data, truncated, size = check_abstract_data_size(abstract.get("abstract_data"))
        if truncated:
            log.warn(f"[edge-cloud] 鈿?abstract_data 瓒呰繃 10KB锛坽size}B锛夛紝宸茶嚜鍔ㄦ埅鏂?)
            abstract["abstract_data"] = data
            request["abstract"] = abstract
        if size >= ABSTRACT_DATA_MAX_BYTES and not truncated:
            return error_response(
                request_id, "E002",
                f"abstract_data 浣撶Н {size}B 瓒呰繃 10KB 闄愬埗",
                "绔晶鎴柇 abstract_data锛屼粎淇濈暀涓庡喅绛栫浉鍏崇殑鍏抽敭瀛楁",
                degradation_level=self.degradation_level,
            )

        # 4. 鎴愭湰鐔旀柇妫€鏌?
        if self._check_circuit_breaker():
            return error_response(
                request_id, "E202",
                "鎴愭湰鐔旀柇瑙﹀彂锛歝umulative_cost_usd >= monthly_budget",
                "绯荤粺宸插垏鎹㈠埌 Level 5锛堝畬鍏ㄦ湰鍦帮級妯″紡锛岀瓑寰呯鐞嗗憳瑙ｉ櫎",
                degradation_level=5,
            )

        # 5. 闄嶇骇 Level 5锛氬畬鍏ㄦ湰鍦帮紝涓嶈皟浜戠
        if self.degradation_level >= 5:
            return error_response(
                request_id, "E202",
                "褰撳墠闄嶇骇绾у埆 Level 5锛堝畬鍏ㄦ湰鍦帮級锛屼簯绔皟鐢ㄨ绂佺敤",
                "妫€鏌?NPU 鍙敤鎬т笌鎴愭湰棰勭畻鍚庨噸璇?,
                degradation_level=5,
            )

        # 6. 璋?transport 鍙戣姹?
        try:
            response = self.transport(request)
        except TimeoutError:
            self._record_timeout()
            return error_response(
                request_id, "E101",
                f"浜戠璇锋眰瓒呮椂锛坽self.request_timeout}s锛夛紝"
                f"杩炵画瓒呮椂 {self.consecutive_timeouts} 娆?,
                "绯荤粺灏嗚嚜鍔ㄩ檷绾э紝绋嶅悗閲嶈瘯",
                retry_after=min(30, 2 ** self.consecutive_timeouts),
                degradation_level=self.degradation_level,
            )
        except Exception as exc:
            return error_response(
                request_id, "E103",
                f"浜戠鍐呴儴閿欒锛歿exc}",
                "妫€鏌ヤ簯绔湇鍔＄姸鎬佸悗閲嶈瘯",
                degradation_level=self.degradation_level,
            )

        # 7. 璁板綍鎴愭湰 / 鏇存柊闄嶇骇鐘舵€?
        usage = response.get("usage") if isinstance(response, dict) else None
        if isinstance(usage, dict) and self.cost_monitor is not None:
            cost = float(usage.get("cost_usd", 0.0))
            record_fn = getattr(self.cost_monitor, "record_cost", None)
            if callable(record_fn):
                try:
                    record_fn(cost, request_id)
                except Exception:
                    pass
            # 璁板綍鎴愭湰鍚庡啀娆℃鏌ョ啍鏂?
            self._check_circuit_breaker()

        status = response.get("status") if isinstance(response, dict) else None
        if status == "success":
            self._record_success()
        elif status == "error":
            code = (response.get("error") or {}).get("code", "")
            if code == "E101":
                self._record_timeout()
            elif code == "E102":
                # 闄愭祦锛氫篃绠楄秴鏃剁被锛屼絾涓嶅鍔犺繛缁鏁?
                pass

        response.setdefault("cumulative_cost_usd", 0.0)
        return response


# ---------------------------------------------------------------------------
# 榛樿 HTTP transport锛堢敓浜х敤锛屾祴璇曟椂娉ㄥ叆 mock锛?
# ---------------------------------------------------------------------------

# V7.3.2 鏀硅繘1锛氬 provider 閫傞厤锛坥penai-compatible / anthropic / custom锛?
# 浼樺厛绾э細EDGE_CLOUD_PROVIDER 鐜鍙橀噺 > 鏍规嵁 endpoint URL 鎺ㄦ柇
# 鍗忚锛?
#   openai-compatible (default): POST {endpoint} with {"model", "messages", "max_tokens", ...}
#   anthropic: POST {endpoint}/v1/messages with {"model", "max_tokens", "messages", ...}
#   custom: 鐩存帴閫忎紶 V7 6 娈佃姹傦紙鐢ㄤ簬鑷缓 edge-cloud-exchange 鏈嶅姟锛?

_PROVIDER_OPENAI = "openai"
_PROVIDER_ANTHROPIC = "anthropic"
_PROVIDER_CUSTOM = "custom"


def _resolve_provider(endpoint: str) -> str:
    """鏍规嵁 endpoint URL 鎺ㄦ柇 provider 绫诲瀷銆?""
    env = os.environ.get("EDGE_CLOUD_PROVIDER", "").strip().lower()
    if env in (_PROVIDER_OPENAI, _PROVIDER_ANTHROPIC, _PROVIDER_CUSTOM):
        return env
    if "anthropic" in endpoint.lower():
        return _PROVIDER_ANTHROPIC
    return _PROVIDER_OPENAI  # 榛樿 OpenAI-compatible


def _v7_to_openai_request(request: dict) -> dict:
    """V7 6 娈靛崗璁?鈫?OpenAI /chat/completions 鏍煎紡銆?""
    abstract = request.get("abstract") or {}
    intent = request.get("intent", "")
    context = abstract.get("context", "")
    # 鎷艰 system + user 娑堟伅
    system_msg = (
        "浣犳槸 AI 閫氳瘑璇炬暀瀛︿笓瀹躲€俈7 绔簯鍗忓悓鍗忚 v1.0銆俓n"
        f"涓婚锛歿abstract.get('task_type', '')}\n"
        "璇峰熀浜庡厓鏁版嵁锛坅bstract_data锛夎繑鍥炴暀瀛﹀缓璁€?
    )
    user_msg = f"鎰忓浘锛歿intent}\n涓婁笅鏂囷細{context}\n鍏冩暟鎹細{json.dumps(abstract.get('abstract_data', {}), ensure_ascii=False)[:8000]}"
    return {
        "model": os.environ.get("EDGE_CLOUD_MODEL", "gpt-4o-mini"),
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg},
        ],
        "max_tokens": request.get("request", {}).get("max_tokens", 500),
        "temperature": 0.3,
    }


def _openai_to_v7_response(openai_resp: dict, request: dict) -> dict:
    """OpenAI 鍝嶅簲 鈫?V7 6 娈靛搷搴斻€?""
    request_id = request.get("request_id", str(uuid.uuid4()))
    try:
        choice = openai_resp.get("choices", [{}])[0]
        content = choice.get("message", {}).get("content", "")
        usage = openai_resp.get("usage", {})
        # OpenAI usage 涓嶈繑鍥?cost锛岄渶鏍规嵁妯″瀷 + tokens 浼扮畻
        cost = _estimate_openai_cost(usage, request)
        return {
            "protocol_version": PROTOCOL_VERSION,
            "request_id": request_id,
            "timestamp": _utc_now_iso(),
            "status": "success",
            "data": {
                "decision": content,
                "decision_type": request.get("request", {}).get("decision_type", "educational"),
                "model": openai_resp.get("model", "unknown"),
            },
            "usage": {
                "prompt_tokens": usage.get("prompt_tokens", 0),
                "completion_tokens": usage.get("completion_tokens", 0),
                "total_tokens": usage.get("total_tokens", 0),
                "cost_usd": cost,
            },
        }
    except (IndexError, KeyError, TypeError) as e:
        return error_response(
            request_id, "E103", f"OpenAI 鍝嶅簲瑙ｆ瀽澶辫触锛歿e}",
        )


def _estimate_openai_cost(usage: dict, request: dict) -> float:
    """浼扮畻 OpenAI 璋冪敤鎴愭湰锛堝熀浜?usage + 宸茬煡妯″瀷瀹氫环锛夈€?

    鍙傝€?2026-08 浠锋牸琛紙USD / 1K tokens锛夛細
      gpt-4o-mini:        in 0.00015, out 0.0006
      gpt-4o:             in 0.0025,  out 0.01
      deepseek-chat:      in 0.00014, out 0.00028
    """
    model = os.environ.get("EDGE_CLOUD_MODEL", "gpt-4o-mini")
    pricing = {
        "gpt-4o-mini": (0.00015, 0.0006),
        "gpt-4o": (0.0025, 0.01),
        "deepseek-chat": (0.00014, 0.00028),
        "claude-3-5-sonnet": (0.003, 0.015),
    }
    in_rate, out_rate = pricing.get(model, (0.00015, 0.0006))
    prompt = usage.get("prompt_tokens", 0)
    completion = usage.get("completion_tokens", 0)
    return round(prompt * in_rate / 1000 + completion * out_rate / 1000, 6)


def _v7_to_anthropic_request(request: dict) -> dict:
    """V7 6 娈靛崗璁?鈫?Anthropic /v1/messages 鏍煎紡銆?""
    abstract = request.get("abstract") or {}
    intent = request.get("intent", "")
    context = abstract.get("context", "")
    return {
        "model": os.environ.get("EDGE_CLOUD_MODEL", "claude-3-5-sonnet-20241022"),
        "max_tokens": request.get("request", {}).get("max_tokens", 500),
        "messages": [
            {
                "role": "user",
                "content": f"鎰忓浘锛歿intent}\n涓婁笅鏂囷細{context}\n鍏冩暟鎹細{json.dumps(abstract.get('abstract_data', {}), ensure_ascii=False)[:8000]}",
            }
        ],
        "system": "浣犳槸 AI 閫氳瘑璇炬暀瀛︿笓瀹躲€傚熀浜庡厓鏁版嵁杩斿洖鏁欏寤鸿銆?,
    }


def _anthropic_to_v7_response(anthropic_resp: dict, request: dict) -> dict:
    """Anthropic 鍝嶅簲 鈫?V7 6 娈靛搷搴斻€?""
    request_id = request.get("request_id", str(uuid.uuid4()))
    try:
        content_blocks = anthropic_resp.get("content", [])
        text = "".join(b.get("text", "") for b in content_blocks if b.get("type") == "text")
        usage = anthropic_resp.get("usage", {})
        # Anthropic: input_tokens / output_tokens
        prompt = usage.get("input_tokens", 0)
        completion = usage.get("output_tokens", 0)
        cost = _estimate_openai_cost(
            {"prompt_tokens": prompt, "completion_tokens": completion}, request
        )
        return {
            "protocol_version": PROTOCOL_VERSION,
            "request_id": request_id,
            "timestamp": _utc_now_iso(),
            "status": "success",
            "data": {
                "decision": text,
                "decision_type": request.get("request", {}).get("decision_type", "educational"),
                "model": anthropic_resp.get("model", "unknown"),
            },
            "usage": {
                "prompt_tokens": prompt,
                "completion_tokens": completion,
                "total_tokens": prompt + completion,
                "cost_usd": cost,
            },
        }
    except (KeyError, TypeError) as e:
        return error_response(
            request_id, "E103", f"Anthropic 鍝嶅簲瑙ｆ瀽澶辫触锛歿e}",
        )


def _default_http_transport(request: dict) -> dict:
    """榛樿 HTTP transport锛圴7.3.2 澶?provider 鐗堟湰锛夈€?

    鏀寔锛?
      1. openai-compatible: 榛樿锛岄€傜敤浜?OpenAI / DeepSeek / Moonshot / 鏅鸿氨 绛?
      2. anthropic: 閫傜敤浜?Claude 绯诲垪
      3. custom: 鑷缓 edge-cloud-exchange 鏈嶅姟鐨?V7 6 娈甸€忎紶

    鐜鍙橀噺锛?
      EDGE_CLOUD_ENDPOINT   - 浜戠 endpoint URL锛堝繀濉級
      EDGE_CLOUD_PROVIDER   - openai | anthropic | custom锛堥粯璁わ細鎸?URL 鎺ㄦ柇锛?
      EDGE_CLOUD_MODEL      - 妯″瀷鍚嶏紙榛樿锛歡pt-4o-mini锛?
      EDGE_CLOUD_API_KEY    - API 瀵嗛挜锛圓uthorization header锛?
      EDGE_CLOUD_CONNECT_TIMEOUT - 杩炴帴瓒呮椂绉掞紙榛樿 5锛?
      EDGE_CLOUD_READ_TIMEOUT    - 璇诲彇瓒呮椂绉掞紙榛樿 30锛?

    娴嬭瘯鏃朵笉搴斾娇鐢ㄦ transport锛屽簲娉ㄥ叆 mock銆?
    """
    import urllib.request
    import urllib.error
    import socket

    endpoint = os.environ.get("EDGE_CLOUD_ENDPOINT", "")
    if not endpoint:
        raise RuntimeError(
            "鏈缃?EDGE_CLOUD_ENDPOINT 鐜鍙橀噺銆?
            "璇峰湪 run.ps1 / run.sh 涓厤缃簯绔?endpoint URL銆?
        )
    provider = _resolve_provider(endpoint)

    # V7.3.2 鏀硅繘2锛氭媶鍒嗕负 connect_timeout / read_timeout
    connect_timeout = float(os.environ.get("EDGE_CLOUD_CONNECT_TIMEOUT", "5"))
    read_timeout = float(os.environ.get("EDGE_CLOUD_READ_TIMEOUT", "30"))

    api_key = os.environ.get("EDGE_CLOUD_API_KEY", "")

    # 鎸?provider 杞崲璇锋眰
    if provider == _PROVIDER_ANTHROPIC:
        # Anthropic: 鎷兼帴 /v1/messages 璺緞
        url = endpoint.rstrip("/") + "/v1/messages" if not endpoint.endswith("/v1/messages") else endpoint
        provider_payload = _v7_to_anthropic_request(request)
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "anthropic-version": "2023-06-01",
        }
        if api_key:
            headers["x-api-key"] = api_key
    elif provider == _PROVIDER_CUSTOM:
        # Custom: V7 6 娈甸€忎紶
        url = endpoint
        provider_payload = request
        headers = {
            "Content-Type": "application/json; charset=utf-8",
        }
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"
    else:
        # OpenAI-compatible: 鎷兼帴 /v1/chat/completions 璺緞
        url = endpoint.rstrip("/") + "/v1/chat/completions" if not endpoint.endswith("/chat/completions") else endpoint
        provider_payload = _v7_to_openai_request(request)
        headers = {
            "Content-Type": "application/json; charset=utf-8",
        }
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"

    payload = json.dumps(provider_payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req, timeout=connect_timeout) as resp:
            body = resp.read().decode("utf-8")
            provider_resp = json.loads(body)
    except socket.timeout as exc:
        # V7.3.2 鏀硅繘2锛歝onnect_timeout 瓒呮椂鍗曠嫭鍖哄垎锛堢綉缁滃眰 vs 璇诲彇灞傦級
        raise TimeoutError(f"connect_timeout={connect_timeout}s 瑙﹀彂锛歿exc}") from exc
    except urllib.error.HTTPError as exc:
        if exc.code == 429:
            request_id = request.get("request_id", "")
            return error_response(request_id, "E102", "浜戠闄愭祦锛圚TTP 429锛?)
        if exc.code in (401, 403):
            request_id = request.get("request_id", "")
            return error_response(request_id, "E003", f"閴存潈澶辫触 HTTP {exc.code}锛氭鏌?EDGE_CLOUD_API_KEY")
        raise
    except TimeoutError:
        raise
    except Exception as exc:
        raise RuntimeError(f"HTTP transport 澶辫触锛歿exc}") from exc

    # 浜屾璇诲彇瓒呮椂锛坲rllib 涓嶆敮鎸佸崟鐙?read timeout锛屼娇鐢ㄦ暣浣?timeout锛?
    # 娉ㄦ剰锛歅ython urllib 涓嶅尯鍒?connect/read timeout锛涜繖閲岀敤 read_timeout 鍏滃簳
    if provider == _PROVIDER_ANTHROPIC:
        return _anthropic_to_v7_response(provider_resp, request)
    elif provider == _PROVIDER_CUSTOM:
        return provider_resp  # 宸茬粡鏄?V7 6 娈垫牸寮?
    else:
        return _openai_to_v7_response(provider_resp, request)


# ---------------------------------------------------------------------------
# CLI锛堜究浜庢墜鍔ㄦ祴璇曞崟涓姹傦級
# ---------------------------------------------------------------------------

def main(argv: Optional[list[str]] = None) -> int:
    log = get_logger("edge_cloud")
    import argparse

    p = argparse.ArgumentParser(
        prog="edge_cloud_dispatch",
        description="V7 绔簯鍗忓悓鍗忚 Python SDK锛堟瀯寤?+ 鏍￠獙 + 浜ゆ崲锛?,
    )
    sub = p.add_subparsers(dest="cmd")

    p_build = sub.add_parser("build", help="鏋勫缓涓€涓ず渚嬭姹傚苟鎵撳嵃")
    p_build.add_argument("--intent", default="娴嬭瘯璇锋眰")
    p_build.add_argument("--task-type", default="pedagogy_recommendation")
    p_build.add_argument("--json", action="store_true")

    p_val = sub.add_parser("validate", help="鏍￠獙 stdin / 鏂囦欢涓殑璇锋眰 JSON")
    p_val.add_argument("--file", default=None, help="璇锋眰 JSON 鏂囦欢锛堥粯璁よ stdin锛?)

    p_exch = sub.add_parser("exchange", help="鎵ц涓€娆＄浜戜氦鎹紙闇€瑕佷簯绔湇鍔★級")
    p_exch.add_argument("--file", required=True, help="璇锋眰 JSON 鏂囦欢")

    args = p.parse_args(argv)

    if args.cmd == "build":
        req = build_request(
            intent=args.intent,
            task_type=args.task_type,
            context="CLI 娴嬭瘯",
            abstract_data={"note": "this is a test request"},
            decision_type="educational",
            max_tokens=500,
            max_cost_usd=0.001,
        )
        print(json.dumps(req, ensure_ascii=False, indent=2))
        return 0

    if args.cmd == "validate":
        if args.file:
            text = Path(args.file).read_text(encoding="utf-8")
        else:
            text = sys.stdin.read()
        try:
            req = json.loads(text)
        except json.JSONDecodeError as e:
            log.error(f"JSON 瑙ｆ瀽澶辫触锛歿e}")
            return 2
        passed, errors = validate_request(req)
        report = {"passed": passed, "errors": errors, "error_count": len(errors)}
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if passed else 1

    if args.cmd == "exchange":
        try:
            req = json.loads(Path(args.file).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            log.error(f"璇诲彇璇锋眰澶辫触锛歿e}")
            return 2
        client = EdgeCloudClient()
        resp = client.exchange(req)
        print(json.dumps(resp, ensure_ascii=False, indent=2))
        if resp.get("status") == "success":
            return 0
        # 閫氫俊灞傚け璐ワ紙瓒呮椂/transport 閿欒/鐔旀柇锛夆啋 Exit 2
        if resp.get("error_code") in ("E301", "E302", "E303", "E202"):
            return 2
        # 鍗忚灞傚け璐ワ紙schema/PII/澶у皬锛夆啋 Exit 1
        return 1

    p.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

