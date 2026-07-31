load "test_helper"
source "$LIB/config.sh"

@test "parse_env reads KEY=value pairs into CONFIG" {
  d="$(mktemp -d)"; printf 'MONERO_NETWORK="mainnet"\nMONERO_RPC_URL="http://x:1"\nBLANK=""\n' > "$d/.env"
  declare -gA CONFIG; parse_env "$d/.env"
  [ "${CONFIG[MONERO_NETWORK]}" = "mainnet" ]
  [ "${CONFIG[MONERO_RPC_URL]}" = "http://x:1" ]
  [ "${CONFIG[BLANK]}" = "" ]
}

@test "parse_env skips comments and blanks and strips quotes" {
  d="$(mktemp -d)"; printf -- '# comment\n\nABCDEFGHIJK="v1"\nZZ=\'\''v2'\''\n' > "$d/.env"
  declare -gA CONFIG; parse_env "$d/.env"
  [ "${CONFIG[ABCDEFGHIJK]}" = "v1" ]
  [ "${CONFIG[ZZ]}" = "v2" ]
}

@test "parse_env rejects shell metacharacters" {
  d="$(mktemp -d)"; printf 'EVIL="a;rm -rf /"\n' > "$d/.env"
  declare -gA CONFIG
  run parse_env "$d/.env"
  [ "$status" -ne 0 ]
  [[ "$output" == *"CONFIG_INVALID"* ]]
}

@test "require_config fails on missing key" {
  declare -gA CONFIG=([MONERO_NETWORK]="mainnet")
  run require_config MONERO_NETWORK MONERO_RPC_USER
  [ "$status" -ne 0 ]
  [[ "$output" == *"CONFIG_MISSING"* ]]
}

@test "validate_network accepts mainnet/stagenet and rejects others" {
  unset MONERO_NETWORK
  declare -gA CONFIG=([MONERO_NETWORK]="mainnet")
  validate_network
  CONFIG[MONERO_NETWORK]="stagenet"; validate_network
  CONFIG[MONERO_NETWORK]="testnet"
  run validate_network; [ "$status" -ne 0 ]
}

@test "validate_network uses exported MONERO_NETWORK when CONFIG empty (env-mode)" {
  declare -gA CONFIG=()
  MONERO_NETWORK=mainnet validate_network; [ $? -eq 0 ]
  MONERO_NETWORK=stagenet validate_network; [ $? -eq 0 ]
  MONERO_NETWORK=testnet
  run validate_network
  [ "$status" -ne 0 ]
  unset MONERO_NETWORK
}

@test "get_config returns value or empty" {
  declare -gA CONFIG=([FOO]="bar")
  [ "$(get_config FOO)" = "bar" ]
  [ -z "$(get_config NOPE)" ]
}

teardown() { stop_mock_rpc; }
