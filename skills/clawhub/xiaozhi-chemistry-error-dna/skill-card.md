## Description:

Analyzes chemistry mistakes across six dimensions and identifies recurring learning weaknesses for Chinese middle and high school students.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and educators use this skill to diagnose the root causes of chemistry mistakes, track confirmed weak areas, and request progress summaries. It covers chemistry taught in mainland Chinese middle schools and high schools, including required and selective-required courses.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: A minor's mistake history or parent-visible summary could be saved or shared without appropriate consent.

Mitigation: Confirm platform consent settings and the student's required approvals before retaining profiles, sharing across skills, sending reminders, or preparing parent summaries.

Risk: Mainland China crisis contacts, curriculum, and minor-consent assumptions may be unsuitable elsewhere.

Mitigation: Localize emergency referrals, curriculum expectations, and consent requirements before use outside Mainland China.

Risk: Chemistry experiment guidance could expose students to unsafe procedures.

Mitigation: Apply the supplied laboratory safety rules and avoid suggesting unsupervised hazardous experiments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-chemistry-error-dna)
- [Chemistry error dimension table](artifact/references/chemistry-error-dimension-table.md)
- [Profile schema](artifact/shared/dna-profile.schema.json)
- [Handover schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Chinese-language guidance and reports in Markdown; structured profile and handover records in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long-term records and sharing require consent; historical reports depend on available profile data.]

## Skill Version(s):

2.11.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
