## Description:

语文病句专项教练：按中考六类病句判定，并在学生同意后建立语病档案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese K12 learners use this skill to identify six common grammar-error categories, practice corrections through guided prompts, and maintain a consent-based profile of recurring grammar weaknesses.

### Deployment Geography for Use:

Mainland China by default; other regions require localized consent and safety review.

## Known Risks and Mitigations:

Risk: The skill can maintain a long-term grammar-error profile for students, including minors.

Mitigation: Confirm profile, guardian, and cross-skill sharing consent before profile creation, sharing, or reminders.

Risk: The skill's safety and consent assumptions are designed for mainland China.

Mitigation: Deployments in other regions should replace local safety channels and consent assumptions before use.

Risk: Grammar classification or generated practice items could be incorrect or overcorrect acceptable expressions.

Mitigation: Use the bundled error library and item self-check protocol, and present uncertain classifications as uncertain rather than definitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-grammar-tracker)
- [Grammar error library](references/grammar-error-library.md)
- [Chinese error dimension table](shared/chinese-error-dimension-table.md)
- [Learning profile schema](shared/dna-profile.schema.json)
- [Handover protocol schema](shared/handover-protocol.schema.json)
- [Platform conventions](shared/platform-conventions.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with structured profile and handover data when consent allows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce grammar-error classifications, correction prompts, practice items, progress summaries, and consent-gated profile updates.]

## Skill Version(s):

2.1.10 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
