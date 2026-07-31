#!/usr/bin/env bash
source "$LIB/format.sh" 2>/dev/null || source "$(dirname "${BASH_SOURCE[0]}")/format.sh"

validate_label() {
  local l="$1"
  [[ ${#l} -le 255 ]] || { echo "LABEL_INVALID: too long" >&2; return 1; }
  [[ "$l" =~ [[:cntrl:]] ]] && { echo "LABEL_INVALID: control chars" >&2; return 1; }
  return 0
}

validate_tx_hash() {
  [[ "$1" =~ ^[0-9a-f]{64}$ ]] || { echo "TXHASH_INVALID: expected 64 hex chars" >&2; return 1; }
}

validate_dest_json() {
  local j="$1"
  echo "$j" | jq -e 'type=="array" and all(.[]; has("address") and has("amount"))' >/dev/null 2>&1 \
    || { echo "DEST_JSON_INVALID: expected array of {address,amount}" >&2; return 1; }
}

validate_address_format() {
  [[ "$1" =~ ^[0-9A-Za-z]{90,110}$ ]] || { echo "ADDRESS_FORMAT_INVALID" >&2; return 1; }
}

validate_amount() { xmr_to_piconero "$1" >/dev/null; }
