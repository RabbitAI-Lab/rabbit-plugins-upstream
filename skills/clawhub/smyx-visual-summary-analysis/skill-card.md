## Description:

Analyzes videos and images to produce natural-language scene descriptions and visual summary reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media teams use this skill to summarize images and short videos for content understanding, accessibility assistance, and media asset management. It can also retrieve past reports from the cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded media and supplied URLs are sent to a cloud service.

Mitigation: Avoid sensitive media and internal URLs unless the service account and retention practices are acceptable.

Risk: Identity resolution and account/token handling occur automatically, with service tokens stored locally.

Mitigation: Review the identity and token-storage behavior before installation and restrict access to the workspace data directory.

Risk: Cloud history lookup may expose previously generated reports associated with the account.

Mitigation: Use an appropriately scoped service account and review access to historical reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-visual-summary-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Scene descriptions and structured reports; Markdown tables for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include cloud-hosted links; JSON output is available.]

## Skill Version(s):

1.0.18 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
