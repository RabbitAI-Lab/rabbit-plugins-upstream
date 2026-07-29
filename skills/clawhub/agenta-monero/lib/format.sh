#!/usr/bin/env bash
json_error() {
  local code="$1" msg="$2" sug="${3:-}"
  local out
  out=$(jq -nc --arg c "$code" --arg m "$msg" --arg s "$sug" \
    '{error:true, code:$c, message:$m, suggestion:$s}')
  [[ -z "$sug" ]] && out=$(echo "$out" | jq -c 'del(.suggestion)')
  printf '%s\n' "$out" >&2
  exit 1
}

json_success() {
  printf '%s\n' "$1"
}

piconero_to_xmr() {
  local p="${1:?piconero amount required}"
  [[ ! "$p" =~ ^-?[0-9]+$ ]] && json_error "AMOUNT_INVALID" "not an integer: $p"
  local sign=""; [[ "$p" =~ ^- ]] && { sign="-"; p="${p#-}"; }
  local s; s="$(printf '%013s' "$p" | tr ' ' '0')"   # left-pad integer to 13 digits
  local int="${s:0:-12}" dec="${s: -12}"            # last 12 digits = fractional piconeros
  dec="${dec%"${dec##*[!0]}"}"                       # strip trailing zeros
  if [[ -z "$dec" ]]; then printf '%s\n' "${sign}${int}"
  else printf '%s\n' "${sign}${int}.${dec}"; fi
}

xmr_to_piconero() {
  local xmr="$1"
  [[ ! "$xmr" =~ ^[0-9]+(\.[0-9]+)?$ ]] && { json_error "AMOUNT_INVALID" "Amount must be a positive decimal: $xmr"; }
  local int_part="${xmr%%.*}" dec_part
  [[ "$int_part" == "$xmr" ]] && dec_part="" || dec_part="${xmr#*.}"
  [[ -n "$dec_part" && ${#dec_part} -gt 12 ]] && { json_error "AMOUNT_INVALID" "Amount has more than 12 decimal places: $xmr"; }
  dec_part="$(printf '%-12s' "${dec_part:-0}" | tr ' ' '0')"
  echo "$(( 10#$int_part * 1000000000000 + 10#$dec_part ))"
}
