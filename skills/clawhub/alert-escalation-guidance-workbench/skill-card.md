## Description:

Assign an incident owner.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Service operators use this skill to assign an incident owner from supplied severity guidance and record the assignment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured HTTP or email delivery can send incident assignment data to an external destination.

Mitigation: Review the skill before use with sensitive incident data; enable delivery only to explicitly trusted destinations and control delivery-related environment variables.

Risk: The skill writes local assignment records.

Mitigation: Run it with a dedicated, writable output directory.

## Reference(s):

- [Incident Assignment Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/alert-escalation-guidance-workbench)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [JSON object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns alert ID, severity, assignment, and rule-match status; writes a local assignment record and may return a delivery receipt when delivery is configured.]

## Skill Version(s):

1.1.1 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
