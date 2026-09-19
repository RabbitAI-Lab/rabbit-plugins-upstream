#!/usr/bin/env bash
# test-cli-commands.sh — functional smoke test for huawei-cloud-obs-dir-count
set -uo pipefail

SKILL_PATH="${1:-$(cd "$(dirname "$0")/.." && pwd)}"
REGION="${HUAWEI_CLOUD_REGION:-cn-north-4}"
BUCKET="${TEST_OBS_BUCKET:-obs-hd-dev-static}"

pass=0
fail=0
skip=0

SCRIPT="$SKILL_PATH/scripts/count_obs_directories.py"

run_test() {
    local id="$1" name="$2" cmd="$3"
    echo -n "  [$id] $name ... "
    if output=$(bash -c "$cmd" 2>&1); then
        echo "PASS"
        pass=$((pass + 1))
    else
        echo "FAIL"
        echo "    Error: $output"
        fail=$((fail + 1))
    fi
}

run_expected() {
    local id="$1" name="$2" expected="$3" cmd="$4"
    echo -n "  [$id] $name ... "
    if output=$(bash -c "$cmd" 2>&1) && [ "$output" = "$expected" ]; then
        echo "PASS"
        pass=$((pass + 1))
    else
        echo "FAIL"
        echo "    Expected: $expected"
        echo "    Got:      $output"
        fail=$((fail + 1))
    fi
}

echo "=== OBS Directory Count Skill Tests (region: $REGION, bucket: $BUCKET) ==="
echo

# Prerequisite check
if ! command -v python3 &>/dev/null; then
    echo "SKIP: python3 not available"
    skip=$((skip + 4))
    exit 0
fi

run_test "TC-01" "Help output" "python3 $SCRIPT --help"
run_test "TC-02" "Immediate count (CLI auto)" "python3 $SCRIPT --bucket $BUCKET"
run_test "TC-03" "Immediate count (SDK)" "python3 $SCRIPT --bucket $BUCKET --executor sdk"
run_test "TC-04" "Recursive count (SDK)" "python3 $SCRIPT --bucket $BUCKET --recursive"

# TC-05: a prefix that has its own zero-byte folder-marker object (e.g.
# 'openplatform/') must NOT count the prefix itself. Expected value is the
# number of 'obs://.../openplatform/.../' folder lines in the raw -d listing
# that are strictly below the prefix.
MARKER_PREFIX="${TEST_MARKER_PREFIX:-openplatform}"
EXPECTED=$(hcloud OBS ls "obs://$BUCKET/$MARKER_PREFIX/" -d 2>/dev/null \
    | sed -n '/^Folder list:/,/^Object list:/p' \
    | grep -c "^obs://$BUCKET/$MARKER_PREFIX/[^/]*/\$" || true)
run_expected "TC-05" "Prefix count excludes self folder-marker ($MARKER_PREFIX)" "$EXPECTED" \
    "python3 $SCRIPT --bucket $BUCKET --prefix $MARKER_PREFIX"

echo
echo "=== Results: $pass passed, $fail failed, $skip skipped ==="
if [ "$fail" -gt 0 ]; then
    exit 1
fi
exit 0
