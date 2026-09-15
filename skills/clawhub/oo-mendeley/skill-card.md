## Description:

Mendeley (mendeley.com). Use this skill for ANY Mendeley request - reading, creating, updating, and deleting data. Whenever a task involves Mendeley, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected Mendeley account through the OOMOL oo CLI for document creation, retrieval, listing, catalog search, metadata updates, and deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that could execute unverified shell or PowerShell scripts.

Mitigation: Review the OOMOL CLI installation method first, prefer an official package manager or pinned installer with checksum or signature verification, and do not let an agent run the remote installer automatically.

Risk: Write and destructive Mendeley actions can change or delete library records.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running create, update, or delete actions.

## Reference(s):

- [Mendeley homepage](https://www.mendeley.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mendeley)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use live action-schema inspection and return connector responses containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: artifact metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
