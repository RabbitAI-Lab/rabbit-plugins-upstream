## Description:

Guides developers through Huifu payment integration and troubleshooting across aggregation, hosted, balance, and checkout flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huifu](https://clawhub.ai/user/huifu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers integrating Huifu payments use this skill to select payment flows, build Java, PHP, or Python SDK integrations, handle notifications and refunds, and troubleshoot transactions. Merchant onboarding and account activation require a separate skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some recommended official SDK versions have known TLS certificate or hostname verification weaknesses that can expose live payment traffic.

Mitigation: Before production use, confirm a secure vendor-supported SDK version or compensating production control; do not treat the skill's SDK requirement as a security fix.

Risk: Using real merchant keys during sandbox testing or exposing keys in client code and logs can compromise payment credentials.

Mitigation: Use separate sandbox credentials and keep production keys in server-side secret storage; exclude secrets from clients, logs, and repositories.

Risk: Treating a browser redirect or synchronous acceptance as a settled payment can misstate transaction status.

Mitigation: Verify signed notifications and transaction details, update orders idempotently, and query the transaction when confirmation is missing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huifu/skills/huifu-pay-integration)
- [Huifu payment API documentation](https://paas.huifu.com/partners/api/doc/)
- [Official service source index](references/official-service-source-index.md)
- [Server SDK compatibility matrix](references/shared-server-sdk-matrix.md)
- [Webhook signature handling](references/shared-webhook-signing.md)
- [Credential handling boundaries](references/shared-credential-boundary.md)
- [Go-live checklist](references/copilot-go-live-checklist.md)

## Skill Output:

**Output Type(s):** [Text, Code, Configuration instructions, Shell commands]

**Output Format:** [Markdown with code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples require merchant configuration and validation before live transactions.]

## Skill Version(s):

1.4.0 (source: ClawHub release metadata and skill documentation)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
