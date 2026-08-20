## Description:

Combines livestock behavior in continuous barn videos with environmental sensor data to identify group stress responses caused by abnormal barn conditions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze livestock barn images, videos, URLs, and optional sensor data for environment-behavior anomaly reports. It returns behavior findings, environmental correlations, group stress levels, historical report lists, and report links for barn monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Livestock media, media URLs, and identity data may be sent to a configured remote service for analysis.

Mitigation: Use the skill only with media and URLs approved for remote processing, and avoid submitting sensitive farm footage or internal-only media URLs.

Risk: Cloud report history is associated with an automatically managed identity.

Mitigation: Confirm that account identity handling and report retention meet the deployment environment's privacy and access-control requirements before use.

Risk: Returned account tokens may be stored in the local workspace.

Mitigation: Run the skill in a sandboxed workspace when credential storage is a concern, and clear local token state according to the operator's security process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-environmental-anomaly-analysis)
- [API interface documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files]

**Output Format:** [Markdown report text with optional JSON-style detail and optional saved output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior feature lists, environment correlation results, group stress levels, historical report tables, and report links.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
