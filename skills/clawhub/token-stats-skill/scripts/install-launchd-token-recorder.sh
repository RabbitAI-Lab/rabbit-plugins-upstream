#!/bin/sh
set -eu

label="com.baijian.ai-token-ayalysis"
interval="1800"
agent="all"
data_dir=""
run_dir="$HOME/.local/state/ai-token-ayalysis/runs"
token_stats_bin="${TOKEN_STATS_BIN:-${AI_TOKEN_STATS_BIN:-token-stats}}"
codex_home=""
claude_home=""
openclaw_home=""
hermes_home=""
opencode_home=""
deepseek_home=""

usage() {
  cat <<'USAGE'
Usage: install-launchd-token-recorder.sh [options]

Options:
  --interval SECONDS      Refresh interval, default 1800.
  --agent NAME            codex, claude, openclaw, hermes, opencode,
                          deepseek, or all; default all.
  --label LABEL           LaunchAgent label.
  --data-dir PATH         Optional token-stats token-usage data dir.
  --run-dir PATH          Optional per-run snapshot dir.
  --bin PATH              token-stats command or absolute path.
  --codex-home PATH       Optional Codex home override.
  --claude-home PATH      Optional Claude Code home override.
  --openclaw-home PATH    Optional OpenClaw home override.
  --hermes-home PATH      Optional Hermes Agent home override.
  --opencode-home PATH    Optional OpenCode data directory override.
  --deepseek-home PATH    Optional DeepSeek Harness home override.
  --help                 Show this help.
USAGE
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --interval)
      interval="$2"
      shift 2
      ;;
    --agent)
      agent="$2"
      shift 2
      ;;
    --label)
      label="$2"
      shift 2
      ;;
    --data-dir)
      data_dir="$2"
      shift 2
      ;;
    --run-dir)
      run_dir="$2"
      shift 2
      ;;
    --bin)
      token_stats_bin="$2"
      shift 2
      ;;
    --codex-home)
      codex_home="$2"
      shift 2
      ;;
    --claude-home)
      claude_home="$2"
      shift 2
      ;;
    --openclaw-home)
      openclaw_home="$2"
      shift 2
      ;;
    --hermes-home)
      hermes_home="$2"
      shift 2
      ;;
    --opencode-home)
      opencode_home="$2"
      shift 2
      ;;
    --deepseek-home)
      deepseek_home="$2"
      shift 2
      ;;
    --help)
      usage
      exit 0
      ;;
    *)
      echo "unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

case "$interval" in
  ''|*[!0-9]*)
    echo "--interval must be a positive integer number of seconds" >&2
    exit 2
    ;;
esac
if [ "$interval" -lt 60 ]; then
  echo "--interval must be at least 60 seconds" >&2
  exit 2
fi

case "$agent" in
  codex|claude|openclaw|hermes|opencode|deepseek|all)
    ;;
  *)
    echo "--agent must be codex, claude, openclaw, hermes, opencode, deepseek, or all" >&2
    exit 2
    ;;
esac

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
record_script="$script_dir/record-token-usage.sh"
if [ ! -f "$record_script" ]; then
  echo "record-token-usage.sh not found next to installer" >&2
  exit 1
fi

xml_escape() {
  printf '%s' "$1" | sed \
    -e 's/&/\&amp;/g' \
    -e 's/</\&lt;/g' \
    -e 's/>/\&gt;/g' \
    -e 's/"/\&quot;/g' \
    -e "s/'/\&apos;/g"
}

launch_agents_dir="$HOME/Library/LaunchAgents"
log_dir="$HOME/Library/Logs/ai-token-ayalysis"
plist_path="$launch_agents_dir/$label.plist"

mkdir -p "$launch_agents_dir" "$log_dir" "$run_dir"

escaped_label=$(xml_escape "$label")
escaped_record_script=$(xml_escape "$record_script")
escaped_path=$(xml_escape "$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin")
escaped_agent=$(xml_escape "$agent")
escaped_run_dir=$(xml_escape "$run_dir")
escaped_bin=$(xml_escape "$token_stats_bin")
escaped_data_dir=$(xml_escape "$data_dir")
escaped_codex_home=$(xml_escape "$codex_home")
escaped_claude_home=$(xml_escape "$claude_home")
escaped_openclaw_home=$(xml_escape "$openclaw_home")
escaped_hermes_home=$(xml_escape "$hermes_home")
escaped_opencode_home=$(xml_escape "$opencode_home")
escaped_deepseek_home=$(xml_escape "$deepseek_home")
escaped_stdout=$(xml_escape "$log_dir/stdout.log")
escaped_stderr=$(xml_escape "$log_dir/stderr.log")

cat > "$plist_path" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>$escaped_label</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/sh</string>
    <string>$escaped_record_script</string>
  </array>
  <key>EnvironmentVariables</key>
  <dict>
    <key>PATH</key>
    <string>$escaped_path</string>
    <key>TOKEN_STATS_BIN</key>
    <string>$escaped_bin</string>
    <key>AI_TOKEN_AGENT</key>
    <string>$escaped_agent</string>
    <key>AI_TOKEN_RUN_DIR</key>
    <string>$escaped_run_dir</string>
    <key>AI_TOKEN_DATA_DIR</key>
    <string>$escaped_data_dir</string>
    <key>AI_TOKEN_CODEX_HOME</key>
    <string>$escaped_codex_home</string>
    <key>AI_TOKEN_CLAUDE_HOME</key>
    <string>$escaped_claude_home</string>
    <key>AI_TOKEN_OPENCLAW_HOME</key>
    <string>$escaped_openclaw_home</string>
    <key>AI_TOKEN_HERMES_HOME</key>
    <string>$escaped_hermes_home</string>
    <key>AI_TOKEN_OPENCODE_HOME</key>
    <string>$escaped_opencode_home</string>
    <key>AI_TOKEN_DEEPSEEK_HOME</key>
    <string>$escaped_deepseek_home</string>
  </dict>
  <key>StartInterval</key>
  <integer>$interval</integer>
  <key>RunAtLoad</key>
  <true/>
  <key>StandardOutPath</key>
  <string>$escaped_stdout</string>
  <key>StandardErrorPath</key>
  <string>$escaped_stderr</string>
</dict>
</plist>
PLIST

uid=$(id -u)
launchctl bootout "gui/$uid" "$plist_path" >/dev/null 2>&1 || true
launchctl bootstrap "gui/$uid" "$plist_path"
launchctl kickstart -k "gui/$uid/$label" >/dev/null 2>&1 || true

echo "installed $label"
echo "plist: $plist_path"
echo "logs: $log_dir"
echo "run snapshots: $run_dir"
