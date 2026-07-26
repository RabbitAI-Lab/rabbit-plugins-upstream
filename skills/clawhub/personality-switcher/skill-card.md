## Description: <br>
Create, manage, and switch persistent OpenClaw assistant personalities with backups, rollback safeguards, heartbeat restoration, and optional Telegram commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robb1010](https://clawhub.ai/user/robb1010) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External OpenClaw users and developers use this skill to maintain multiple assistant personality profiles and switch the active SOUL.md and IDENTITY.md across sessions. It is useful when a workspace needs persistent persona variants while preserving shared user context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Crafted personality names may allow delete, rename, or switch operations to affect files outside the intended personalities folder. <br>
Mitigation: Review the skill before installing and only use trusted, simple personality names until the scripts validate delete, rename, and switch inputs before resolving paths. <br>
Risk: The skill makes persistent changes to assistant identity files and exposes personality commands through Telegram when configured. <br>
Mitigation: Install only in workspaces where persistent identity changes and Telegram-accessible personality commands are acceptable. <br>


## Reference(s): <br>
- [Personality Template Guide](references/personality-template.md) <br>
- [Personality Switcher on ClawHub](https://clawhub.ai/robb1010/skills/personality-switcher) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown files, JSON command responses, shell commands, and configuration changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or updates OpenClaw personality files, state files, backups, heartbeat configuration, and Telegram command registrations.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
