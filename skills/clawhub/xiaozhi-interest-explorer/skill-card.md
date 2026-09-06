## Description:

每周引导学生记录兴趣探索、困难反应、时间感和外部反馈，帮助区分浅层喜好与遇到困难仍想继续的真实兴趣。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in supported K12 grade bands use this skill to run weekly interest explorations, record consent-gated observations, and review whether an interest persists when work becomes difficult. Guardians or educators may receive limited factual summaries only when the student and required consent settings allow sharing.

### Deployment Geography for Use:

China mainland by default; deployment elsewhere requires localized crisis resources, curriculum framing, and minor-data consent review.

## Known Risks and Mitigations:

Risk: Persistent student interest data could be written outside the intended scope if the receiving profile system accepts loose writeback paths.

Mitigation: Allowlist only the permitted interestDNA fields, reject unknown paths, and recheck profileEnabled plus interestTrackingConsent before every persistent write.

Risk: Interest records involve minors and could be exposed to guardians or other skills without the intended consent controls.

Mitigation: Verify the current speaker, guardian requirements, parentSharingConsent, crossSkillSharing, and one-time user confirmation before sharing, exporting, or summarizing records.

Risk: Crisis or safety signals may arise during student conversations and require region-appropriate escalation.

Mitigation: Stop the interest-exploration flow for crisis signals and localize emergency contacts, trusted-adult referral language, and minor-safety procedures before deployment outside the default region.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-interest-explorer)
- [Interest exploration record template](artifact/references/interest-exploration-template.md)
- [Platform capability conventions](artifact/shared/platform-conventions.md)
- [Shared vocabulary and consent fields](artifact/shared/vocab.md)
- [Crisis exception protocol](artifact/shared/crisis-exception.md)
- [Grade bands](artifact/shared/grade-bands.md)
- [Learning DNA profile schema](artifact/shared/dna-profile.schema.json)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Conversational Chinese text with structured Markdown-style interest records and consent-gated writeback proposals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce parent-facing factual summaries, exports, or profile writeback proposals only after the required consent checks.]

## Skill Version(s):

2.1.10 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
