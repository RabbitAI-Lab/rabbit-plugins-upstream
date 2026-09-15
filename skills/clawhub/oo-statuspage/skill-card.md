## Description:

Operates Atlassian Statuspage through OOMOL's oo CLI for reading pages, components, incidents, events, and automation emails and for creating, updating, or deleting components and incidents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support engineers use this skill to inspect and manage Statuspage pages, components, incidents, events, and automation email settings through an OOMOL-connected Statuspage account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands create avoidable supply-chain risk if executed blindly.

Mitigation: Prefer official installation documentation, pinned packages, and checksum or signature verification before installing the oo CLI.

Risk: Write and destructive actions can create, update, or delete Statuspage resources.

Mitigation: Inspect the live connector schema, confirm exact payloads and targets with the user, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Statuspage skill page](https://clawhub.ai/oomol/skills/oo-statuspage)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Atlassian Statuspage](https://www.atlassian.com/software/statuspage)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
