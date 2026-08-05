## Description:

KLYC-PMM is a cloud-backed AI agent memory management skill for initializing an identity, saving and searching memories, recovering from a recovery URL, running watch and distillation workflows, and handling paid upgrades through X402 WeChat Pay.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sylncn](https://clawhub.ai/user/sylncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, AI-agent operators, and external users use this skill to persist, search, distill, and recover agent memories across restarts or workspace migrations. It is intended for environments where cloud-backed memory storage is acceptable and the operator can review watched files before enabling automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Watch mode and cloud memory operations can upload sensitive workspace memory files to the service.

Mitigation: Install only when cloud-backed memory is intended, review watched paths before enabling watch mode, and run dry-run or local checks before distillation.

Risk: One-click installation and daemon scripts can install persistent user services.

Mitigation: Review the exact service file before running oneclick or install-daemon, and run the skill as a non-root user where possible.

Risk: Recovery URLs and local credentials can expose memory recovery paths if stored in synced files.

Mitigation: Keep recovery URLs out of MEMORY.md and other synced files, protect local config files, and rotate tokens when exposure is suspected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sylncn/skills/klyc-pmm)
- [Security Policy](artifact/SECURITY.md)
- [PMM Full Architecture](artifact/klyc-pmm/references/pmm-full-architecture.md)
- [Pay Skill Packaging Standard](artifact/klyc-pmm/references/pay-skill-spec.md)
- [SkillHub Pay Skill Reference](https://skillhub.cn/skillpay)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated local configuration files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local KLYC-PMM configuration files and user-level service files when installation or daemon commands are run.]

## Skill Version(s):

9.1.14 (source: frontmatter, changelog, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
