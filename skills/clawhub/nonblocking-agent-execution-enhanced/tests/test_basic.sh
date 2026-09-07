#!/usr/bin/env bash
# =============================================================================
# test_basic.sh - Basic Functionality Tests for nonblocking-agent-execution
# =============================================================================
# Tests the core functionality of jobctl.sh
# Run with: ./tests/test_basic.sh
# =============================================================================

set -euo pipefail

# Setup test environment
TEST_DIR="${TEST_DIR:-/tmp/nonblocking_test}"
BASE_DIR="${BASE_DIR:-$TEST_DIR}"
PASSED=0
FAILED=0
TOTAL=0

export NONBLOCKING_BASE_DIR="$BASE_DIR"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Create test directories
cleanup() {
    rm -rf "$BASE_DIR"
}

setup() {
    cleanup
    mkdir -p "$BASE_DIR"
    export NONBLOCKING_BASE_DIR="$BASE_DIR"
}

# Test helper
run_test() {
    local test_name="$1"
    shift
    TOTAL=$((TOTAL + 1))
    echo -e "${YELLOW}Running: ${test_name}${NC}"
    if "$@" >/dev/null 2>&1; then
        echo -e "${GREEN}✓ PASS${NC}: ${test_name}"
        PASSED=$((PASSED + 1))
        return 0
    else
        echo -e "${RED}✗ FAIL${NC}: ${test_name}"
        FAILED=$((FAILED + 1))
        return 1
    fi
}

# Assert helper
assert() {
    local condition="$1"
    local message="$2"
    if eval "$condition"; then
        echo "  ✓ $message"
        return 0
    else
        echo "  ✗ $message"
        return 1
    fi
}

echo "=========================================="
echo "Basic Functionality Tests"
echo "=========================================="
echo ""

# Test 1: Script exists and is executable
run_test "Script exists" test -f./scripts/jobctl.sh
run_test "Script is executable" test -x./scripts/jobctl.sh

# Test 2: Help command works
run_test "Help command works" bash./scripts/jobctl.sh --help

# Test 3: Start command with invalid arguments
setup
run_test "Start fails without job_id" bash ./scripts/jobctl.sh start
run_test "Start fails without command" bash ./scripts/jobctl.sh start test-job

# Test 4: Start a simple job
setup
run_test "Start simple job" bash./scripts/jobctl.sh start test-job-1 'echo hello' >/dev/null

# Check if job was created
if [[ -f "$BASE_DIR/state/test-job-1.json" ]]; then
    echo -e "${GREEN}✓ PASS${NC}: Job state file created"
    PASSED=$((PASSED + 1))
else
    echo -e "${RED}✗ FAIL${NC}: Job state file not created"
    FAILED=$((FAILED + 1))
fi
TOTAL=$((TOTAL + 1))

# Check if PID file was created
if [[ -f "$BASE_DIR/run/test-job-1.pid" ]]; then
    echo -e "${GREEN}✓ PASS${NC}: Job PID file created"
    PASSED=$((PASSED + 1))
else
    echo -e "${RED}✗ FAIL${NC}: Job PID file not created"
    FAILED=$((FAILED + 1))
fi
TOTAL=$((TOTAL + 1))

# Test 5: Status command
setup
bash ./scripts/jobctl.sh start test-job-2 'echo hello' >/dev/null 2>&1
run_test "Status command works" bash ./scripts/jobctl.sh status test-job-2

# Test 6: List command
run_test "List command works" bash ./scripts/jobctl.sh list

# Test 7: Stop command
setup
bash ./scripts/jobctl.sh start test-job-3 'sleep 10' >/dev/null 2>&1
sleep 1
run_test "Stop command works" bash ./scripts/jobctl.sh stop test-job-3

# Check if job was stopped
setup
bash ./scripts/jobctl.sh start test-job-4 'sleep 10' >/dev/null 2>&1
sleep 1
bash ./scripts/jobctl.sh stop test-job-4 >/dev/null 2>&1
STATUS=$(bash ./scripts/jobctl.sh status test-job-4 2>/dev/null | grep -o '"status":"[^"]*"' | cut -d'"' -f4)
if [[ "$STATUS" == "stopped" ]]; then
    echo -e "${GREEN}✓ PASS${NC}: Job status is 'stopped' after stop command"
    PASSED=$((PASSED + 1))
else
    echo -e "${RED}✗ FAIL${NC}: Job status is '$STATUS' instead of 'stopped'"
    FAILED=$((FAILED + 1))
fi
TOTAL=$((TOTAL + 1))

# Test 8: Cleanup command
setup
bash ./scripts/jobctl.sh start test-job-5 'echo hello' >/dev/null 2>&1
run_test "Cleanup command works" bash ./scripts/jobctl.sh cleanup test-job-5

# Check if files were removed
if [[ ! -f "$BASE_DIR/state/test-job-5.json" ]] && \
   [[ ! -f "$BASE_DIR/run/test-job-5.pid" ]]; then
    echo -e "${GREEN}✓ PASS${NC}: Job files removed by cleanup"
    PASSED=$((PASSED + 1))
else
    echo -e "${RED}✗ FAIL${NC}: Job files still exist after cleanup"
    FAILED=$((FAILED + 1))
fi
TOTAL=$((TOTAL + 1))

# Test 9: Debug command
setup
bash ./scripts/jobctl.sh start test-job-6 'echo hello' >/dev/null 2>&1
run_test "Debug command works" bash ./scripts/jobctl.sh debug test-job-6

# Test 10: Duplicate job prevention
setup
bash ./scripts/jobctl.sh start test-job-7 'echo hello' >/dev/null 2>&1
if bash ./scripts/jobctl.sh start test-job-7 'echo hello2' >/dev/null 2>&1; then
    echo -e "${RED}✗ FAIL${NC}: Duplicate job was allowed"
    FAILED=$((FAILED + 1))
else
    echo -e "${GREEN}✓ PASS${NC}: Duplicate job prevented"
    PASSED=$((PASSED + 1))
fi
TOTAL=$((TOTAL + 1))

# Test 11: Command optimization
setup
OPTIMIZED=$(bash ./scripts/jobctl.sh start test-job-8 'apt-get install package' >/dev/null 2>&1 && \
    cat "$BASE_DIR/state/test-job-8.json" | grep -o '"command":"[^"]*"' | cut -d'"' -f4)
if echo "$OPTIMIZED" | grep -q "-y"; then
    echo -e "${GREEN}✓ PASS${NC}: Command was optimized with -y flag"
    PASSED=$((PASSED + 1))
else
    echo -e "${RED}✗ FAIL${NC}: Command was not optimized"
    FAILED=$((FAILED + 1))
fi
TOTAL=$((TOTAL + 1))

# Test 12: Token monitoring setup
setup
export TOKEN_WARNING_THRESHOLD=1000
export TOKEN_ERROR_THRESHOLD=2000
bash ./scripts/jobctl.sh start test-job-9 'echo hello' >/dev/null 2>&1
STATUS_FILE="$BASE_DIR/state/test-job-9.json"
if grep -q '"tokens_used"' "$STATUS_FILE" && \
   grep -q '"token_rate"' "$STATUS_FILE"; then
    echo -e "${GREEN}✓ PASS${NC}: Token monitoring fields present"
    PASSED=$((PASSED + 1))
else
    echo -e "${RED}✗ FAIL${NC}: Token monitoring fields missing"
    FAILED=$((FAILED + 1))
fi
TOTAL=$((TOTAL + 1))

# Cleanup
cleanup

echo ""
echo "=========================================="
echo "Test Results: $PASSED passed, $FAILED failed, $TOTAL total"
echo "=========================================="

if [[ $FAILED -eq 0 ]]; then
    echo -e "${GREEN}All tests passed!${NC}"
    exit 0
else
    echo -e "${RED}Some tests failed.${NC}"
    exit 1
fi
