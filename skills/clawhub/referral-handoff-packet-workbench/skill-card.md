## Description:

Create a referral handoff packet.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Care coordination staff use this skill to turn a supplied referral digest into a concise handoff packet for scheduling and routing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Referral details may contain sensitive care-coordination information.

Mitigation: Provide only data intended for the packet and handle the generated packet according to the user's care-coordination privacy requirements.

Risk: Generated routing or packet fields may be incorrect for operational use.

Mitigation: Review the packet identifier, routing lane, and fields before using them for scheduling or coordination.

## Reference(s):

- [Referral Packet Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/referral-handoff-packet-workbench)
- [wxt-ai publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Object with packet_id, routing_lane, and fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses only referral details supplied in the current request.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
