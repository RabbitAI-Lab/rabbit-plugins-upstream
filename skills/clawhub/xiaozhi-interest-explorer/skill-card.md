## Description:

Helps students distinguish surface-level likes from more durable interests by guiding weekly exploration and recording attraction, challenge response, time perception, and external feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students from middle elementary through high school use this Chinese-language skill to explore possible interests through weekly reflection, difficulty-response checks, and consent-controlled interest records. It supports self-discovery and growth planning signals, while avoiding subject tutoring, career recommendations, major selection, and admissions advice.

### Deployment Geography for Use:

Global, with localization review before deployment outside a Chinese-language/mainland-China context.

## Known Risks and Mitigations:

Risk: The skill targets students and can involve long-term interest profile data.

Mitigation: Enable long-term profile and interest tracking only after the student and any required guardian understand retention, deletion, export, and sharing controls.

Risk: The bundled crisis guidance contains China-specific emergency and youth-support resources.

Mitigation: Review deployments outside a Chinese-language/mainland-China context and replace or constrain crisis resources to local emergency and youth-support channels.

Risk: The security verdict requires review before installation despite finding no malicious behavior.

Mitigation: Review the skill before deployment, especially consent handling, parent-sharing behavior, and crisis-escalation language.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-interest-explorer)
- [Interest exploration template](references/interest-exploration-template.md)
- [DNA profile schema](https://xiaozhi-skills.openclaw.dev/schemas/dna-profile.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese-language conversational guidance and Markdown-style records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Consent-gated long-term interest records; no executable output.]

## Skill Version(s):

2.1.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
