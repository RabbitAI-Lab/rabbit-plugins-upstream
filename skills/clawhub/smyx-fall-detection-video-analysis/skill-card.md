## Description:

Detects whether a person has fallen in a target area from uploaded or URL-based video and returns structured fall-detection results for home safety monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and care-monitoring developers use this skill to analyze local or network video for suspected falls, return structured findings, and retrieve prior fall-detection reports. Results are intended as safety alerts that still require human confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive videos, video URLs, report queries, and local identity values may be sent to LifeEmergence or configured service endpoints.

Mitigation: Use only footage and URLs that affected people have consented to share, and confirm endpoint configuration before deployment.

Risk: The skill can create or reuse local identity records and store service tokens during analysis and report-history queries.

Mitigation: Review token storage, identity creation, retention, and access controls before installing in a shared or production environment.

Risk: Fall-detection output can be incorrect or incomplete.

Mitigation: Treat results as safety alerts and require human confirmation before taking medical or emergency-response action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fall-detection-video-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Fall detection API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration]

**Output Format:** [Markdown text with structured JSON report content, status messages, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write results to a user-specified output file; historical report queries return service-provided JSON rendered as text.]

## Skill Version(s):

1.0.13 (source: server release evidence; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
