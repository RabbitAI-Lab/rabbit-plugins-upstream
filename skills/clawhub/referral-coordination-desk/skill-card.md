## Description:

Prepares referral handoff digests and creates local referral handoff packets for care coordination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Care coordination staff use this skill to turn supplied referral details into a handoff digest and save a referral packet for local scheduling workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Referral handoff fields may contain patient or business-sensitive information retained in a local packet file.

Mitigation: Use a dedicated output directory and avoid real sensitive data unless local retention is acceptable.

## Reference(s):

- [Referral Coordination Desk release](https://clawhub.ai/wxt-ai/skills/referral-coordination-desk)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON objects and a local JSON packet file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The upstream operation returns a digest; the downstream operation writes a packet in the chosen output directory.]

## Skill Version(s):

3.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
