## Description:

Sync a user's Bilibili/B站, Xiaohongshu/小红书/RedNote, and Douyin/抖音 favorites into local Markdown/Obsidian with local ASR/OCR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dvlin-dev](https://clawhub.ai/user/dvlin-dev)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to back up, migrate, and organize their own authorized Bilibili, Xiaohongshu/RedNote, and Douyin favorites into a local Markdown or Obsidian vault.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires a dedicated authenticated browser profile for supported platforms.

Mitigation: Use only user-authorized accounts and let platform QR, captcha, login, account, or device-confirmation prompts be completed by the user.

Risk: Optional text enrichment can send allowlisted text to a configured OpenAI-compatible provider.

Mitigation: Keep enrichment disabled unless explicitly requested, and confirm provider configuration before enabling it.

Risk: Optional scheduler configuration can repeatedly run archive commands.

Mitigation: Complete a manual doctor, login, collection listing, sync, and report first, then review scheduler configuration before enabling it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dvlin-dev/skills/social-media-favorites-archiver)
- [Project Homepage](https://github.com/dvlin-dev/social-media-favorites-archiver)
- [Configuration](references/configuration.md)
- [Bilibili](references/platform-bilibili.md)
- [Xiaohongshu / RedNote](references/platform-xiaohongshu.md)
- [Douyin](references/platform-douyin.md)
- [Troubleshooting and Scheduling](references/troubleshooting.md)
- [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON status/report interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides local archiving workflows and sanitized aggregate reporting; optional enrichment is disabled unless explicitly enabled.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
