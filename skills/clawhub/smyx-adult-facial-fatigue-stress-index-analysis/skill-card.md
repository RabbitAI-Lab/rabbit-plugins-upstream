## Description:

Analyzes adult face images or short videos to estimate fatigue and stress indicators, returning a 0–100 index with directional wellness suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and workplace health teams can use the skill to estimate fatigue-related facial features from an adult image or short video and receive general rest or wellness suggestions. The score is a visual estimate, not a medical diagnosis or clinical stress assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports unclear user control over account creation and saved credentials, and says facial videos may still be submitted when using the export-only option.

Mitigation: Require explicit consent for facial analysis and remote processing, confirm the provider's retention and deletion terms, and review account creation and credential handling. Do not rely on the export-only option to prevent uploads.

## Reference(s):

- [ClawHub release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-adult-facial-fatigue-stress-index-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Structured data, Guidance, Markdown]

**Output Format:** [Structured analysis report with a fatigue/stress score, feature measurements, level, and directional suggestions; history results may be shown in a Markdown table.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The index ranges from 0 to 100. Results are visual estimates and are not medical diagnoses.]

## Skill Version(s):

1.0.12 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
