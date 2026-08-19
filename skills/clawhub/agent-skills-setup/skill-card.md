## Description:

Use when a user names two supported IDEs or agent products to plan, migrate, or inspect specific skills, instructions, and MCP; the skill inventories local paths and runs bundled Bash/Python, while approved apply or rollback may write targets, create backups/manifests, verify results, and scan or redact secrets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckycat133](https://clawhub.ai/user/luckycat133)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect, plan, and execute reviewed migrations of agent skills, instructions, MCP entries, and related portable configuration between supported IDE and agent products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Migration apply or rollback can write local target configuration files when explicitly approved.

Mitigation: Use migration commands only for explicitly named source and target products, save and inspect the plan before approval, and apply only the reviewed plan.

Risk: The artifact claims no network access while bundling a documentation freshness script with an online-fetch mode.

Mitigation: Avoid running documentation freshness checks with --online unless outbound network access is intentionally permitted.

Risk: Portable configuration migration can accidentally include credentials or private runtime state if boundaries are ignored.

Mitigation: Rely on the skill's allowlisted object handling, secret scanning, redaction, and explicit exclusions for OAuth/session state, runtime metadata, approval grants, chat history, and generated memory.

## Reference(s):

- [IDE Reference Index](references/ide-registry.md)
- [Registry v2](references/registry-v2.json)
- [Migration Safety and Conflicts](references/migration-safety.md)
- [MCP Migration](references/mcp-migration.md)
- [File-Backed Object Migration](references/object-migration.md)
- [Verification and Evidence](references/verification.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON plan, manifest, or bundle outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Approved apply and rollback flows may create backups, manifests, reviewed plans, and portable bundle artifacts; secret-bearing runtime state is excluded.]

## Skill Version(s):

0.8.23 (source: frontmatter metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
