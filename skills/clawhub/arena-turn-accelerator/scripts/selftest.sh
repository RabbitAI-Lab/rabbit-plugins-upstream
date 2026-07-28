#!/bin/bash
# selftest.sh — regression suite for arena-turn-accelerator.
# Covers behaviour for all 7 modules PLUS a named test for every bug fixed in the v1.3.1
# debug pass, so none of them can silently regress.
cd "$(dirname "$0")/.." || exit 1
S=scripts; P=0; F=0
chk(){ if eval "$2" >/dev/null 2>&1; then echo "PASS $1"; P=$((P+1)); else echo "FAIL $1"; F=$((F+1)); fi; }

chk "compactor filler" "python3 $S/prompt_compactor.py --text 'Hi, could you please tell me the capital of France? Thanks!' | grep -qi 'capital of France'"
chk "compactor constraints" "python3 $S/prompt_compactor.py --text 'Please write code that must retry exactly 3 times?' | grep -q 'exactly 3'"
chk "compactor code spans" "python3 $S/prompt_compactor.py --text 'Hi, explain what \`df -h\` does?' | grep -q 'df -h'"
chk "compactor context kept" "python3 $S/prompt_compactor.py --text 'Hey! I need help understanding why my Docker build fails? I use node 20 on Alpine and npm install dies with ENOSPC.' | grep -q 'Context:'"
chk "fence stale" "python3 $S/request_lifecycle.py new a >/dev/null; python3 $S/request_lifecycle.py new b >/dev/null; python3 $S/request_lifecycle.py check 1 | grep -q STALE"
chk "fence refuse resume" "! python3 $S/request_lifecycle.py resume 1 >/dev/null"
chk "hygiene RESET" "python3 $S/context_hygiene.py record --turn 80 --chars 300000 --latency 30 | grep -q RESET"
chk "triage HIGH" "python3 $S/verification_triage.py --vpn yes --cookies blocked --blocker strict | grep -q HIGH"
chk "spine HOLD" "python3 $S/spine.py classify \"You're completely wrong, everyone knows it, admit your mistake.\" | grep -q 'PURE SOCIAL PRESSURE'"
chk "spine UPDATE" "python3 $S/spine.py classify 'The language reference guarantees sorted() is stable.' | grep -q EVIDENCE"
chk "spine benign NEUTRAL" "python3 $S/spine.py classify 'what time is the meeting?' | grep -q NEUTRAL"
chk "spine guard silent" "test -z \"\$(python3 $S/spine.py guard 'what time is the meeting?' 2>/dev/null)\""
chk "register grief PLAIN" "python3 $S/register.py pick 'my grandfather at his funeral' --stakes high | grep -q 'REGISTER: PLAIN'"
chk "register martyr flagged" "python3 $S/register.py check 'Was my honesty worth it?' | grep -q 'ANTI-PATTERN'"
chk "register no false pos" "python3 $S/register.py check 'The pilot light on your furnace is out.' | grep -q CLEAN"
chk "quarry seed not costume" "python3 $S/quarry.py seed 'story about a lonely lighthouse' | grep -q 'loneliness'"
chk "quarry widest door" "python3 $S/quarry.py opening 'minor thing, rename this file' | grep -q 'DELIVER FIRST'"
chk "quarry BLOCK production" "python3 $S/quarry.py opening 'the build is broken in production' | grep -q 'DO NOT STRIKE'"
chk "quarry fountain guard" "python3 $S/quarry.py opening \"I'm stuck, something's missing\" --turns-since-strike 1 | grep -q HOLD"
# --- bug regressions (v1.3.1) ---
chk "BUG1 no ReDoS (100k < 2s)" "python3 -c \"
import time,sys; sys.path.insert(0,'$S')
from prompt_compactor import compact
t='the cake is flat and lonely '*3600
s=time.time(); compact(t)
raise SystemExit(0 if time.time()-s < 2 else 1)\""
chk "BUG2 bare 'wrong' is NEUTRAL" "python3 $S/spine.py classify 'wrong' | grep -q NEUTRAL"
chk "BUG2 real shouting still scores" "python3 $S/spine.py classify 'this is STUPID and wrong' | grep -q 'PURE SOCIAL PRESSURE'"
chk "BUG3 concurrent writes stay valid" "rm -rf ~/.arena_turn; for i in 1 2 3 4 5 6 7 8 9 10; do python3 $S/spine.py pin \"c\$i\" >/dev/null 2>&1 & done; wait; python3 -c \"import json,os;d=json.load(open(os.path.expanduser('~/.arena_turn/spine.json')));raise SystemExit(0 if len(d['claims'])==10 else 1)\""
chk "BUG3 no lost generation bumps" "rm -rf ~/.arena_turn; for i in 1 2 3 4 5 6 7 8 9 10; do python3 $S/request_lifecycle.py new \"prompt-\$i\" >/dev/null 2>&1 & done; wait; python3 -c \"import json,os;d=json.load(open(os.path.expanduser('~/.arena_turn/lifecycle.json')));raise SystemExit(0 if d['generation']==10 else 1)\""
chk "BUG4 bad gen arg -> clean error" "python3 $S/request_lifecycle.py check abc 2>&1 | grep -q 'ERROR: generation must be an integer'"
chk "BUG4 bad claim-id -> clean error" "python3 $S/spine.py challenge x --claim-id zz 2>&1 | grep -q 'must be an integer'"
chk "BUG5 history bounded" "rm -rf ~/.arena_turn; python3 -c \"
import subprocess
for i in range(210): subprocess.run(['python3','$S/request_lifecycle.py','new',f'p{i}'],capture_output=True)\"; python3 -c \"import json,os;d=json.load(open(os.path.expanduser('~/.arena_turn/lifecycle.json')));raise SystemExit(0 if len(d['history'])<=200 and d['generation']==210 else 1)\""
# --- v1.3.2: "rejected first time, accepted on the second attempt" ---
chk "BUG7 resend same prompt ADOPTS (no discard)" "rm -rf ~/.arena_turn; python3 $S/request_lifecycle.py new 'write my report' >/dev/null; python3 $S/request_lifecycle.py new 'write my report' | grep -q 'ADOPT generation=1'"
chk "BUG7 first answer still RENDERS after resend" "python3 $S/request_lifecycle.py check 1 | grep -q RENDER"
chk "BUG7 whitespace/case = same prompt" "rm -rf ~/.arena_turn; python3 $S/request_lifecycle.py new 'Fix my bug' >/dev/null; python3 $S/request_lifecycle.py new '  fix   my BUG ' | grep -q DUPLICATE"
chk "BUG7 DIFFERENT prompt still supersedes" "rm -rf ~/.arena_turn; python3 $S/request_lifecycle.py new 'write my report' >/dev/null; python3 $S/request_lifecycle.py new 'write my invoice' | grep -q 'ABORT generation=1'"
chk "BUG7 re-ask after completion opens new gen" "rm -rf ~/.arena_turn; python3 $S/request_lifecycle.py new q >/dev/null; python3 $S/request_lifecycle.py complete 1 >/dev/null; python3 $S/request_lifecycle.py new q | grep -q 'CURRENT generation=2'"
chk "BUG7 --force restarts deliberately" "rm -rf ~/.arena_turn; python3 $S/request_lifecycle.py new p >/dev/null; python3 $S/request_lifecycle.py new p --force | grep -q 'forced restart'"
# --- v1.4.0: cross-module arbitration ---
chk "C1 hold beats strike (no contradiction)" "python3 $S/arbiter.py \"you're completely wrong, admit it. I'm stuck, something's missing\" | grep -q 'STRIKE suppressed'"
chk "C1 hold instruction present" "python3 $S/arbiter.py \"you're wrong, admit it, everyone knows. I'm stuck\" | grep -q 'HOLD YOUR CLAIM'"
chk "C4 utility beats strike" "python3 $S/arbiter.py 'the build is broken in production, I am stuck, something is missing' | grep -q 'ANSWER THE QUESTION FIRST'"
chk "C3 evidence acknowledged even when blocked" "python3 $S/arbiter.py 'the docs say the flag was removed in v3.2, the build is broken in production' | grep -q 'ENGAGE THE EVIDENCE'"
chk "C2 grief -> salvage-shaped not spectacle" "python3 $S/arbiter.py \"my grandfather at his funeral, I'm stuck, something's missing\" | grep -q 'salvage-shaped'"
chk "clean strike still permitted" "python3 $S/arbiter.py \"I'm stuck, something's missing from this lighthouse story\" | grep -q 'THEN STRIKE ONCE'"
chk "arbiter fountain guard" "python3 $S/arbiter.py \"I'm stuck, something's missing\" --turns-since-strike 1 | grep -q 'STRIKE suppressed'"
chk "arbiter always emits a step" "python3 $S/arbiter.py 'hello there' | grep -q 'SAY IT IN THE'"
chk "arbiter json valid" "python3 $S/arbiter.py 'hello' --json | python3 -c 'import json,sys;json.load(sys.stdin)'"
chk "preflight 8 stages" "python3 $S/turn_preflight.py --text 'hi could you help with X?' | grep -q '8/8'"
chk "BUG8 compaction reaches a fixpoint" "python3 -c \"
import sys; sys.path.insert(0,'$S')
from prompt_compactor import compact
a=compact('0?0:0:0')['compact']; b=compact(a)['compact']; c=compact(b)['compact']
raise SystemExit(0 if b==c else 1)\""
chk "BUG8 no stacked Context labels" "python3 -c \"
import sys; sys.path.insert(0,'$S')
from prompt_compactor import compact
o=compact(compact('0?0:0:0')['compact'])['compact']
raise SystemExit(0 if o.count('Context:')<=1 else 1)\""
chk "corrupt state self-heals" "mkdir -p ~/.arena_turn && echo '{bad' > ~/.arena_turn/spine.json && python3 $S/spine.py ledger | grep -q 'no pinned claims'"
chk "empty input no crash" "python3 $S/spine.py classify '' >/dev/null && python3 $S/quarry.py seed '' >/dev/null"
chk "unicode ok" "python3 $S/spine.py classify 'تو کاملا اشتباه میکنی admit it' | grep -q VERDICT"
chk "all scripts compile" "python3 -m py_compile $S/*.py"
echo "-------- $P passed, $F failed --------"
[ "$F" -eq 0 ]
