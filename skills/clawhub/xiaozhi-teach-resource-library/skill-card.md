## Description:

Helps independent teachers catalog, find, adapt, and reuse teaching resources while tracking sources, copyright, and usage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill to organize teaching materials and de-identified case notes, retrieve resources by topic and difficulty, and record adaptations and reuse. Teachers review materials before using them with students.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Resource notes or shared cases could expose identifiable student information.

Mitigation: Store only de-identified teaching-resource details; honor deletion requests and obtain consent before cross-skill sharing.

Risk: Unverified AI-generated or adapted exercises could contain errors.

Mitigation: Label generated items and require teacher verification, including rechecking adapted exercises, before student use.

Risk: Saving copyrighted questions or scans could copy materials without permission.

Mitigation: Record only source references for textbook questions and past exams; do not store unauthorized text or scans.

Risk: Missing workspace capabilities or homework-tracker integration could limit retrieval and follow-up.

Mitigation: Confirm storage and sharing controls, and fix or document the homework-tracker dependency before deployment.

Risk: China-specific education and privacy defaults may not fit other jurisdictions.

Mitigation: Review grade bands and local student-data requirements before use outside mainland China.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-resource-library)
- [Resource categorization and search](references/resource-categorization.md)
- [Resource entry examples](references/resource-entry-examples.md)
- [Copyright annotation template](references/copyright-annotation-template.md)
- [AI-generated item check](shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown resource recommendations and structured catalog entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Resource matches include relevance and verification status; teachers approve materials before student use.]

## Skill Version(s):

2.8.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
