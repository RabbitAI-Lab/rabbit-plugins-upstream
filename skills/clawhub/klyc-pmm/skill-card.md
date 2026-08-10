## Description:

KLYC-PMM is an AI-agent memory management skill that helps persist, search, synchronize, and recover text memories using local shell scripts and authenticated HTTPS communication with kunlunyaochi.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sylncn](https://clawhub.ai/user/sylncn)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and AI-agent operators use this skill to give agents durable, searchable text memory that can survive restarts, workspace resets, and migrations. It also supports paid upgrade flows for guarded memory and memory-clone features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected memory and identity files may contain sensitive information and can be sent to kunlunyaochi.com by the skill's sync flows.

Mitigation: Use the skill only in workspaces where those files have been reviewed and scrubbed of secrets, regulated data, private client data, and credentials.

Risk: The optional daemon can persistently monitor file changes and sync selected files after installation.

Mitigation: Prefer dry-run or manual setup, review the generated systemd user service, and enable persistent watch mode only after confirming the intended files and API endpoint.

Risk: The recovery URL functions like a credential for restoring memory.

Mitigation: Treat the recovery URL as a password and avoid placing it in MEMORY.md, repositories, chat logs, or other shared records.

Risk: Non-dry-run distillation can mark redundant or conflicting memory records as soft-deleted.

Mitigation: Run distillation in dry-run mode first and review proposed changes before allowing automatic memory cleanup.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sylncn/skills/klyc-pmm)
- [SKILL.md](artifact/SKILL.md)
- [Security Policy](artifact/SECURITY.md)
- [PMM Full Architecture](artifact/klyc-pmm-src/references/pmm-full-architecture.md)
- [Pay Skill Specification](artifact/klyc-pmm-src/references/pay-skill-spec.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples, configuration details, and JSON/API response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose commands that create local configuration, install a user service, and send selected memory files to a remote HTTPS API when executed.]

## Skill Version(s):

9.2.2 (source: server release metadata, SKILL.md frontmatter, skill.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
