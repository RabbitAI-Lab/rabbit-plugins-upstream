## Description:

ContentStudio helps agents schedule social-media posts, manage social inbox activity, and pull performance analytics across supported ContentStudio workspaces and social platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[contentstudio-official](https://clawhub.ai/user/contentstudio-official)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and social-media teams use this skill to operate ContentStudio from an agent, including workspace discovery, post scheduling, inbox triage, approvals, media management, reporting, and analytics. It is intended for authenticated ContentStudio accounts with an API key and an installed contentstudio CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a globally installed contentstudio CLI package that may not be pinned by default.

Mitigation: Install only from a trusted package source and pin or verify the CLI version before production use.

Risk: A ContentStudio API key can authorize posts, deletions, approvals, customer messages, and workspace or account changes.

Mitigation: Use a narrowly scoped API key where possible and confirm the active workspace before any mutating action.

Risk: Customer-facing replies and social posts can publish externally and may not be reversible on the provider side.

Mitigation: Require dry-run previews and explicit human approval before sending posts, deletions, approvals, share links, report schedules, or inbox replies.

Risk: Bulk delete or auto-approve workflows can make large account changes if run unattended.

Mitigation: Avoid unattended bulk mutations; enumerate targets, review the dry-run payloads, and approve the final operation deliberately.

## Reference(s):

- [ContentStudio API Guide](https://api.contentstudio.io/guide)
- [ContentStudio API Docs](https://api.contentstudio.io/api-docs)
- [contentstudio-cli on npm](https://www.npmjs.com/package/contentstudio-cli)
- [ContentStudio Website](https://contentstudio.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented command expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill expects JSON-mode CLI output for stable parsing and requires dry-run previews before mutating ContentStudio resources.]

## Skill Version(s):

1.4.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
