## Description:

Use this skill for Render (render.com) requests to read, create, update, and delete data through the OOMOL Render connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Render services, deploys, workspaces, and user profile information, and to manage Render service lifecycle actions through the oo CLI. It supports read operations directly and requires confirmation before write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill operates Render through OOMOL as an intermediary for the user's Render account.

Mitigation: Install and use it only when the user is comfortable authorizing OOMOL for the relevant Render account.

Risk: First-time setup includes remote shell installer commands for the oo CLI.

Mitigation: Review the installer source or use official/manual installation guidance before running remote installer commands.

Risk: Service lifecycle actions can restart, resume, trigger deploys, roll back deploys, or suspend Render services.

Mitigation: Require explicit user confirmation for the target, payload, and effect before write or destructive service actions.

## Reference(s):

- [Render homepage](https://render.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-render)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI Render connector and may return JSON responses with execution metadata.]

## Skill Version(s):

1.0.4 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
