## Description:

Mendeley connector for reading, creating, updating, and deleting documents through the OOMOL oo CLI, with live schema inspection before requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected Mendeley account from an agent, including catalog search, document lookup, library listing, metadata creation, metadata updates, and document deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer pipe commands that execute downloaded scripts directly.

Mitigation: Review and independently verify the OOMOL installer source before running installer commands; prefer inspecting the downloaded script or following the install guide manually.

Risk: Write and destructive actions can modify or permanently delete documents in the user's Mendeley library.

Mitigation: Confirm the exact action, target document, payload, and expected effect with the user before running write or destructive commands.

## Reference(s):

- [Mendeley homepage](https://www.mendeley.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mendeley)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include oo CLI commands and JSON connector payloads; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
