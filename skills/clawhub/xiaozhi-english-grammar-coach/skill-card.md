## Description:

A Chinese K12 English grammar coaching skill that helps students identify grammar errors through guided questions and, with consent, track recurring grammar weaknesses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese K12 learners use this skill to practice English grammar through Socratic questioning, focused correction, and targeted drills. The skill can optionally record recurring grammar weaknesses and progress signals when the student or guardian has granted the required consent.

### Deployment Geography for Use:

China mainland by default; other regions require localized crisis-support channels, curriculum alignment, and minor-consent review before student-facing use.

## Known Risks and Mitigations:

Risk: The skill may handle student data, recurring learning weaknesses, and minor consent choices.

Mitigation: Enable profile, reminder, parent-sharing, and cross-skill sharing features only after the student or guardian has granted the required consent.

Risk: The bundled safety guidance and crisis-support numbers are designed for China mainland and may be inappropriate elsewhere.

Mitigation: Before deployment outside China mainland, localize crisis-support channels, curriculum assumptions, and minor-consent rules.

Risk: Cross-session statistics or progress reports can be misleading when persistent memory or statistics capabilities are unavailable.

Mitigation: Use only current-session counts or explicitly labeled limited-evidence summaries unless the platform provides the required memory and statistics capabilities.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-grammar-coach)
- [English error dimension table](artifact/references/english-error-dimension-table.md)
- [Grammar patterns](artifact/references/grammar-patterns.md)
- [Platform conventions](artifact/shared/platform-conventions.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [Hint ladder](artifact/shared/hint-ladder.md)
- [Shared vocabulary and consent model](artifact/shared/vocab.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown or conversational text with optional structured profile update payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are consent-gated for long-term records and should mark limited evidence when only session-local counts are available.]

## Skill Version(s):

2.1.12 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
