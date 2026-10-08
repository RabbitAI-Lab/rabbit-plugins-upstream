## Description:

Helps Chinese-language teachers plan classical Chinese and poetry lessons covering recitation, vocabulary in context, interpretation, themes, and cultural connections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-language teachers use this skill to draft classical Chinese and poetry lesson frameworks, discussion questions, recitation activities, and proposed class learning records for teacher review.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Proposed updates to persistent class weakness records could change analyzer-owned diagnostic counters.

Mitigation: Require teacher review and platform-enforced field-level write controls that prevent this skill from changing stubbornCount.

Risk: Class or student records and parent-facing content may expose sensitive learning information.

Mitigation: Check writeback and parent-sharing consent before sharing or saving; keep student details minimal.

Risk: Mainland China curriculum, privacy, and crisis-referral assumptions may not fit other regions.

Mitigation: Localize these rules and referral routes before use outside Mainland China.

## Reference(s):

- [Classical Chinese vocabulary quick reference](artifact/references/classical-vocab-quick-ref.md)
- [Recitation and rhythm guide](artifact/references/recitation-rhythm-guide.md)
- [High school classical Chinese teaching guide](artifact/references/hs-classical-teaching.md)
- [Class teaching workspace schema](artifact/shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, JSON]

**Output Format:** [Teacher-facing Markdown drafts and structured proposals for class records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher confirmation required before class-record updates; no full-text modern translations or whole-work line-by-line explanations.]

## Skill Version(s):

2.11.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
