## Description:

Prepares a referral digest and local handoff packet, with optional delivery to a configured destination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Care coordination teams and developers use this skill to turn referral form data into a routing digest and a local referral handoff packet; configured delivery can submit the packet and return a receipt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive referral data may be sent to a configured HTTP endpoint without a separate send confirmation.

Mitigation: Review referral data before use; prefer local-only mode and check delivery endpoint and API-key settings before running.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wxt-ai/skills/referral-handoff-packet-complete)
- [Skill README](artifact/README.md)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON result and local JSON referral packet]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes local artifact and delivery receipts; external delivery is optional.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
