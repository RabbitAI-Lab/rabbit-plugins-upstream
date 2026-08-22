"""
analyze_courseware.py - 闃舵 2锛氭湰鍦版枃鏈帹鐞嗗垎鏋愯绋嬫潗鏂欍€?

瀵瑰簲 video-editing-skills-main/scripts/analyze_video.py锛屼絾鎶?VLM 瑙嗛鎶藉抚鐞嗚В"
閲嶆槧灏勪负"DeepSeek-R1-1.5B 鏂囨湰鍒囩墖鎺ㄧ悊"銆?

鍏抽敭宸紓锛坴s video-editing锛夛細
  - 浣跨敤 openvino_genai.LLMPipeline锛堥潪 VLMPipeline锛?
  - 杈撳叆鏄枃鏈垏鐗囷紙闈炶棰戝抚锛?
  - 涓ら樁娈垫彁绀鸿瘝锛氶樁娈? 鐭ヨ瘑鐐瑰垽瀹?32 token) 鈫?闃舵2 璇︾粏鏁欏寤鸿(鈮?00 token)
  - 杈撳嚭 output_reasoning.json锛圴7 abstract_data 鏍煎紡锛? 10KB锛?

璁惧闄嶇骇锛圴7 npu-scheduling-guide 搂2.2锛夛細
  NPU 鈫?GPU 鈫?CPU锛坮equested_device 涓嶅彲鐢ㄦ椂鑷姩闄嶇骇锛?

mock 妯″紡锛?-mock-mode锛夛細
  涓嶅姞杞界湡瀹炴ā鍨嬶紝鐢ㄥ熀浜庤鍒欑殑妯℃嫙鎺ㄧ悊锛屼究浜庢棤妯″瀷鐜娴嬭瘯鍏ㄩ摼璺€?

鐢ㄦ硶锛?
    python scripts/analyze_courseware.py \\
        --course-dir "<your_course_dir>" \\
        --output "<workspace>/output_reasoning.json" \\
        --theme "鏈哄櫒瀛︿範鍏ラ棬" \\
        --device GPU

    # mock 妯″紡锛堟棤闇€妯″瀷锛屾祴璇曠敤锛?
    python scripts/analyze_courseware.py --course-dir "<your_course_dir>" --output "<workspace>/output_reasoning.json" --mock-mode

    # 绀轰緥锛歐indows 涓?D:\courses 鐩綍
    #   python scripts/analyze_courseware.py --course-dir "D:\\courses" --output "...\\output_reasoning.json" --theme "鏈哄櫒瀛︿範"
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

log = get_logger("analyze")

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Optional

from skill_runtime import DEFAULT_MODEL_DIR

# 鏂囨湰鍒囩墖鍙傛暟
SEGMENT_MAX_CHARS = 800      # 姣忔鏈€澶у瓧绗︽暟
SEGMENT_OVERLAP_CHARS = 100  # 娈甸棿閲嶅彔锛堜繚鎸佷笂涓嬫枃杩炶疮锛?

# 涓ら樁娈垫彁绀鸿瘝 token 棰勭畻
STAGE1_MAX_TOKENS = 32   # 鐭ヨ瘑鐐瑰垽瀹?
STAGE2_MAX_TOKENS = 256  # 璇︾粏鏁欏寤鸿锛堚墺200锛?


# ---------------------------------------------------------------------------
# 鏂囨湰鍒囩墖
# ---------------------------------------------------------------------------

def split_text(text: str, max_chars: int = SEGMENT_MAX_CHARS,
               overlap: int = SEGMENT_OVERLAP_CHARS) -> list[str]:
    """鎶婇暱鏂囨湰鍒囨垚 ~max_chars 瀛楃鐨勬锛屾闂撮噸鍙?overlap 瀛楃銆?

    浼樺厛鎸夊弻鎹㈣锛堟钀斤級鍒囷紝娈佃惤杩囬暱鏃舵寜鍙ュ彿鍒囷紝鍐嶈繃闀挎寜 max_chars 纭垏銆?
    """
    if not text or not text.strip():
        return []
    text = text.strip()

    # 鍏堟寜娈佃惤鍒?
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    segments: list[str] = []
    buf = ""

    def _flush() -> None:
        nonlocal buf
        if buf.strip():
            segments.append(buf.strip())
        buf = ""

    for para in paragraphs:
        if len(para) > max_chars:
            # 娈佃惤杩囬暱锛氬厛 flush锛屽啀鎸夊彞鍙峰垏
            _flush()
            sentences = re.split(r"(?<=[銆傦紒锛?!?\n])", para)
            for sent in sentences:
                if not sent.strip():
                    continue
                if len(buf) + len(sent) > max_chars and buf:
                    segments.append(buf.strip())
                    buf = sent if len(sent) <= max_chars else sent[:max_chars]
                else:
                    buf += sent
                while len(buf) > max_chars:
                    segments.append(buf[:max_chars])
                    buf = buf[max_chars - overlap:]
            _flush()
        elif len(buf) + len(para) + 2 > max_chars:
            _flush()
            buf = para
        else:
            buf = (buf + "\n\n" + para) if buf else para
    _flush()
    return segments


def read_courseware(path: Path) -> str:
    """璇诲彇璇剧▼鏉愭枡鏂囦欢鍐呭锛?md/.txt 鐩磋锛?pdf 灏濊瘯瀵煎叆搴擄級銆?""
    suffix = path.suffix.lower()
    if suffix in (".md", ".txt"):
        return path.read_text(encoding="utf-8", errors="replace")
    if suffix == ".pdf":
        try:
            import PyPDF2  # type: ignore
        except ImportError:
            try:
                import pdfplumber  # type: ignore
                with pdfplumber.open(path) as pdf:
                    return "\n\n".join((p.extract_text() or "") for p in pdf.pages)
            except ImportError:
                log.warn(f"[analyze] 鈿?璺宠繃 PDF锛堟湭瑁?PyPDF2/pdfplumber锛夛細{path.name}")
                return ""
        text_parts: list[str] = []
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text_parts.append(page.extract_text() or "")
        return "\n\n".join(text_parts)
    return ""


# ---------------------------------------------------------------------------
# 涓ら樁娈垫彁绀鸿瘝
# ---------------------------------------------------------------------------

def build_topic_judgement_prompt(text: str, theme: str) -> str:
    """闃舵 1锛氱煡璇嗙偣鍒ゅ畾锛?2 token锛夈€?

    璁╂ā鍨嬪垽鏂娈垫枃鏈槸鍚︿笌涓婚鐩稿叧锛岃繑鍥?绗﹀悎/閮ㄥ垎绗﹀悎/涓嶇鍚堛€?
    """
    snippet = text[:300] if len(text) > 300 else text
    return (
        f"鍒ゆ柇浠ヤ笅鏁欏鍐呭鏄惁涓庝富棰樸€寋theme}銆嶇浉鍏炽€俓n"
        f"鍙洖绛旓細绗﹀悎 / 閮ㄥ垎绗﹀悎 / 涓嶇鍚圽n\n"
        f"鏁欏鍐呭锛歿snippet}\n\n"
        f"鍥炵瓟锛?
    )


def build_detail_prompt(text: str, theme: str) -> str:
    """闃舵 2锛氳缁嗘暀瀛﹀缓璁紙鈮?00 token锛夈€?

    璁╂ā鍨嬭緭鍑虹煡璇嗙偣鏍囩 + 闅惧害绛夌骇 + 鏁欏寤鸿銆?
    """
    return (
        f"浣犳槸AI閫氳瘑璇炬暀瀛︿笓瀹躲€傝鍒嗘瀽浠ヤ笅鏁欏鍐呭锛岃緭鍑猴細\n"
        f"1. 鐭ヨ瘑鐐规爣绛撅紙3~5涓紝閫楀彿鍒嗛殧锛塡n"
        f"2. 闅惧害绛夌骇锛?~5锛?鏈€绠€鍗曪級\n"
        f"3. 鏁欏寤鸿锛堥€傚悎鐨勬暀瀛︽硶銆佷簰鍔ㄦ柟寮忋€佹敞鎰忎簨椤癸級\n\n"
        f"涓婚锛歿theme}\n"
        f"鏁欏鍐呭锛歿text}\n\n"
        f"璇锋寜浠ヤ笅鏍煎紡杈撳嚭锛歕n"
        f"鐭ヨ瘑鐐癸細xxx,xxx,xxx\n"
        f"闅惧害锛歂\n"
        f"寤鸿锛歺xx"
    )


# ---------------------------------------------------------------------------
# 鎺ㄧ悊缁撴灉瑙ｆ瀽
# ---------------------------------------------------------------------------

def parse_detail_response(text: str) -> dict:
    """瑙ｆ瀽闃舵 2 鐨勬ā鍨嬭緭鍑猴紝鎻愬彇 knowledge_tags / difficulty / pedagogy_suggestion銆?""
    result: dict[str, Any] = {
        "knowledge_tags": [],
        "difficulty": 2,
        "pedagogy_suggestion": "",
    }
    if not text:
        return result

    # 鎻愬彇鐭ヨ瘑鐐?
    m = re.search(r"鐭ヨ瘑鐐筟锛?]\s*(.+)", text)
    if m:
        tags = [t.strip() for t in re.split(r"[,锛?锛涖€乚", m.group(1)) if t.strip()]
        result["knowledge_tags"] = tags[:5]

    # 鎻愬彇闅惧害
    m = re.search(r"闅惧害[锛?]\s*(\d)", text)
    if m:
        try:
            d = int(m.group(1))
            result["difficulty"] = max(1, min(5, d))
        except ValueError:
            pass

    # 鎻愬彇寤鸿
    m = re.search(r"寤鸿[锛?]\s*(.+)", text, re.DOTALL)
    if m:
        result["pedagogy_suggestion"] = m.group(1).strip()[:500]

    # 濡傛灉娌℃彁鍙栧埌寤鸿锛岀敤鍏ㄦ枃鍏滃簳
    if not result["pedagogy_suggestion"]:
        result["pedagogy_suggestion"] = text.strip()[:500]

    return result


def is_topic_relevant(judgement: str) -> bool:
    """鍒ゆ柇闃舵 1 杈撳嚭鏄惁琛ㄧず鐩稿叧銆?""
    if not judgement:
        return True  # 鏃犳硶鍒ゆ柇鏃堕粯璁ょ浉鍏筹紙閬垮厤婕忛€夛級
    j = judgement.strip()
    return "绗﹀悎" in j and "涓嶇鍚? not in j


# ---------------------------------------------------------------------------
# Pipeline 鍒濆鍖栵紙鐪熷疄妯″紡锛?
# ---------------------------------------------------------------------------

def init_text_pipeline(model_dir: Path, device: str) -> tuple[Any, str]:
    """鍔犺浇 OpenVINO LLMPipeline锛岃澶囦笉鍙敤鏃惰嚜鍔ㄩ檷绾с€?

    闄嶇骇閾撅細NPU 鈫?GPU 鈫?CPU锛圴7 npu-scheduling-guide 搂2.2锛?

    V7-AIPC锛歞evice="AUTO" 鑷姩璋冨害 NPU/iGPU/CPU锛圴7.3.2 鏀硅繘3 鍗囩骇鐗堬級銆?

    Returns:
        (pipeline, actual_device)
    """
    try:
        import openvino_genai  # type: ignore
    except ImportError as e:
        raise RuntimeError(
            f"鏈畨瑁?openvino-genai锛屾棤娉曞姞杞芥ā鍨嬶細{e}\n"
            "璇疯繍琛?bootstrap.py 瀹夎渚濊禆锛屾垨浣跨敤 --mock-mode 娴嬭瘯銆?
        ) from e

    # V7.3.2 鏀硅繘3锛氳嚜鍔ㄧ‖浠惰皟搴?
    if device.upper() == "AUTO":
        try:
            from hardware_probe import auto_select_device
            device = auto_select_device(prefer="GPU")
            log.info(f"[analyze] 鑷姩纭欢璋冨害锛氶€夋嫨 {device}")
        except ImportError:
            log.warn("[analyze] hardware_probe 涓嶅彲鐢紝fallback 鍒?GPU")
            device = "GPU"

    # 闄嶇骇閾?
    devices_to_try = [device]
    for fallback in ("NPU", "GPU", "CPU"):
        if fallback not in devices_to_try:
            devices_to_try.append(fallback)

    last_error: Optional[Exception] = None
    for dev in devices_to_try:
        try:
            pipeline = openvino_genai.LLMPipeline(str(model_dir), dev)
            if dev != device:
                log.error(f"[analyze] 鈿?璇锋眰璁惧 {device} 涓嶅彲鐢紝闄嶇骇鍒?{dev}")
            return pipeline, dev
        except Exception as e:
            last_error = e
            log.error(f"[analyze] 璁惧 {dev} 涓嶅彲鐢細{e}")
            continue

    raise RuntimeError(f"鎵€鏈夎澶囧潎涓嶅彲鐢細{last_error}")


def generate(pipeline: Any, prompt: str, max_new_tokens: int) -> str:
    """璋冪敤 LLMPipeline.generate锛堝吋瀹逛笉鍚?openvino_genai 鐗堟湰锛夈€?""
    try:
        import openvino_genai  # type: ignore
        config = openvino_genai.GenerationConfig()
        config.max_new_tokens = max_new_tokens
        result = pipeline.generate(prompt, config)
        return getattr(result, "text", str(result))
    except ImportError:
        pass
    # 鍏滃簳锛氱洿鎺ヨ皟 generate
    if hasattr(pipeline, "generate"):
        result = pipeline.generate(prompt)
        return getattr(result, "text", str(result))
    return ""


# ---------------------------------------------------------------------------
# Mock 鎺ㄧ悊锛堟棤妯″瀷鏃舵祴璇曠敤锛?
# ---------------------------------------------------------------------------

_MOCK_KEYWORD_MAP = {
    "鏈哄櫒瀛︿範": ["鏈哄櫒瀛︿範", "鐩戠潱瀛︿範", "鏃犵洃鐫ｅ涔?, "娣卞害瀛︿範", "绁炵粡缃戠粶"],
    "浜哄伐鏅鸿兘": ["浜哄伐鏅鸿兘", "AI", "鏅鸿兘", "鏈哄櫒鏅鸿兘"],
    "鏁版嵁": ["鏁版嵁", "鏁版嵁闆?, "鏁版嵁鍒嗘瀽", "鏁版嵁鎸栨帢"],
    "绠楁硶": ["绠楁硶", "鎺掑簭", "鎼滅储", "閫掑綊"],
    "Python": ["Python", "缂栫▼", "浠ｇ爜", "鍑芥暟"],
    "浼︾悊": ["浼︾悊", "闅愮", "瀹夊叏", "鍋忚", "鍏钩"],
}

_MOCK_PEDAGOGY = {
    1: "寤鸿閲囩敤璁叉巿寮?瀹炰緥婕旂ず锛岄檷浣庤鐭ラ棬妲?,
    2: "寤鸿閲囩敤鎺㈢┒寮忔暀瀛︼紝寮曞瀛︾敓涓诲姩鎬濊€?,
    3: "寤鸿閲囩敤 PBL 椤圭洰寮忓涔狅紝缁撳悎瀹為檯妗堜緥",
    4: "寤鸿閲囩敤缈昏浆璇惧爞锛岃鍓嶉涔?璇句腑娣卞害璁ㄨ",
    5: "寤鸿閲囩敤 5E 妯″瀷锛屽己璋冨垱閫犱笌璇勪环",
}


def mock_analyze_segment(text: str, theme: str) -> dict:
    """鍩轰簬瑙勫垯鐨勬ā鎷熸帹鐞嗭紙mock 妯″紡锛夈€?""
    tags: list[str] = []
    text_lower = text.lower()
    for keyword, related in _MOCK_KEYWORD_MAP.items():
        for r in related:
            if r.lower() in text_lower:
                if keyword not in tags:
                    tags.append(keyword)
                break

    if not tags:
        # 鏃犲懡涓椂锛屽彇鍓嶅嚑涓悕璇嶄綔鍏滃簳
        words = re.findall(r"[\u4e00-\u9fa5]{2,4}", text)
        tags = list(dict.fromkeys(words))[:3] or ["閫氳瘑姒傚康"]

    # 闅惧害锛氭牴鎹枃鏈暱搴﹀拰鍏抽敭璇嶆暟閲忕矖浼?
    difficulty = min(5, max(1, 2 + len(text) // 1000 - len(tags) // 2))
    difficulty = max(1, min(5, difficulty))

    return {
        "knowledge_tags": tags[:5],
        "difficulty": difficulty,
        "pedagogy_suggestion": _MOCK_PEDAGOGY.get(difficulty, _MOCK_PEDAGOGY[2]),
    }


# ---------------------------------------------------------------------------
# 涓诲垎鏋愭祦绋?
# ---------------------------------------------------------------------------

def analyze_segment(
    pipeline: Any,
    text: str,
    theme: str,
    *,
    mock_mode: bool = False,
) -> dict:
    """鍒嗘瀽鍗曟鏂囨湰锛岃繑鍥?{knowledge_tags, difficulty, pedagogy_suggestion}銆?

    涓ら樁娈垫帹鐞嗭紙鐪熷疄妯″紡锛夛細
      Stage 1: 涓婚鍒ゅ畾锛?2 token锛夆啋 涓嶇浉鍏冲垯璺宠繃璇︾粏鎺ㄧ悊
      Stage 2: 璇︾粏鏁欏寤鸿锛堚墺200 token锛?
    """
    if mock_mode:
        return mock_analyze_segment(text, theme)

    # 闃舵 1锛氫富棰樺垽瀹?
    if theme:
        j_prompt = build_topic_judgement_prompt(text, theme)
        j_result = generate(pipeline, j_prompt, STAGE1_MAX_TOKENS)
        if not is_topic_relevant(j_result):
            return {
                "knowledge_tags": [],
                "difficulty": 0,
                "pedagogy_suggestion": f"[涓婚涓嶇浉鍏砞 妯″瀷鍒ゅ畾涓庛€寋theme}銆嶄笉绗﹀悎",
            }

    # 闃舵 2锛氳缁嗘暀瀛﹀缓璁?
    d_prompt = build_detail_prompt(text, theme)
    d_result = generate(pipeline, d_prompt, STAGE2_MAX_TOKENS)
    return parse_detail_response(d_result)


def process_courseware(
    courseware_path: Path,
    pipeline: Any,
    theme: str,
    *,
    mock_mode: bool = False,
    seg_id_start: int = 0,
) -> tuple[list[dict], int]:
    """澶勭悊鍗曚釜璇剧▼鏉愭枡鏂囦欢锛岃繑鍥?(segments, next_seg_id)銆?""
    content = read_courseware(courseware_path)
    if not content.strip():
        return [], seg_id_start

    chunks = split_text(content)
    segments: list[dict] = []
    seg_id = seg_id_start

    for chunk in chunks:
        analysis = analyze_segment(pipeline, chunk, theme, mock_mode=mock_mode)
        segments.append({
            "seg_id": seg_id,
            "source_file": str(courseware_path),
            "source_filename": courseware_path.name,
            "seg_text": chunk[:200] + ("..." if len(chunk) > 200 else ""),
            "seg_text_full_length": len(chunk),
            "knowledge_tags": analysis["knowledge_tags"],
            "difficulty": analysis["difficulty"],
            "pedagogy_suggestion": analysis["pedagogy_suggestion"],
        })
        seg_id += 1

    return segments, seg_id


# ---------------------------------------------------------------------------
# CLI 涓诲叆鍙?
# ---------------------------------------------------------------------------

def main() -> int:
    log = get_logger("analyze")
    parser = argparse.ArgumentParser(description="闃舵 2锛氭湰鍦版枃鏈帹鐞嗗垎鏋愯绋嬫潗鏂?)
    parser.add_argument("--course-dir", required=True, help="璇剧▼鏉愭枡鎵€鍦ㄧ洰褰?)
    parser.add_argument("--output", required=True, help="杈撳嚭 output_reasoning.json 璺緞")
    parser.add_argument("--theme", default=None, help="鏁欏涓婚锛堝惎鐢ㄤ袱闃舵鎻愮ず璇嶏級")
    parser.add_argument("--device", default="GPU", help="鎺ㄧ悊璁惧锛圢PU/GPU/CPU/AUTO锛岄粯璁?GPU锛汚UTO 鑷姩鎺㈡祴锛?)
    parser.add_argument("--model-dir", default=None, help="妯″瀷鐩綍锛堥粯璁?DEFAULT_MODEL_DIR锛?)
    parser.add_argument(
        "--mock-mode",
        action="store_true",
        help="涓嶅姞杞界湡瀹炴ā鍨嬶紝鐢ㄥ熀浜庤鍒欑殑妯℃嫙鎺ㄧ悊锛堟祴璇曠敤锛?,
    )
    args = parser.parse_args()

    course_dir = Path(args.course_dir).resolve()
    if not course_dir.is_dir():
        log.error(f"閿欒锛氳绋嬬洰褰曚笉瀛樺湪锛歿course_dir}")
        return 1

    # 鏀堕泦璇剧▼鏉愭枡
    exts = {".md", ".txt", ".pdf"}
    courseware = sorted(
        f for f in course_dir.iterdir()
        if f.is_file() and f.suffix.lower() in exts
    )
    if not courseware:
        log.error(f"閿欒锛氱洰褰曚腑鏈壘鍒拌绋嬫潗鏂欙細{course_dir}")
        return 1

    log.info(f"[analyze] 鎵惧埌 {len(courseware)} 涓绋嬫潗鏂?)
    if args.theme:
        log.info(f"[analyze] 涓婚鎰熺煡妯″紡锛歿args.theme}")

    # 鍒濆鍖?pipeline
    if args.mock_mode:
        log.info("[analyze] mock 妯″紡锛氫娇鐢ㄥ熀浜庤鍒欑殑妯℃嫙鎺ㄧ悊")
        pipeline = None
    else:
        model_dir = Path(args.model_dir) if args.model_dir else DEFAULT_MODEL_DIR
        if not model_dir.exists():
            log.error(f"閿欒锛氭ā鍨嬬洰褰曚笉瀛樺湪锛歿model_dir}")
            log.error("璇峰厛杩愯 bootstrap.py锛屾垨浣跨敤 --mock-mode 娴嬭瘯銆?)
            return 1
        log.info(f"[analyze] 鍔犺浇妯″瀷锛歿model_dir}锛堣澶囷細{args.device}锛?)
        pipeline, actual_device = init_text_pipeline(model_dir, args.device)
        log.info(f"[analyze] 鉁?妯″瀷宸插姞杞斤紙瀹為檯璁惧锛歿actual_device}锛?)

    # 閫愭枃浠跺鐞?
    all_segments: list[dict] = []
    processed_docs: list[dict] = []
    seg_id = 0

    for cw in courseware:
        log.info(f"[analyze] 澶勭悊锛歿cw.name}")
        segs, seg_id = process_courseware(
            cw, pipeline, args.theme or "",
            mock_mode=args.mock_mode,
            seg_id_start=seg_id,
        )
        all_segments.extend(segs)
        processed_docs.append({
            "file": str(cw),
            "filename": cw.name,
            "segment_count": len(segs),
            "segment_ids": [s["seg_id"] for s in segs],
        })
        log.info(f"  鈫?{len(segs)} 娈?)

    # 鏋勫缓杈撳嚭锛堜繚鎸佷笌 video-editing 瀛楁鍚嶅吋瀹癸細vlm_prompt / processed_documents / segments锛?
    vlm_prompt = (
        build_detail_prompt(f"涓婚锛歿args.theme}", args.theme)
        if args.theme else "鏃犱富棰橈紙鍏ㄩ噺鍒嗘瀽妯″紡锛?
    )

    output = {
        "vlm_prompt": vlm_prompt[:500],
        "theme": args.theme,
        "device": args.device if not args.mock_mode else "mock",
        "processed_documents": processed_docs,
        "segments": all_segments,
        "total_segments": len(all_segments),
    }

    # 鍐欏嚭
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(output, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # V7 搂4.1 绾︽潫锛歛bstract_data < 10KB锛堝鏋滆秴浜嗙粰璀﹀憡锛?
    size = output_path.stat().st_size
    if size >= 10240:
        log.warn(
            f"[analyze] 鈿?output_reasoning.json 澶у皬 {size}B 鈮?10KB锛岀浜戜氦鎹㈡椂灏嗚 edge_cloud_dispatch 鎴柇"
        )

    log.info(f"[analyze] 鉁?杈撳嚭锛歿output_path}锛坽len(all_segments)} 娈碉紝{size}B锛?)
    print(str(output_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())

