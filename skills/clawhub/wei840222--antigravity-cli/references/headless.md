# Headless Mode

Source: <https://antigravity.google/docs/cli/headless/>. Flag names and defaults that differ on `agy` 1.4.12 stay in `references/cli-usage.md`. The installed `agy --help` wins.

Headless mode is print mode. One prompt runs, the response returns, and the process exits. Response text goes to stdout. Errors, auth prompts, progress, and permission notices go to stderr.

Authenticate in an interactive `agy` session first. Headless uses cached credentials. In a non-interactive environment with no terminal, a missing login exits with an authentication-required error. It does not hang.

```bash
agy -p "In one sentence, what is a git rebase?"
answer=$(agy -p "Name three popular version control systems, comma-separated.")
```

`--prompt` is an alias of `--print`. It is not interactive.

## Output

| Format | stdout | Use |
| --- | --- | --- |
| `text` | Response text. Default | Scripts a person reads |
| `json` | One JSON object when the run ends | Result plus metadata |
| `stream-json` | One NDJSON event per line | Progress, tools, token usage |

JSON envelope fields: `conversation_id`, `status`, `response`, `error` (failure only), `duration_seconds`, `num_turns`, `usage`. With `--json-schema`, add `structured_output` and `json_schema`. `response` then holds the same payload as a string. Read the object from `structured_output`.

```bash
agy -p "Parse v2.14.3 into integer major, minor, and patch." \
  --output-format json \
  --json-schema '{"type":"object","properties":{"major":{"type":"integer"},"minor":{"type":"integer"},"patch":{"type":"integer"}},"required":["major","minor","patch"]}' \
  | jq '.structured_output'
```

`--json-schema` accepts a schema string, a `.json` file path, or `string`, `number`, `integer`, `boolean`.

`usage` keys: `input_tokens`, `output_tokens`, `thinking_tokens`, `cache_read_tokens`, `total_tokens`.

## Stream events

The stream is one `init`, then `step_update` lines, then one `result`. `result` has the same shape as the JSON envelope. With `--json-schema`, the schema applies to that `result`.

`init` carries `cwd`, `tools`, and `permission_mode`. Default mode is `request-review`. `--dangerously-skip-permissions` makes it `always-proceed`. `model` and `agent` appear only when `--model` or `--agent` set them. `json_schema` appears when set.

`step_update` carries `conversation_id`, `step_index`, `state` (`ACTIVE` or `DONE`), and `step_type`. Observed types: `user_input`, `agent_response`, `tool`, `checkpoint`. A long response emits `ACTIVE` events with partial `text_delta` before `DONE`. A short response can arrive as one `DONE`.

Tool steps add `tool_name` and `tool_info`: `name`, `parameters`, `output`, and on failure `error.type` plus `error.message`. Subagent steps use `subagent_info.subagents` instead, with `type_name`, `role`, `conversation_id`, `log_uri`, and `workspace_uris`.

```bash
agy -p "Explain a merge conflict in two sentences." --output-format stream-json \
  | jq -j 'select(.event=="step_update") | .step_update.text_delta // empty'
agy -p "In one sentence, what is a git rebase?" --output-format stream-json \
  | jq 'select(.event=="result") | .result.usage'
```

Use `jq -j` when joining `text_delta`. Plain `jq` inserts newlines between fragments.

## Resume

A headless run is stateless unless you resume. `--continue` uses the latest conversation. `--conversation <id>` uses `conversation_id` from an earlier envelope. Each flag starts a new process. Multi-turn inside one process uses stdin streaming below.

## Stdin streaming

`--input-format stream-json` requires `--output-format stream-json`. Write one JSON object per line. Each line is one turn and emits its own `result`. One process, one `init`, one `conversation_id`. Later turns reuse the warm conversation, so this is faster than repeated `--continue`.

```json
{"event":"user","message":{"content":"Reply with exactly the word: apple. Nothing else."}}
```

`content` may instead be a list of blocks. `text` is the only block type. Any other type ends the session with an error. The agent does not answer a dropped block.

```json
{"event":"user","message":{"content":[{"type":"text","text":"Reply with exactly: banana"}]}}
```

Per result, `response` is this turn only. `num_turns`, `usage`, and `duration_seconds` are cumulative for the session.

Read stdout line by line. Wait for the current `result` before writing the next prompt. Close stdin to end the session. The current turn still returns its `result`. A clean session exits 0.

| Input | Result | Exit |
| --- | --- | --- |
| Unknown event name | Skipped. Warning on stderr | Process continues |
| `control_request` or `control_response` | `ERROR`, session ends | exit 2 |
| CLI-handled slash command, such as `/model` or `/usage` | `ERROR`, session ends | exit 2 |
| Missing `event` | `ERROR`, session ends | 1 |
| Invalid JSON | `ERROR`, session ends | 1 |
| Content block type other than `text` | `ERROR`, session ends | 1 |

An unknown event logs `warning: ignoring unsupported stream input message event "<name>"` and continues. Every other row aborts the rest of the session. Earlier turns keep their `result` events.

Do not pair this input with `--output-format json` or `text`: only the last turn survives. Do not also pass `-p`: that prompt is dropped. Do not send `/model` or `/usage` into the stream. Run `agy -p /model` as its own command. Do not wait for process exit before reading stdout: the process stays open until stdin closes.

## Model, effort, permissions

```bash
agy models
agy -p "Reverse the string antigravity." --model gemini-3.8-flash-medium
agy -p "Outline a caching plan." --effort high
agy -p "Review this function for edge cases." --agent <agent-name>
```

The official page lists effort as `low`, `medium`, or `high`. Local 1.4.12 `--help` also lists `xhigh` and `max`. Quote the installed help.

An unknown `--model` does not fall back. The process exits non-zero with `status` `ERROR`.

Headless has no approval prompt. The settings permission mode applies. A tool that needs approval and cannot get it is soft-denied: the run continues, exits 0, and names the tool on stderr. Workspace file reads and writes are auto-allowed. Shell commands default to Ask and are soft-denied unless a rule allows them.

Grant a tool before the run with `permissions.allow` in `~/.gemini/antigravity-cli/settings.json`, using `action(target)` rules. Ask the user before adding a rule. Ask again before passing `--dangerously-skip-permissions`: it approves every tool call, including file writes and commands.

```json
{
  "permissions": {
    "allow": [
      "command(git)",
      "command(regex:npm run (build|lint|test))",
      "write_file(src/)"
    ]
  }
}
```

## Exit and timeout

Success exits 0. A run that produces no response exits non-zero, writes the reason to stderr, and sets `status` plus `error` in JSON modes.

| Status | Meaning |
| --- | --- |
| `SUCCESS` | Completed and produced a response |
| `ERROR` | Ended with an error |
| `CANCELED` | Canceled |
| `INTERRUPTED` | Interrupted, for example SIGINT |
| `INVALID` | Reached an invalid state |
| `WAITING` | Ended while waiting on input |
| `RUNNING` | Did not reach a terminal state |

The official page says `--print-timeout` defaults to `5m`. Local `agy` 1.4.12 `--help` says `0s`, and `0` waits until the turn ends. Quote the installed binary. On any other version, say this note is for 1.4.12 and tell the user to upgrade before trusting it.

```bash
agy -p "Summarize optimistic locking." --print-timeout 15m
```

Fail a job from the envelope, not only from the exit code:

```bash
result=$(agy -p "Name three version control systems, comma-separated." \
  --output-format json --print-timeout 10m)
status=$(echo "$result" | jq -r '.status')
if [[ "$status" != "SUCCESS" ]]; then
  echo "Agent run failed: $(echo "$result" | jq -r '.error')" >&2
  exit 1
fi
echo "$result" | jq -r '.response' > result.txt
```
