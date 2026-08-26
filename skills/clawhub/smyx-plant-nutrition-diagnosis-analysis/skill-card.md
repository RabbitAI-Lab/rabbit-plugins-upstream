## Description:

Diagnoses plant nutrient deficiency or excess based on computer vision and plant physiology, outputs targeted fertilization suggestions for precision nutrient management. | 植物营养诊断技能，基于计算机视觉与植物生理学，通过叶片特征诊断氮磷钾及微量元素缺乏或过剩，输出精准施肥建议

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External growers, agronomists, and developers use this skill to diagnose plant nutrient deficiency or excess from leaf images or videos, generate structured analysis, and retrieve cloud-hosted diagnosis history. The results support precision fertilization decisions but should be checked against soil tests and local agricultural guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automatically links a local or cloud identity and persists account tokens.

Mitigation: Install only if the publisher and backend service are trusted, and review account linkage and token storage behavior before use.

Risk: Plant media and report history requests are sent to backend services with incomplete and inconsistent disclosure.

Mitigation: Review configured backend URLs, retention, and account behavior before deployment, and avoid submitting sensitive media unless that storage model is acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-nutrition-diagnosis-analysis)
- [Publisher Profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown text with structured JSON report content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload plant media to backend services and query cloud report history associated with an automatically resolved identity.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
