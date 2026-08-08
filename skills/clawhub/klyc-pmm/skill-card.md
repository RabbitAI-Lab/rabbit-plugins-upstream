## Description:

KLYC-PMM is an AI-agent memory management skill for encrypted memory backup, search, recovery, file watching, and paid service upgrades through HTTPS APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sylncn](https://clawhub.ai/user/sylncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to give AI agents persistent, searchable memory across restarts, workspace resets, and migrations. It is intended for workflows where the user deliberately wants agent memory and identity files synchronized with the Kunlun Yaochi service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for persistent access to sensitive agent memory and identity files.

Mitigation: Review the watched file list before enabling watch or daemon mode, and keep MEMORY.md and related identity files out of version control.

Risk: The skill sends memory contents and recovery credentials to kunlunyaochi.com.

Mitigation: Install it only when that external storage and processing is intended, and treat the recovery URL as a password.

Risk: Use in workspaces containing secrets or regulated data could expose sensitive material through memory synchronization.

Mitigation: Avoid using the skill in those workspaces unless separate approval, controls, and data-handling review are in place.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sylncn/skills/klyc-pmm)
- [README](artifact/README.md)
- [Security Policy](artifact/SECURITY.md)
- [Skill Guide](artifact/SKILL.md)
- [PMM Full Architecture](artifact/klyc-pmm-src/references/pmm-full-architecture.md)
- [Pay Skill Specification](artifact/klyc-pmm-src/references/pay-skill-spec.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local memory, identity, configuration, backup, and daemon-related files when the user runs the bundled scripts.]

## Skill Version(s):

9.2.1 (source: evidence release, SKILL.md frontmatter, skill.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
