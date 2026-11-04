## Description:

Analyzes plant leaf images or video for visual signs of nutrient deficiency and returns likely nutrient diagnoses with confidence and fertilization direction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Home gardeners, greenhouse operators, and plant growers can use the skill to review suspected nutrient deficiencies from leaf images or video and receive likely nutrient causes, confidence, and general fertilization direction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags possible credential exposure through profile handling and media uploads even when the no-analysis option is selected.

Mitigation: Avoid using sensitive media or credentials until the noted fixes are available. Verify the provider's upload retention, account deletion, local token cleanup, and possible charges; consider rotating an API secret if it may already have been sent as profile data.

## Reference(s):

- [ClawHub release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-nutrient-diagnosis-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured diagnosis report with likely deficiency, confidence, recommendations, and a report link when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include confidence scores and links to reports.]

## Skill Version(s):

1.0.15 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
