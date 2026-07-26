# Authorized DNS TTL change review

- DNS zone/record owner:
- Change purpose: planned migration / tested failover / other approved reason
- Current DNS TTL:
- Proposed DNS TTL:
- Why a lower value is needed:
- Expected increase in authoritative query load:
- Authoritative capacity and monitoring confirmed:
- Change window and approver:
- Validation: record correctness, resolution success, query load, error rate
- Rollback: restore prior value/record and owner
- Post-change normal TTL restoration time:

IP packet TTL/hop-limit changes are out of scope for performance tuning. This change must not be used for deceptive redirection or policy evasion.
