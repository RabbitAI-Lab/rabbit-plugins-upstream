## Description:

Estimates daily feed intake per livestock individual from continuous feeder videos by tracking the change of feed remaining in the trough, and outputs intake trend with anomaly alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators, livestock-management teams, and developers use this skill to analyze feeder-area images or videos, estimate daily feed intake and intake trends, flag anomalies, and retrieve cloud-hosted historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Feeder images, videos, and report queries may be sent to configured lifeemergence.com services.

Mitigation: Use the skill only when that transfer is acceptable for the farm data involved, and review retention, deletion, and account-authorization expectations before using sensitive footage or operational records.

Risk: The skill automatically creates or reuses a local or cloud identity and stores access tokens in the workspace data area.

Mitigation: Run it in an access-controlled workspace and clear stored credentials or tokens when the identity should not persist.

Risk: Feed-intake estimates can be affected by camera angle, lighting, occlusions, file size, format support, and inconsistent trough setup.

Mitigation: Use stable capture conditions, review anomaly alerts, and validate estimates against farm measurement procedures before making operational decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-feed-intake-estimation-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Feed intake estimation API documentation](artifact/references/api_doc.md)
- [Common AI analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON report text with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are visual estimates and anomaly alerts; the skill can submit local media or media URLs to configured lifeemergence.com services.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
