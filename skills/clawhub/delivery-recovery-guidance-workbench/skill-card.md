## Description:

Turn delivery failure details into a bounded retry schedule and a next-action handoff record.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Delivery operators and developers use this skill to plan bounded retries after failed deliveries and record the next handoff action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured delivery endpoint can receive the retry schedule automatically using available credentials.

Mitigation: Review the destination before installation and run only when the delivery endpoint and credentials are intentionally configured.

Risk: The operation writes local CSV retry records.

Mitigation: Use a dedicated output directory and review local records before sharing them.

## Reference(s):

- [Handoff Recovery Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/delivery-recovery-guidance-workbench)

## Skill Output:

**Output Type(s):** [Structured data, Files]

**Output Format:** [JSON response and local CSV schedule]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes remaining attempts, retry times, and the next action; a configured delivery endpoint may receive the record and return a receipt.]

## Skill Version(s):

1.1.1 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
