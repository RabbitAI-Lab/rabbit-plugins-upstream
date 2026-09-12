## Description:

KLYC-PMM helps agents persist, recover, synchronize, search, and distill long-term memory through local shell commands and HTTPS APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sylncn](https://clawhub.ai/user/sylncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to initialize an agent memory store, back up selected text memory files, recover memory with a recovery token, synchronize watched files, and run optional DeepSeek-based distillation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload local memory, identity, user, agent-rule, and tool files to kunlunyaochi.com, and optional distillation can send memory contents to DeepSeek.

Mitigation: Install only if this data transfer is acceptable, review the configured watch targets, and use the DeepSeek option only with an intended user-provided key.

Risk: The one-click and daemon paths can create a persistent watcher that continuously syncs selected files.

Mitigation: Avoid the daemon path unless continuous monitoring is intended, review any systemd unit before enabling it, and stop or disable the watcher when it is no longer needed.

Risk: Recovery tokens and API keys protect memory access and can be exposed if placed in watched files or shell history.

Mitigation: Store recovery tokens outside watched files, do not put them in MEMORY.md, clear shell history after recovery commands, and rotate exposed tokens.

Risk: The authoritative security review flags misleading encryption and credential-handling guidance.

Mitigation: Treat remote sync as sensitive data transfer and review the scripts and service behavior before using private or regulated memory content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sylncn/skills/klyc-pmm)
- [Publisher profile](https://clawhub.ai/user/sylncn)
- [Kunlun Yaochi homepage](https://kunlunyaochi.com)
- [PMM full architecture](references/pmm-full-architecture.md)
- [Pay Skill packaging standard](references/pay-skill-spec.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON/API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local configuration, recovery output, memory reports, and watched text memory files when users run the scripts.]

## Skill Version(s):

9.3.12 (source: SKILL.md frontmatter, skill.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
