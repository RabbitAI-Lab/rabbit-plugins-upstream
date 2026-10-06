## Description:

Helps agents write natural Persian Telegram messages and check drafts for leftover Latin text and Western digits before sending.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ehsanghaffar](https://clawhub.ai/user/ehsanghaffar)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers preparing Telegram replies, notifications, reports, captions, and button labels use this skill to produce natural Persian text and review drafts before sending. An explicit request for another language takes precedence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Drafts checked from local files may leave sensitive message text on disk.

Mitigation: Use standard input where appropriate, and remove temporary draft files after review.

Risk: Approved terms and exempted spans may let unnecessary Latin text pass the ordinary check.

Mitigation: Review proposed terms before approval and run the final strict check with human review before sending.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ehsanghaffar/skills/telegram-persian-enforcer)
- [Server-resolved source repository](https://github.com/ehsanghaffar/skills/tree/main/skills/telegram-persian-enforcer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Persian Telegram message text, optionally with Telegram-compatible Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves code, links, and identifiers where necessary; does not translate incoming messages automatically.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
