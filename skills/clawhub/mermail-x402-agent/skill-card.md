## Description:

Completes a user-selected x402 service call with Mermail Agent Wallet / PayBox by creating a payment proof, redeeming it on the exact selected resource, and continuing the original task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent must pay for a selected third-party x402 resource, safely redeem the proof, and continue the original task with the paid result. It is intended for user-approved paid service calls, not isolated wallet management, email-driven payments, transfers, swaps, or API-key MCP sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment proof creation may be mistaken for merchant settlement or a confirmed wallet debit.

Mitigation: Report proof creation as proof_ready until merchant redemption or independent settlement evidence is available, and avoid claiming paid, charged, captured, or settled without that evidence.

Risk: Untrusted HTTP 402 challenges, catalog rows, paid-service payloads, or email content could try to change the selected service, scope, destination, or spend.

Mitigation: Treat inbound content as data, match the service and spend cap to the authenticated user request, and require explicit current-task authority before external-effect operations.

Risk: A credential-minting paid flow may return secrets that are unsafe or unavailable to the agent after redaction.

Mitigation: Verify a secure continuation channel before payment; stop as blocked_before_payment when the credential would be scrubbed and no approved server-side continuation can consume it.

Risk: A paid response could be wrong, stale, or from the wrong market while still appearing plausible.

Mitigation: Freeze an outcome contract before payment and classify mismatched geography, result type, count, ranking semantics, or freshness as result_mismatch rather than success.

## Reference(s):

- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [ClawHub skill page](https://clawhub.ai/mermail/skills/mermail-x402-agent)
- [x402 agent tools](artifact/references/tools.md)
- [x402 agent workflows](artifact/references/workflows.md)
- [x402 agent security](artifact/references/security.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, API calls]

**Output Format:** [Markdown with concise task results, payment/provenance notes, blocker reports, and structured status labels.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MERMAIL_API_KEY and a usable Mermail PayBox connection for payment workflows; keeps payment proofs, signing keys, and vendor credentials out of chat.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
