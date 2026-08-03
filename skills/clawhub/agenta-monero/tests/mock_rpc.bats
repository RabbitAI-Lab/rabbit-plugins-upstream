load "test_helper"

@test "mock serves a canned get_height response" {
  mkdir -p "$FIXTURES/smoke"
  printf '{"jsonrpc":"2.0","id":"0","result":{"height":123}}' > "$FIXTURES/smoke/get_height.json"
  start_mock_rpc 18099 "$FIXTURES/smoke"
  run curl -s -X POST "http://127.0.0.1:18099/json_rpc" \
    -d '{"jsonrpc":"2.0","id":"0","method":"get_height"}'
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.result.height == 123' >/dev/null
  [ "$(mock_call_count get_height)" = "1" ]
  stop_mock_rpc
}

@test "mock_call_count returns a single 0 for unlogged methods" {
  mkdir -p "$FIXTURES/smoke2"
  printf '{"jsonrpc":"2.0","id":"0","result":{"height":1}}' > "$FIXTURES/smoke2/get_height.json"
  start_mock_rpc 18098 "$FIXTURES/smoke2"
  # call get_height once
  curl -s -X POST "http://127.0.0.1:18098/json_rpc" -d '{"jsonrpc":"2.0","id":"0","method":"get_height"}' >/dev/null
  # logged method -> 1
  [ "$(mock_call_count get_height)" = "1" ]
  # unlogged method -> exactly "0" (single line)
  [ "$(mock_call_count never_called)" = "0" ]
  stop_mock_rpc
}
