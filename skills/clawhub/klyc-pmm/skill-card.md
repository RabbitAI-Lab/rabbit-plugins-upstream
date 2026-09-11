## Description:

KLYC-PMM gives AI agents persistent memory with one-command initialization, token-based recovery, automated distillation, semantic search, and encrypted remote backup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sylncn](https://clawhub.ai/user/sylncn)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to save, search, back up, and recover long-lived text memories for AI agents across restarts, workspace resets, and migrations. It also provides guidance and commands for optional paid service upgrades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create persistent watch or daemon behavior and sync sensitive local memory, identity, user, and tool files to a remote service.

Mitigation: Audit the exact file list and persistence behavior before using oneclick, setup, daemon, or watch modes; enable remote sync only for files you intend to share.

Risk: Recovery URLs and API keys can expose access to stored memories if copied into MEMORY.md, chat history, shell history, or logs.

Mitigation: Keep recovery URLs and API keys in a password manager or protected local config, remove exposed tokens from history, and rotate exposed credentials.

Risk: The authoritative security summary says the remote backup behavior is overbroad and inconsistent with some security claims.

Mitigation: Use the skill only if you are comfortable with the remote service receiving encrypted agent memory, and prefer local-only or separately audited encrypted backups for highly sensitive material.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sylncn/skills/klyc-pmm)
- [KLYC-PMM homepage](https://kunlunyaochi.com)
- [Security policy](SECURITY.md)
- [PMM full architecture](references/pmm-full-architecture.md)
- [Pay Skill packaging standard](references/pay-skill-spec.md)
- [SkillHub Pay Skill specification](https://skillhub.cn/skillpay)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose commands that call remote HTTPS APIs, manage local configuration files, and enable persistent watch behavior; review commands before execution.]

## Skill Version(s):

9.3.7 (source: server release, skill.json, and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
