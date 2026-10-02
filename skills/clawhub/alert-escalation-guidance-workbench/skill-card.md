## Description:

Assigns an incident owner using supplied severity guidance and records the local assignment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Service operators use this skill to assign an incident to a response queue based on supplied severity guidance and record the assignment locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incident details written to the local assignment receipt may be sensitive.

Mitigation: Use a dedicated output directory and omit sensitive incident details unless they are intended to appear in the receipt.

## Reference(s):

- [Incident Assignment Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/alert-escalation-guidance-workbench)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON assignment result and local JSON receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes alert ID, severity, assigned queue, and whether a severity rule matched; writes a receipt under the specified output directory.]

## Skill Version(s):

1.1.0 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
