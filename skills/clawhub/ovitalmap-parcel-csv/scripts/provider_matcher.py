"""Return conservative provider-name candidates; never merge names automatically."""

import json
import re
import sys

try:
    from pypinyin import lazy_pinyin
except ImportError:  # Optional enhancement; all other matching remains available.
    lazy_pinyin = None


HONORIFICS = ("先生", "经理", "老板", "女士", "小姐", "老师", "师傅", "总", "哥", "姐")
PREFIXES = ("中非", "三一", "非洲", "刚果")


def _normalize(value):
    return re.sub(r"[\s\-_.·]+", "", str(value).strip().lower())


def _strip_affixes(value):
    result = _normalize(value)
    for prefix in PREFIXES:
        normalized = _normalize(prefix)
        if result.startswith(normalized):
            result = result[len(normalized):]
            break
    for suffix in HONORIFICS:
        normalized = _normalize(suffix)
        if result.endswith(normalized):
            result = result[:-len(normalized)]
            break
    return result


def _contains_chinese(value):
    return bool(re.search(r"[\u4e00-\u9fff]", str(value)))


def _pinyin(value):
    if not lazy_pinyin or not _contains_chinese(value):
        return None
    return "".join(lazy_pinyin(str(value))).lower()


def _score(input_name, existing_name):
    input_normalized = _normalize(input_name)
    existing_normalized = _normalize(existing_name)
    if input_normalized == existing_normalized:
        return "exact", 100

    input_pinyin = _pinyin(input_name)
    existing_pinyin = _pinyin(existing_name)
    if input_pinyin and existing_pinyin and input_pinyin == existing_pinyin:
        return "pinyin_match", 90
    if input_pinyin == existing_normalized or existing_pinyin == input_normalized:
        return "pinyin_cross_match", 85

    input_stripped = _strip_affixes(input_name)
    existing_stripped = _strip_affixes(existing_name)
    if input_stripped and input_stripped == existing_stripped:
        return "affix_variation", 80
    if (
        input_normalized
        and existing_normalized
        and (
            input_normalized in existing_normalized
            or existing_normalized in input_normalized
        )
    ):
        return "substring", 70
    return None, 0


def fuzzy_match(input_name, existing_names):
    candidates = []
    for existing_name in dict.fromkeys(existing_names):
        reason, score = _score(input_name, existing_name)
        if reason:
            candidates.append(
                {"name": existing_name, "reason": reason, "score": score}
            )
    candidates.sort(key=lambda item: (-item["score"], item["name"]))

    exact_match = next(
        (
            candidate["name"]
            for candidate in candidates
            if candidate["reason"] == "exact"
        ),
        None,
    )
    top_score = candidates[0]["score"] if candidates else None
    ambiguous = bool(
        top_score is not None
        and top_score < 100
        and sum(item["score"] == top_score for item in candidates) > 1
    )
    return {
        "exact_match": exact_match,
        "candidates": candidates,
        "ambiguous": ambiguous,
        "input_name": input_name,
    }


def main():
    try:
        data = json.load(sys.stdin)
        result = fuzzy_match(data["input_name"], data.get("existing_names", []))
        json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    except (KeyError, TypeError, ValueError) as exc:
        json.dump({"error": str(exc)}, sys.stdout, ensure_ascii=False)
        sys.stdout.write("\n")
        raise SystemExit(2)


if __name__ == "__main__":
    main()
