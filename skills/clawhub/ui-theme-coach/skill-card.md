## Description:

引导式 UI 主题设计顾问：通过问答引导帮用户定制任意风格的 OpenClaw Control UI 主题（像素/赛博朋克/卡通/极简/暗色科技等），含主色派生调色板、双保险注入、升级自愈（cron+快照）与反馈学习循环。

This skill is ready for commercial/non-commercial use.

## Publisher:

[hanhan1137](https://clawhub.ai/user/hanhan1137)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to design, generate, inject, validate, and maintain custom OpenClaw Control UI themes. It guides style discovery, palette generation, accessibility checks, local UI modification, upgrade recovery, and preference feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify local OpenClaw Control UI files.

Mitigation: Review proposed file changes before applying them, keep backups of dist/control-ui/index.html, and run the documented syntax and visual validation checks.

Risk: The daily cron self-healing job can repeatedly reapply UI modifications after upgrades.

Mitigation: Confirm the cron entry before installation, verify the snapshot location, and document the uninstall command and crontab removal step before use.

Risk: The skill may store user theme preferences in data/feedback.json.

Mitigation: Confirm local feedback storage is acceptable and clear data/feedback.json when preferences should not persist.

## Reference(s):

- [MC Pixel Style Worked Example](references/minecraft-example.md)
- [Pixel/Game Style](references/styles/pixel-game.md)
- [Cyberpunk Style](references/styles/cyberpunk.md)
- [Cartoon/Cute Style](references/styles/cartoon-cute.md)
- [Minimal/Modern Style](references/styles/minimal-modern.md)
- [Dark Tech Style](references/styles/dark-tech.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with CSS, HTML, JavaScript, JSON, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local theme files, design tokens, palette values, validation commands, and instructions for backups, cron self-healing, and feedback storage.]

## Skill Version(s):

1.3.0 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
