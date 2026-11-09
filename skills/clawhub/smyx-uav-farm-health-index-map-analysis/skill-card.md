## Description:

Analyzes UAV farmland imagery to calculate vegetation indices and produce crop health heatmaps and structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators, agricultural cooperatives, crop monitoring services, and agricultural researchers use the skill to assess UAV imagery, locate low vegetation health areas, and review crop coverage and health statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports that the skill silently registers service accounts and retains credentials.

Mitigation: Confirm account creation, credential storage, retention, and revocation practices with the publisher before use; avoid providing sensitive account identifiers.

Risk: The security assessment reports that media may be uploaded even when analysis is instructed to be skipped, and remote processing and retention are unverified.

Mitigation: Submit imagery only after confirming Lifeemergence's upload, retention, account, and billing practices. Do not rely on --export-env-only to prevent uploads.

Risk: The security guidance identifies credential destinations and secret handling as needing publisher fixes.

Mitigation: Ask the publisher to restrict credential destinations and provide protected token storage and revocation controls.

## Reference(s):

- [Farm health analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Files]

**Output Format:** [Structured analysis text or JSON with heatmap and report links; historical reports can be shown as a Markdown table.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include vegetation index values, health-zone coordinates and area estimates, crop coverage statistics, and report links.]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
