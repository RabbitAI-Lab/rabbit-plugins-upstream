#!/usr/bin/env bash
# Sourced by every .bats file via: load "../test_helper"
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export ROOT="$DIR/.."
export LIB="$ROOT/lib"
export SCRIPTS="$ROOT/scripts"
export FIXTURES="$ROOT/tests/fixtures"
export MONERO_LOCK_DIR="$(mktemp -d)"
source "$ROOT/tests/helpers/mock_rpc.sh"
# Minimal defaults so lib files can be sourced in unit tests
export MONERO_RPC_URL="http://127.0.0.1:18088"
export MONERO_NETWORK="mainnet"
export MONERO_CONFIRMATIONS="10"
