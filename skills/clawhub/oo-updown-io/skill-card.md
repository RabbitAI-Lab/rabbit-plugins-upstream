## Description:

Enables agents to manage updown.io monitoring checks and node information through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect, create, update, and delete updown.io monitoring checks, list monitoring nodes and IP addresses, and handle setup or account-connection errors through OOMOL's oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote shell and PowerShell installer commands.

Mitigation: Review official install documentation and verify installer provenance before running installation commands.

Risk: Create, update, and delete actions can change or remove updown.io monitoring data.

Mitigation: Confirm the target, payload, and expected effect with the user before executing write or destructive actions.

Risk: The skill operates against a connected updown.io account through OOMOL's oo CLI.

Mitigation: Install and use it only when comfortable with OOMOL account-mediated access and the connected account scopes.

## Reference(s):

- [updown.io homepage](https://updown.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are expected to call the OOMOL oo CLI and may return JSON responses from the connector.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
