## Description:

Identifies common crop pests in leaf, bud, and fruit images or videos and returns pest findings with confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Growers and agricultural advisers use crop photos or videos to identify possible pests and review prior analysis reports. Findings support field assessment but do not provide pesticide or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crop photos, videos, or supplied URLs are sent to lifeemergence.com services for analysis.

Mitigation: Use only media and URLs approved for external processing; avoid including unrelated sensitive content.

Risk: The skill automatically creates or reuses an identity and associates cloud report history with it.

Mitigation: Review this account and history behavior before use; limit access to reports and shared workspaces.

Risk: Authentication tokens are stored locally in the workspace database.

Mitigation: Restrict workspace access and protect or remove local credentials when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-crop-pest-identification-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Structured JSON findings or Markdown report tables and links; optional saved result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes pest types, estimated counts, confidence scores, and report links when available.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata; bundled SKILL.md lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
