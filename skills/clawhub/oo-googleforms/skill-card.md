## Description:

Enables agents to read, create, and update Google Forms through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external users use this skill to inspect Google Forms structure and responses, create forms, update form content, and manage publish settings through connected OOMOL credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer scripts that could execute unreviewed code if run directly.

Mitigation: Review the oo CLI installation process first and prefer official, verifiable installation steps that download, inspect, and validate the installer before execution.

Risk: Write actions can create forms, apply batch updates, change publish settings, or otherwise alter Google Forms state.

Mitigation: Confirm the exact payload, target form, and expected effect with the user before running any write action.

Risk: The skill operates through an OOMOL-connected Google Forms account and can act with the permissions granted to that connection.

Mitigation: Use the skill only for intended Google Forms tasks and reconnect or expand scopes only when an auth or scope error proves it is necessary.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-googleforms)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Google Forms](https://workspace.google.com/products/forms/)
- [OOMOL Google Forms Connection](https://console.oomol.com/app-connections?provider=googleforms)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the googleforms connector through the oo CLI and may return JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: evidence.release.version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
