## Description:

Analyzes workplace images and videos for possible employee absences and provides monitoring reports and report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Workplace managers and operators use this skill to review staff presence in monitored areas from images or video and consult prior absence reports. Results should inform, not replace, human review before personnel decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workplace images, videos or media URLs and an internal user identity are sent to external services.

Mitigation: Obtain authorization and explicit confirmation before submitting media; confirm the provider's data retention and access terms.

Risk: The skill may silently create or reuse an identity and store tokens locally.

Mitigation: Confirm account-creation and token-storage practices with the publisher; limit access to local credentials.

Risk: History queries may expose sensitive staff monitoring reports.

Mitigation: Require explicit confirmation for history queries and verify who can access stored reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-staff-absence-detection-analysis)
- [Absence monitoring API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text reports and Markdown tables; optional JSON result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include absence status, durations, report links, and configurable detection thresholds.]

## Skill Version(s):

1.0.15 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
