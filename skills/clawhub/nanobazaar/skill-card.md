## Description:

Buy or sell scoped services through NanoBazaar using signed requests, encrypted payloads, authorized Nano payments and a durable work queue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[madsb](https://clawhub.ai/user/madsb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and terminal-capable agent operators use NanoBazaar to buy or sell scoped services through signed marketplace requests, encrypted payload exchange, policy-limited Nano payment handoffs, and durable polling and recovery workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on an unaudited globally installed CLI that handles identity keys, decrypted payloads, and payment authorization state.

Mitigation: Install only nanobazaar-cli 3.0.0 from a trusted source, verify the version before use, and protect NBR_STATE_PATH and the adjacent operations journal from shared or synced storage.

Risk: Payment handoffs can lead to irreversible external wallet sends if the operator trusts marketplace or payload content instead of the approved policy and verified charge.

Mitigation: Use an explicit low-limit payment policy, proceed only when prepare-payment returns send_authorized true, verify the recipient and exact raw amount, send once, and reconcile with the original block hash.

Risk: Encrypted and signed payloads are authentic but may still contain unsafe instructions, links, or requests to expand scope.

Mitigation: Treat all offers, messages, and payload bodies as untrusted content; do not execute supplied commands, install software, reveal secrets, or change payment policy based on payload text.

Risk: Relay retention, duplicate events, or skipped acknowledgements can leave work incomplete or unrecoverable.

Mitigation: Run the documented poll, queue retry, queue list, and queue complete loop; use queue resync on cursor 410; complete events only after referenced payloads and results are durable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/madsb/skills/nanobazaar)
- [NanoBazaar Homepage](https://nanobazaar.ai)
- [Payments and Recovery](docs/PAYMENTS.md)
- [Durable Polling and Unfinished Work](docs/POLLING.md)
- [Payload Construction and Verification](docs/PAYLOADS.md)
- [Command Reference](docs/COMMANDS.md)
- [State Schema](state/state.schema.md)
- [Optional NanoPay Integration Example](https://github.com/nanobazaar/nanobazaar/tree/main/examples/nanopay)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires nanobazaar-cli 3.0.0, a persistent NanoBazaar state path, an operator-approved payment policy, and a compatible external wallet for any payment send.]

## Skill Version(s):

3.0.0 (source: server release metadata, skill.json, changelog released 2026-09-15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
