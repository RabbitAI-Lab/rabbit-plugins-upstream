## Description:

在明确授权下管理学生的长期学习档案，包括学科表现、成长记录以及单独授权的情绪和兴趣信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and their guardians use this skill to create, review, correct, export, or delete a consent-based learning profile for personalized tutoring. Educators may contribute limited updates when authorized.

### Deployment Geography for Use:

China (mainland); other regions require localized curriculum, language, emergency resources, and minor-consent rules

## Known Risks and Mitigations:

Risk: Sensitive student records could be accessed or shared across students without effective platform controls.

Mitigation: Enable long-term profiles only where per-student isolation, identity confirmation, consent checks, and export/delete controls are enforceable; otherwise use session-only information.

Risk: Crisis referrals or minor consent practices could be inappropriate outside the intended region.

Mitigation: Localize emergency resources, curriculum, language, and minor-consent rules before use outside mainland China.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-dna)
- [Student profile schema](schemas/dna-profile.schema.json)
- [Crisis referral protocol](references/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Conversational profile summaries and text exports; structured profile records when authorized]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile access, updates, and sharing depend on identity confirmation and separate consent settings.]

## Skill Version(s):

2.6.0 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
