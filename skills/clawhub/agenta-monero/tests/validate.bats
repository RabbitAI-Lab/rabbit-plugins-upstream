load "test_helper"
source "$LIB/format.sh"
source "$LIB/validate.sh"

@test "validate_label accepts <=255 chars, no control chars" {
  validate_label "Payment from Alice"
  run validate_label "$(printf 'a\ta')"; [ "$status" -ne 0 ]
}

@test "validate_tx_hash wants 64 hex" {
  validate_tx_hash "19d5089f9469db3d90aca9024dfcb17ce94b948300101c8345a5e9f7257353be"
  run validate_tx_hash "deadbeef"; [ "$status" -ne 0 ]
}

@test "validate_dest_json accepts array of {address,amount}" {
  validate_dest_json '[{"address":"A","amount":"1.0"},{"address":"B","amount":"2.0"}]'
  run validate_dest_json '{"address":"A","amount":"1.0"}'; [ "$status" -ne 0 ]
}

@test "validate_amount delegates to xmr_to_piconero" {
  validate_amount "1.5"
  run validate_amount "-1"; [ "$status" -ne 0 ]
}
