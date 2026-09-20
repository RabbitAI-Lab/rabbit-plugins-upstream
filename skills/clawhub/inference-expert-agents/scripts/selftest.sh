#!/usr/bin/env bash
# selftest.sh — sandboxed test suite for inference-expert-agents.
# Runs entirely inside a throwaway HOME (mktemp); touches NO real user state.
set -u
SBX="$(mktemp -d)"
trap 'rm -rf "$SBX"' EXIT
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
pass=0; fail=0
ok(){ echo "  [ok] $1"; pass=$((pass+1)); }
bad(){ echo "  [!!] $1"; fail=$((fail+1)); }

echo "── selftest: inference-expert-agents (sandbox: $SBX) ──"

# T1 scorecard runs on a hard-difficulty verified-style answer
cat > "$SBX/a1.txt" <<'EOF'
The ASAs 2016 p-value statement was published in The American Statistician 70(2):129-133,
confirmed against the publisher page. Two supporting numbers were verified: the statement
passed with six principles, and the DOI resolves. Confidence: high on both claims.
EOF
out="$(python3 "$HERE/tools/inference_scorecard.py" --text-file "$SBX/a1.txt" --difficulty hard)" \
  && ok "scorecard runs (hard)" || bad "scorecard failed (hard)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['rubric']['escalation_match']==1" \
  && ok "hard answer with verification scores escalation_match=1" || bad "hard escalation scoring wrong"

# T2 scorecard flags a hard answer with no verification evidence
cat > "$SBX/a2.txt" <<'EOF'
Einstein visited Paris in 1934 and gave three lectures which were later published
by the university and attended by exactly 400 people at the main hall.
EOF
out="$(python3 "$HERE/tools/inference_scorecard.py" --text-file "$SBX/a2.txt" --difficulty hard)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['rubric']['escalation_match']==0" \
  && ok "unverified hard answer flagged (escalation_match=0)" || bad "unverified hard answer not flagged"

# T3 trivial answer on trivial difficulty passes; bloated trivial answer fails
out="$(python3 "$HERE/tools/inference_scorecard.py" --text "Paris is the capital of France." --difficulty trivial)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['rubric']['escalation_match']==1" \
  && ok "trivial single-pass answer matches trivial triage" || bad "trivial scoring wrong"
out="$(python3 "$HERE/tools/inference_scorecard.py" --text "$(python3 -c 'print("word " * 600)')" --difficulty trivial)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['rubric']['escalation_match']==0" \
  && ok "overthinking (600-word trivial answer) flagged" || bad "overthinking not flagged"

# T4 abstention language is detected
out="$(python3 "$HERE/tools/inference_scorecard.py" --text "I could not verify the exact figure; I do not know the number for certain." --difficulty hard)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['rubric']['abstention_present']==1" \
  && ok "abstention detected" || bad "abstention not detected"

# T5 SKILL.md frontmatter sanity (name, version, emoji, categories)
grep -q '^name: inference-expert-agents' "$HERE/SKILL.md" && ok "frontmatter name" || bad "frontmatter name"
grep -qE '^version: [0-9]+\.[0-9]+\.[0-9]+$' "$HERE/SKILL.md" && ok "frontmatter version" || bad "frontmatter version"
grep -q 'emoji: "🧠"' "$HERE/SKILL.md" && ok "frontmatter emoji" || bad "frontmatter emoji"

# T6 verified-grounding reference exists and cites sources
grep -q 'DeepSeek-R1' "$HERE/references/verified-grounding.md" && ok "grounding reference present" || bad "grounding reference missing"

# T7 triage classifies a hard multi-part proof query
out="$(python3 "$HERE/tools/triage.py" --text "Prove the claim, then derive the bound, and also explain the counterexample")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['difficulty']=='hard' and d['preset']['rung']=='L2'" \
  && ok "triage: hard→L2 preset" || bad "triage hard classification"
out="$(python3 "$HERE/tools/triage.py" --text "hi")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['difficulty']=='trivial' and d['preset']['samples']==1" \
  && ok "triage: trivial→L0/1 sample" || bad "triage trivial classification"

# T8 deliberate plan includes force-final + early-exit/abort thresholds
out="$(python3 "$HERE/tools/deliberate.py" --difficulty hard --budget-tokens 3000 --force-final-at 2500)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['budget']['force_final_at_tokens']==2500 and d['early_exit']['confidence_upper']==0.9 and any(x['rung']=='FORCE' for x in d['plan'])" \
  && ok "deliberate: budget forcing + thresholds" || bad "deliberate plan fields"

# T9 selfcheck flags the planted wrong fact
cat > "$SBX/claim.txt" <<'EOF2'
The Eiffel Tower is in Paris. It was built in 1889. It has 500 floors.
EOF2
out="$(python3 "$HERE/tools/selfcheck.py" --claim-file "$SBX/claim.txt" --samples "The Eiffel Tower is in Paris and opened in 1889||Paris is home to the Eiffel Tower, completed in 1889||The Eiffel Tower stands in Paris; construction finished in 1889")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['high_risk_facts']>=1 and d['verdict']=='verify-with-tools'" \
  && ok "selfcheck: planted 500-floors fact flagged" || bad "selfcheck missed planted fact"

# T10 grounding gate: grounded sentence passes, fabricated one fails -> refuse
echo '{"1":"The Eiffel Tower is a wrought-iron tower in Paris, France, completed in 1889."}' > "$SBX/ev.json"
out="$(python3 "$HERE/tools/grounding_gate.py" --text "The Eiffel Tower was completed in 1889 [1]. It has 500 floors [1]." --evidence-file "$SBX/ev.json")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['n_grounded']==1 and d['n_unsupported']==1 and d['decision']=='refuse'" \
  && ok "grounding gate: 1 grounded, 1 unsupported → refuse" || bad "grounding gate verdicts"

# T11 judge panel minority-veto: single fail vetoes the majority
out="$(python3 "$HERE/tools/judge_panel.py" aggregate --mode minority-veto --verdicts '[{"judge":"a","verdict":"pass"},{"judge":"b","verdict":"pass"},{"judge":"c","verdict":"fail"}]')"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['consensus']=='fail'" \
  && ok "judge panel: minority veto works" || bad "judge panel minority-veto"

# T12 conformal gate: escalate zone between threshold and ceiling
out="$(python3 "$HERE/tools/conformal.py" gate --threshold 0.1 --u 0.15 --escalate-above 0.3)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['decision']=='escalate'" \
  && ok "conformal gate: escalate zone" || bad "conformal gate decision"

# T13 cascade prefers the cheap model first and reports savings
out="$(python3 "$HERE/tools/cascade.py" --models '[{"name":"small","cost":0.05,"quality":0.9},{"name":"large","cost":1.0,"quality":0.97}]' --target-quality 0.9 --confidence 0.9)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['cascade'][0]['model']=='small' and d['expected_savings_pct']>0" \
  && ok "cascade: cheap-first + savings" || bad "cascade plan"

# T14 cache put/get roundtrip (exact hit) in sandbox db
python3 "$HERE/tools/cache_kit.py" put --db "$SBX/ck.json" --prompt "capital of france?" --answer "Paris" >/dev/null \
  && ok "cache put" || bad "cache put"
out="$(python3 "$HERE/tools/cache_kit.py" get --db "$SBX/ck.json" --prompt "capital of france?")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['hit'] and d['answer']=='Paris'" \
  && ok "cache exact get" || bad "cache exact get"

# T15 memory add/search roundtrip with prefix-stem matching
python3 "$HERE/tools/memory_kit.py" add --db "$SBX/mem.json" --kind rule --text "always verify DOIs before citing" >/dev/null
out="$(python3 "$HERE/tools/memory_kit.py" search --db "$SBX/mem.json" --query "verifying citations DOI")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert len(d['results'])>=1" \
  && ok "memory: rule recalled by fuzzy query" || bad "memory recall"

# T16 tool guards reject a hallucinated tool
echo '{"tools":[{"name":"search","args":{"query":{"type":"string","required":true}}}],"name":"guard"}' > "$SBX/spec.json"
out="$(python3 "$HERE/tools/tool_guards.py" validate --spec "$SBX/spec.json" --call '{"name":"web_search","args":{"q":"x"}}')"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert not d['ok'] and 'hallucinated tool' in d['errors'][0]" \
  && ok "tool guards: hallucinated tool rejected" || bad "tool guards validation"

# T17 eval regression: gate pass recorded in ledger
echo '[{"q":"2+2?","a_expect":"4","mode":"exact"}]' > "$SBX/golden.json"; echo '["4"]' > "$SBX/outs.json"
out="$(python3 "$HERE/tools/eval_regression.py" run --db "$SBX/evals.json" --golden "$SBX/golden.json" --outputs "$SBX/outs.json" --gate 0.9)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['verdict']=='pass' and d['pass_rate']==1.0" \
  && ok "eval regression: gate pass" || bad "eval regression gate"

# T18 answer certificate: assembled cert validates; unverified claim downgrades verdict
out="$(python3 "$HERE/tools/answer_certificate.py" assemble --answer "Paris is the capital." --claims '[{"claim":"Paris is capital","method":"retrieval-citation","verdict":"supported","evidence":"[1]"}]')"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['validation']['verdict']=='certified'" \
  && ok "certificate: certified" || bad "certificate certified"
out="$(python3 "$HERE/tools/answer_certificate.py" validate --cert '{"answer":"x","claims":[{"claim":"c","method":"tool-execution","verdict":"unverified","evidence":"none"}]}')"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['verdict']=='conditionally-certified'" \
  && ok "certificate: unverified → conditional" || bad "certificate conditional"

# T19 deep research tiering: arxiv=primary, medium=tertiary
out="$(python3 "$HERE/tools/deep_research.py" tier --urls '["https://arxiv.org/abs/1234.5678","https://medium.com/some-post"]')"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); t={x['url']:x['tier'] for x in d['sources']}; assert t['https://arxiv.org/abs/1234.5678']=='primary' and t['https://medium.com/some-post']=='tertiary'" \
  && ok "deep research: source tiers" || bad "deep research tiers"

# T20 sandbox drill: OOM recovery scored
out="$(python3 "$HERE/tools/sandbox_drill.py" drill --drill oom --recovery "exit 137 means SIGKILL from the OOM killer; check the memory limit and batch the workload")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['verdict'] in ('pass','partial')" \
  && ok "sandbox drill: OOM scored" || bad "sandbox drill"

# T21 MCP server: initialize + tools/list over stdio JSON-RPC
out="$(printf '%s\n%s\n' '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{}}' '{"jsonrpc":"2.0","id":2,"method":"tools/list"}' | python3 "$HERE/tools/mcp_server.py")"
echo "$out" | python3 -c "import json,sys; lines=[json.loads(l) for l in sys.stdin if l.strip()]; assert lines[0]['result']['protocolVersion']=='2024-11-05' and len(lines[1]['result']['tools'])==5" \
  && ok "MCP: handshake + 5 tools exposed" || bad "MCP server"

# T22 debate: contested consensus is not shipped as settled
out="$(python3 "$HERE/tools/debate.py" consensus --positions '[{"agent":"a","answer":"Paris"},{"agent":"b","answer":"Paris"},{"agent":"c","answer":"Lyon"}]')"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['verdict'].startswith('contested')" \
  && ok "debate: contested consensus flagged" || bad "debate consensus"

# T23 scorecard v2 reports atomic_claim_support (FActScore dimension)
out="$(python3 "$HERE/tools/inference_scorecard.py" --text "According to [1] the cohort study of 500 patients found X, verified against the journal page. Uncertainty: moderate." --difficulty hard)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert 'atomic_claim_support' in d['rubric']" \
  && ok "scorecard v2: atomic_claim_support present" || bad "scorecard v2 dimension"


# T24 cove: plan -> crosscheck -> revise pipeline
out="$(python3 "$HERE/tools/cove.py" plan --text "The Eiffel Tower was completed in 1889. It has 500 floors.")"
echo "$out" > "$SBX/claims.json"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['n_claims']==2 and all('how_to_answer' in i for i in d['verification_items'])" \
  && ok "cove plan: claims + factored questions" || bad "cove plan"
CID=$(echo "$out" | python3 -c "import json,sys; print(json.load(sys.stdin)['verification_items'][0]['claim_id'])")
python3 -c "
import json
d=json.load(open('$SBX/claims.json'))
cid=d['verification_items'][0]['claim_id']
json.dump({cid: 'YES - completed in 1889 after two years of construction'}, open('$SBX/ans.json','w'))
"
out="$(python3 "$HERE/tools/cove.py" crosscheck --claims-file "$SBX/claims.json" --answers-file "$SBX/ans.json")"
echo "$out" > "$SBX/verd.json"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['decision']=='revise' and d['n_unverified']>=1" \
  && ok "cove crosscheck: unanswered claim -> unverified/revise" || bad "cove crosscheck"
out="$(python3 "$HERE/tools/cove.py" revise --text "The Eiffel Tower was completed in 1889. It has 500 floors." --verdicts-file "$SBX/verd.json")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['dropped']+d['flagged']>=1" \
  && ok "cove revise: acts on verdicts" || bad "cove revise"

# T25 compress: refuses short, compresses long, protects numbers
out="$(python3 "$HERE/tools/compress.py" compress --text "Short text.")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert 'skipped' in d" \
  && ok "compress: refuses sub-500-token input" || bad "compress min-tokens"
LONG="$(python3 -c 'print("The committee reviewed evidence carefully during long sessions. " * 40)') and the final decision in 2021 was 42 votes."
out="$(python3 "$HERE/tools/compress.py" compress --text "$LONG" --force --ratio 0.4)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['compression_ratio']>1.5 and d['est_tokens_compressed']<d['est_tokens_orig']" \
  && ok "compress: ratio > 1.5 on long text" || bad "compress ratio"
out="$(python3 "$HERE/tools/compress.py" draft)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert '5 WORDS' in d['chain_of_draft_contract'] and 'eval_regression' in d['when_not']" \
  && ok "chain-of-draft contract + gating advice" || bad "cod contract"

# T26 portability tier table
for pair in "gpt-5:frontier" "gemini-3.1-flash-lite:small" "llama-3.1-8b-instant:mid" "qwen2.5-0.5b:local" "gpt-4o-mini:small" "llama-3.3-70b-versatile:large" "gemini-3-pro:frontier"; do
  m="${pair%%:*}"; want="${pair##*:}"
  out="$(python3 "$HERE/tools/portability.py" --model "$m")"
  echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['tier']=='$want', d['tier']" \
    && ok "portability: $m -> $want" || bad "portability: $m -> $want"
done

# T27 speed: measure + plan + parallelize
out="$(python3 "$HERE/tools/speed.py" measure --tokens 420 --seconds 3.5)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert abs(d['tokens_per_second']-120.0)<0.1" \
  && ok "speed measure: 120 tok/s" || bad "speed measure"
out="$(python3 "$HERE/tools/speed.py" plan --deployment local)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert len(d['levers'])>=5 and any('EAGLE' in l['lever'] for l in d['levers'])" \
  && ok "speed plan: local levers incl. EAGLE" || bad "speed plan"
out="$(python3 "$HERE/tools/speed.py" parallelize --samples 5)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert 'n=5' in d['preferred']" \
  && ok "speed parallelize: n>1 single request" || bad "speed parallelize"

# T28 selfimprove: record -> rank -> prune -> adopt gate
SI="$SBX/si.json"
python3 "$HERE/tools/selfimprove.py" record --db "$SI" --rule "verify DOIs before citing" --outcome win >/dev/null
python3 "$HERE/tools/selfimprove.py" record --db "$SI" --rule "verify DOIs before citing" --outcome win >/dev/null
python3 "$HERE/tools/selfimprove.py" record --db "$SI" --rule "verify DOIs before citing" --outcome win >/dev/null
out="$(python3 "$HERE/tools/selfimprove.py" rank --db "$SI")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); r=d['ranking'][0]; assert r['wins']==3 and r['wilson_lb']>0.4" \
  && ok "selfimprove: wilson ranking" || bad "selfimprove rank"
out="$(python3 "$HERE/tools/selfimprove.py" prune --db "$SI" --min-n 10 --below 0.5)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['pruned']==0" \
  && ok "selfimprove: prune respects min-n" || bad "selfimprove prune"
echo '[{"q":"cap of France","expected":"Paris","got":"Lyon"}]' > "$SBX/f.json"
out="$(python3 "$HERE/tools/selfimprove.py" propose --failures-file "$SBX/f.json")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert 'JSON array' in d['amendment_prompt']" \
  && ok "selfimprove: amendment prompt" || bad "selfimprove propose"

# T29 manifest parses and lists every shipped tool
python3 - "$HERE" <<'EOF3'
import json, os, sys
HERE = sys.argv[1]
m = json.load(open(os.path.join(HERE, "manifest.json")))
tools = {os.path.basename(t["file"]) for t in m["tools"]}
actual = {f for f in os.listdir(os.path.join(HERE, "tools")) if f.endswith(".py")}
missing = actual - tools
extra = tools - actual
assert not missing, f"manifest missing: {missing}"
assert not extra, f"manifest stale: {extra}"
EOF3
[ $? -eq 0 ] && ok "manifest: 1:1 with tools/ (no missing, no stale)" || bad "manifest sync"
python3 -c "import json; d=json.load(open('$HERE/manifest.json')); assert d['version']=='3.0.2' and len(d['tools'])==30 and set(d['loading_plan'])=={'core','verify','ops'}, d" \
  && ok "manifest: version/tools/loading_plan" || bad "manifest meta"

# T30 _compact roundtrip preserves data, strips whitespace
out="$(python3 "$HERE/tools/inference_scorecard.py" --text "Paris." --difficulty trivial | python3 "$HERE/tools/_compact.py")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert 'rubric' in d" \
  && ok "_compact: parseable compact JSON" || bad "_compact"
COMP_LEN=$(printf '%s' "$out" | wc -c)

# T31 grounding_gate multi-citation sentence
echo '{"1":"Paris is the capital of France.","2":"Lyon is a big city in France."}' > "$SBX/ev2.json"
out="$(python3 "$HERE/tools/grounding_gate.py" --text "Paris is the capital of France [1]. Lyon is a big city in France [2]." --evidence-file "$SBX/ev2.json")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['n_grounded']==2 and d['decision']=='accept'" \
  && ok "grounding_gate: two citations, both grounded" || bad "grounding_gate multiref"

# T32 memory_kit entries carry stable ids (selfimprove contract)
MID="$SBX/mid.json"
python3 "$HERE/tools/memory_kit.py" add --db "$MID" --kind rule --text "always verify DOIs before citing" >/dev/null
out="$(python3 "$HERE/tools/memory_kit.py" search --db "$MID" --query "verifying citations DOI")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['results'][0]['id']" \
  && ok "memory_kit: stable ids exposed" || bad "memory_kit ids"

# T33 state files are 0600 on write and repaired on load
python3 "$HERE/tools/cache_kit.py" put --db "$SBX/perm.json" --prompt "p" --answer "a" >/dev/null
[ "$(stat -c %a "$SBX/perm.json")" = "600" ] && ok "cache db written 0600" || bad "cache db perms"
chmod 644 "$SBX/perm.json"
python3 "$HERE/tools/cache_kit.py" get --db "$SBX/perm.json" --prompt "p" >/dev/null
[ "$(stat -c %a "$SBX/perm.json")" = "600" ] && ok "cache db repaired to 0600 on load" || bad "cache db repair"
python3 "$HERE/tools/selfimprove.py" record --db "$SBX/si.json" --rule "test rule" --outcome win >/dev/null
[ "$(stat -c %a "$SBX/si.json")" = "600" ] && ok "selfimprove db written 0600" || bad "selfimprove db perms"

# T34 bad input -> clean {"error"} + rc 2, never a traceback
out="$(python3 "$HERE/tools/triage.py" --text-file /nonexistent-xyz 2>&1)"; rc=$?
echo "$out" | grep -q '"error"' && [ "$rc" -eq 2 ] && ! echo "$out" | grep -q 'Traceback' \
  && ok "triage missing file: clean error rc=2" || bad "triage missing file"
echo '[oops' > "$SBX/bad.json"
out="$(python3 "$HERE/tools/conformal.py" calibrate --labels-file "$SBX/bad.json" 2>&1)"; rc=$?
echo "$out" | grep -q '"error"' && [ "$rc" -eq 2 ] && ! echo "$out" | grep -q 'Traceback' \
  && ok "conformal bad labels: clean error rc=2" || bad "conformal bad labels"

# T35 triage: puzzle + clinical-safety prompts are hard
out="$(python3 "$HERE/tools/triage.py" --text "Monty Hall: 3 doors, 1 car. You pick door 1. Stay or switch?")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['difficulty']=='hard'" \
  && ok "triage: monty-hall -> hard" || bad "triage monty-hall"
out="$(python3 "$HERE/tools/triage.py" --text "Is it safe to combine ibuprofen with warfarin?")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['difficulty']=='hard'" \
  && ok "triage: drug-interaction -> hard" || bad "triage drug-interaction"

# T36 scorecard: unsure -> abstention
out="$(python3 "$HERE/tools/inference_scorecard.py" --text "I am unsure about the exact figure and cannot confirm it." --difficulty hard)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['rubric']['abstention_present']==1" \
  && ok "scorecard: unsure -> abstention" || bad "scorecard unsure"

# T37 mcp --help + version sync + F38 refusal
python3 "$HERE/tools/mcp_server.py" --help | grep -q 'inference_triage' \
  && ok "mcp: --help lists tools" || bad "mcp --help"
out="$(printf '%s\n' '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{}}' | python3 "$HERE/tools/mcp_server.py")"
ver="$(grep -E '^version: ' "$HERE/SKILL.md" | awk '{print $2}')"
echo "$out" | grep -q "\"version\": \"$ver\"" && ok "mcp: version matches SKILL.md ($ver)" || bad "mcp version sync"
out="$(printf '%s\n' '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"inference_triage","arguments":{"text":"hi","wants_side_effects":true}}}' | python3 "$HERE/tools/mcp_server.py")"
echo "$out" | grep -q 'F38' && ok "mcp: F38 refuses side-effecting call" || bad "mcp F38"


# T38 retrieval: build/query + 0600 + clean errors
cat > "$SBX/docs.json" <<'EOF'
[{"id":"p1","text":"Paris is the capital of France. The Eiffel Tower was completed in 1889."},{"id":"p2","text":"Lyon is a large city in eastern France, known for cuisine."}]
EOF
python3 "$HERE/tools/retrieval.py" build --db "$SBX/idx.db" --docs "$SBX/docs.json" >/dev/null \
  && ok "retrieval: build" || bad "retrieval build"
[ "$(stat -c %a "$SBX/idx.db")" = "600" ] && ok "retrieval db written 0600" || bad "retrieval db perms"
out="$(python3 "$HERE/tools/retrieval.py" query --db "$SBX/idx.db" --q "capital Eiffel" --top 1)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['hits'] and d['hits'][0]['id']=='p1' and d['hits'][0]['bm25']>=0" \
  && ok "retrieval: top hit p1, bm25 higher=better" || bad "retrieval query"
out="$(python3 "$HERE/tools/retrieval.py" query --db "$SBX/idx.db" --q "!!!" 2>&1)"; rc=$?
echo "$out" | grep -q '"error"' && [ "$rc" -eq 2 ] && ok "retrieval: empty query clean error" || bad "retrieval empty query"
out="$(python3 "$HERE/tools/retrieval.py" query --db "$SBX/nope.db" --q "x" 2>&1)"; rc=$?
echo "$out" | grep -q '"error"' && [ "$rc" -eq 2 ] && ok "retrieval: missing db clean error" || bad "retrieval missing db"

# T39 brevity: drops boilerplate, protects content, reports savings
out="$(python3 "$HERE/tools/brevity.py" --text "Sure, here is the answer: Paris is the capital of France. As an AI, I try to help. I hope this helps.")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['condensed']=='Paris is the capital of France.' and d['saved_pct']>50 and d['openers_stripped']>=2" \
  && ok "brevity: strips openers + boilerplate" || bad "brevity strip"
out="$(python3 "$HERE/tools/brevity.py" --text "The answer is 42. It is certain.")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert '42' in d['condensed']" \
  && ok "brevity: protects sentences with numbers" || bad "brevity protect"

# T40 jsonfix: repairs near-JSON, rejects garbage cleanly
out="$(python3 "$HERE/tools/jsonfix.py" --text '```json
{"a": 1, "b": True, "c": [1, 2,]}')"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['fixed'] and d['data']['b'] is True" \
  && ok "jsonfix: fence+literals+comma repaired" || bad "jsonfix repair"
out="$(python3 "$HERE/tools/jsonfix.py" --text '{"x": {"y": [1, 2')"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['fixed'] and d['data']=={'x':{'y':[1,2]}}" \
  && ok "jsonfix: truncated brackets closed" || bad "jsonfix truncate"
out="$(python3 "$HERE/tools/jsonfix.py" --text 'just prose nothing here' 2>&1)"; rc=$?
echo "$out" | grep -q '"error"' && [ "$rc" -eq 2 ] && ok "jsonfix: garbage clean error rc=2" || bad "jsonfix garbage"

# T41 _compact --keys roundtrip, default strip unchanged
orig='{"answer":"Paris","claims":[{"claim":"x"}]}'
echo "$orig" | python3 "$HERE/tools/_compact.py" --keys | python3 "$HERE/tools/_compact.py" --expand > "$SBX/kc.out"
[ "$(cat "$SBX/kc.out")" = "$orig" ] && ok "_compact: --keys roundtrip lossless" || bad "_compact keys"
echo '{"a":  1}' | python3 "$HERE/tools/_compact.py" | grep -q '{"a":1}' \
  && ok "_compact: default strip unchanged" || bad "_compact default"

# T42 grounding reports rouge_l_recall
echo '{"1":"Paris is the capital of France."}' > "$SBX/ev.json"
out="$(python3 "$HERE/tools/grounding_gate.py" --text "Paris is the capital of France [1]." --evidence-file "$SBX/ev.json")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['claim_verdicts'][0]['rouge_l_recall']>0.5" \
  && ok "grounding: rouge_l_recall reported" || bad "grounding rouge"

# T43 speed batch measure
echo '[{"tokens":420,"seconds":3.5},{"tokens":600,"seconds":4.0},{"tokens":120,"seconds":2.0}]' > "$SBX/sp.json"
out="$(python3 "$HERE/tools/speed.py" measure --samples-file "$SBX/sp.json")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['n']==3 and d['p50_tps']==120.0 and d['mean_tps']==110.0" \
  && ok "speed: batch aggregate (n/mean/p50)" || bad "speed batch"

# T44 selfimprove thompson + seed determinism
python3 "$HERE/tools/selfimprove.py" record --db "$SBX/si.json" --rule "test rule one" --outcome win >/dev/null
a="$(python3 "$HERE/tools/selfimprove.py" rank --db "$SBX/si.json" --method thompson --seed 7)"
b="$(python3 "$HERE/tools/selfimprove.py" rank --db "$SBX/si.json" --method thompson --seed 7)"
[ "$a" = "$b" ] && echo "$a" | grep -q '"method": "thompson"' \
  && ok "selfimprove: thompson deterministic under --seed" || bad "selfimprove thompson"

# T45 portability --emit-prompt (default output unchanged)
python3 "$HERE/tools/portability.py" --model "qwen2.5-0.5b" --emit-prompt | grep -q '"system_prompt"' \
  && ok "portability: --emit-prompt adds system_prompt" || bad "portability emit"
python3 "$HERE/tools/portability.py" --model "qwen2.5-0.5b" | grep -q '"system_prompt"' \
  && bad "portability default leaks prompt" || ok "portability: default has no prompt field"

# T46 cove: UNSUPPORTED answers are unverified, not refuted
python3 -c "
import sys; sys.path.insert(0, '$HERE/tools')
from cove import classify_answer
assert classify_answer('UNSUPPORTED - no source found')=='unverified'
assert classify_answer('YES - confirmed by two sources')=='supported'
assert classify_answer('NO, that is false')=='refuted'
assert classify_answer('This claim is not supported by evidence')=='unverified'
" && ok "cove: unsupported->unverified, yes/no stable" || bad "cove classify"

# T47 mcp tools carry readOnly annotations
out="$(printf '%s\n' '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | python3 "$HERE/tools/mcp_server.py")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert all(t.get('annotations',{}).get('readOnlyHint') for t in d['result']['tools'])" \
  && ok "mcp: all tools annotated readOnlyHint" || bad "mcp annotations"

# T48 _common.fail hint is additive
python3 -c "
import sys, json, io; sys.path.insert(0, '$HERE/tools')
from _common import fail
from contextlib import redirect_stdout
buf = io.StringIO()
with redirect_stdout(buf):
    rc = fail('boom', hint='try this')
assert json.loads(buf.getvalue())=={'error':'boom','hint':'try this'} and rc==2
buf = io.StringIO()
with redirect_stdout(buf):
    fail('plain')
assert json.loads(buf.getvalue())=={'error':'plain'}
" && ok "_common: fail hint additive, default unchanged" || bad "_common hint"


# T49 corrupt state is refused (rc=2) and left untouched; fresh db still works
echo '{corrupt!!' > "$SBX/corrupt.json"
out="$(python3 "$HERE/tools/cache_kit.py" get --db "$SBX/corrupt.json" --prompt "p" 2>&1)"; rc=$?
echo "$out" | grep -q 'corrupt/unreadable' && [ "$rc" -eq 2 ] && [ "$(cat "$SBX/corrupt.json")" = '{corrupt!!' ] \
  && ok "cache: corrupt db refused, file preserved" || bad "cache corrupt"
out="$(python3 "$HERE/tools/eval_regression.py" run --db "$SBX/corrupt.json" --golden '[]' --outputs '[]' 2>&1)"; rc=$?
echo "$out" | grep -q 'corrupt/unreadable' && [ "$rc" -eq 2 ] && [ "$(cat "$SBX/corrupt.json")" = '{corrupt!!' ] \
  && ok "eval: corrupt db refused, file preserved" || bad "eval corrupt"
python3 "$HERE/tools/cache_kit.py" put --db "$SBX/fresh.json" --prompt "p" --answer "a" >/dev/null \
  && [ "$(stat -c %a "$SBX/fresh.json")" = "600" ] \
  && ok "cache: fresh db created 0600 (atomic write)" || bad "cache fresh"

# T50 jsonfix: unclosed fence + string-literal safety
out="$(python3 "$HERE/tools/jsonfix.py" --text 'Here:
```json
{"a": 1, "b": [2, 3')"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['fixed'] and d['data']=={'a':1,'b':[2,3]}" \
  && ok "jsonfix: unclosed fence repaired" || bad "jsonfix unclosed fence"
out="$(python3 "$HERE/tools/jsonfix.py" --text '{"a": "None", "b": True, "c": "x,}", "d": "```z```"}')"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['fixed'] and d['data']=={'a':'None','b':True,'c':'x,}','d':'\`\`\`z\`\`\`'}, d" \
  && ok "jsonfix: strings untouched, literals fixed" || bad "jsonfix string safety"

# T51 retrieval: unicode + dup ids + top validation
echo '[{"id":"t1","text":"تهران پایتخت ایران است."}]' > "$SBX/fa.json"
python3 "$HERE/tools/retrieval.py" build --db "$SBX/fa.db" --docs "$SBX/fa.json" >/dev/null
out="$(python3 "$HERE/tools/retrieval.py" query --db "$SBX/fa.db" --q "تهران")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert [h['id'] for h in d['hits']]==['t1']" \
  && ok "retrieval: Persian query hits" || bad "retrieval unicode"
echo '[{"id":"d","text":"first"},{"id":"d","text":"second"}]' > "$SBX/dups.json"
python3 "$HERE/tools/retrieval.py" build --db "$SBX/d.db" --docs "$SBX/dups.json" >/dev/null
out="$(python3 "$HERE/tools/retrieval.py" query --db "$SBX/d.db" --q "first second" --top 5)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert len(d['hits'])==1 and d['hits'][0]['snippet']=='second'" \
  && ok "retrieval: dup ids deduped (last wins)" || bad "retrieval dedupe"
out="$(python3 "$HERE/tools/retrieval.py" query --db "$SBX/d.db" --q "x" --top 0 2>&1)"; rc=$?
echo "$out" | grep -q -- '--top must be' && [ "$rc" -eq 2 ] \
  && ok "retrieval: --top 0 rejected" || bad "retrieval top"

# T52 brevity: max-sentences edge + capped phrase honesty
out="$(python3 "$HERE/tools/brevity.py" --text "First point here. Second point here. Third point here." --max-sentences 1)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['sentences_out']==1" \
  && ok "brevity: --max-sentences 1 keeps 1" || bad "brevity max1"
out="$(python3 "$HERE/tools/brevity.py" --text "It is important to note that cats sit. Dogs run fast. Birds fly high." --max-sentences 2)"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['phrases_stripped']==1 and 'important to note' not in d['condensed']" \
  && ok "brevity: capped mode strips phrases" || bad "brevity capped"

# T53 _compact deep --keys clean error; cove maybe-hedge
out="$(python3 -c "print('['*1500 + ']'*1500)" | python3 "$HERE/tools/_compact.py" --keys 2>&1)"; rc=$?
echo "$out" | grep -q '"error"' && [ "$rc" -eq 2 ] && ! echo "$out" | grep -q 'Traceback' \
  && ok "_compact: deep --keys clean error rc=2" || bad "_compact deep"
python3 -c "
import sys; sys.path.insert(0, '$HERE/tools')
from cove import classify_answer
assert classify_answer('maybe yes')=='unverified'
" && ok "cove: maybe-hedge -> unverified" || bad "cove maybe"

# ── v3.0.0 regression tests ─────────────────────────────────────────────────
# Each one pins a WRONG ANSWER that the previous 97 assertions did not cover.

# T54 selfcheck: a fact every sample states verbatim must NOT be flagged
out="$(python3 "$HERE/tools/selfcheck.py" --claim "The Eiffel Tower was completed in 1889." \
  --samples "The Eiffel Tower was completed in 1889. It is located in Paris, France, and was designed by Gustave Eiffel for the 1889 World's Fair.||Yes. The Eiffel Tower was completed in 1889. The structure was originally criticized by many artists but became an icon.||The Eiffel Tower was completed in 1889. Construction began in 1887 and it opened to the public in May 1889 in Paris.")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['measurable'] is True and d['per_fact'][0]['label']=='unlikely' and d['hallucination_score'] < 0.35, d['per_fact'][0]" \
  && ok "selfcheck: verbatim-confirmed fact not flagged (was 0.667/'possible')" || bad "selfcheck verbatim regression"

# T55 selfcheck: one sample is unmeasurable, never maximal risk
out="$(python3 "$HERE/tools/selfcheck.py" --claim "The Eiffel Tower was completed in 1889." --samples "solo")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['measurable'] is False and d['hallucination_score'] is None and d['verdict']=='insufficient-samples' and 'warning' in d" \
  && ok "selfcheck: n=1 -> measurable=false, no fabricated risk" || bad "selfcheck n=1"

# T56/T57 grounding_gate: thresholds that cannot fail are rejected
out="$(python3 "$HERE/tools/grounding_gate.py" --text "Aspirin cures cancer in mice [1]." --evidence-file "$SBX/ev.json" --lex 0 --sem 0 2>&1)"; rc=$?
echo "$out" | grep -q '"error"' && [ "$rc" -eq 2 ] && echo "$out" | grep -q '"hint"' \
  && ok "grounding_gate: --lex 0 rejected rc=2 with hint" || bad "grounding_gate lex0"
out="$(python3 "$HERE/tools/grounding_gate.py" --text "Aspirin cures cancer in mice [1]." --evidence-file "$SBX/ev.json" --lex -1 --sem -1 2>&1)"; rc=$?
[ "$rc" -eq 2 ] && echo "$out" | grep -q '"error"' && ! echo "$out" | grep -q 'Traceback' \
  && ok "grounding_gate: negative thresholds rejected rc=2" || bad "grounding_gate negative"

# T58 grounding_gate: skipped short sentences are counted, not silently dropped
out="$(python3 "$HERE/tools/grounding_gate.py" --text "The Eiffel Tower was completed in 1889 [1]. It has 500 floors [1]. Water is wet." --evidence-file "$SBX/ev.json")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['n_skipped_short']>=1 and d['n_audited']>d['n_sentences'] and 'Water is wet' in d['skipped_short'][0]" \
  && ok "grounding_gate: short sentence counted as skipped" || bad "grounding_gate skipped"

# T59/T60/T61 conformal: risk-parameter and schema validation
out="$(python3 "$HERE/tools/conformal.py" calibrate --labels-file "$SBX/labels.json" --alpha 5 2>&1)"; rc=$?
[ "$rc" -eq 2 ] && echo "$out" | grep -q '"error"' && ! echo "$out" | grep -q 'Traceback' \
  && ok "conformal: --alpha 5 rejected rc=2" || bad "conformal alpha"
out="$(python3 "$HERE/tools/conformal.py" calibrate --labels-file "$SBX/labels.json" --delta 0 2>&1)"; rc=$?
[ "$rc" -eq 2 ] && echo "$out" | grep -q 'must be in (0, 1)' \
  && ok "conformal: --delta 0 rejected before log(1/0)" || bad "conformal delta"
cat > "$SBX/labels.json" <<'LBL'
[{"u":0.1,"correct":true},{"u":0.3,"correct":true},{"u":0.6,"correct":false},{"u":0.8,"correct":true},{"u":0.9,"correct":false}]
LBL
echo '[]' > "$SBX/empty.json"
out="$(python3 "$HERE/tools/conformal.py" calibrate --labels-file "$SBX/empty.json" 2>&1)"; rc=$?
[ "$rc" -eq 2 ] && echo "$out" | grep -q '"hint"' \
  && ok "conformal: empty labels is a usage error, not 'abstain-by-default'" || bad "conformal empty"

# T62/T63 theatre: catches a no-op gate, passes a real check
out="$(python3 "$HERE/tools/theatre.py" --json '{"decision":"accept","n_sentences":2,"n_grounded":2,"n_unsupported":0,"n_skipped_short":0,"thresholds":{"lex":0.0,"sem":0.0},"claim_verdicts":[{"verdict":"grounded","lex_containment":0.0,"trigram_cos":0.0}]}')"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['theatre_risk']=='high' and d['n_findings']>=2" \
  && ok "theatre: no-op gate flagged high" || bad "theatre no-op"
python3 "$HERE/tools/theatre.py" --json '{"decision":"accept","n_sentences":2,"n_grounded":2,"n_unsupported":0,"n_skipped_short":0,"thresholds":{"lex":0.0,"sem":0.0},"claim_verdicts":[{"verdict":"grounded","lex_containment":0.0,"trigram_cos":0.0}]}' --fail-on high >/dev/null 2>&1; rc=$?
[ "$rc" -eq 2 ] && ok "theatre: --fail-on high exits 2" || bad "theatre fail-on"
out="$(python3 "$HERE/tools/selfcheck.py" --claim "The Eiffel Tower was completed in 1889." --samples "The Eiffel Tower was completed in 1889.||The tower finished construction in 1889.||It was completed in 1889." | python3 "$HERE/tools/theatre.py" --json "$(cat)")"
echo "$out" | python3 -c "import json,sys; d=json.load(sys.stdin); assert d['theatre_risk']=='none'" \
  && ok "theatre: healthy selfcheck -> none" || bad "theatre healthy"

# T64 citecheck: validation is hermetic (no network needed for these paths)
out="$(python3 "$HERE/tools/citecheck.py" check --citations-file /nonexistent.json 2>&1)"; rc=$?
[ "$rc" -eq 2 ] && echo "$out" | grep -q '"error"' && ! echo "$out" | grep -q 'Traceback' \
  && ok "citecheck: missing file clean error rc=2" || bad "citecheck missing file"
echo '[{"id":"not-an-arxiv-id"}]' > "$SBX/badclaim.json"
out="$(python3 "$HERE/tools/citecheck.py" check --citations-file "$SBX/badclaim.json" 2>&1)"; rc=$?
[ "$rc" -eq 2 ] && echo "$out" | grep -q 'not an arXiv id' \
  && ok "citecheck: malformed id rejected with hint" || bad "citecheck bad id"
echo '{"error":"upstream blew up"}' > "$SBX/err.json"
out="$(python3 "$HERE/tools/theatre.py" --result-file "$SBX/err.json" 2>&1)"; rc=$?
[ "$rc" -eq 2 ] && echo "$out" | grep -q 'tool ERROR object' \
  && ok "theatre: refuses an upstream error object as a result" || bad "theatre error object"

# T65 manifest/SKILL.md agree, and the new tools are registered
python3 -c "
import json,sys
m=json.load(open('$HERE/manifest.json'))
skill=open('$HERE/SKILL.md').read()
assert m['version']=='3.0.2' and 'version: 3.0.2' in skill, 'version drift'
names={t['name'] for t in m['tools']}
assert {'citecheck','theatre'} <= names, names
assert {'citecheck','theatre'} <= set(m['loading_plan']['verify'])
import os
for t in m['tools']:
    assert os.path.exists(os.path.join('$HERE', t['file'])), t['file']
" && ok "manifest: v3.0.2, 30 tools, new tools registered + present" || bad "manifest v3"


echo "── selftest complete: $pass passed, $fail failed ──"
[ "$fail" -eq 0 ]
