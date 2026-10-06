## Description:

Analyzes office workstation video for prolonged sitting and posture changes, returning alerts and structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and workplace health teams use workstation video to identify prolonged sitting and posture concerns, receive behavioral reminders, and review past reports. Results are wellness guidance, not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workplace camera footage and posture reports expose sensitive employee data.

Mitigation: Obtain employee consent and restrict access to footage and reports before deployment.

Risk: Automatic identity creation, locally stored account tokens, and cloud history queries may expose reports to unintended users.

Mitigation: Confirm the cloud service and identity model, limit history-query access, avoid arbitrary identity values, and review token storage and removal.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-office-worker-posture-warning-analysis)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured analysis reports and Markdown history tables, with optional JSON or saved text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes posture alerts, suggestions, and report links when available.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; artifact frontmatter lists 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
