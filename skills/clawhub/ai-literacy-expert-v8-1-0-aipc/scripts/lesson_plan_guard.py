#!/usr/bin/env python3
"""
lesson_plan_guard.py - 瑙勫垯灞傚閿欙紙8 椤圭‖瑙勫垯锛?

V7-AIPC 瑙勫垯灞傦細鍦?plan 杩涘叆 SDK/浜戠涔嬪墠鍋氱‖鏍￠獙锛圴7.3 鍗囩骇鐗?+ 涓?work_summary 鑱斿姩锛夈€?
8 椤圭‖瑙勫垯 (G001 ~ G008)锛?
  G001 plan 寮曠敤 鈮?min_unique_knowledge_points 涓笉鍚?knowledge_point
  G002 鐩搁偦 clip 闅惧害绛夌骇宸?鈮?max_difficulty_jump
  G003 plan 涓嫢鍚?abstract_data锛屽簭鍒楀寲瀛楄妭鏁?< abstract_data_max_bytes (10KB)
  G004 plan 涓?assessment.questions 鏁伴噺 鈮?min_assessment_questions 涓旀瘡棰樻湁 answer
  G005 姣忎釜 clip 鏃堕暱 鈭?[min_clip_duration_sec, max_clip_duration_sec]
  G006 plan 涓?pedagogy_method 鈭?valid_pedagogy_methods
  G007 plan 涓?learning_objectives 鑷冲皯 1 涓紝涓旀瘡鏉′互 valid verb 寮€澶?
  G008 cost_monitor 宸茶Е鍙戠啍鏂?鈫?鐩存帴鎷掔粷

CLI:
    python lesson_plan_guard.py --plan plan.json [--candidates cand.json] [--json]
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

import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, FrozenSet, List, Optional, Set, Tuple
import uuid


# ---------------------------------------------------------------------------
# 瑙勫垯閰嶇疆
# ---------------------------------------------------------------------------

@dataclass
class RuleConfig:
    """8 椤圭‖瑙勫垯鐨勯厤缃泦鍚堛€?""
    # G001: 鑷冲皯寮曠敤鐨勪笉鍚?knowledge_point 鏁伴噺锛堝幓閲嶅悗锛?
    min_unique_knowledge_points: int = 3
    # G002: 鐩搁偦 clip 闅惧害绛夌骇鏈€澶у樊
    max_difficulty_jump: int = 2
    # G003: abstract_data 搴忓垪鍖栧悗鏈€澶у瓧鑺傛暟锛堥粯璁?10KB = 10240B锛?
    abstract_data_max_bytes: int = 10240
    # G004: 璇勪及闂鏈€灏戦鏁?
    min_assessment_questions: int = 3
    # G005: clip 鏃堕暱涓婁笅闄愶紙绉掞級
    min_clip_duration_sec: float = 60.0
    max_clip_duration_sec: float = 600.0
    # G006: 鏁欏娉曠櫧鍚嶅崟
    valid_pedagogy_methods: FrozenSet[str] = frozenset(
        {"5E", "PBL", "鎺㈢┒寮?, "璁叉巿寮?, "缈昏浆璇惧爞"}
    )
    # G007: 瀛︿範鐩爣鍔ㄨ瘝鐧藉悕鍗曪紙甯冮瞾濮嗗垎绫绘硶涓枃鍖栫殑甯歌鍔ㄨ瘝锛?
    valid_learning_objective_verbs: FrozenSet[str] = frozenset(
        {"浜嗚В", "鐞嗚В", "鎺屾彙", "搴旂敤", "鍒嗘瀽", "璇勪环", "鍒涢€?}
    )
    # G002 杈呭姪锛氬悎娉曢毦搴︾瓑绾?1~5
    valid_difficulty_levels: FrozenSet[int] = frozenset({1, 2, 3, 4, 5})


# ---------------------------------------------------------------------------
# 杈呭姪鍑芥暟
# ---------------------------------------------------------------------------

def normalize_kp(raw: Any) -> str:
    """鐭ヨ瘑鐐瑰綊涓€鍖栵細鍘荤┖鐧?+ 缁熶竴灏忓啓锛屼究浜庡幓閲嶆瘮杈冦€?""
    if raw is None:
        return ""
    return str(raw).strip().lower()


_WS_PATTERN = re.compile(r"\s+")


def _norm_obj_text(raw: Any) -> str:
    """鏇存縺杩涚殑鏂囨湰褰掍竴鍖栵細鍘绘墍鏈夌┖鐧斤紙灏忓啓鍓?鍚庯級銆?""
    if raw is None:
        return ""
    return _WS_PATTERN.sub("", str(raw)).strip().lower()


def _is_circuit_breaker_triggered(cost_monitor: Any) -> bool:
    """鍏煎澶氱 cost_monitor 鐔旀柇妫€娴嬫帴鍙ｏ紙duck-typing锛夈€?""
    if cost_monitor is None:
        return False
    # 1) 鏂规硶锛歩s_circuit_breaker_triggered()
    fn = getattr(cost_monitor, "is_circuit_breaker_triggered", None)
    if callable(fn):
        try:
            return bool(fn())
        except Exception:
            return False
    # 2) 灞炴€э細circuit_breaker_triggered / triggered / circuit_breaker_open
    for attr in (
        "circuit_breaker_triggered",
        "circuit_breaker_open",
        "triggered",
        "is_open",
    ):
        if hasattr(cost_monitor, attr):
            try:
                return bool(getattr(cost_monitor, attr))
            except Exception:
                return False
    # 3) 鍏滃簳锛歝umulative_cost_usd >= monthly_budget_usd
    cum = _get_cumulative_cost(cost_monitor)
    budget = _get_monthly_budget(cost_monitor)
    if budget is not None and budget > 0:
        return cum >= budget
    return False


def _get_cumulative_cost(cost_monitor: Any) -> float:
    if cost_monitor is None:
        return 0.0
    for attr in ("cumulative_cost_usd", "cumulative_cost", "total_cost_usd", "cost_usd"):
        if hasattr(cost_monitor, attr):
            try:
                return float(getattr(cost_monitor, attr))
            except Exception:
                continue
    return 0.0


def _get_monthly_budget(cost_monitor: Any) -> Optional[float]:
    if cost_monitor is None:
        return None
    for attr in ("monthly_budget_usd", "monthly_budget", "budget_usd", "budget"):
        if hasattr(cost_monitor, attr):
            try:
                v = float(getattr(cost_monitor, attr))
                return v
            except Exception:
                continue
    return None


# ---------------------------------------------------------------------------
# plan 缁撴瀯瑙ｆ瀽
# ---------------------------------------------------------------------------

def _get_clips(plan: Any) -> List[dict]:
    """浠?plan 涓彁鍙?clip 鍒楄〃锛堝吋瀹?clips / lessons[].clips / segments锛夈€?""
    if not isinstance(plan, dict):
        return []
    clips = plan.get("clips")
    if isinstance(clips, list):
        return [c for c in clips if isinstance(c, dict)]
    lessons = plan.get("lessons")
    if isinstance(lessons, list):
        out: List[dict] = []
        for l in lessons:
            if isinstance(l, dict):
                cs = l.get("clips")
                if isinstance(cs, list):
                    out.extend(c for c in cs if isinstance(c, dict))
        return out
    segments = plan.get("segments")
    if isinstance(segments, list):
        return [s for s in segments if isinstance(s, dict)]
    return []


def _collect_unique_kps(plan: Any) -> Set[str]:
    """浠?plan 鏀堕泦鎵€鏈?knowledge_point锛屽綊涓€鍖栧悗鍘婚噸銆?""
    kps: Set[str] = set()
    if not isinstance(plan, dict):
        return kps

    def _walk(value: Any) -> None:
        if value is None:
            return
        if isinstance(value, str):
            n = normalize_kp(value)
            if n:
                kps.add(n)
            return
        if isinstance(value, (int, float)):
            # 鏁板瓧鐭ヨ瘑鐐癸紙濡傜紪鍙凤級杞瓧绗︿覆
            n = normalize_kp(value)
            if n:
                kps.add(n)
            return
        if isinstance(value, list):
            for x in value:
                _walk(x)
            return
        if isinstance(value, dict):
            # 鍙栧嚭鍏抽敭瀛楁
            for key in ("knowledge_point", "knowledge_points", "kps", "kp",
                        "topic", "topics", "name", "label"):
                if key in value:
                    _walk(value[key])

    # 椤跺眰瀛楁
    for key in ("knowledge_points", "knowledge_point", "kps", "topics"):
        if key in plan:
            _walk(plan[key])

    # clips 鍐呴儴
    for c in _get_clips(plan):
        for key in ("knowledge_point", "knowledge_points", "kps", "topic", "topics"):
            if key in c:
                _walk(c[key])

    # lessons 鍐呴儴
    lessons = plan.get("lessons")
    if isinstance(lessons, list):
        for l in lessons:
            if not isinstance(l, dict):
                continue
            for key in ("knowledge_point", "knowledge_points", "kps", "topic", "topics"):
                if key in l:
                    _walk(l[key])
            for c in l.get("clips", []) or []:
                if isinstance(c, dict):
                    for key in ("knowledge_point", "knowledge_points", "kps", "topic", "topics"):
                        if key in c:
                            _walk(c[key])

    kps.discard("")
    return kps


def _get_clip_difficulty(clip: Any) -> Optional[int]:
    """浠?clip 涓幏鍙栭毦搴︾瓑绾э紙1~5锛夈€?""
    if not isinstance(clip, dict):
        return None
    for key in ("difficulty", "difficulty_level", "level"):
        if key in clip and clip[key] is not None:
            try:
                return int(clip[key])
            except (TypeError, ValueError):
                return None
    meta = clip.get("metadata") or {}
    if isinstance(meta, dict):
        for key in ("difficulty", "difficulty_level", "level"):
            if key in meta and meta[key] is not None:
                try:
                    return int(meta[key])
                except (TypeError, ValueError):
                    return None
    return None


def _get_clip_duration_sec(clip: Any) -> Optional[float]:
    """浠?clip 涓幏鍙栨椂闀匡紙绉掞級銆?""
    if not isinstance(clip, dict):
        return None
    # 1) 椤跺眰鏄惧紡 duration 瀛楁
    for key in ("duration_sec", "duration_seconds", "duration"):
        if key in clip and clip[key] is not None:
            try:
                v = float(clip[key])
                if v >= 0:
                    return v
            except (TypeError, ValueError):
                pass
    # 2) timecode 宓屽
    tc = clip.get("timecode") or {}
    if isinstance(tc, dict):
        for key in ("duration", "duration_sec", "duration_seconds"):
            if key in tc and tc[key] is not None:
                try:
                    v = float(tc[key])
                    if v >= 0:
                        return v
                except (TypeError, ValueError):
                    pass
        try:
            ip = tc.get("in_point")
            op = tc.get("out_point")
            if ip is not None and op is not None:
                v = float(op) - float(ip)
                return v if v >= 0 else None
        except (TypeError, ValueError):
            pass
    return None


def _abstract_data_size(abstract_data: Any) -> int:
    """璁＄畻 abstract_data 搴忓垪鍖栧悗鐨勫瓧鑺傛暟锛圲TF-8锛夈€?""
    if abstract_data is None:
        return 0
    if isinstance(abstract_data, bytes):
        return len(abstract_data)
    if isinstance(abstract_data, str):
        try:
            return len(abstract_data.encode("utf-8"))
        except Exception:
            return len(abstract_data)
    try:
        return len(json.dumps(abstract_data, ensure_ascii=False).encode("utf-8"))
    except Exception:
        try:
            return len(str(abstract_data).encode("utf-8"))
        except Exception:
            return 0


def _get_assessment(plan: Any) -> dict:
    if not isinstance(plan, dict):
        return {}
    a = plan.get("assessment")
    if isinstance(a, dict):
        return a
    return {}


def _get_assessment_questions(plan: Any) -> List[Any]:
    a = _get_assessment(plan)
    qs = a.get("questions") if isinstance(a, dict) else None
    if isinstance(qs, list):
        return qs
    return []


def _get_pedagogy_method(plan: Any) -> Optional[str]:
    if not isinstance(plan, dict):
        return None
    for key in ("pedagogy_method", "teaching_method", "pedagogy", "method"):
        if key in plan and plan[key] is not None and str(plan[key]).strip():
            return str(plan[key]).strip()
    meta = plan.get("lesson_metadata") or plan.get("metadata") or {}
    if isinstance(meta, dict):
        for key in ("pedagogy_method", "teaching_method", "pedagogy", "method"):
            if key in meta and meta[key] is not None and str(meta[key]).strip():
                return str(meta[key]).strip()
    return None


def _get_learning_objectives(plan: Any) -> List[str]:
    out: List[str] = []
    if not isinstance(plan, dict):
        return out
    for key in ("learning_objectives", "objectives", "goals", "鏁欏鐩爣"):
        v = plan.get(key)
        if isinstance(v, list):
            for x in v:
                if x is not None and str(x).strip():
                    out.append(str(x).strip())
        elif isinstance(v, str) and v.strip():
            # 鍗曟潯瀛楃涓诧紝鎸夊彞鍙?鎹㈣鎷嗗垎
            for chunk in re.split(r"[銆俓n;锛沒+", v):
                if chunk.strip():
                    out.append(chunk.strip())
    return out


def _objective_starts_with_verb(text: str, verbs: FrozenSet[str]) -> bool:
    """鍒ゆ柇鐩爣鏂囨湰鏄惁浠ョ櫧鍚嶅崟鍔ㄨ瘝寮€澶达紙鍏佽鍔ㄨ瘝鍚庤窡绌烘牸/鏍囩偣/浠绘剰鍐呭锛夈€?""
    s = str(text or "").strip()
    if not s:
        return False
    for verb in verbs:
        if not verb:
            continue
        if s == verb:
            return True
        if s.startswith(verb):
            # 鍔ㄨ瘝鍚庡繀椤绘槸闈炲瓧姣嶏紙涓枃/鏍囩偣/鏁板瓧/绌烘牸/鑻辨枃瀛楁瘝锛夋墠绠椾互鍔ㄨ瘝寮€澶?
            tail = s[len(verb):]
            if not tail:
                return True
            first = tail[0]
            # 涓枃琛ㄦ剰鏂囧瓧锛歕u4e00-\u9fff
            if "\u4e00" <= first <= "\u9fff":
                return True
            if first in " \t,锛屻€?;锛?锛?锛?锛熴€?)锛堬級銆娿€嬨€愩€慬]":
                return True
            # 鏁板瓧
            if first.isdigit():
                return True
            # 鑻辨枃瀛楁瘝锛堝厑璁?鐞嗚В CNN 鍘熺悊"绛夊惈鑻辨枃鏈鐨勫涔犵洰鏍囷級
            if ("a" <= first <= "z") or ("A" <= first <= "Z"):
                return True
    return False


# ---------------------------------------------------------------------------
# 鏍￠獙涓诲叆鍙?
# ---------------------------------------------------------------------------

def validate_lesson_plan(
    plan: Any,
    candidates: Optional[dict],
    cost_monitor: Any,
    config: Optional[RuleConfig] = None,
) -> Tuple[bool, List[dict]]:
    """鎵ц 8 椤圭‖瑙勫垯鏍￠獙銆?

    Args:
        plan: lesson_plan dict锛堝繀濉級
        candidates: 鍊欓€夌煡璇嗙偣/绱犳潗 dict锛堝彲閫夛紱褰撳墠涓哄墠鍚戝吋瀹逛繚鐣欙級
        cost_monitor: 鎴愭湰鐩戞帶瀵硅薄锛坉uck-typing锛歩s_circuit_breaker_triggered / 灞炴€э級
        config: RuleConfig锛圢one 鏃朵娇鐢ㄩ粯璁わ級

    Returns:
        (passed, errors)锛歟rrors 姣忛」褰㈠ {"code": "G001", "message": "...", "suggestion": "..."}
    """
    cfg = config or RuleConfig()
    errors: List[dict] = []

    if not isinstance(plan, dict):
        return False, [
            {
                "code": "G000",
                "message": "plan 蹇呴』涓?dict 绫诲瀷",
                "suggestion": "浼犲叆鍚堟硶 lesson_plan dict锛堥《灞?JSON 瀵硅薄锛?,
            }
        ]

    # ---------------- G008: 鎴愭湰鐩戞帶鐔旀柇妫€娴嬶紙鏈€鍏堟鏌ワ紝閬垮厤鏃犳晥宸ヤ綔锛?----------------
    if _is_circuit_breaker_triggered(cost_monitor):
        cum = _get_cumulative_cost(cost_monitor)
        budget = _get_monthly_budget(cost_monitor)
        budget_txt = f"{budget:.2f}" if budget is not None else "鏈煡"
        errors.append(
            {
                "code": "G008",
                "message": (
                    f"鎴愭湰鐩戞帶宸茶Е鍙戠啍鏂紙cumulative_cost_usd={cum:.4f} 鈮?"
                    f"monthly_budget_usd={budget_txt}锛夛紝褰撳墠 lesson_plan 鐩存帴鎷掔粷"
                ),
                "suggestion": (
                    "绛夊緟绠＄悊鍛樿В闄ょ啍鏂垨涓婅皟鏈堥绠楀悗閲嶈瘯锛?
                    "鐔旀柇鏈熼棿绯荤粺宸茶嚜鍔ㄥ垏鎹㈠埌 Level 5锛堝畬鍏ㄦ湰鍦帮級妯″紡"
                ),
            }
        )
        # 鐔旀柇瑙﹀彂鏃剁洿鎺ユ嫆缁濓紝璺宠繃鍏跺畠妫€鏌?
        return False, errors

    # ---------------- G001: 鑷冲皯 N 涓笉鍚?knowledge_point ----------------
    unique_kps = _collect_unique_kps(plan)
    if len(unique_kps) < cfg.min_unique_knowledge_points:
        errors.append(
            {
                "code": "G001",
                "message": (
                    f"鐭ヨ瘑鐐规暟閲忎笉瓒筹細褰撳墠 {len(unique_kps)} 涓笉鍚?knowledge_point "
                    f"锛堝綊涓€鍖栧幓閲嶅悗锛夛紝瑕佹眰鑷冲皯 {cfg.min_unique_knowledge_points} 涓?
                ),
                "suggestion": (
                    "鍦?plan['knowledge_points'] 鎴栧悇 clip['knowledge_point'] 涓ˉ鍏呮洿澶?
                    f"涓嶅悓鐨?knowledge_point锛岀洿鑷冲綊涓€鍖栧幓閲嶆暟 鈮?{cfg.min_unique_knowledge_points}锛?
                    "閬垮厤閲嶅/鍚屼箟璇嶏紙褰掍竴鍖栨寜灏忓啓+鍘荤┖鐧斤級"
                ),
            }
        )

    # ---------------- G002: 鐩搁偦 clip 闅惧害绛夌骇宸?鈮?max_difficulty_jump ----------------
    clips = _get_clips(plan)
    if not clips:
        # 娌℃湁 clips 涔熶笉鍏佽锛堝叾瀹冭鍒欏彲鑳芥棤娉曟牎楠岋級鈥斺€旂粰涓€涓蒋鎻愮ず浣嗕笉寮哄埗
        pass
    else:
        prev_difficulty: Optional[int] = None
        prev_idx: int = -1
        for i, c in enumerate(clips):
            d = _get_clip_difficulty(c)
            if d is None:
                # 缂洪毦搴︿俊鎭細閲嶇疆 prev锛岄伩鍏嶆妸 None 涓庢暟瀛楄姣旇緝
                prev_difficulty = None
                prev_idx = -1
                continue
            if d not in cfg.valid_difficulty_levels:
                errors.append(
                    {
                        "code": "G002",
                        "message": (
                            f"clip#{i+1}: 闅惧害绛夌骇 {d} 涓嶅湪鍚堟硶闆嗗悎 "
                            f"{sorted(cfg.valid_difficulty_levels)} 鍐?
                        ),
                        "suggestion": (
                            f"灏嗛毦搴﹁皟鏁翠负 1~5 涔嬮棿鐨勬暣鏁帮紱鎺ㄨ崘璧峰闅惧害 1-2锛岄€愭閫掑锛?
                            f"涓旂浉閭诲樊 鈮?{cfg.max_difficulty_jump}"
                        ),
                    }
                )
            if prev_difficulty is not None and prev_idx >= 0:
                try:
                    jump = abs(int(d) - int(prev_difficulty))
                except (TypeError, ValueError):
                    jump = 0
                if jump > cfg.max_difficulty_jump:
                    errors.append(
                        {
                            "code": "G002",
                            "message": (
                                f"clip#{prev_idx+1}鈫抍lip#{i+1}: 闅惧害璺宠穬 {jump} "
                                f"锛坽prev_difficulty} 鈫?{d}锛夛紝"
                                f"瓒呰繃闃堝€?{cfg.max_difficulty_jump}"
                            ),
                            "suggestion": (
                                f"璋冩暣涓棿 clip 鐨勯毦搴︼紝浣跨浉閭诲樊 鈮?{cfg.max_difficulty_jump}锛?
                                "鏁欏寤鸿鎸夎灪鏃嬪紡涓婂崌鎺掑垪锛堝樊鍊?0~1锛?
                            ),
                        }
                    )
            prev_difficulty = d
            prev_idx = i

    # ---------------- G003: abstract_data 浣撶Н < 10KB ----------------
    if "abstract_data" in plan:
        size = _abstract_data_size(plan["abstract_data"])
        if size >= cfg.abstract_data_max_bytes:
            errors.append(
                {
                    "code": "G003",
                    "message": (
                        f"abstract_data 浣撶Н杩囧ぇ锛歿size} bytes锛?
                        f"蹇呴』 < {cfg.abstract_data_max_bytes} bytes锛?0KB锛?
                    ),
                    "suggestion": (
                        "绔晶鎴柇鎴栧帇缂?abstract_data锛屼粎淇濈暀涓庡喅绛栫浉鍏崇殑鍏抽敭瀛楁锛?
                        "閬靛惊绔簯鍗忚 搂4.1 鏁版嵁澶у皬绾︽潫"
                    ),
                }
            )

    # ---------------- G004: assessment.questions 鏁伴噺 鈮?N 涓旀瘡棰樻湁 answer ----------------
    questions = _get_assessment_questions(plan)
    if len(questions) < cfg.min_assessment_questions:
        errors.append(
            {
                "code": "G004",
                "message": (
                    f"璇勪及闂鏁伴噺涓嶈冻锛氬綋鍓?{len(questions)} 棰橈紝"
                    f"瑕佹眰鑷冲皯 {cfg.min_assessment_questions} 棰?
                ),
                "suggestion": (
                    f"鍦?plan['assessment']['questions'] 涓ˉ鍏呰嚦 "
                    f"鈮?{cfg.min_assessment_questions} 棰橈紙寤鸿瑕嗙洊 浜嗚В/鐞嗚В/鎺屾彙 3 涓眰绾э級"
                ),
            }
        )
    else:
        missing_idx: List[int] = []
        for i, q in enumerate(questions):
            if not isinstance(q, dict):
                missing_idx.append(i)
                continue
            ans = q.get("answer")
            if ans is None:
                missing_idx.append(i)
                continue
            if isinstance(ans, str) and not ans.strip():
                missing_idx.append(i)
                continue
            if isinstance(ans, (list, dict)) and len(ans) == 0:
                missing_idx.append(i)
        if missing_idx:
            errors.append(
                {
                    "code": "G004",
                    "message": (
                        f"璇勪及闂缂哄皯 answer锛氬叡 {len(missing_idx)} 棰?"
                        f"锛堢储寮?{missing_idx[:10]}{'鈥? if len(missing_idx) > 10 else ''}锛?
                    ),
                    "suggestion": (
                        "涓烘瘡棰樿ˉ鍏?answer 瀛楁锛堟爣鍑嗙瓟妗堟垨绛旀瑕佺偣锛夛紱"
                        "answer 绫诲瀷鍙负 string / list / dict锛屼絾涓嶈兘涓虹┖"
                    ),
                }
            )

    # ---------------- G005: clip 鏃堕暱 鈭?[min, max] ----------------
    if clips:
        bad_clips: List[str] = []
        missing_dur: List[int] = []
        for i, c in enumerate(clips):
            d = _get_clip_duration_sec(c)
            if d is None:
                missing_dur.append(i + 1)
                continue
            if d < cfg.min_clip_duration_sec or d > cfg.max_clip_duration_sec:
                bad_clips.append(
                    f"clip#{i+1}:{d:.1f}s锛堣姹?"
                    f"{cfg.min_clip_duration_sec:.0f}~{cfg.max_clip_duration_sec:.0f}s锛?
                )
        if missing_dur:
            errors.append(
                {
                    "code": "G005",
                    "message": (
                        f"浠ヤ笅 clip 缂哄皯 duration 瀛楁: clip# {missing_dur[:10]}"
                        f"{'鈥? if len(missing_dur) > 10 else ''}"
                    ),
                    "suggestion": (
                        "鍦?clip['duration_sec'] 鎴?clip['timecode']['in_point/out_point'] "
                        "涓ˉ鍏ㄦ椂闀匡紙绉掞級"
                    ),
                }
            )
        if bad_clips:
            errors.append(
                {
                    "code": "G005",
                    "message": (
                        f"瀛樺湪 {len(bad_clips)} 涓?clip 鏃堕暱涓嶅悎瑙? "
                        + "; ".join(bad_clips[:5])
                        + ("鈥? if len(bad_clips) > 5 else "")
                    ),
                    "suggestion": (
                        f"璋冩暣姣忎釜 clip 鏃堕暱鑷?{cfg.min_clip_duration_sec:.0f}~"
                        f"{cfg.max_clip_duration_sec:.0f} 绉掍箣闂?
                    ),
                }
            )

    # ---------------- G006: pedagogy_method 鐧藉悕鍗?----------------
    method = _get_pedagogy_method(plan)
    if method is None:
        errors.append(
            {
                "code": "G006",
                "message": "plan 涓己灏?pedagogy_method / teaching_method 瀛楁",
                "suggestion": (
                    f"鍦?plan 椤跺眰濉叆 pedagogy_method锛屽彇鍊?鈭?"
                    f"{sorted(cfg.valid_pedagogy_methods)}"
                ),
            }
        )
    elif method not in cfg.valid_pedagogy_methods:
        errors.append(
            {
                "code": "G006",
                "message": f"pedagogy_method 闈炴硶锛?{method}' 涓嶅湪鐧藉悕鍗曞唴",
                "suggestion": (
                    f"鏀逛负鐧藉悕鍗曞唴鐨勬暀瀛︽硶涔嬩竴: {sorted(cfg.valid_pedagogy_methods)}"
                ),
            }
        )

    # ---------------- G007: learning_objectives 鑷冲皯 1 涓紝姣忔潯浠ュ悎娉?verb 寮€澶?----------------
    objectives = _get_learning_objectives(plan)
    if not objectives:
        errors.append(
            {
                "code": "G007",
                "message": "plan 涓己灏?learning_objectives锛堣嚦灏?1 涓級",
                "suggestion": (
                    "鍦?plan['learning_objectives'] 涓ˉ鍏呯洰鏍囷紝姣忔潯浠ュ悎娉曞姩璇嶅紑澶达紝"
                    f"濡?{sorted(cfg.valid_learning_objective_verbs)} 绛?
                ),
            }
        )
    else:
        bad_objs: List[int] = []
        for i, obj in enumerate(objectives):
            if not _objective_starts_with_verb(obj, cfg.valid_learning_objective_verbs):
                bad_objs.append(i)
        if bad_objs:
            sample_lines: List[str] = []
            for i in bad_objs[:3]:
                txt = objectives[i]
                if len(txt) > 24:
                    txt = txt[:24] + "鈥?
                sample_lines.append(f"#{i+1}:'{txt}'")
            errors.append(
                {
                    "code": "G007",
                    "message": (
                        f"瀛︿範鐩爣鏈互鍚堟硶鍔ㄨ瘝寮€澶达細{len(bad_objs)} 鏉★紝"
                        f"鏍蜂緥 {'; '.join(sample_lines)}"
                    ),
                    "suggestion": (
                        f"灏嗘瘡鏉＄洰鏍囪皟鏁翠负浠?{sorted(cfg.valid_learning_objective_verbs)} "
                        "涔嬩竴寮€澶达紙鍙傝€冨竷椴佸鍒嗙被娉曪級锛?
                        "鍔ㄨ瘝鍚庡彲璺熶腑鏂?鑻辨枃/鏁板瓧/鏍囩偣/绌烘牸"
                    ),
                }
            )

    passed = len(errors) == 0
    return passed, errors


# ---------------------------------------------------------------------------
# 閿欒鎶ュ憡
# ---------------------------------------------------------------------------

def render_error_report(errors: List[dict]) -> str:
    """灏嗛敊璇垪琛ㄦ覆鏌撲负浜虹被鍙鎶ュ憡銆?""
    if not errors:
        return "[lesson_plan_guard] 鍏ㄩ儴 8 椤圭‖瑙勫垯閫氳繃 鉁?

    lines: List[str] = []
    lines.append(f"[lesson_plan_guard] 鍙戠幇 {len(errors)} 椤硅鍒欒繚鍙嶏細")
    # 鎸?code 鎺掑簭
    sorted_errors = sorted(
        errors,
        key=lambda e: (str(e.get("code", "G???")),),
    )
    for i, err in enumerate(sorted_errors, start=1):
        code = err.get("code", "G???")
        msg = err.get("message", "")
        sug = err.get("suggestion", "")
        lines.append(f"  {i}. [{code}] {msg}")
        if sug:
            lines.append(f"     寤鸿: {sug}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 绠€鏄?CostMonitor锛圕LI 榛樿锛?
# ---------------------------------------------------------------------------

class CostMonitor:
    """榛樿鎴愭湰鐩戞帶锛圕LI 鍏ュ彛浣跨敤锛夈€?

    鎺ュ彛锛?
        is_circuit_breaker_triggered() -> bool
        cumulative_cost_usd: float
        monthly_budget_usd: float
    """

    def __init__(
        self,
        monthly_budget_usd: float = 10.0,
        cumulative_cost_usd: float = 0.0,
    ) -> None:
        self.monthly_budget_usd = float(monthly_budget_usd)
        self.cumulative_cost_usd = float(cumulative_cost_usd)
        self.circuit_breaker_triggered: bool = (
            self.cumulative_cost_usd >= self.monthly_budget_usd
            if self.monthly_budget_usd > 0
            else False
        )

    def is_circuit_breaker_triggered(self) -> bool:
        return bool(self.circuit_breaker_triggered)


def get_default_monitor() -> CostMonitor:
    """鑾峰彇 CLI 浣跨敤鐨勯粯璁?CostMonitor銆?""
    return CostMonitor(monthly_budget_usd=10.0, cumulative_cost_usd=0.0)


# ---------------------------------------------------------------------------
# CLI 鍏ュ彛
# ---------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    log = get_logger("guard")
    import argparse

    p = argparse.ArgumentParser(
        prog="lesson_plan_guard",
        description="Validate lesson_plan.json against 8 hard rules (V7.3 瑙勫垯灞傚閿?銆?,
    )
    p.add_argument("--plan", required=True, help="Path to lesson_plan.json")
    p.add_argument(
        "--candidates",
        default=None,
        help="Optional path to candidates.json锛堝€欓€夌煡璇嗙偣/绱犳潗锛屽墠鍚戝吋瀹癸級",
    )
    p.add_argument(
        "--json",
        action="store_true",
        help="杈撳嚭 JSON 鎶ュ憡锛堥粯璁や汉绫诲彲璇伙級",
    )
    p.add_argument(
        "--monthly-budget-usd",
        type=float,
        default=10.0,
        help="鍐呯疆 CostMonitor 鐨勬湀棰勭畻锛堥粯璁?10.0锛?,
    )
    p.add_argument(
        "--cumulative-cost-usd",
        type=float,
        default=0.0,
        help="鍐呯疆 CostMonitor 鐨勫垵濮嬬疮璁℃垚鏈紙榛樿 0.0锛?,
    )

    args = p.parse_args(argv)

    plan_path = Path(args.plan)
    if not plan_path.exists():
        log.error(f"ERROR: plan file not found: {plan_path}")
        return 2
    try:
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        log.error(f"ERROR: invalid plan JSON ({plan_path}): {e}")
        return 2

    candidates: Optional[dict] = None
    if args.candidates:
        cand_path = Path(args.candidates)
        if not cand_path.exists():
            log.error(f"ERROR: candidates file not found: {cand_path}")
            return 2
        try:
            candidates = json.loads(cand_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            log.error(f"ERROR: invalid candidates JSON ({cand_path}): {e}")
            return 2

    monitor = CostMonitor(
        monthly_budget_usd=args.monthly_budget_usd,
        cumulative_cost_usd=args.cumulative_cost_usd,
    )

    passed, errors = validate_lesson_plan(plan, candidates, monitor)

    if args.json:
        report = {
            "passed": bool(passed),
            "errors": errors,
            "error_count": len(errors),
            "report_id": f"lpg-{uuid.uuid4().hex[:12]}",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "config": {
                "min_unique_knowledge_points": 3,
                "max_difficulty_jump": 2,
                "abstract_data_max_bytes": 10240,
                "min_assessment_questions": 3,
                "min_clip_duration_sec": 60.0,
                "max_clip_duration_sec": 600.0,
            },
        }
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        log.info(render_error_report(errors))

    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

