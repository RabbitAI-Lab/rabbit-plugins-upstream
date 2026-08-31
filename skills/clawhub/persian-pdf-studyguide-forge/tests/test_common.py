import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from common import (normalize_persian,search_normalize,extract_json,
                    coerce_ref,coerce_answer,is_bare_answer,strip_option_prefix)

def test_persian_letters_digits_and_zwnj():
    out=normalize_persian('كتاب 123 ي\u200cك')
    assert out=='کتاب ۱۲۳ ی\u200cک'

def test_bidi_removed():
    assert '\u202b' not in normalize_persian('\u202bمتن\u202c')

def test_search_digit_equivalence():
    assert search_normalize('صفحه ۱۲۳')==search_normalize('صفحه 123')

def test_json_fence():
    assert extract_json('```json\n[{"page":1}]\n```')[0]['page']==1

def test_coerce_ref_persian_string():
    assert coerce_ref('صفحهٔ ۳',1,10)==3
    assert coerce_ref('5',1,10)==5

def test_coerce_ref_clamps_and_falls_back():
    assert coerce_ref(99,1,10)==10
    assert coerce_ref(0,1,10)==1
    assert coerce_ref('بدون عدد',1,10)==1

def test_coerce_answer_persian_labels():
    assert coerce_answer('الف')=='A'
    assert coerce_answer('ج')=='C'
    assert coerce_answer('۲')=='B'
    assert coerce_answer('b')=='B'
    assert coerce_answer('')==''

def test_is_bare_answer():
    assert is_bare_answer('A') is True
    assert is_bare_answer('') is True
    assert is_bare_answer('ورزش') is False

def test_strip_option_prefix():
    assert strip_option_prefix('الف) مرحله دیوار')=='مرحله دیوار'
    assert strip_option_prefix('A) hello')=='hello'


# ── v1.4.0: model-agnostic layer ──────────────────────────────────────────
import os, json as _json
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from common import (canonical_json, content_key, dedupe_items, similarity,
                    consensus_pick, stable_sort_items)
import model_adapters as MA


def test_canonical_json_is_stable_and_sorted():
    a = canonical_json({"b": 1, "a": {"z": 1, "y": 2}})
    b = canonical_json({"a": {"y": 2, "z": 1}, "b": 1})
    assert a == b and '"a"' in a.split('\n')[1]


def test_strip_reasoning_tags():
    assert MA.sanitize_model_text('<think>plan</think>{"a":1}') == '{"a":1}'
    # unterminated reasoning block (truncated response)
    assert MA.sanitize_model_text('{"a":1}\n<think>cut off...') == '{"a":1}'


def test_strip_fences_bom_and_bidi():
    raw = '\ufeff```json\n\u200f{"a": 1}\u200e\n```'
    assert _json.loads(MA.sanitize_model_text(raw)) == {"a": 1}


def test_parse_trailing_commas_and_python_constants():
    got = MA.parse_json_loose('{"a": [1,2,], "b": True, "c": None,}')
    assert got == {"a": [1, 2], "b": True, "c": None}


def test_parse_ndjson():
    got = MA.parse_json_loose('{"page":1}\n{"page":2}')
    assert [x["page"] for x in got] == [1, 2]


def test_parse_truncated_json_recovers_prefix():
    got = MA.parse_json_loose('{"flash":[{"q":"a","a":"b"},{"q":"c","a":"d"')
    assert got["flash"][0]["q"] == "a"


def test_refusal_is_detected():
    try:
        MA.parse_json_loose("I'm sorry, I can't help with that request.")
    except MA.ContractError:
        pass
    else:
        raise AssertionError("refusal should raise ContractError")


def test_finish_reason_normalization_across_vendors():
    assert MA._finish("end_turn") == "stop"          # anthropic
    assert MA._finish("MAX_TOKENS") == "length"      # gemini
    assert MA._finish("length") == "length"          # openai
    assert MA._finish("COMPLETE") == "stop"          # cohere
    assert MA._finish("SAFETY") == "filter"


def test_usage_normalization_across_vendors():
    assert MA._usage({"input_tokens": 5, "output_tokens": 7})["total"] == 12
    assert MA._usage({"promptTokenCount": 3, "candidatesTokenCount": 4})["completion"] == 4


def test_rejection_classifier_handles_pydantic_extra_forbidden():
    body = '{"detail":[{"type":"extra_forbidden","loc":["body","seed"],"msg":"Extra inputs are not permitted"}]}'
    assert MA._classify_rejection(body) == "seed"


def test_rejection_classifier_max_completion_tokens():
    body = "Unsupported parameter: 'max_tokens' is not supported; use 'max_completion_tokens' instead."
    assert MA._classify_rejection(body) == "max_tokens_field"


def test_retired_model_suggestion_is_followed():
    body = ("This model models/gemini-2.5-flash is no longer available to new users. "
            "Please update your code to use models/gemini-3.6-flash for the latest features.")
    assert MA._suggested_model(body) == "gemini-3.6-flash"


def test_dedupe_and_similarity_across_models():
    a = {"q": "ظرفیت حافظهٔ کوتاه‌مدت چقدر است؟", "a": "هفت واحد", "ref": 1}
    b = {"q": "ظرفیت حافظه کوتاه مدت چقدر است ؟", "a": "هفت واحد", "ref": 1}
    assert content_key(a["q"]) == content_key(b["q"])
    assert len(dedupe_items([a, b])) == 1
    assert similarity("حافظهٔ کوتاه‌مدت هفت واحد", "حافظه کوتاه مدت هفت واحد") > 0.9


def test_consensus_ranks_agreement_first():
    m1 = [{"q": "الف چیست؟", "ref": 1}, {"q": "تنها در مدل یک", "ref": 1}]
    m2 = [{"q": "الف چیست ؟", "ref": 1}]
    m3 = [{"q": "الف چیست؟", "ref": 1}]
    out = consensus_pick([m1, m2, m3])
    assert content_key(out[0]["q"]) == content_key("الف چیست؟")
    assert len(out) == 2
    strict = consensus_pick([m1, m2, m3], min_votes=2)
    assert len(strict) == 1


def test_stable_sort_is_deterministic():
    items = [{"q": "ب", "ref": 3}, {"q": "الف", "ref": 1}, {"q": "ج", "ref": 1}]
    assert [x["ref"] for x in stable_sort_items(items)] == [1, 1, 3]
    assert stable_sort_items(items) == stable_sort_items(list(reversed(items)))


def test_mock_provider_is_deterministic_and_offline():
    p = MA.ProviderInfo(name="mock", dialect="mock", model="deterministic-mock")
    prompt = 'صفحه 1 test {"flash":[2 objects]}'
    a = MA.call_model(p, prompt, "sys", max_tokens=500, use_cache=False)
    b = MA.call_model(p, prompt, "sys", max_tokens=500, use_cache=False)
    assert a.text == b.text and a.finish == "stop"
    assert len(_json.loads(a.text)["flash"]) == 2


def test_provider_info_is_dict_compatible_with_v13_code():
    p = MA.ProviderInfo(name="x", dialect="gemini", model="m")
    assert p["name"] == "x" and p["model"] == "m"
    assert p.get("kind") == "gemini"          # v1.3 code read provider["kind"]


def test_discover_providers_from_env(monkeypatch=None):
    old = dict(os.environ)
    try:
        for k in list(os.environ):
            if k.endswith("_API_KEY") or k in ("HF_TOKEN", "OLLAMA_HOST"):
                del os.environ[k]
        os.environ["ANTHROPIC_API_KEY"] = "test-key"
        provs = MA.discover_providers()
        assert any(p.dialect == "anthropic" for p in provs)
    finally:
        os.environ.clear()
        os.environ.update(old)


def test_all_dialects_have_an_adapter():
    assert set(MA.DIALECTS) == set(MA._ADAPTERS)
