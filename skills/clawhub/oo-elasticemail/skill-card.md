## Description:

Elastic Email (elasticemail.com). Use this skill for ANY Elastic Email request: reading, creating, updating, and deleting data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Elastic Email contacts, contact lists, and list membership through an OOMOL-connected account. It supports read, write, and destructive workflows while directing agents to inspect live action schemas before constructing payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes direct remote installer commands executed in a shell.

Mitigation: Review the official installer documentation first, prefer a trusted package manager or signed release when available, and avoid pipe-to-shell execution unless the source has been verified and the local execution risk is acceptable.

Risk: The skill can run write and destructive Elastic Email actions that modify or remove contacts and lists.

Mitigation: Confirm the exact payload, target, and expected effect with the user before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [Elastic Email homepage](https://elasticemail.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-elasticemail)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect connector schemas and run Elastic Email actions with JSON payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
