## Description:

Detects whether anyone has fallen within a specified target area, supports image and short video analysis, and returns structured safety-monitoring results for elder-care and nursing-home scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, and safety-monitoring operators use this skill to analyze uploaded images or short videos for potential falls, abnormal activity, and related elder-care risks. It can also query cloud-hosted fall-detection report history for the current resolved user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Caregiving images, videos, and report-history queries are sent to the lifeemergence.com cloud service.

Mitigation: Use the skill only when cloud processing of sensitive caregiving media is acceptable, and avoid submitting unnecessary personal or identifying content.

Risk: The skill silently manages user identity and stores tokens locally in smyx-common-claw.db.

Mitigation: Limit who can run the skill, protect the workspace data directory, and review token storage expectations before deployment.

Risk: Report-history queries can expose sensitive prior analysis records associated with the resolved user identity.

Mitigation: Do not pass or expose open-id values, and run the skill only in workspaces where report access is appropriate for the current user.

Risk: Fall-detection results may be incomplete or incorrect and are not a substitute for direct emergency verification.

Mitigation: Treat results as safety reference only, and require human confirmation and emergency response when a possible fall is detected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fall-detection-image-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Fall detection API documentation](references/api_doc.md)
- [Common AI analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown or plain text containing structured JSON analysis results, report links, or a report-history table; optionally saved to a user-specified output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include cloud report export links and safety guidance; analysis results are for safety reference and do not replace human confirmation.]

## Skill Version(s):

1.0.15 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
