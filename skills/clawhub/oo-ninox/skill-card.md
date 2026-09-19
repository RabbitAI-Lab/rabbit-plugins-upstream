## Description:

This skill helps agents read, create, update, and delete Ninox data through the OOMOL-connected `oo` CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Ninox action schemas and operate Ninox workspaces, databases, tables, and records through an OOMOL-connected account. It supports read operations directly and requires explicit user confirmation before write or destructive record operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands piped into shell interpreters, and evidence.security flags this for review before installation.

Mitigation: Inspect or independently verify OOMOL installer paths before running `curl | bash` or `irm | iex`; use trusted installation channels when available.

Risk: Ninox write and destructive actions can create, update, or delete records.

Mitigation: Confirm the exact payload, target workspace, database, table, record IDs, and intended effect with the user before write or delete operations.

## Reference(s):

- [Ninox homepage](https://ninox.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ninox)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before constructing Ninox action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
