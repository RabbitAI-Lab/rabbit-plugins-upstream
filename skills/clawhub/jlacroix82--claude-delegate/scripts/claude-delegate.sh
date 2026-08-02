#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  claude-delegate.sh --prompt TEXT [options]
  command | claude-delegate.sh --prompt TEXT [options]

Options:
  --cwd PATH                  Run Claude Code from PATH. Default: current directory.
  --prompt TEXT               Task prompt to send to Claude Code.
  --prompt-file PATH          Read the task prompt from PATH.
  --stdin-file PATH           Read additional context from PATH and pipe it to Claude Code.
  --sandbox MODE              read-only, workspace-write, or danger-full-access.
                              Default: read-only. Maps to Claude permission modes:
                                read-only          -> plan
                                workspace-write    -> acceptEdits
                                danger-full-access -> bypassPermissions
  --permission-mode MODE      Direct Claude permission mode override: plan,
                              acceptEdits, dontAsk, auto, or bypassPermissions.
                              Overrides the --sandbox mapping.
  --allowed-tools LIST        Comma-separated tool allowlist for Claude
                              (e.g. "Read,Edit,Bash(git *)").
  --model MODEL               Claude model alias (e.g. sonnet, opus, fable).
  --add-dir PATH              Additional directory to allow tool access to.
                              Repeatable.
  --append-system-prompt TEXT Extra system prompt context for Claude.
  --output-format FMT         text, json, or stream-json. Default: text.
  --output PATH               Write Claude's final message to PATH.
  --json-log PATH             Capture Claude stream-json events to PATH and
                              print only the extracted final answer.
  --verbose                   Include tool results and metadata in output.
  -h, --help                  Show this help.

The wrapper intentionally clears ANTHROPIC_API_KEY and ANTHROPIC_AUTH_TOKEN
before running claude so it uses the saved Claude CLI OAuth login
(Pro/Max/Enterprise — no API key required) instead of an inline API key.
USAGE
}

cwd="."
prompt=""
prompt_file=""
stdin_file=""
sandbox="read-only"
permission_mode=""
allowed_tools=""
model=""
add_dirs=()
append_system_prompt=""
output_format="text"
output_file=""
json_log=""
verbose=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --cwd)
      cwd="${2:?--cwd requires a path}"
      shift 2
      ;;
    --prompt)
      prompt="${2:?--prompt requires text}"
      shift 2
      ;;
    --prompt-file)
      prompt_file="${2:?--prompt-file requires a path}"
      shift 2
      ;;
    --stdin-file)
      stdin_file="${2:?--stdin-file requires a path}"
      shift 2
      ;;
    --sandbox)
      sandbox="${2:?--sandbox requires a mode}"
      shift 2
      ;;
    --permission-mode)
      permission_mode="${2:?--permission-mode requires a mode}"
      shift 2
      ;;
    --allowed-tools)
      allowed_tools="${2:?--allowed-tools requires a list}"
      shift 2
      ;;
    --model)
      model="${2:?--model requires a value}"
      shift 2
      ;;
    --add-dir)
      add_dirs+=("${2:?--add-dir requires a path}")
      shift 2
      ;;
    --append-system-prompt)
      append_system_prompt="${2:?--append-system-prompt requires text}"
      shift 2
      ;;
    --output-format)
      output_format="${2:?--output-format requires a value}"
      shift 2
      ;;
    --output)
      output_file="${2:?--output requires a path}"
      shift 2
      ;;
    --json-log)
      json_log="${2:?--json-log requires a path}"
      shift 2
      ;;
    --verbose)
      verbose=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if ! command -v claude >/dev/null 2>&1; then
  echo "claude CLI not found on PATH. Install Claude Code and sign in with 'claude auth login' (Pro/Max/Enterprise OAuth — no API key needed)." >&2
  exit 127
fi

case "$output_format" in
  text|json|stream-json) ;;
  *)
    echo "--output-format must be text, json, or stream-json" >&2
    exit 2
    ;;
esac

case "$sandbox" in
  read-only|workspace-write|danger-full-access) ;;
  *)
    echo "--sandbox must be read-only, workspace-write, or danger-full-access" >&2
    exit 2
    ;;
esac

if [[ -n "$permission_mode" ]]; then
  case "$permission_mode" in
    plan|acceptEdits|dontAsk|auto|bypassPermissions) ;;
    *)
      echo "--permission-mode must be plan, acceptEdits, dontAsk, auto, or bypassPermissions" >&2
      exit 2
      ;;
  esac
else
  case "$sandbox" in
    read-only) permission_mode="plan" ;;
    workspace-write) permission_mode="acceptEdits" ;;
    danger-full-access) permission_mode="bypassPermissions" ;;
  esac
fi

if [[ -n "$prompt_file" ]]; then
  if [[ -n "$prompt" ]]; then
    echo "Use either --prompt or --prompt-file, not both." >&2
    exit 2
  fi
  prompt="$(<"$prompt_file")"
fi

if [[ -z "$prompt" && -z "$stdin_file" && -t 0 ]]; then
  echo "Provide --prompt, --prompt-file, --stdin-file, or pipe a full prompt on stdin." >&2
  usage >&2
  exit 2
fi

if [[ ! -d "$cwd" ]]; then
  echo "--cwd does not exist or is not a directory: $cwd" >&2
  exit 2
fi

# Force saved Claude CLI OAuth authentication instead of inline API-key auth.
unset ANTHROPIC_API_KEY
unset ANTHROPIC_AUTH_TOKEN

cmd=(claude -p --permission-mode "$permission_mode")

if [[ -n "$json_log" ]]; then
  output_format="stream-json"
  # stream-json events require --verbose in current Claude Code versions.
  verbose=true
  mkdir -p "$(dirname "$json_log")"
fi

cmd+=(--output-format "$output_format")

if [[ "$verbose" == true ]]; then
  cmd+=(--verbose)
fi

if [[ -n "$model" ]]; then
  cmd+=(--model "$model")
fi

if [[ -n "$allowed_tools" ]]; then
  # Use the = form: --allowedTools is variadic and would otherwise swallow
  # the positional prompt (e.g. --allowedTools Read "prompt").
  cmd+=(--allowedTools="$allowed_tools")
fi

for d in "${add_dirs[@]}"; do
  cmd+=(--add-dir "$d")
done

if [[ -n "$append_system_prompt" ]]; then
  cmd+=(--append-system-prompt "$append_system_prompt")
fi

if [[ "$permission_mode" == "bypassPermissions" ]]; then
  # Make the bypass option available (recommended only for isolated sandboxes).
  cmd+=(--allow-dangerously-skip-permissions)
fi

if [[ -n "$output_file" ]]; then
  mkdir -p "$(dirname "$output_file")"
fi

run_claude() {
  if [[ -n "$prompt" ]]; then
    "${cmd[@]}" "$prompt"
  elif [[ -n "$stdin_file" ]]; then
    "${cmd[@]}" <"$stdin_file"
  else
    "${cmd[@]}"
  fi
}

if [[ -n "$json_log" ]]; then
  (cd "$cwd" && run_claude) >"$json_log" || {
    code=$?
    echo "claude exited with code $code (event stream captured at $json_log)" >&2
    exit "$code"
  }
  # Extract the final answer from the stream-json event log.
  if command -v python3 >/dev/null 2>&1; then
    python3 - "$json_log" <<'PY'
import json, sys
path = sys.argv[1]
result = None
with open(path) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            evt = json.loads(line)
        except json.JSONDecodeError:
            continue
        if evt.get("type") == "result":
            result = evt.get("result")
            break
if result is not None:
    sys.stdout.write(result if isinstance(result, str) else json.dumps(result))
    sys.stdout.write("\n")
else:
    print("Claude completed, but no final message was found in the event stream.", file=sys.stderr)
PY
  else
    tail -n 1 "$json_log"
  fi
elif [[ -n "$output_file" ]]; then
  (cd "$cwd" && run_claude) | tee "$output_file"
else
  (cd "$cwd" && run_claude)
fi
