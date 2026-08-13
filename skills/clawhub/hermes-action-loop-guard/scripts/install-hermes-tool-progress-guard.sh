#!/usr/bin/env bash
set -euo pipefail
cmd="${1:-status}"; shift || true
hermes_home="${HERMES_HOME:-$HOME/.hermes}"
agent_dir="${HERMES_AGENT_DIR:-$hermes_home/hermes-agent}"
service="${HERMES_GATEWAY_SERVICE:-hermes-gateway.service}"
guard_file="${HERMES_TOOL_GUARD_FILE:-$agent_dir/agent/tool_guardrails.py}"
config="${HERMES_CONFIG:-$hermes_home/config.yaml}"
python_bin="${HERMES_PYTHON:-$agent_dir/venv/bin/python}"
backup_root="${HERMES_GUARD_BACKUP_ROOT:-$hermes_home/backups}"
backup_arg=""; dry_run=0
while (($#)); do case "$1" in --dry-run) dry_run=1;; --backup) shift; backup_arg="${1:-}";; *) echo "unknown argument: $1" >&2; exit 2;; esac; shift; done
die(){ echo "error: $*" >&2; exit 2; }
active(){ systemctl --user is-active --quiet "$service"; }
detect(){
  test -f "$guard_file" || die "missing $guard_file"
  test -f "$config" || die "missing $config"
  test -x "$python_bin" || die "missing $python_bin"
  "$python_bin" - "$guard_file" <<'PY'
from pathlib import Path
import sys
s=Path(sys.argv[1]).read_text()
anchors=[
'    no_progress_block_after: int = 5\n',
'        self._turn_subagent_count = 0\n',
'        if not self._is_idempotent(tool_name):\n            self._no_progress.pop(signature, None)\n            return ToolGuardrailDecision(tool_name=tool_name, signature=signature)\n',
]
if 'successful_no_progress_tools' in s:
 print('already-patched'); raise SystemExit(0)
missing=[a for a in anchors if s.count(a)!=1]
if missing: raise SystemExit('unsupported or ambiguous tool_guardrails layout')
print('compatible')
PY
}
patch(){
 "$python_bin" - "$guard_file" "$config" <<'PY'
from pathlib import Path
import re,sys
p=Path(sys.argv[1]); cfg=Path(sys.argv[2]); s=p.read_text()
if 'successful_no_progress_tools' not in s:
 s=s.replace('    no_progress_block_after: int = 5\n',
'''    no_progress_block_after: int = 5
    successful_no_progress_tools: frozenset[str] = field(
        default_factory=lambda: frozenset({"execute_code", "terminal", "process"})
    )
    max_total_calls_per_turn: int = 20
''',1)
 s=s.replace('            loop_caps=LoopCapConfig.from_mapping(data.get("loop_caps")),\n',
'''            successful_no_progress_tools=frozenset(
                str(x) for x in data.get(
                    "successful_no_progress_tools",
                    defaults.successful_no_progress_tools,
                )
            ),
            max_total_calls_per_turn=_non_negative_int(
                data.get("max_total_calls_per_turn"),
                defaults.max_total_calls_per_turn,
            ),
            loop_caps=LoopCapConfig.from_mapping(data.get("loop_caps")),
''',1)
 s=s.replace('        self._turn_subagent_count = 0\n',
'''        self._turn_subagent_count = 0
        self._turn_total_call_count = 0
''',1)
 s=s.replace('        signature = ToolCallSignature.from_call(tool_name, _coerce_args(args))\n',
'''        signature = ToolCallSignature.from_call(tool_name, _coerce_args(args))
        if (
            self.config.max_total_calls_per_turn
            and self._turn_total_call_count >= self.config.max_total_calls_per_turn
        ):
            decision = ToolGuardrailDecision(
                action="halt",
                code="total_tool_call_cap",
                message=(
                    f"Stopped this turn after {self._turn_total_call_count} tool calls. "
                    "The tool budget was exhausted; summarize progress and choose a new strategy."
                ),
                tool_name=tool_name,
                count=self._turn_total_call_count,
                signature=signature,
            )
            self._halt_decision = decision
            return decision
        self._turn_total_call_count += 1
''',1)
 s=s.replace('        if self._is_idempotent(tool_name):\n',
'''        if self._is_idempotent(tool_name) or tool_name in self.config.successful_no_progress_tools:
''',1)
 old='''        if not self._is_idempotent(tool_name):
            self._no_progress.pop(signature, None)
            return ToolGuardrailDecision(tool_name=tool_name, signature=signature)
'''
 new='''        tracks_success = (
            self._is_idempotent(tool_name)
            or tool_name in self.config.successful_no_progress_tools
        )
        if not tracks_success:
            self._no_progress.pop(signature, None)
            return ToolGuardrailDecision(tool_name=tool_name, signature=signature)
        if file_mutation_result_landed(tool_name, result or ""):
            self._no_progress.pop(signature, None)
            return ToolGuardrailDecision(tool_name=tool_name, signature=signature)
'''
 if old not in s: raise SystemExit('after_call anchor changed')
 s=s.replace(old,new,1)
 p.write_text(s)
raw=cfg.read_text()
if 'successful_no_progress_tools:' not in raw:
 raw=re.sub(r'(?m)^(\s*hard_stop_enabled:\s*true\s*)$',r'''\1
  successful_no_progress_tools:
    - execute_code
    - terminal
    - process
  max_total_calls_per_turn: 20''',raw,1)
raw=re.sub(r'(?m)^(\s*exact_failure:)\s*5\s*$',r'\1 3',raw)
raw=re.sub(r'(?m)^(\s*same_tool_failure:)\s*8\s*$',r'\1 5',raw)
raw=re.sub(r'(?m)^(\s*idempotent_no_progress:)\s*5\s*$',r'\1 3',raw)
cfg.write_text(raw)
PY
}
case "$cmd" in
 status) detect; grep -E 'hard_stop_enabled:|successful_no_progress_tools:|max_total_calls_per_turn:|exact_failure:|same_tool_failure:|idempotent_no_progress:' "$config" || true;;
 install)
  detect
  if grep -q successful_no_progress_tools "$guard_file"; then echo "already installed"; exit 0; fi
  if test "$dry_run" = 1; then echo "compatible dry_run=true"; exit 0; fi
  backup="$backup_root/hermes-tool-progress-guard-$(date -u +%Y%m%dT%H%M%SZ)"; mkdir -p "$backup"
  cp -a "$guard_file" "$backup/tool_guardrails.py"; cp -a "$config" "$backup/config.yaml"
  printf 'HERMES_TOOL_GUARD_FILE=%q\nHERMES_CONFIG=%q\nHERMES_GATEWAY_SERVICE=%q\n' "$guard_file" "$config" "$service" >"$backup/manifest.env"
  was=0; active && was=1 || true; systemctl --user stop "$service"
  trap 'cp -a "$backup/tool_guardrails.py" "$guard_file"; cp -a "$backup/config.yaml" "$config"; test "$was" = 1 && systemctl --user start "$service" || true' ERR
  patch
  "$python_bin" -m py_compile "$guard_file"
  cd "$agent_dir"
  if "$python_bin" -c 'import pytest' >/dev/null 2>&1; then
    "$python_bin" -m pytest -q tests/agent/test_tool_guardrails.py tests/run_agent/test_tool_call_guardrail_runtime.py
  else
    "$python_bin" - <<'PY'
from agent.tool_guardrails import ToolCallGuardrailConfig, ToolCallGuardrailController
cfg=ToolCallGuardrailConfig.from_mapping({
 "hard_stop_enabled":True,
 "hard_stop_after":{"idempotent_no_progress":3},
 "successful_no_progress_tools":["execute_code"],
 "max_total_calls_per_turn":20,
})
g=ToolCallGuardrailController(cfg)
args={"code":"print(1)"}
for _ in range(3):
 d=g.before_call("execute_code",args); assert d.allows_execution, d
 g.after_call("execute_code",args,'{"status":"success","output":"same"}',failed=False)
d=g.before_call("execute_code",args)
assert d.should_halt and d.code=="idempotent_no_progress_block",d
g=ToolCallGuardrailController(ToolCallGuardrailConfig.from_mapping({
 "hard_stop_enabled":True,"max_total_calls_per_turn":2,
}))
assert g.before_call("execute_code",{"code":"a"}).allows_execution
assert g.before_call("execute_code",{"code":"b"}).allows_execution
d=g.before_call("execute_code",{"code":"c"})
assert d.should_halt and d.code=="total_tool_call_cap",d
print("tool_progress_smoke=ok")
PY
  fi
  test "$was" = 0 || systemctl --user start "$service"
  trap - ERR
  echo "installed backup=$backup";;
 verify)
  detect; grep -q successful_no_progress_tools "$guard_file" || die "patch absent"
  "$python_bin" -m py_compile "$guard_file"; active; echo verify=ok;;
 rollback)
  test -f "$backup_arg/manifest.env" || die "invalid backup"
  source "$backup_arg/manifest.env"; was=0; active && was=1 || true; systemctl --user stop "$HERMES_GATEWAY_SERVICE"
  cp -a "$backup_arg/tool_guardrails.py" "$HERMES_TOOL_GUARD_FILE"; cp -a "$backup_arg/config.yaml" "$HERMES_CONFIG"
  "$python_bin" -m py_compile "$HERMES_TOOL_GUARD_FILE"; test "$was" = 0 || systemctl --user start "$HERMES_GATEWAY_SERVICE"
  echo rolled_back;;
 *) echo "usage: $0 {status|install [--dry-run]|verify|rollback --backup PATH}" >&2; exit 2;;
esac
