## Description:

Analyzes fixed home-entrance or balcony-door video to estimate a child's daily outdoor time from exit and return events and provide activity reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and caregivers use the skill to review estimated outdoor time and reminders for children using fixed doorway or balcony camera footage. They can also retrieve previous analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child and household entrance footage and report history are sent to a cloud service.

Mitigation: Obtain guardian consent and review the service's access controls, retention, and handling of exported reports before uploading real footage.

Risk: The skill silently creates or reuses identity state and stores tokens.

Mitigation: Review account creation and token storage before installation; limit access to credentials and report history.

Risk: Doorway events may misrepresent actual outdoor activity, especially for balcony visits or multiple children.

Mitigation: Treat reported time as an estimate, check ambiguous results, and avoid using it as a medical assessment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-child-outdoor-activity-monitor-analysis)
- [Skill API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis results or a Markdown table of historical reports with links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Estimated outdoor duration and reminders are based on observed door crossings, not measured exercise.]

## Skill Version(s):

1.0.11 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
