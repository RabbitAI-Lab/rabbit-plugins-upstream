## Description:

Analyzes gaze direction and facial pose in video to estimate focus, distraction, and mind-wandering for classroom, office, and driving scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers, managers, safety teams, and developers use it to analyze supplied videos and review focus scores, distraction counts, trends, and reports. Treat results as estimates and review them with a person.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared account handling can mix users’ reports.

Mitigation: Use only after account separation is addressed; require explicit enrollment and protect account tokens.

Risk: The “export only” option can still upload videos.

Mitigation: Confirm authorization before uploading footage, check the provider’s retention and deletion practices, and do not rely on --api-url to redirect processing.

Risk: Backend privacy controls and analysis accuracy are unverified.

Mitigation: Avoid sensitive footage until controls are confirmed, and treat scores as estimates that require human review.

## Reference(s):

- [ClawHub release](https://clawhub.ai/18072937735/skills/smyx-focus-analysis)
- [Skill introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured focus analysis report with scores, trends, statistics, recommendations, and report links; JSON or Markdown presentation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Estimates of focus and distraction; results are for reference and do not replace human assessment.]

## Skill Version(s):

1.0.19 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
