## Description:

Analyzes in-cabin driver video for head-down and side-view events and returns distraction alerts and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Fleet operators and developers use this skill to assess driver-facing video for sustained head-down or side-view events and review distraction reports and alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driver-facing video or video URLs are sent to a cloud service and may expose sensitive footage.

Mitigation: Obtain driver consent before fleet or employee use, review the provider's retention and access controls, and avoid highly sensitive footage unless those controls are acceptable.

Risk: The skill silently creates or reuses a local identity and stores authentication tokens for report history.

Mitigation: Review and restrict access to local identity and token storage before installation, and confirm the report-history behavior is acceptable.

## Reference(s):

- [Driver head-pose API documentation](references/api_doc.md)
- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-driver-head-pose-abnormality-analysis)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured analysis report or report-history list with links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include head-pose events, distraction warnings, and report links.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; packaged SKILL.md states 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
