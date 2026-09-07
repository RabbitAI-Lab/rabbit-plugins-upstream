#!/usr/bin/env bash
# test-cli-commands.sh — functional smoke test for huawei-cloud-vpc-list
set -uo pipefail

SKILL_PATH="${1:-$(cd "$(dirname "$0")/.." && pwd)}"
REGION="${HUAWEI_CLOUD_REGION:-cn-north-4}"
SCRIPT="${SKILL_PATH}/scripts/list_vpcs.py"

pass=0
fail=0
skip=0

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

echo "=== VPC List Skill Tests (region: $REGION) ==="
echo

# Check if SDK is available
if python3 -c "from huaweicloudsdkvpc.v3 import VpcClient" 2>/dev/null; then
    echo "SDK available, running SDK tests"
else
    echo "SKIP: huaweicloudsdkvpc not installed"
    skip=$((skip + 4))
    exit 0
fi

# Check if script exists
if [ ! -f "$SCRIPT" ]; then
    echo "FAIL: list_vpcs.py script not found at $SCRIPT"
    fail=$((fail + 4))
    exit 1
fi

# Syntax check
run_test "TC-01" "list_vpcs.py syntax check" "python3 -c \"import py_compile; py_compile.compile('$SCRIPT', doraise=True)\""

# Help output
run_test "TC-02" "list_vpcs.py --help" "python3 \"$SCRIPT\" --help >/dev/null 2>&1"

# SDK import test
run_test "TC-03" "SDK VpcClient importable" "python3 -c \"from huaweicloudsdkvpc.v3 import VpcClient; print('SDK OK')\" >/dev/null 2>&1"

# Live query test (if project_id provided via env)
if [ -n "${HUAWEI_PROJECT_ID:-}" ]; then
    run_test "TC-04" "List VPCs live (full aggregation)" "python3 \"$SCRIPT\" --project_id=\"$HUAWEI_PROJECT_ID\" --region=\"$REGION\" >/dev/null 2>&1"
else
    echo "  [TC-04] List VPCs live ... SKIP (HUAWEI_PROJECT_ID not set)"
    skip=$((skip + 1))
fi

echo
echo "=== Results: $pass passed, $fail failed, $skip skipped ==="
if [ "$fail" -gt 0 ]; then
    exit 1
fi
exit 0