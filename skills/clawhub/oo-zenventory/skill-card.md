## Description:

Zenventory (zenventory.com). Use this skill for any Zenventory request, including reading, creating, updating, and deleting data through the OOMOL-connected Zenventory connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Zenventory connector schemas and run Zenventory inventory actions through the oo CLI. It supports list, get, create, and update item workflows while requiring confirmation before write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance can execute remote installer scripts for the oo CLI.

Mitigation: Review the installer source first and prefer a verified or package-managed oo CLI installation.

Risk: The skill can run state-changing Zenventory item operations.

Mitigation: Allow read-only list and get requests directly, but require a clear payload preview and explicit user approval before create_item or update_item.

## Reference(s):

- [Zenventory homepage](https://www.zenventory.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zenventory)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI connector commands that return JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
