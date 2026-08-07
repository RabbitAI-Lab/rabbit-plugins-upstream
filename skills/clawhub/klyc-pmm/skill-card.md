## Description:

KLYC-PMM is an AI-agent memory management skill that uses shell workflows and HTTPS APIs to initialize, persist, search, recover, distill, and optionally upgrade encrypted text memories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sylncn](https://clawhub.ai/user/sylncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent operators use this skill to give agents persistent, searchable text memory across restarts, workspace resets, migrations, and multi-agent workflows. It supports backup and recovery, local and cloud search, file watching, memory distillation, and optional paid memory services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may continuously read selected workspace files and upload their contents to kunlunyaochi.com when file watching is enabled.

Mitigation: Review the watched file list and generated systemd user service before enabling persistent monitoring.

Risk: The recovery URL is sensitive and can be used to recover memory data.

Mitigation: Treat the recovery URL as a password; do not commit MEMORY.md and do not share the URL with untrusted assistants.

Risk: Local files under ~/.klyc-pmm and recovery_result.json may contain sensitive configuration or recovered data.

Mitigation: Keep those files private and review them for sensitive content before sharing logs, archives, or workspaces.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sylncn/skills/klyc-pmm)
- [README](artifact/README.md)
- [Security Policy](artifact/SECURITY.md)
- [PMM full architecture](artifact/klyc-pmm/references/pmm-full-architecture.md)
- [Pay Skill spec](artifact/klyc-pmm/references/pay-skill-spec.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, JSON]

**Output Format:** [Markdown guidance with bash command examples, configuration notes, and JSON/API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local configuration files, MEMORY.md content, systemd user service files, and recovery_result.json during use.]

## Skill Version(s):

9.1.22 (source: server release evidence, SKILL.md frontmatter, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
