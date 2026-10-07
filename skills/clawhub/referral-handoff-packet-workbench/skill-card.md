## Description:

Create a referral handoff packet.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Care coordination and scheduling teams use this skill to turn a referral digest into a handoff packet and routing details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery can send referral packet data to an external endpoint without a separate confirmation or tight destination controls.

Mitigation: For local-only generation, clear delivery endpoint, API key, and SMTP settings and use a dedicated output directory; before enabling delivery, verify the intended destination and packet contents.

## Reference(s):

- [Referral Packet Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/referral-handoff-packet-workbench)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON response and local JSON packet]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a packet ID and routing details; includes a delivery receipt when delivery is configured.]

## Skill Version(s):

1.1.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
