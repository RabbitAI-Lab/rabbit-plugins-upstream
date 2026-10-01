## Description:

Create a referral handoff packet.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Care coordination and scheduling teams use this skill to turn a supplied referral digest into a handoff packet and a local JSON record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Referral details are stored in a local JSON file under the chosen output directory.

Mitigation: Use a dedicated output directory and supply only the referral details needed for the packet.

## Reference(s):

- [Referral Packet Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/referral-handoff-packet-workbench)

## Skill Output:

**Output Type(s):** [JSON, Local file]

**Output Format:** [JSON referral packet result and local JSON packet file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a packet ID, routing lane, referral fields and a local effect receipt; does not confirm an external handoff.]

## Skill Version(s):

1.1.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
