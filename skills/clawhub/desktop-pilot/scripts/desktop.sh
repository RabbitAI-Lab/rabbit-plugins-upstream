#!/usr/bin/env bash
# Desktop Pilot - one CLI for Windows (incl. from WSL), macOS and Linux desktops.
# Usage: desktop.sh <action> [--process P] [--title T] [--name LABEL] [--text S] [--keys K] [--x N --y N] [--button left|right|double|move] [--out file.png]
# Actions: os | screenshot | windows | buttons | click | close | focus | type | key | mouse
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ACTION="${1:-help}"; shift || true
declare -A O=()
while [[ $# -gt 0 ]]; do
  case "$1" in --*) O["${1#--}"]="${2:-}"; shift 2 || shift ;; *) shift ;; esac
done
die() { echo "ERROR: $*" >&2; exit 1; }
has() { command -v "$1" >/dev/null 2>&1; }

detect_os() {
  case "$(uname -s)" in
    Darwin) echo macos ;;
    Linux) if grep -qi microsoft /proc/version 2>/dev/null && [[ -x /mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe ]] || has powershell.exe; then echo wsl; else echo linux; fi ;;
    MINGW*|MSYS*|CYGWIN*) echo windows ;;
    *) echo unknown ;;
  esac
}
OS="$(detect_os)"
[[ "$ACTION" == os ]] && { echo "$OS"; exit 0; }

# ---------- Windows (native Git Bash/MSYS or WSL) ----------
run_windows() {
  local ps ps1 winps1 args=() out="${O[out]:-}"
  if [[ "$OS" == wsl ]]; then
    ps="$(command -v powershell.exe || echo /mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe)"
    # powershell.exe cannot reliably run scripts from \\wsl$: stage it in the Windows temp folder.
    local wtemp; wtemp="$("$ps" -NoProfile -Command '[IO.Path]::GetTempPath()' | tr -d '\r')"
    local ltemp; ltemp="$(wslpath -u "$wtemp")"
    mkdir -p "$ltemp/desktop-pilot"; cp "$HERE/windows/desktop.ps1" "$ltemp/desktop-pilot/desktop.ps1"
    winps1="${wtemp}desktop-pilot\\desktop.ps1"
  else
    ps="$(command -v powershell.exe || command -v pwsh)"; winps1="$HERE/windows/desktop.ps1"
  fi
  args=("$ACTION")
  for k in process title name keys button; do [[ -n "${O[$k]:-}" ]] && args+=("-${k^}" "${O[$k]}"); done
  [[ -n "${O[text]:-}" ]] && args+=(-TextB64 "$(printf %s "${O[text]}" | base64 -w0)")
  [[ -n "${O[x]:-}" ]] && args+=(-X "${O[x]}"); [[ -n "${O[y]:-}" ]] && args+=(-Y "${O[y]}")
  local winout=""
  if [[ "$ACTION" == screenshot ]]; then
    if [[ "$OS" == wsl ]]; then winout="${wtemp}desktop-pilot\\shot.png"; args+=(-Out "$winout")
    elif [[ -n "$out" ]]; then args+=(-Out "$out"); fi
  fi
  "$ps" -NoProfile -ExecutionPolicy Bypass -File "$winps1" "${args[@]}" | tr -d '\r'
  if [[ -n "$winout" ]]; then
    out="${out:-/tmp/desktop-pilot.png}"; cp "$(wslpath -u "$winout")" "$out"; echo "Linux path: $out"
  fi
}

# ---------- macOS ----------
run_macos() {
  local args=("$ACTION")
  for k in process title name text keys x y button out; do [[ -n "${O[$k]:-}" ]] && args+=("--$k" "${O[$k]}"); done
  osascript -l JavaScript "$HERE/macos/desktop.js" "${args[@]}"
}

# ---------- Linux (X11 via xdotool/wmctrl; Wayland partial via grim/wtype/ydotool) ----------
win_id() {
  local id=""
  if [[ -n "${O[title]:-}" ]] && has xdotool; then id="$(xdotool search --onlyvisible --name "${O[title]}" | head -1)"; fi
  if [[ -z "$id" && -n "${O[process]:-}" ]] && has xdotool; then id="$(xdotool search --onlyvisible --class "${O[process]}" | head -1)"; fi
  [[ -n "$id" ]] || die "No window matches (needs xdotool on X11; on Wayland focus the window manually)"
  echo "$id"
}
run_linux() {
  local wayland=""; [[ -n "${WAYLAND_DISPLAY:-}" ]] && wayland=1
  case "$ACTION" in
    screenshot)
      local out="${O[out]:-/tmp/desktop-pilot.png}"
      if [[ -n "$wayland" ]] && has grim; then grim "$out"
      elif has gnome-screenshot; then gnome-screenshot -f "$out"
      elif has spectacle; then spectacle -b -n -f -o "$out"
      elif has scrot; then scrot -o "$out"
      elif has import; then import -window root "$out"
      else die "Install one of: grim (Wayland), gnome-screenshot, scrot, imagemagick"; fi
      echo "OK screenshot $out" ;;
    windows)
      if has wmctrl; then wmctrl -lp | awk '{pid=$3; $1=$2=$3=$4=""; sub(/^ +/,""); print pid"\t"$0}'
      elif has xdotool; then for w in $(xdotool search --onlyvisible --name .); do echo "$(xdotool getwindowpid "$w" 2>/dev/null)	$(xdotool getwindowname "$w")"; done
      else die "Install wmctrl or xdotool"; fi ;;
    buttons|click)
      python3 "$HERE/linux/atspi.py" "$ACTION" ${O[process]:+--app "${O[process]}"} ${O[title]:+--title "${O[title]}"} ${O[name]:+--name "${O[name]}"} ;;
    close)
      if has wmctrl && [[ -n "${O[title]:-}" ]]; then wmctrl -c "${O[title]}" && echo "OK closed '${O[title]}'"
      elif has xdotool; then xdotool windowclose "$(win_id)" 2>/dev/null || xdotool windowactivate --sync "$(win_id)" key alt+F4; echo "OK closed"
      else python3 "$HERE/linux/atspi.py" close ${O[process]:+--app "${O[process]}"} ${O[title]:+--title "${O[title]}"}; fi ;;
    focus)
      if has wmctrl && [[ -n "${O[title]:-}" ]]; then wmctrl -a "${O[title]}"; else xdotool windowactivate --sync "$(win_id)"; fi; echo "OK focused" ;;
    type)
      [[ -n "${O[text]:-}" ]] || die "Specify --text"
      [[ -n "${O[process]:-}${O[title]:-}" ]] && has xdotool && xdotool windowactivate --sync "$(win_id)"
      if [[ -n "$wayland" ]] && has wtype; then wtype "${O[text]}"; elif has xdotool; then xdotool type --delay 20 -- "${O[text]}"; elif has ydotool; then ydotool type "${O[text]}"; else die "Install xdotool (X11) or wtype/ydotool (Wayland)"; fi
      echo "OK typed ${#O[text]} chars" ;;
    key)
      [[ -n "${O[keys]:-}" ]] || die "Specify --keys (ctrl+c, alt+f4, enter...)"
      [[ -n "${O[process]:-}${O[title]:-}" ]] && has xdotool && xdotool windowactivate --sync "$(win_id)"
      local k="${O[keys]}"; k="${k//enter/Return}"; k="${k//esc/Escape}"; k="${k//backspace/BackSpace}"; k="${k//pageup/Prior}"; k="${k//pagedown/Next}"
      has xdotool || die "Install xdotool"; xdotool key -- "$k"; echo "OK keys ${O[keys]}" ;;
    mouse)
      [[ -n "${O[x]:-}" && -n "${O[y]:-}" ]] || die "Specify --x and --y"
      has xdotool || die "Install xdotool (X11) or use ydotool on Wayland"
      xdotool mousemove "${O[x]}" "${O[y]}"
      case "${O[button]:-left}" in left) xdotool click 1 ;; right) xdotool click 3 ;; double) xdotool click --repeat 2 1 ;; move) ;; esac
      echo "OK mouse ${O[button]:-left} at ${O[x]},${O[y]}" ;;
    *) sed -n '2,4p' "$0" ;;
  esac
}

case "$OS" in
  wsl|windows) run_windows ;;
  macos) run_macos ;;
  linux) run_linux ;;
  *) die "Unsupported OS: $(uname -s)" ;;
esac
