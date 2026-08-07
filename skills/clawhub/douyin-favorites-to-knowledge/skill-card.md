## Description:

Synchronizes a user's authorized Douyin favorites, or explicitly selected likes, into a local Markdown or Obsidian knowledge base with optional transcription.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tars1230](https://clawhub.ai/user/tars1230)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to configure and run a local workflow that turns authorized Douyin favorites into searchable knowledge notes. It supports optional cloud or local transcription, Obsidian setup, Feishu notifications, and daily Markdown reports when the user's environment supports scheduling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create unattended daily synchronization jobs.

Mitigation: Confirm the knowledge directory, transcription provider, schedule, and disable path before enabling a scheduled task.

Risk: Advanced adapters can run arbitrary local Python modules.

Mitigation: Use only trusted adapters and keep secrets in environment variables or a secret manager.

Risk: Cloud ASR and Feishu options can send user-controlled content to external services.

Mitigation: Enable these integrations only when the user accepts the external data flow; otherwise use local transcription or no transcription.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tars1230/skills/douyin-favorites-to-knowledge)
- [Project Documentation](https://github.com/tars1230/douyin-favorites-to-knowledge)
- [Gitee Download Mirror](https://gitee.com/tars123/douyin-favorites-to-knowledge)
- [SiliconFlow Pricing](https://siliconflow.cn/pricing)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Files]

**Output Format:** [Markdown guidance with inline shell commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local Markdown or Obsidian notes and optional daily Markdown reports through the installed CLI.]

## Skill Version(s):

2.2.5 (source: pyproject.toml, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
