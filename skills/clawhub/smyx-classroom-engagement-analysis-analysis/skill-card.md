## Description:

Analyzes classroom camera footage to produce class-level engagement scores, seat-based alerts, teaching suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and school staff use classroom video or a video URL to review group engagement, identify seats needing attention, and adjust teaching; they can also retrieve historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Classroom footage of minors is sent to external services for analysis.

Mitigation: Confirm school authority and informed consent before use; establish a retention policy and deletion controls.

Risk: Persistent local identity and token records and cloud report history may conflict with anonymity expectations.

Mitigation: Use an administrator-controlled identity model and review stored identifiers and report access before deployment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-classroom-engagement-analysis-analysis)
- [Classroom engagement API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured analysis reports or Markdown lists of report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes engagement scores, seat-level alerts, teaching suggestions, and optional saved results.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
