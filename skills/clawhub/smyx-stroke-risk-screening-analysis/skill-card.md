## Description:

Combines TCM facial feature recognition with physiological indicator information to provide early warnings of high-risk stroke conditions such as cerebral infarction and cerebral hemorrhage, and provides lifestyle intervention suggestions and medical guidance. | 脑卒中风险筛查技能，结合中医面部特征辨识结合生理指标信息，提前预警脑梗塞、脑出血等脑卒中高危状态，给出生活干预建议和就医指引

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit face images or videos with optional physiological indicators for stroke risk screening reports, risk warnings, lifestyle suggestions, medical guidance, and report history lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facial images or videos and health indicators are sent to LifeEmergence remote services.

Mitigation: Use only with appropriate consent and data-handling review, and ask the publisher for privacy, retention, deletion, and backend validation details before using sensitive personal or patient data.

Risk: The skill may silently create or reuse a local or remote account identity for history and reports.

Mitigation: Review identity handling before deployment and avoid exposing internal identity values in user-facing output.

Risk: The output is health screening guidance, not a medical diagnosis.

Mitigation: Present results as screening information only and direct users to professional medical evaluation for high-risk findings or clinical decisions.

Risk: Backend documentation is inconsistent with the stroke-screening claims.

Mitigation: Validate the configured service endpoints and expected response fields with the publisher before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-stroke-risk-screening-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown or JSON structured screening report; Markdown table or structured text for report history.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk levels, extracted findings, health warnings, lifestyle suggestions, medical guidance, and report links.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter reports 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
