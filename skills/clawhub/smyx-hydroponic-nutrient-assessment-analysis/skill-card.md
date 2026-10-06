## Description:

Assesses hydroponic root and leaf images or videos for signs of nutrient imbalance and provides qualitative adjustment advice and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Hydroponic growers and developers use root and leaf media to assess possible nutrient-solution imbalance, receive directional care advice, and access historical reports. The assessment is qualitative and does not provide EC or ppm measurements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or media URLs are sent to the configured cloud service.

Mitigation: Use only media you are comfortable sharing with that service; avoid sensitive or unrelated content.

Risk: The skill creates and reuses a local user identity and stores cloud tokens in a workspace database.

Mitigation: Review local data storage and limit access to the workspace before installation.

Risk: Implementation differences from the documented image-focused workflow may affect results.

Mitigation: Test with non-sensitive sample media and review outputs before relying on care recommendations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-hydroponic-nutrient-assessment-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis text or JSON, with Markdown report links and history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Qualitative assessments and adjustment suggestions; optional saved JSON report]

## Skill Version(s):

1.0.10 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
