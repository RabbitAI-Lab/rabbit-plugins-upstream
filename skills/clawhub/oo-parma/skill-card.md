## Description:

Parma lets an agent read, create, update, and delete data in a connected Parma workspace through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and agents connected to Parma use this skill to inspect workspace records and, with explicit confirmation, create or update relationships, notes, and group assignments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on a connected Parma workspace through broad oo CLI authority.

Mitigation: Install only for workspaces where this level of access is acceptable and confirm the exact payload and effect before create, update, or delete actions.

Risk: The skill includes one-line remote installer commands for the oo CLI.

Mitigation: Prefer a verified, versioned installation path for the oo CLI instead of running the remote installer as written.

## Reference(s):

- [Parma homepage](https://parma.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-parma)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Parma connector calls that return JSON responses through the oo CLI.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
