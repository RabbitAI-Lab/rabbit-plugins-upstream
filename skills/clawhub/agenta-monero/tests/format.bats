load "test_helper"
source "$LIB/format.sh"

@test "json_error writes structured JSON error to stderr and exits 1" {
  run json_error "WALLET_NOT_LOADED" "no wallet" "load it"
  [ "$status" -eq 1 ]
  echo "$output" | jq -e '.error==true and .code=="WALLET_NOT_LOADED" and .suggestion=="load it"' >/dev/null
}

@test "json_error no-suggestion path emits single-line compact JSON" {
  run json_error "CONFIG_MISSING" "missing"
  [ "$status" -eq 1 ]
  echo "$output" | jq -e '.error==true and .code=="CONFIG_MISSING" and (.suggestion|not)' >/dev/null
  [ "$(echo "$output" | wc -l)" -eq 1 ]
}

@test "json_success writes JSON to stdout exit 0" {
  run json_success '{"x":1}'
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.x==1' >/dev/null
}

@test "piconero_to_xmr formats with up to 12 decimals, strips trailing zeros" {
  [ "$(piconero_to_xmr 1500000000000)" = "1.5" ]
  [ "$(piconero_to_xmr 1)" = "0.000000000001" ]
  [ "$(piconero_to_xmr 1000000000000)" = "1" ]
  [ "$(piconero_to_xmr 0)" = "0" ]
}

@test "xmr_to_piconero converts and rejects >12 decimals" {
  [ "$(xmr_to_piconero 1.5)" = "1500000000000" ]
  [ "$(xmr_to_piconero 0.000000000001)" = "1" ]
  [ "$(xmr_to_piconero 5)" = "5000000000000" ]
  run xmr_to_piconero "1.0000000000001"; [ "$status" -ne 0 ]
  run xmr_to_piconero "abc"; [ "$status" -ne 0 ]
}
