## Description:

语文写作素材的存取工具：存的时候打好标签，用的时候按主题检索得到。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, guardians, and education agents use this skill to save Chinese writing material with tags, retrieve relevant material by topic, and summarize confirmed material usage with consent.

### Deployment Geography for Use:

Mainland China by default; localize crisis resources, curriculum assumptions, guardian-consent requirements, and emergency guidance before use elsewhere.

## Known Risks and Mitigations:

Risk: Use outside mainland China may apply the wrong crisis resources, curriculum assumptions, or guardian-consent expectations for minors.

Mitigation: Localize crisis resources, emergency guidance, curriculum assumptions, and consent requirements before deployment in another region.

Risk: Persistent memory or cross-skill sharing could retain student material or usage records beyond the learner's intent.

Mitigation: Keep profile and cross-skill sharing consent-gated, and preserve view, correct, delete, pause, sharing-control, and export controls.

Risk: Recommended writing material could include uncertain sources or usage counts that are inferred instead of confirmed.

Mitigation: Mark uncertain sources as needing student confirmation and record usage only when the student or writing coach confirms the material was used.

Risk: Crisis signals in student text could be mishandled if the normal material-storage flow continues.

Mitigation: Stop the skill flow on crisis signals and follow the crisis referral protocol with local emergency resources and trusted-adult escalation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-material-library)
- [DNA profile schema](https://xiaozhi-skills.openclaw.dev/schemas/dna-profile.schema.json)
- [Handover protocol schema](https://xiaozhi-skills.openclaw.dev/schemas/handover-protocol.schema.json)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [Platform conventions](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese conversational text and Markdown lists, with optional JSON-compatible profile or handover updates when consented.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code; uses consent-gated memory, sharing, export, and deletion controls.]

## Skill Version(s):

2.3.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
