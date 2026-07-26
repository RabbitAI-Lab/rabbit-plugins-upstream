#!/usr/bin/env bash
# generate_tts.sh —— 批量 TTS 生成
# 用法:
#   generate_tts.sh <voice_plan.json> <output_dir>
#
# voice_plan.json 格式:
# {
#   "provider": "dashscope",   # dashscope | openai | say
#   "voice": "longxiaobai",    # 音色
#   "speed": 1.0,
#   "scenes": [
#     { "id": "card-01", "text": "最近在看 AI 硬件..." },
#     { "id": "card-02", "text": "戒指也来了..." },
#     ...
#   ]
# }
#
# 输出:
#   <output_dir>/card-01.mp3, card-02.mp3, ...
#   合并: <output_dir>/full.mp3 (按 scenes 顺序串接)

set -euo pipefail

PLAN_FILE="$1"
OUT_DIR="$2"

if [[ -z "$PLAN_FILE" || -z "$OUT_DIR" ]]; then
  echo "usage: $0 <voice_plan.json> <output_dir>" >&2
  exit 1
fi

mkdir -p "$OUT_DIR"

# 解析 JSON（用 jq）
PROVIDER=$(jq -r '.provider' "$PLAN_FILE")
VOICE=$(jq -r '.voice' "$PLAN_FILE")
COUNT=$(jq '.scenes | length' "$PLAN_FILE")

echo "Provider: $PROVIDER"
echo "Voice: $VOICE"
echo "Scenes: $COUNT"
echo "Output: $OUT_DIR"

case "$PROVIDER" in
  dashscope)
    if [[ -z "${DASHSCOPE_API_KEY:-}" ]]; then
      echo "ERROR: DASHSCOPE_API_KEY not set" >&2
      exit 1
    fi
    python3 - "$PLAN_FILE" "$OUT_DIR" <<'PY'
import sys, os, json, subprocess
plan, out_dir = sys.argv[1], sys.argv[2]
with open(plan) as f:
    cfg = json.load(f)
voice = cfg["voice"]
for scene in cfg["scenes"]:
    sid, text = scene["id"], scene["text"]
    out_mp3 = f"{out_dir}/{sid}.mp3"
    print(f"  TTS [{sid}] {len(text)} chars -> {out_mp3}")
    # 调用 dashscope Python SDK
    import dashscope
    from dashscope.audio.tts import SpeechSynthesizer
    dashscope.api_key = os.environ["DASHSCOPE_API_KEY"]
    result = SpeechSynthesizer.call(
        model="cosyvoice-v1",
        voice=voice,
        text=text,
        format="mp3",
        sample_rate=24000,
    )
    with open(out_mp3, "wb") as f:
        f.write(result.get_audio_data())
PY
    ;;

  say)
    for i in $(seq 0 $((COUNT-1))); do
      SID=$(jq -r ".scenes[$i].id" "$PLAN_FILE")
      TEXT=$(jq -r ".scenes[$i].text" "$PLAN_FILE")
      AIFF="$OUT_DIR/${SID}.aiff"
      MP3="$OUT_DIR/${SID}.mp3"
      echo "  say [$SID] $TEXT"
      say -v "$VOICE" -o "$AIFF" "$TEXT"
      ffmpeg -y -loglevel error -i "$AIFF" -codec:a libmp3lame -qscale:a 2 "$MP3"
      rm "$AIFF"
    done
    ;;

  openai)
    if [[ -z "${OPENAI_API_KEY:-}" ]]; then
      echo "ERROR: OPENAI_API_KEY not set" >&2
      exit 1
    fi
    python3 - "$PLAN_FILE" "$OUT_DIR" <<'PY'
import sys, os, json
plan, out_dir = sys.argv[1], sys.argv[2]
with open(plan) as f:
    cfg = json.load(f)
voice = cfg["voice"]
for scene in cfg["scenes"]:
    sid, text = scene["id"], scene["text"]
    out_mp3 = f"{out_dir}/{sid}.mp3"
    print(f"  TTS [{sid}] {len(text)} chars -> {out_mp3}")
    import openai
    client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice=voice,
        input=text,
    ) as resp:
        resp.stream_to_file(out_mp3)
PY
    ;;

  *)
    echo "ERROR: unknown provider '$PROVIDER' (expected: dashscope | say | openai)" >&2
    exit 1
    ;;
esac

# 合并所有 mp3 到 full.mp3（用 ffmpeg concat demuxer）
echo ""
echo "Concatenating scenes..."
LIST_FILE=$(mktemp)
for i in $(seq 0 $((COUNT-1))); do
  SID=$(jq -r ".scenes[$i].id" "$PLAN_FILE")
  echo "file '$OUT_DIR/${SID}.mp3'" >> "$LIST_FILE"
done
ffmpeg -y -loglevel error -f concat -safe 0 -i "$LIST_FILE" -c copy "$OUT_DIR/full.mp3"
rm "$LIST_FILE"

echo ""
echo "Done. Files in $OUT_DIR:"
ls -lh "$OUT_DIR"
