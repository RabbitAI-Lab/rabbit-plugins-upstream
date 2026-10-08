## Description:

Analyzes recurring biology mistakes for Chinese secondary-school students across six error dimensions and provides targeted weakness reports and study guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Secondary-school biology learners in mainland China use this skill to identify recurring causes of wrong answers, review weak topics and plan focused practice. It can provide a weakness report on request and share learning-profile updates only with appropriate consent.

### Deployment Geography for Use:

Mainland China; localize crisis contacts, curriculum and minor-consent requirements before use elsewhere.

## Known Risks and Mitigations:

Risk: A learner's error history or sensitive learning profile could be shared without informed consent.

Mitigation: Confirm profile, cross-skill, parent-sharing and reminder permissions before recording, sharing or scheduling; honor pause and deletion requests.

Risk: Mainland China crisis contacts and school or minor-consent assumptions may be inappropriate elsewhere.

Mitigation: Localize emergency contacts, educational standards and consent requirements before using the skill outside mainland China.

Risk: Incorrectly generated biology exercises or unsupported historical counts could mislead learners.

Mitigation: Check generated exercises for accuracy and grade fit; use notebook-provided counts and flag insufficient data rather than inventing statistics.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-biology-error-dna)
- [Biology error dimension table](references/biology-error-dimension-table.md)
- [Learning profile schema](shared/dna-profile.schema.json)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language text or Markdown; structured profile updates when consented]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are provided on request; historical counts rely on the general error notebook.]

## Skill Version(s):

2.11.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
