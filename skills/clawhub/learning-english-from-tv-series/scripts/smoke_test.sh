#!/usr/bin env bash
# DramaLex · smoke_test.sh — 防回归冒烟测试（自带最小夹具，不依赖 examples/）
# 用法：PYTHON=/path/to/python bash scripts/smoke_test.sh
# 校验最小夹具的 5 JSON 通过 validate，build html/md 产物非空，
# 并覆盖 空字幕防护 / 诚实档位 warning / estimate 自检。
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
PY="${PYTHON:-python3}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
ok=1

# ---- 生成自带最小有效夹具（真实台词风格，全部字段满足 validate/export 要求）----
FIX="$TMP/fix"
mkdir -p "$FIX"
"$PY" - <<PY
import json, os
fix = "$FIX"
lines = [
    {"text": "Welcome to the real world. It sucks. You are gonna love it."},
    {"text": "I got off the plane."},
    {"text": "How you doin?"},
    {"text": "We were on a break."},
    {"text": "Could I be wearing any more clothes?"},
]
json.dump({"episode": "Friends S01E01 (smoke fixture)", "lines": lines},
          open(os.path.join(fix, "subtitle.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)

words = [
    {"term": "real world", "cefr": "B1", "ipa": "/riːl wɜːrld/", "gloss": "现实世界",
     "collocation": "welcome to the real world", "example": "Welcome to the real world.",
     "line": "Welcome to the real world. It sucks. You are gonna love it."},
    {"term": "break", "cefr": "B1", "ipa": "/breɪk/", "gloss": "分手；休息",
     "collocation": "on a break", "example": "We were on a break.",
     "line": "We were on a break."},
    {"term": "clothes", "cefr": "A2", "ipa": "/kloʊðz/", "gloss": "衣服",
     "collocation": "wear clothes", "example": "Could I be wearing any more clothes?",
     "line": "Could I be wearing any more clothes?"},
]
json.dump(words, open(os.path.join(fix, "words.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)

listening = {
    "comprehension": [
        {"id": 1, "type": "detail", "question": "Where does the speaker say they just arrived from?",
         "options": ["The real world", "A plane", "A break"], "answer": "A plane",
         "rationale": "台词 'I got off the plane.' 表明刚下飞机。", "line": "I got off the plane."}
    ],
    "dictation": [
        {"id": 1, "line": "We were on a break.", "blanked": "We were on a ___.",
         "answers": ["break"], "line_ref": "We were on a break."}
    ],
}
json.dump(listening, open(os.path.join(fix, "listening.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)

annotated = {
    "annotations": [
        {"id": 1, "line": "We were on a break.", "focus": "collocation",
         "tip": "on a break 口语中常指情侣暂时分手。", "note": "搭配：on a break 表暂时分手。"}
    ],
    "cloze": [
        {"id": 1, "blanked": "We were on a ___.", "answers": ["break"], "line": "We were on a break."}
    ],
}
json.dump(annotated, open(os.path.join(fix, "annotated.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)

tasks = {
    "speaking": [
        {"id": 1, "type": "shadow", "instruction": "跟读：We were on a break.", "use_words": ["break"],
         "focus_sounds": ["/eɪ/"], "asr_target": "We were on a break."}
    ],
    "writing": [
        {"id": 1, "type": "summary", "register": "casual",
         "instruction": "用 break / real world 写一句。", "require_words": ["break", "real world"]}
    ],
}
json.dump(tasks, open(os.path.join(fix, "tasks.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("fixture generated at", fix)
PY

echo "== 1) validate 自带夹具 =="
if "$PY" "$HERE/validate.py" --work-dir "$FIX" --subtitle "$FIX/subtitle.json"; then
    echo "   ✅ validate 通过"
else
    echo "   ❌ validate 失败"; ok=0
fi

echo "== 2) build html + md（no-validate，验产物非空） =="
if "$PY" "$HERE/run_episode.py" build --work-dir "$FIX" --episode "Friends S01E01" \
    --formats html,md --no-validate --out-base "$FIX/out" >/tmp/dlex_smoke.err 2>&1; then
    echo "   ✅ build exit=0"
else
    echo "   ⚠️  build 失败（可能缺 TTS/依赖，属环境项非逻辑回归）；stderr 末尾："
    tail -5 /tmp/dlex_smoke.err
fi
for f in out/out_html/practice.html out/out_md/Friends\ S01E01.md; do
    if [ -s "$FIX/$f" ]; then
        echo "   ✅ $f 非空 ($(wc -c < "$FIX/$f") bytes)"
    else
        echo "   ❌ $f 为空或未生成"; ok=0
    fi
done

echo "== 3) estimate 自检 =="
"$PY" -c "import sys; sys.path.insert(0,'$HERE'); import estimate; e=estimate.estimate_counts(subtitle_json='$FIX/subtitle.json'); assert e['word_cap']>0; print('   word_cap =', e['word_cap'], '| cefr≈', estimate.suggest_cefr(subtitle_json='$FIX/subtitle.json'))" \
    || { echo "   ❌ estimate 自检失败"; ok=0; }

echo "== 4) 空字幕防护（expect 失败，exit≠0） =="
mkdir -p "$TMP/empty"
echo '{"episode":"X","lines":[]}' > "$TMP/empty/subtitle.json"
if "$PY" "$HERE/run_episode.py" prepare --work-dir "$TMP/empty" --episode "Test X" >/tmp/dlex_empty.err 2>&1; then
    echo "   ❌ 空字幕未拦截（prepare 不应成功）"; ok=0
else
    echo "   ✅ 空字幕被正确拦截（exit=$?）"
fi

echo "== 5) 诚实档位 warning（C1 占比高应给 warning） =="
mkdir -p "$TMP/hon"
cat > "$TMP/hon/words.json" <<'EOF'
[{"term":"apple","cefr":"B1","line":"I ate an apple","gloss":"苹果","ipa":"/ˈæpəl/","collocation":"x","example":"x"},
 {"term":"revelation","cefr":"C1","line":"It was a revelation","gloss":"启示","ipa":"/r/","collocation":"","example":"x"},
 {"term":"epiphany","cefr":"C1","line":"He had an epiphany","gloss":"顿悟","ipa":"/i/","collocation":"","example":"x"},
 {"term":"vulnerability","cefr":"C1","line":"show vulnerability","gloss":"脆弱","ipa":"/v/","collocation":"","example":"x"}]
EOF
echo '{"comprehension":[],"dictation":[]}' > "$TMP/hon/listening.json"
echo '{"annotations":[],"cloze":[]}' > "$TMP/hon/annotated.json"
echo '{"speaking":[],"writing":[]}' > "$TMP/hon/tasks.json"
if "$PY" "$HERE/validate.py" --work-dir "$TMP/hon" 2>&1 | grep -q "C1 占比"; then
    echo "   ✅ 诚实档位 warning 已给出"
else
    echo "   ❌ 诚实档位 warning 缺失"; ok=0
fi

if [ "$ok" -eq 1 ]; then
    echo "ALL SMOKE CHECKS PASSED ✅"
else
    echo "SMOKE CHECKS FAILED ❌"
    exit 1
fi
