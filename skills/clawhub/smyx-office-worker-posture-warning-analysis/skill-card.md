## Description:

Analyzes office workstation video for prolonged sitting and posture concerns, returning warnings and a structured report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Workplace teams and developers use the skill to analyze consented workstation footage for sitting-duration and posture alerts and to review historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workplace camera footage and posture records are sent to a cloud service.

Mitigation: Obtain informed employee consent and approve the cloud service for this data before uploading video.

Risk: The skill may create or reuse an identity and persist account tokens locally.

Mitigation: Review local credential storage and restrict access to the workspace data directory.

Risk: Historical workplace records may be queried without clear user-visible scope.

Mitigation: Require explicit confirmation and appropriate access controls before history queries.

## Reference(s):

- [Skill API documentation](references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-office-worker-posture-warning-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured JSON or plain-text analysis and Markdown report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Posture measurements, sitting-duration warnings, suggestions, and optional history links]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
