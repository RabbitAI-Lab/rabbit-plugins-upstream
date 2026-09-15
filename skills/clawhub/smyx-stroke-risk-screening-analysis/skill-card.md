## Description:

Combines TCM facial feature recognition with physiological indicator information to provide early warnings of high-risk stroke conditions such as cerebral infarction and cerebral hemorrhage, and provides lifestyle intervention suggestions and medical guidance. | 脑卒中风险筛查技能，结合中医面部特征辨识结合生理指标信息，提前预警脑梗塞、脑出血等脑卒中高危状态，给出生活干预建议和就医指引

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to screen stroke risk from facial images or video, optional physiological indicators, and cloud report history. It produces structured risk reports with warnings, lifestyle suggestions, medical guidance, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive facial images, videos, medical indicators, identity data, billing data, and credentials with unclear consent and unsafe defaults.

Mitigation: Review carefully before installing; require informed consent for account and history features, use HTTPS production endpoints, and confirm credential storage before using real user data.

Risk: Stroke risk output can be mistaken for clinical diagnosis or emergency guidance.

Mitigation: Present results only as health risk screening, keep the medical disclaimer visible, and direct high-risk users to professional medical care.

Risk: The packaged workflow may invoke cloud processing and report-history APIs for sensitive media and health data.

Mitigation: Confirm cloud processing, retention, access controls, and report-history behavior before deployment.

Risk: A payment-skill prompt appears in shared artifact behavior and may represent a separate workflow.

Mitigation: Treat payment-related actions as separate from stroke screening and require explicit user approval before installing or invoking payment workflows.

## Reference(s):

- [API Interface Documentation](artifact/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-stroke-risk-screening-analysis)

## Skill Output:

**Output Type(s):** [analysis, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON structured report with risk level, risk factors, warnings, lifestyle suggestions, medical guidance, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and json detail levels; history queries return Markdown tables from cloud report data.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter reports 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
