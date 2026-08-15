## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to run multi-round code review, targeted fixes, project onboarding, validation, and iteration workflows across supported AI coding assistants. It can operate in a normal edit-and-validate mode or a read-only review-only/dry-run mode for audits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Normal mode can edit project files and run configured validation commands.

Mitigation: Use review-only or dry-run for read-only audits, and review iterate.config.yaml validation.commands before normal mode.

Risk: Automated git merge or push can publish changes if enabled.

Mitigation: Leave auto_merge and push_per_round disabled unless automated publishing is intentional, then review results before merging or pushing.

Risk: Project context may expose secrets if users place sensitive information in generated or hand-written skill context files.

Mitigation: Keep secrets out of ITERATE.md and SKILL.md, and rely on the documented sensitive-file exclusions for .env files, keys, certificates, and credential stores.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [npm Installer Package](https://www.npmjs.com/package/iterate-skill-installer)
- [ModelScope Skill Page](https://www.modelscope.cn/skills/jingzhao0/iterate-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and guidance with code edits, shell commands, and configuration files depending on mode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal mode may modify files and run configured validation commands; review-only/dry-run mode emits read-only audit reports.]

## Skill Version(s):

2.3.7 (source: frontmatter and pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
