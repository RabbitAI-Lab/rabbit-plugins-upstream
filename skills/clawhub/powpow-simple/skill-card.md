## Description:

帮助用户把照片或旅行素材写成游记并发布到 PowPow，或创建可聊天并展示在公开地图上的数字人。

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow 用户可用此技能起草和预览游记、发布照片帖子，或创建会聊天的地图数字人；需要 PowPow 账号和配套的 powpow-cli，发布等操作须由用户明确确认。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The companion CLI performs login, uploads, publishing, deletion, and digital-human creation.

Mitigation: Review powpow-cli separately and inspect the proposed action before explicitly confirming it.

Risk: Sharing a password in chat can expose account credentials.

Mitigation: Log in directly from your own terminal; never send your password to the agent.

Risk: Posts with locations and map-based digital humans are publicly visible.

Mitigation: Review the location and preview before confirming publication; omit a post location if you do not want it shown on the public map.

## Reference(s):

- [PowPow Simple ClawHub release](https://clawhub.ai/durenzidu/skills/powpow-simple)
- [PowPow website](https://global.powpow.online)
- [PowPow public map](https://global.powpow.online/map)
- [Security architecture](references/security.md)
- [Product screenshots](references/screenshots.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with draft text, previews, confirmation prompts, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can provide local post previews and links to published posts or map-based digital humans.]

## Skill Version(s):

1.0.5 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
