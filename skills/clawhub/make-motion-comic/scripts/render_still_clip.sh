#!/bin/zsh
set -euo pipefail

input=""
output=""
duration=""
motion="push"
fps="30"
strength="0.04"

usage() {
  print -u2 "Usage: $0 --input image --output clip.mp4 --duration seconds [--motion push|pull|pan-left|pan-right|hold] [--fps 30] [--strength 0.04]"
  exit 2
}

while [[ "$#" -gt 0 ]]; do
  case "$1" in
    --input) input="$2"; shift 2 ;;
    --output) output="$2"; shift 2 ;;
    --duration) duration="$2"; shift 2 ;;
    --motion) motion="$2"; shift 2 ;;
    --fps) fps="$2"; shift 2 ;;
    --strength) strength="$2"; shift 2 ;;
    *) usage ;;
  esac
done

[[ -n "$input" && -n "$output" && -n "$duration" ]] || usage
[[ -f "$input" ]] || { print -u2 "Input not found: $input"; exit 1; }

frames="$(awk -v d="$duration" -v f="$fps" 'BEGIN { printf "%d", (d*f)+0.5 }')"
denom=$((frames > 1 ? frames - 1 : 1))
ease="(0.5-0.5*cos(PI*on/${denom}))"
reverse_ease="(0.5+0.5*cos(PI*on/${denom}))"

case "$motion" in
  push)
    zoom="1+${strength}*${ease}"
    xpos="iw/2-(iw/zoom/2)"
    ypos="ih/2-(ih/zoom/2)"
    ;;
  pull)
    zoom="1+${strength}*${reverse_ease}"
    xpos="iw/2-(iw/zoom/2)"
    ypos="ih/2-(ih/zoom/2)"
    ;;
  pan-right)
    zoom="1+${strength}"
    xpos="(iw-iw/zoom)*${ease}"
    ypos="ih/2-(ih/zoom/2)"
    ;;
  pan-left)
    zoom="1+${strength}"
    xpos="(iw-iw/zoom)*${reverse_ease}"
    ypos="ih/2-(ih/zoom/2)"
    ;;
  hold)
    zoom="1.02"
    xpos="iw/2-(iw/zoom/2)"
    ypos="ih/2-(ih/zoom/2)"
    ;;
  *)
    usage
    ;;
esac

mkdir -p "${output:h}"

ffmpeg -hide_banner -loglevel error -y \
  -loop 1 -i "$input" \
  -vf "scale=2592:4608:force_original_aspect_ratio=increase,crop=2592:4608,\
zoompan=z='${zoom}':x='${xpos}':y='${ypos}':d=${frames}:s=2160x3840:fps=${fps},\
scale=1080:1920:flags=lanczos,format=yuv420p" \
  -frames:v "$frames" -an \
  -c:v libx264 -preset medium -crf 17 -pix_fmt yuv420p -r "$fps" \
  "$output"

