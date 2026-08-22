"""
compose_lesson.py - 闃舵 4锛氬悎鎴愭渶缁堟暀瀛︿氦浠樼墿銆?

瀵瑰簲 video-editing-skills-main/scripts/compose_video.py锛屾妸"ffmpeg 瑙嗛鍚堟垚"
閲嶆槧灏勪负"Markdown 璇句欢 + 璇勪及棰?+ HTML 浜掑姩璇句欢娓叉煋"銆?

绔簯鍗忓悓绾︽潫锛圴7 搂2.4锛夛細
  浜戠鍙繑鍥?lesson_plan.json锛堝喅绛栵級锛屾墍鏈夋覆鏌撳湪绔晶鎵ц銆?

娴佺▼锛?
  1. load_lesson_plan(plan_path) 瑙ｆ瀽浜戠杩斿洖鐨?lesson_plan.json
  2. lesson_plan_guard.validate_lesson_plan() 鏍￠獙锛? 椤圭‖瑙勫垯锛?
  3. 鏍￠獙閫氳繃 鈫?render_markdown / render_assessment / render_courseware_html
  4. 鏍￠獙澶辫触 鈫?鎷掔粷鍚堟垚锛岃緭鍑洪敊璇姤鍛?

鐢ㄦ硶锛?
    python scripts/compose_lesson.py \\
        --blueprint "<workspace>/lesson_plan.json" \\
        --output "<workspace>/final_lesson.md" \\
        --candidates "<workspace>/candidate_knowledge.json" \\
        --assessment "<workspace>/assessment.json" \\
        --html "<workspace>/courseware.html"
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

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from lesson_plan_guard import RuleConfig, render_error_report, validate_lesson_plan


# ---------------------------------------------------------------------------
# 鍔犺浇 lesson_plan
# ---------------------------------------------------------------------------

def load_lesson_plan(plan_path: Path) -> dict:
    """瑙ｆ瀽浜戠杩斿洖鐨?lesson_plan.json銆?""
    if not plan_path.exists():
        raise FileNotFoundError(f"lesson_plan 涓嶅瓨鍦細{plan_path}")
    try:
        return json.loads(plan_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise ValueError(f"lesson_plan JSON 瑙ｆ瀽澶辫触锛歿e}") from e


def load_candidates(candidates_path: Optional[Path]) -> Optional[dict]:
    """鍔犺浇 candidate_knowledge.json锛堝彲閫夛紝鐢ㄤ簬 HTML 鍏宠仈鍘熷鐗囨锛夈€?""
    if candidates_path is None or not candidates_path.exists():
        return None
    try:
        return json.loads(candidates_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


# ---------------------------------------------------------------------------
# Markdown 璇句欢娓叉煋
# ---------------------------------------------------------------------------

def render_markdown(plan: dict, candidates: Optional[dict] = None) -> str:
    """娓叉煋 final_lesson.md锛堝惈璇炬椂銆佺煡璇嗙偣銆佹暀瀛︽硶銆佷簰鍔ㄨ璁★級銆?""
    lines: list[str] = []

    title = plan.get("lesson_title") or plan.get("title") or "AI 閫氳瘑璇炬暀妗?
    lines.append(f"# {title}")
    lines.append("")

    # 鍏冧俊鎭?
    method = plan.get("pedagogy_method") or plan.get("teaching_method") or "鏈寚瀹?
    lines.append(f"**鏁欏娉?*锛歿method}")
    total_duration = _calc_total_duration(plan)
    if total_duration:
        lines.append(f"**棰勮鏃堕暱**锛歿_format_duration(total_duration)}")
    lines.append(f"**鐢熸垚鏃堕棿**锛歿datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")

    # 鏁欏鐩爣
    objectives = _get_learning_objectives(plan)
    if objectives:
        lines.append("## 鏁欏鐩爣")
        lines.append("")
        for i, obj in enumerate(objectives, 1):
            lines.append(f"{i}. {obj}")
        lines.append("")

    # 鐭ヨ瘑鐐?
    kps = _get_knowledge_points(plan)
    if kps:
        lines.append("## 鐭ヨ瘑鐐?)
        lines.append("")
        for kp in kps:
            lines.append(f"- {kp}")
        lines.append("")

    # 鏁欏鐜妭锛坈lips锛?
    clips = _get_clips(plan)
    if clips:
        lines.append("## 鏁欏鐜妭")
        lines.append("")
        for i, clip in enumerate(clips, 1):
            seq = clip.get("sequence_order", i)
            kp = clip.get("knowledge_point", clip.get("topic", ""))
            difficulty = clip.get("difficulty", "")
            duration = _get_clip_duration_sec(clip)
            voiceover = clip.get("voiceover") or {}
            text = voiceover.get("text", "") if isinstance(voiceover, dict) else str(voiceover)
            transition = clip.get("transition") or {}
            trans_type = transition.get("type", "") if isinstance(transition, dict) else ""

            lines.append(f"### 鐜妭 {seq}锛歿kp}")
            if difficulty:
                lines.append(f"- **闅惧害**锛歀{difficulty}")
            if duration:
                lines.append(f"- **鏃堕暱**锛歿_format_duration(duration)}")
            if trans_type:
                lines.append(f"- **杩囨浮**锛歿trans_type}")
            if text:
                lines.append("")
                lines.append(f"> {text}")
            lines.append("")

    # 浜掑姩璁捐
    interaction = plan.get("interaction_design") or plan.get("interaction")
    if interaction:
        lines.append("## 浜掑姩璁捐")
        lines.append("")
        if isinstance(interaction, str):
            lines.append(interaction)
        elif isinstance(interaction, list):
            for item in interaction:
                lines.append(f"- {item}")
        elif isinstance(interaction, dict):
            for k, v in interaction.items():
                lines.append(f"- **{k}**锛歿v}")
        lines.append("")

    # 璇勪及璇存槑
    assessment = _get_assessment(plan)
    if assessment:
        questions = assessment.get("questions", []) if isinstance(assessment, dict) else []
        if questions:
            lines.append("## 璇勪及")
            lines.append("")
            lines.append(f"鍏?{len(questions)} 棰橈紝璇﹁ assessment.json銆?)
            lines.append("")

    lines.append("---")
    lines.append("*鏈暀妗堢敱 ai-literacy-expert-v8-aipc 绔簯鍗忓悓宸ヤ綔娴佺敓鎴愶紙鏈湴 DeepSeek-R1-1.5B 鎺ㄧ悊 + 浜戠鍐崇瓥 + work_summary 鑷姩鎶ュ憡 + p5.js 鎸夐挳瀹屾暣鎬ч棬鎺э級銆?")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# assessment.json 娓叉煋
# ---------------------------------------------------------------------------

def render_assessment(plan: dict) -> dict:
    """娓叉煋 assessment.json锛堝惈閫夋嫨棰?绠€绛旈/绛旀锛夈€?""
    assessment = _get_assessment(plan)
    if not assessment:
        return {
            "assessment_id": f"asm-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "questions": [],
            "note": "lesson_plan 涓棤 assessment 瀛楁",
        }

    questions = assessment.get("questions", []) if isinstance(assessment, dict) else []
    # 鏍囧噯鍖栨瘡棰樼粨鏋?
    standardized: list[dict] = []
    for i, q in enumerate(questions):
        if not isinstance(q, dict):
            continue
        standardized.append({
            "id": q.get("id", f"Q{i + 1}"),
            "type": q.get("type", "short_answer"),
            "question": q.get("question", q.get("stem", "")),
            "options": q.get("options", []),
            "answer": q.get("answer", ""),
            "explanation": q.get("explanation", ""),
            "difficulty": q.get("difficulty", 2),
            "knowledge_point": q.get("knowledge_point", ""),
        })

    return {
        "assessment_id": f"asm-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "total_questions": len(standardized),
        "questions": standardized,
    }


# ---------------------------------------------------------------------------
# HTML 浜掑姩璇句欢娓叉煋锛坧5.js锛屽彲閫夛級
# ---------------------------------------------------------------------------

def render_courseware_html(plan: dict, candidates: Optional[dict] = None) -> str:
    """娓叉煋 courseware.html锛坧5.js 浜掑姩璇句欢楠ㄦ灦锛夈€?

    鐢熸垚涓€涓彲浜や簰鐨勭煡璇嗙偣娴忚椤甸潰锛屾瘡涓煡璇嗙偣瀵瑰簲涓€涓?p5.js canvas 鍗＄墖銆?
    """
    title = plan.get("lesson_title", "AI 閫氳瘑璇句簰鍔ㄨ浠?)
    kps = _get_knowledge_points(plan)
    clips = _get_clips(plan)

    cards_json = json.dumps(
        [
            {
                "title": c.get("knowledge_point", c.get("topic", f"鐜妭{i}")),
                "difficulty": c.get("difficulty", 2),
                "text": (c.get("voiceover") or {}).get("text", "") if isinstance(c.get("voiceover"), dict) else "",
            }
            for i, c in enumerate(clips)
        ],
        ensure_ascii=False,
    )

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.0/p5.min.js"></script>
<style>
body {{ font-family: "Microsoft YaHei", sans-serif; margin: 0; padding: 20px; background: #f5f5f5; }}
h1 {{ color: #333; }}
#cards {{ display: flex; flex-wrap: wrap; gap: 16px; }}
.card {{ background: white; border-radius: 8px; padding: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); width: 300px; }}
.card h3 {{ margin-top: 0; color: #2196F3; }}
.badge {{ display: inline-block; padding: 2px 8px; border-radius: 4px; background: #E3F2FD; color: #1976D2; font-size: 12px; }}
</style>
</head>
<body>
<h1>{title}</h1>
<div id="cards"></div>
<script>
const cards = {cards_json};
function setup() {{
  noCanvas();
  const container = document.getElementById('cards');
  cards.forEach((card, i) => {{
    const div = document.createElement('div');
    div.className = 'card';
    div.innerHTML = `<h3>${{card.title}}</h3>
      <span class="badge">闅惧害 L${{card.difficulty}}</span>
      <p>${{card.text || ''}}</p>`;
    container.appendChild(div);
  }});
}}
</script>
</body>
</html>"""


# ---------------------------------------------------------------------------
# 杈呭姪鍑芥暟
# ---------------------------------------------------------------------------

def _get_clips(plan: dict) -> list[dict]:
    if not isinstance(plan, dict):
        return []
    clips = plan.get("clips")
    if isinstance(clips, list):
        return [c for c in clips if isinstance(c, dict)]
    lessons = plan.get("lessons")
    if isinstance(lessons, list):
        out = []
        for l in lessons:
            if isinstance(l, dict) and isinstance(l.get("clips"), list):
                out.extend(c for c in l["clips"] if isinstance(c, dict))
        return out
    return []


def _get_knowledge_points(plan: dict) -> list[str]:
    if not isinstance(plan, dict):
        return []
    kps = plan.get("knowledge_points") or plan.get("knowledge_point") or []
    if isinstance(kps, str):
        return [kps]
    if isinstance(kps, list):
        return [str(k) for k in kps if k]
    return []


def _get_learning_objectives(plan: dict) -> list[str]:
    if not isinstance(plan, dict):
        return []
    for key in ("learning_objectives", "objectives", "goals"):
        v = plan.get(key)
        if isinstance(v, list):
            return [str(x) for x in v if x]
        if isinstance(v, str) and v.strip():
            import re
            return [c.strip() for c in re.split(r"[銆俓n;锛沒+", v) if c.strip()]
    return []


def _get_assessment(plan: dict) -> dict:
    if not isinstance(plan, dict):
        return {}
    a = plan.get("assessment")
    return a if isinstance(a, dict) else {}


def _get_clip_duration_sec(clip: dict) -> Optional[float]:
    for key in ("duration_sec", "duration_seconds", "duration"):
        if key in clip and clip[key] is not None:
            try:
                return float(clip[key])
            except (TypeError, ValueError):
                pass
    tc = clip.get("timecode") or {}
    if isinstance(tc, dict):
        try:
            ip = tc.get("in_point")
            op = tc.get("out_point")
            if ip is not None and op is not None:
                return float(op) - float(ip)
        except (TypeError, ValueError):
            pass
    return None


def _calc_total_duration(plan: dict) -> float:
    total = 0.0
    for clip in _get_clips(plan):
        d = _get_clip_duration_sec(clip)
        if d:
            total += d
    return total


def _format_duration(seconds: float) -> str:
    m = int(seconds // 60)
    s = int(seconds % 60)
    return f"{m}鍒唟s}绉? if m else f"{s}绉?


# ---------------------------------------------------------------------------
# CLI 涓诲叆鍙?
# ---------------------------------------------------------------------------

def main() -> int:
    log = get_logger("compose")
    parser = argparse.ArgumentParser(description="闃舵 4锛氬悎鎴愭渶缁堟暀瀛︿氦浠樼墿")
    parser.add_argument("--blueprint", required=True, help="浜戠杩斿洖鐨?lesson_plan.json 璺緞")
    parser.add_argument("--output", required=True, help="杈撳嚭 final_lesson.md 璺緞")
    parser.add_argument("--candidates", default=None, help="candidate_knowledge.json 璺緞锛堝彲閫夛級")
    parser.add_argument("--assessment", default=None, help="杈撳嚭 assessment.json 璺緞锛堥粯璁?<output> 鍚岀洰褰曪級")
    parser.add_argument("--html", default=None, help="杈撳嚭 courseware.html 璺緞锛堝彲閫夛級")
    parser.add_argument(
        "--skip-guard",
        action="store_true",
        help="璺宠繃 lesson_plan_guard 鏍￠獙锛堜粎璋冭瘯鐢紝涓嶆帹鑽愶級",
    )
    args = parser.parse_args()

    plan_path = Path(args.blueprint)
    output_path = Path(args.output)

    # 1. 鍔犺浇 lesson_plan
    try:
        plan = load_lesson_plan(plan_path)
    except (FileNotFoundError, ValueError) as e:
        log.error(f"[compose] 鉁?{e}")
        return 1

    candidates = load_candidates(Path(args.candidates) if args.candidates else None)

    # 2. lesson_plan_guard 鏍￠獙锛? 椤圭‖瑙勫垯锛?
    if not args.skip_guard:
        log.info("[compose] 鎵ц lesson_plan_guard 鏍￠獙锛? 椤圭‖瑙勫垯锛?..")
        passed, errors = validate_lesson_plan(plan, candidates, None)
        if not passed:
            log.error("[compose] 鉁?鏍￠獙澶辫触锛屾嫆缁濆悎鎴愶細")
            log.error(render_error_report(errors))
            # 鍐欏嚭閿欒鎶ュ憡
            report_path = output_path.parent / "guard_errors.json"
            report_path.write_text(
                json.dumps({"passed": False, "errors": errors}, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            log.error(f"[compose] 閿欒鎶ュ憡锛歿report_path}")
            return 1
        log.info("[compose] 鉁?鏍￠獙閫氳繃")
    else:
        log.error("[compose] 鈿?宸茶烦杩?guard 鏍￠獙锛?-skip-guard锛?)

    # 3. 娓叉煋 Markdown 璇句欢
    md_content = render_markdown(plan, candidates)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(md_content, encoding="utf-8")
    log.info(f"[compose] 鉁?Markdown 璇句欢锛歿output_path}")

    # 4. 娓叉煋 assessment.json
    assessment_path = Path(args.assessment) if args.assessment else output_path.parent / "assessment.json"
    assessment_data = render_assessment(plan)
    assessment_path.write_text(
        json.dumps(assessment_data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    log.info(f"[compose] 鉁?璇勪及棰橈細{assessment_path}锛坽assessment_data.get('total_questions', 0)} 棰橈級")

    # 5. 娓叉煋 courseware.html锛堝彲閫夛級
    if args.html:
        html_path = Path(args.html)
        html_content = render_courseware_html(plan, candidates)
        html_path.write_text(html_content, encoding="utf-8")
        log.info(f"[compose] 鉁?浜掑姩璇句欢锛歿html_path}")

    log.info("[compose] 鉁?鍏ㄩ儴浜や粯鐗╃敓鎴愬畬鎴?)
    print(str(output_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())

