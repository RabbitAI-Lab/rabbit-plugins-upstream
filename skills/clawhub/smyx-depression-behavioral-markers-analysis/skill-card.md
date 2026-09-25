## Description:

Using fixed home cameras in bedroom and dining areas, this skill analyzes multi-day behavior patterns for elderly or solo-living individuals to report long immobility, reduced eating activity, and related behavior-change alerts without making a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, care-platform operators, and caregiving teams use this skill to analyze qualifying long-duration home-camera footage and produce behavior-change reports about bed duration, eating activity, baseline deviations, and family or community-doctor alerts. It is intended as a behavioral observation aid, not as a depression diagnosis, clinical scale, medication recommendation, or treatment plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles intimate bedroom and dining-area video and health-adjacent behavior reports through cloud APIs.

Mitigation: Use only with explicit consent from the monitored person, confirm the cloud service is trusted for this data, and prefer privacy-preserving modes such as body contours, face masking, encrypted storage, and metric-only retention.

Risk: Evidence reports silent account/token provisioning and a hidden identity override.

Mitigation: Require identity handling to be reviewed and fixed before real caregiving or medical-adjacent use, and verify that account creation, token storage, and history access are transparent and authorized.

Risk: Behavioral changes can be caused by illness, travel, eating outside the home, surgery recovery, or other context unrelated to depression.

Mitigation: Treat outputs as observation signals, not diagnoses; combine them with caregiver context and professional clinical review before action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-depression-behavioral-markers-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured analysis reports with behavior metrics, alert text, recommendations, report links, and optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call cloud APIs for analysis and history retrieval; input normally must be continuous 24-hour or longer bedroom and dining-area video with a 7-14 day personal baseline for full alerting.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
