## Description:

开卷答题教练 is a Chinese junior-high open-book exam study-method coach that teaches textbook indexing, rapid lookup, and answer organization without providing live exam help or subject-specific answers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking junior-high students use this skill to prepare for local open-book exam contexts by building textbook indexes, practicing fast lookup, and organizing responses from source materials and textbook passages. It is a study-method coach, not a tool for live exam assistance or answer generation.

### Deployment Geography for Use:

China Mainland

## Known Risks and Mitigations:

Risk: Using the skill outside Chinese-speaking junior-high China Mainland exam contexts may produce mismatched curriculum assumptions or inappropriate crisis-help contacts.

Mitigation: Localize curriculum assumptions, regional exam rules, and crisis referral contacts before deployment outside China Mainland.

Risk: Students may try to use the skill during a live exam or to obtain direct answers.

Mitigation: Keep the exam-in-progress refusal behavior and method-only boundary active; redirect users to post-exam review.

Risk: 道德与法治 prompts can require sensitive viewpoint content that varies by textbook and locale.

Mitigation: Limit assistance to locating relevant textbook sections and organizing points; require the student to use textbook source text for viewpoint statements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-openbook-coach)
- [Open-book method reference](artifact/references/openbook-method.md)
- [Platform conventions and localization boundaries](artifact/shared/platform-conventions.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-formatted coaching guidance and refusal/redirect responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Concise Chinese educational coaching focused on methods, textbook lookup, and answer organization; no executable output.]

## Skill Version(s):

2.3.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
