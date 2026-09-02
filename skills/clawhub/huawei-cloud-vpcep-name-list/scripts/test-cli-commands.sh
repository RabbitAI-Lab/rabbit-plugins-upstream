#!/usr/bin/env bash
set -euo pipefail

SKILL_PATH="${1:-.}"
EXECUTOR="${2:-cli}"

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)
SKILL_ROOT=$(cd "${SCRIPT_DIR}/.." >/dev/null 2>&1 && pwd)
VARS_FILE="${SKILL_ROOT}/templates/test-vars.json"

read_vars() {
  REGION=""
  ENDPOINT_NAME=""
  if [ -f "$VARS_FILE" ]; then
    REGION=$(python3 -c "import json;print(json.load(open('$VARS_FILE')).get('region',''))" 2>/dev/null || true)
    ENDPOINT_NAME=$(python3 -c "import json;print(json.load(open('$VARS_FILE')).get('endpoint_name',''))" 2>/dev/null || true)
  fi
  REGION="${VPCEP_REGION:-${REGION:-cn-north-4}}"
  if [[ "$ENDPOINT_NAME" == \{*\} ]]; then ENDPOINT_NAME=""; fi
  ENDPOINT_NAME="${VPCEP_ENDPOINT_NAME:-$ENDPOINT_NAME}"
}

read_vars

echo "=== VPCEP Name List Skill Test Script ==="
echo "Skill path: $SKILL_PATH"
echo "Executor: $EXECUTOR"
echo "Region: $REGION"
echo "Vars file: ${VARS_FILE:-not found}"
echo ""

PASS=0
FAIL=0
SKIP=0

run_test() {
  local id="$1"
  local name="$2"
  local cmd="$3"
  local output=""
  local attempt=1
  local max_attempts=2
  local verdict="PASS"

  echo "--- [$id] $name ---"
  echo "Command: $cmd"

  while [ "$attempt" -le "$max_attempts" ]; do
    output=$(eval "$cmd" 2>&1) || verdict="FAIL"

    if grep -qE '\[USE_ERROR\]|"error_msg"|"error_code": *"[A-Za-z]' <<< "$output"; then
      if [ "$attempt" -lt "$max_attempts" ]; then
        echo "  (attempt $attempt failed; retrying)"
        sleep 2
        attempt=$((attempt + 1))
        continue
      fi
      verdict="FAIL"
    fi
    break
  done

  if [ "$verdict" = "PASS" ]; then
    echo "Result: PASS"
    sed -n '1,5p' <<< "$output"
    PASS=$((PASS + 1))
  else
    echo "Result: FAIL"
    sed -n '1,10p' <<< "$output"
    FAIL=$((FAIL + 1))
  fi
  echo ""
}

if [ "$EXECUTOR" = "cli" ]; then
  if ! command -v hcloud &>/dev/null; then
    echo "hcloud CLI not found. Falling back to SDK."
    EXECUTOR="sdk"
  fi
fi

if [ "$EXECUTOR" = "cli" ]; then
  run_test "TC-01" "List All VPCEP Endpoints" \
    "hcloud VPCEP ListEndpoints --cli-region=$REGION --limit=100"

  run_test "TC-02" "Extract VPCEP Endpoint Names Only" \
    "hcloud VPCEP ListEndpoints --cli-region=$REGION --limit=100 | jq -r '.endpoints[].name'"

  run_test "TC-03" "List VPCEP Endpoints Filtered By Name" \
    "hcloud VPCEP ListEndpoints --cli-region=$REGION --endpoint_service_name=${ENDPOINT_NAME:-test} --limit=100"

  run_test "TC-04" "List VPCEP Endpoints With Pagination" \
    "hcloud VPCEP ListEndpoints --cli-region=$REGION --limit=10 --offset=0"

  run_test "TC-05" "Show VPCEP Summary With Total Count" \
    "hcloud VPCEP ListEndpoints --cli-region=$REGION --limit=100 | jq '{total_count, endpoints: [.endpoints[] | {name, id, status, vpc_id, endpoint_ip, created_at}]}'"
fi

if [ "$EXECUTOR" = "sdk" ]; then
  echo "=== SDK Mode Tests ==="
  set +e
  python3 -c "
import os, sys
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkvpcep.v1.region.vpcep_region import VpcepRegion
from huaweicloudsdkvpcep.v1 import vpcep_client
from huaweicloudsdkvpcep.v1.model import ListEndpointsRequest

ak = os.getenv('HUAWEI_ACCESS_KEY', '')
sk = os.getenv('HUAWEI_SECRET_KEY', '')
if not ak or not sk:
    print('SKIP: AK/SK not set in environment variables')
    sys.exit(2)

credentials = BasicCredentials().with_ak(ak).with_sk(sk)
client = vpcep_client.VpcepClient.new_builder() \
    .with_credentials(credentials) \
    .with_region(VpcepRegion.value_of('$REGION')) \
    .build()

req = ListEndpointsRequest()
req.limit = 100
resp = client.list_endpoints(req)
endpoints = resp.endpoints if resp.endpoints else []
names = [ep.name for ep in endpoints]
print(f'PASS: ListEndpoints returned {len(endpoints)} endpoint(s): {names}')
" 2>&1
  SDK_EXIT=$?
  set -e
  if [ "$SDK_EXIT" -eq 0 ]; then
    PASS=$((PASS + 1))
  elif [ "$SDK_EXIT" -eq 2 ]; then
    SKIP=$((SKIP + 1))
  else
    FAIL=$((FAIL + 1))
  fi
fi

echo ""
echo "=== Test Summary ==="
echo "PASS: $PASS"
echo "FAIL: $FAIL"
echo "SKIP: $SKIP"
echo "Total: $((PASS + FAIL + SKIP))"

if [ "$FAIL" -gt 0 ]; then
  exit 1
fi
