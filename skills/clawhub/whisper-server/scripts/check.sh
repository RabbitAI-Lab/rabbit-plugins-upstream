#!/usr/bin/env bash
# Read-only check for the whisper-server setup. Changes nothing.
# Usage: bash check.sh    (set WHISPER_SERVER_URL to check another loopback address)
set -u

url="${WHISPER_SERVER_URL:-http://127.0.0.1:8080}"
status=0

line() { printf '%-9s %s\n' "$1" "$2"; }

# Only loopback addresses are checked: the server must not be on a network.
if ! [[ "$url" =~ ^http://(127\.[0-9]+\.[0-9]+\.[0-9]+|localhost|\[::1\])(:[0-9]+)?$ ]]; then
  line "FAIL" "WHISPER_SERVER_URL is not a loopback address: $url"
  exit 2
fi

if command -v curl >/dev/null 2>&1; then
  health="$(curl -s -m 5 "$url/health" 2>/dev/null || true)"
  case "$health" in
    *'"ok"'*) line "ok" "server ready at $url" ;;
    *loading*) line "wait" "server at $url is still loading its model"; status=1 ;;
    *) line "missing" "no whisper server answers at $url"; status=1 ;;
  esac
else
  line "missing" "curl is not installed"
  status=1
fi

if command -v ffmpeg >/dev/null 2>&1; then
  line "ok" "ffmpeg found"
else
  line "missing" "ffmpeg is not on the PATH (needed for OGG, M4A and MP3 voice notes)"
  status=1
fi

if command -v whisper-server >/dev/null 2>&1; then
  line "ok" "whisper-server is on the PATH"
elif [ -x "$HOME/whisper.cpp/build/bin/whisper-server" ]; then
  line "ok" "whisper-server built at ~/whisper.cpp/build/bin"
else
  line "info" "whisper-server is not on the PATH (fine if it runs from another folder)"
fi

if command -v openclaw >/dev/null 2>&1; then
  if plugins="$(openclaw plugins list 2>/dev/null)"; then
    case "$plugins" in
      *whisper-server*) line "ok" "openclaw-whisper-server plugin installed" ;;
      *) line "missing" "openclaw-whisper-server plugin is not installed"; status=1 ;;
    esac
  else
    line "unknown" "could not list OpenClaw plugins (openclaw plugins list failed)"
    status=1
  fi
  if models="$(openclaw config get tools.media.models 2>/dev/null)"; then
    case "$models" in
      *whisper-server*) line "ok" "OpenClaw is set to use whisper-server for audio" ;;
      *) line "missing" "tools.media.models does not list whisper-server"; status=1 ;;
    esac
  else
    line "unknown" "could not read tools.media.models (openclaw config get failed)"
    status=1
  fi
else
  line "missing" "openclaw is not on the PATH"
  status=1
fi

exit "$status"
