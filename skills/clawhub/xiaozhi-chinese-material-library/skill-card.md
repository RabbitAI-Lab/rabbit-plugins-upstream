## Description:

Helps Chinese-language students save and tag writing material, retrieve it by theme, and review confirmed usage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-language primary and middle-school students use this skill to collect and retrieve quotations, passages, and their own sentences for writing. Primary students use it with a guardian or teacher present.

### Deployment Geography for Use:

Mainland China by default; localize safety contacts and consent rules for other regions.

## Known Risks and Mitigations:

Risk: Student-provided writing material may be retained or shared beyond the current conversation.

Mitigation: Confirm consent before saving or sharing; honor pause, deletion, and sharing controls, and limit cross-skill sharing to confirmed usage counts.

Risk: Mainland China emergency contacts and consent defaults may be inappropriate elsewhere or for younger students.

Mitigation: Localize emergency contacts and consent requirements before deployment outside mainland China, and arrange guardian or teacher supervision for primary students.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-material-library)
- [Privacy and platform conventions](artifact/shared/platform-conventions.md)
- [Crisis referral guidance](artifact/shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text and Markdown lists or summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tagged material suggestions, themed retrieval, text export, and on-request usage summaries; historical summaries require persistent memory and statistics.]

## Skill Version(s):

2.7.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
