## Description:

Analyzes video of children's activity areas for contact with dangerous objects or electrical outlets and provides alerts and analysis reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and developers use the skill to review footage of children's activity areas for possible contact with hazardous objects or electrical outlets and to retrieve related alerts and reports. Alerts support, but do not replace, adult supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child-related home videos, video URLs, and report queries are sent to a remote service.

Mitigation: Obtain guardian consent and explicit user confirmation before each analysis or history lookup; share only necessary footage.

Risk: The skill creates or reuses a local identity record and stores service tokens in the workspace data area.

Mitigation: Review this behavior before installation and restrict access to the workspace data area.

Risk: Missed or inaccurate alerts could leave dangerous behavior unnoticed.

Mitigation: Treat alerts as supplemental information, not a substitute for adult supervision.

## Reference(s):

- [API documentation](references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-dangerous-object-detection-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis results and alerts, with report links or a Markdown report list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include detected behaviors, warning levels, and links to detailed results.]

## Skill Version(s):

1.0.7 (source: server-resolved ClawHub release; bundled SKILL.md lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
