## Description:

Detects aggressive interactions in livestock and poultry from continuous barn videos, including fighting, biting, chasing, and butting, and outputs behavior type, intensity level, and alert level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze barn images, videos, or media URLs for livestock and poultry aggression events, producing structured reports with behavior categories, incident segments, intensity, alert level, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Barn media or media URLs are sent to the skill's configured service for analysis.

Mitigation: Use only approved barn media and approved service endpoints, and confirm data handling requirements before running analysis.

Risk: The skill automatically creates or reuses an identity and may read workspace API-key or identity files.

Mitigation: Review identity and API-key handling before installation, restrict workspace access, and avoid running the skill in workspaces that contain unrelated secrets.

Risk: Authentication tokens may be stored in a local workspace database.

Mitigation: Review local token storage behavior and apply local retention, access control, and cleanup practices appropriate for the deployment environment.

Risk: The packaged configuration includes development HTTP endpoints.

Mitigation: Correct or verify the configuration before use, and prefer approved production HTTPS endpoints.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-aggressive-behavior-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API 接口文档](references/api_doc.md)
- [API接口文档](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands]

**Output Format:** [Markdown reports or JSON analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior type, intensity level, alert level, incident segments, subject positions, timestamps, and report links.]

## Skill Version(s):

1.0.8 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
