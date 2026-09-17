## Description:

Miro (miro.com). Use this skill for ANY Miro request: reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to inspect Miro action schemas and operate boards, items, connectors, shapes, sticky notes, and text through the OOMOL oo CLI. It supports read, create, update, and explicitly confirmed delete workflows for users with a connected Miro account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run remote install scripts for the oo CLI.

Mitigation: Review setup before installation and prefer a pinned, verifiable oo CLI release or official package source.

Risk: Miro write and destructive actions can change or delete board content.

Mitigation: Confirm the exact payload and effect before write actions, and require explicit approval before destructive actions.

Risk: OOMOL processes request payloads, responses, and authorized Miro operations for connected accounts.

Mitigation: Connect Miro through OOMOL only when that processing model is acceptable for the user's data and workspace.

## Reference(s):

- [Miro homepage](https://miro.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-miro)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI connector commands that return JSON responses from Miro actions.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
