#!/bin/zsh
set -u

missing=()
warnings=()

for command in ffmpeg ffprobe edge-tts python3; do
  if ! command -v "$command" >/dev/null 2>&1; then
    missing+=("$command")
  fi
done

if command -v ffmpeg >/dev/null 2>&1; then
  if ! ffmpeg -hide_banner -filters 2>/dev/null | grep -q " zoompan "; then
    missing+=("ffmpeg:zoompan-filter")
  fi
fi

if command -v edge-tts >/dev/null 2>&1; then
  voices="$(edge-tts --list-voices 2>/dev/null | grep '^zh-CN' | wc -l | tr -d ' ')"
  if [[ "$voices" == "0" ]]; then
    warnings+=("Edge TTS is installed but online Mandarin voices were not reachable.")
  fi
fi

if [[ "${#missing[@]}" -gt 0 ]]; then
  print '{"ok":false,"missing":['
  for ((i = 1; i <= ${#missing[@]}; i++)); do
    [[ "$i" -gt 1 ]] && print -n ','
    print -n "\"${missing[$i]}\""
  done
  print ']}'
  exit 1
fi

print -n '{"ok":true,"warnings":['
for ((i = 1; i <= ${#warnings[@]}; i++)); do
  [[ "$i" -gt 1 ]] && print -n ','
  print -n "\"${warnings[$i]}\""
done
print ']}'

