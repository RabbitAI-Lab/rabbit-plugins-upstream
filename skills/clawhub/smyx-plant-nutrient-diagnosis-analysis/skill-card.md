## Description:

Analyzes plant leaf images or videos for visual signs of nutrient deficiencies and returns likely nutrients with confidence and directional care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Gardeners, greenhouse teams, and plant-care developers can use the skill to review leaf images for possible nutrient deficiencies and get a confidence-rated diagnosis with general fertilization direction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared accounts may expose reports belonging to other users.

Mitigation: Use an isolated account and avoid shared-user deployments until sender isolation is addressed.

Risk: Local media is uploaded to LifeEmergence services, and export-only may still trigger uploads; retention and billing terms are unverified.

Mitigation: Do not rely on export-only to prevent transfer. Avoid sensitive media and verify upload, retention, and billing behavior before use.

Risk: Credential destination restrictions and account or token retention need review.

Mitigation: Confirm where credentials are sent and how account and token data are retained before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-nutrient-diagnosis-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API interface notes](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Structured diagnosis report with likely nutrient, confidence, and general care guidance; report lists can be formatted as Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations are directional and do not include fertilizer concentrations or amounts.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
