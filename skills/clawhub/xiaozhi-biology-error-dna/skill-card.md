## Description:

Analyzes recurring mistakes in middle- and high-school biology across six dimensions and produces targeted weakness reports and practice guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking secondary-school students and educators use this skill to identify the causes of repeated biology mistakes, plan focused practice, and review weakness reports with consent-controlled learning profiles.

### Deployment Geography for Use:

China mainland; localize curriculum, minor-consent requirements, and crisis referrals before use elsewhere.

## Known Risks and Mitigations:

Risk: Student learning profiles may expose personal data through storage or sharing.

Mitigation: Explain what is retained or shared, obtain student and guardian consent as appropriate, and honor pause, access, correction, export, deletion, and sharing controls.

Risk: Chinese-language curriculum and crisis guidance may be unsuitable outside China mainland.

Mitigation: Localize curriculum, minor-consent practices, and emergency resources before deployment in another region.

Risk: Mistake classifications or generated practice questions may mislead students.

Mitigation: Confirm classifications with a focused check, verify generated questions before use, and flag reports based on too few examples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-biology-error-dna)
- [Biology error dimension table](artifact/references/biology-error-dimension-table.md)
- [Learning profile schema](artifact/shared/dna-profile.schema.json)
- [Skill handover schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Chinese-language weakness reports, practice guidance, and structured profile handovers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile updates and cross-skill sharing require consent; insufficient samples are flagged rather than reported as reliable trends.]

## Skill Version(s):

2.7.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
