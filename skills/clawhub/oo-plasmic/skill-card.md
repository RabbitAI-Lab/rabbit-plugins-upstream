## Description:

Plasmic support for searching and reading CMS data through an OOMOL-connected Plasmic account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Plasmic connector schemas and run read-only CMS count and list operations through an OOMOL-connected Plasmic account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Verify the installer source and integrity independently before running installation commands.

Risk: Plasmic request parameters and returned CMS data are routed through OOMOL.

Mitigation: Use a least-privilege Plasmic account and install only if this data routing is acceptable.

Risk: Only count_items and list_items are reviewed read actions in the supplied evidence.

Mitigation: Require explicit user confirmation before running any other connector action, especially actions that write, delete, remove, or overwrite data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-plasmic)
- [Plasmic Homepage](https://www.plasmic.app)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL connector responses that include data and execution metadata.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
