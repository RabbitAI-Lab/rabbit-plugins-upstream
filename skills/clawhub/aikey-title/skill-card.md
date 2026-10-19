## Description:

Creates platform-specific video titles, cover text, and post descriptions that fit the creator's content and stage of production.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Independent content creators use this skill to draft and compare titles, cover wording, and post descriptions for Douyin, WeChat Channels, and Xiaohongshu. It checks proposed claims against the supplied content and explains why each title fits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read local reference rules and save title preferences or performance feedback for later sessions.

Mitigation: Review the local rules and memory folder before use; disable or avoid memory writes if cross-session personalization is unwanted.

Risk: A compelling title may promise something the finished video does not contain.

Mitigation: Compare selected titles and cover text with the actual footage or transcript before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/iamzifei/skills/aikey-title)
- [Production-stage guidance](artifact/references/拍摄进度分档.md)
- [Title structure reference](artifact/references/标题结构库.md)
- [Writing and review rules](artifact/references/规则卡.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with platform-specific candidate tables and selected recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [For each requested platform, proposes five titles and five cover-text options, selects a preferred option, and drafts one post description; does not design cover images.]

## Skill Version(s):

0.3.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
