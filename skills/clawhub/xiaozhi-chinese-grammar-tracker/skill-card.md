## Description:

Coaches Chinese-language students through six common sentence-error categories and, with consent, tracks recurring grammar mistakes for targeted practice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-language K12 students and educators use this skill to identify and practice correcting sentence errors, track recurring patterns with consent, and review progress on request.

### Deployment Geography for Use:

Mainland China (localize crisis resources and consent rules before use elsewhere)

## Known Risks and Mitigations:

Risk: Student grammar profiles could be stored or shared without appropriate consent.

Mitigation: Confirm consent before recording or sharing, enforce pause, deletion, export and parent-sharing controls, and share only necessary profile fields.

Risk: Mainland China crisis contacts and consent rules may be unsuitable for students elsewhere.

Mitigation: Localize crisis resources and consent requirements before deployment outside Mainland China; ask the student's location before providing regional contacts.

Risk: Progress summaries could imply unsupported historical tracking.

Mitigation: Use historical comparisons only when the platform supports persistent profiles and statistics; otherwise report current-session results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-grammar-tracker)
- [Grammar error library](artifact/references/grammar-error-library.md)
- [Chinese error dimension table](artifact/shared/chinese-error-dimension-table.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Conversational guidance and Markdown progress reports; structured profile updates when permitted]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Persistent tracking and cross-skill sharing require consent; without history support, reports use current-session counts only.]

## Skill Version(s):

2.6.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
