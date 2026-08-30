## Description:

Operate a connected mymind account through OOMOL for reading, creating, updating, organizing, searching, and deleting mymind data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate their connected mymind account through the oo CLI. It supports object retrieval, search, URL saving, notes, tags, spaces, pins, links, restoration, and soft deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write and destructive actions can change or remove mymind objects, tags, notes, spaces, pins, and links.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write actions, and require explicit approval before destructive actions.

Risk: The skill operates a user's mymind account through an OOMOL-connected account.

Mitigation: Install and use it only when the user intends the agent to operate that connected account; review proposed write or delete payloads before approval.

Risk: Connector schemas and available fields may change over time.

Mitigation: Fetch the live action schema with `oo connector schema` before building each payload.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [mymind](https://mymind.com)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mymind)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
