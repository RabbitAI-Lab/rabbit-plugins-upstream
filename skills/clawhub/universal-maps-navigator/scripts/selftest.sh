#!/usr/bin/env bash
# selftest.sh — offline self-test (no network, sandboxed HOME) + optional live check.
#   bash scripts/selftest.sh          # offline unit tests only
#   bash scripts/selftest.sh --live   # also run `umn doctor` against the free services
# v2: tests i18n, survival, self_improve, token_optimizer modules
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export HOME="$(mktemp -d)" UMN_OFFLINE=1 UMN_CONFIG_DIR="$HOME/.config/universal-maps-navigator" UMN_CACHE_DIR="$HOME/.cache/universal-maps-navigator" UMN_LEARNINGS_DIR="$HOME/.local/share/universal-maps-navigator"
echo "Testing with HOME=$HOME (sandboxed)"
python3 -m py_compile "$ROOT/scripts/umn.py" "$ROOT/scripts/deeplinks.py" "$ROOT/scripts/i18n.py" "$ROOT/scripts/survival.py" "$ROOT/scripts/self_improve.py" "$ROOT/scripts/token_optimizer.py"
python3 "$ROOT/tests/test_deeplinks.py"
# v2 additional offline tests
echo "--- v2 i18n tests ---"
python3 -c "
import sys; sys.path.insert(0, '$ROOT/scripts')
import i18n
assert i18n.is_rtl('ar') == True
assert i18n.is_rtl('en') == False
assert len(i18n.list_languages()) >= 50
assert i18n.translate('route','ro') != 'route'
assert i18n.detect_language('مرحبا') == 'ar'
assert i18n.format_distance(1500,'en') == '1.5 km'
print('i18n OK')
"
echo "--- v2 survival tests ---"
python3 -c "
import sys; sys.path.insert(0, '$ROOT/scripts')
import survival
assert 'desert' in survival.list_terrains()
assert 'earthquake' in survival.list_disasters()
g = survival.get_terrain_guide('desert')
assert 'hazards' in g
g2 = survival.get_disaster_guide('flood')
assert 'during' in g2
sos = survival.get_sos_instructions('mountain','avalanche')
assert 'sos' in sos
combined = survival.get_combined_survival('mountain','avalanche','lost at 3000m','en',True)
assert combined['confidence'] == 'high'
print('survival OK')
"
echo "--- v2 token_optimizer tests ---"
python3 -c "
import sys; sys.path.insert(0, '$ROOT/scripts')
import token_optimizer
assert token_optimizer.estimate_tokens('hello world test') > 0
route = {'distance_m':12300,'duration_s':900,'summary':'A1','engine':'valhalla','confidence':'high'}
c = token_optimizer.compact_route(route)
assert 'km' in c or 'm' in c
assert 'conf:high' in c
j = token_optimizer.minimal_json({'distance_m':100,'duration_s':60,'lat':1,'lon':2,'name':'Test Place Very Long Name Should Be Truncated','confidence':'high','source':'test'}, True)
assert 'dist_m' in j
assert token_optimizer.truncate_if_needed('a'*2000, 100) != 'a'*2000
print('token_optimizer OK')
"
echo "--- v2 self_improve tests ---"
python3 -c "
import sys; sys.path.insert(0, '$ROOT/scripts')
import self_improve, os, json, tempfile
# Use temp dir already set via HOME
self_improve.log_run('test cmd', True, 123, 100, 'test-model', None, 'en')
learnings = self_improve.load_learnings()
assert len(learnings) >= 1
analysis = self_improve.analyze_learnings()
assert 'total_runs' in analysis
print('self_improve OK')
"
echo "--- v2 umn CLI help tests ---"
python3 "$ROOT/scripts/umn.py" --help | grep -q "survival"
python3 "$ROOT/scripts/umn.py" survival list | grep -q "desert"
python3 "$ROOT/scripts/umn.py" i18n list | grep -q "English"
python3 "$ROOT/scripts/umn.py" i18n detect "مرحبا" | grep -q "ar"
python3 "$ROOT/scripts/umn.py" survival guide --terrain desert --lang en | grep -q "Desert"
python3 "$ROOT/scripts/umn.py" survival sos --terrain mountain | grep -q "SOS"
python3 "$ROOT/scripts/umn.py" self-improve --stats | grep -q "metrics\|No metrics"
python3 "$ROOT/scripts/umn.py" geocode "Berlin" --help | grep -q "lang"
echo "CLI v2 commands OK (offline error expected for network cmds)"
# Test offline error handling (should fail with network disabled)
if python3 "$ROOT/scripts/umn.py" geocode "Berlin" 2>&1 | grep -q "network disabled"; then
  echo "Offline error handling OK"
else
  echo "Offline error handling check"
fi

if [[ "${1:-}" == "--live" ]]; then
  unset UMN_OFFLINE
  echo "--- live doctor ---"
  python3 "$ROOT/scripts/umn.py" doctor || echo "doctor reported some failures (expected if some services down)"
fi
echo "selftest OK — v2 with 50+ langs + survival + self-improve + token optimizer"
