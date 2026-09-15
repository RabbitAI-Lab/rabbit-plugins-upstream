## Description:

Xata (xata.io). Use this skill for searching and reading Xata organizations, projects, branches, branch details, and available deployment regions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Xata account resources through the OOMOL `oo` CLI without handling raw credentials directly. It supports read-oriented discovery of organizations, projects, branches, branch details, and available regions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to execute remote installer scripts directly in a shell.

Mitigation: Review the install path before installing and prefer a verified, pinned installer or package-manager flow when available.

Risk: Connector calls depend on a live OOMOL account connection and scoped Xata credentials.

Mitigation: Run setup only after an auth, connection, scope, credential, app, or billing error and avoid exposing raw credentials.

## Reference(s):

- [Xata homepage](https://xata.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-xata)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and execution metadata when actions are run.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
