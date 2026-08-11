## Description:

klyc-pmm helps agents initialize, back up, watch, search, recover, and distill long-term text memory through authenticated HTTPS calls to kunlunyaochi.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sylncn](https://clawhub.ai/user/sylncn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to give an agent persistent text memory: initialize an identity, push and search memories, recover from a token URL, and optionally enable file watching, distillation, and payment-backed service tiers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected local memory and identity files to kunlunyaochi.com for backup and synchronization.

Mitigation: Install only if the user trusts kunlunyaochi.com with the selected files, and review the watched file list before enabling daemon or watch mode.

Risk: The skill can install persistent file watchers and a systemd user service.

Mitigation: Review the generated service unit and keep daemon mode disabled unless continuous synchronization is intended.

Risk: The recovery token is a sensitive credential for restoring memory.

Mitigation: Keep the recovery token out of public repositories and shared logs, and store it in a private password manager or equivalent secret store.

Risk: The package includes server and database administration scripts that are broader than a normal memory client.

Mitigation: Avoid running server or admin scripts on ordinary workstations, and use pmm_distill.sh --dry-run before any distillation operation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sylncn/skills/klyc-pmm)
- [PMM full architecture](references/pmm-full-architecture.md)
- [Pay Skill packaging standard](references/pay-skill-spec.md)
- [Examples](examples/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated local configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local memory, identity, configuration, backup, service, and watch-state files when invoked by the user.]

## Skill Version(s):

9.2.4 (source: evidence.release.version, SKILL.md frontmatter, skill.json, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
