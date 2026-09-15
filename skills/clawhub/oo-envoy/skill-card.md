## Description:

Use Envoy through the OOMOL-connected oo CLI to read and manage employees, sign-in flows, invites, and locations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to operate Envoy account data through an OOMOL-connected account. It supports schema inspection and Envoy actions for employees, flows, invites, and locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Prefer a verified, pinned installer or official package path before installing the oo CLI.

Risk: Envoy actions can operate through connected account credentials, including actions tagged as write.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect before running any write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-envoy)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Envoy homepage](https://envoy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.2 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
