## Description:

Helps an agent operate Discord through an OOMOL-connected account using the oo CLI, including reading account-related data and performing clearly marked write or destructive actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to interact with Discord via OOMOL-managed credentials, inspect connector schemas, run supported Discord actions, and handle first-time setup only when authentication or connection errors require it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Discord account-related data through an OOMOL-connected account.

Mitigation: Install only after confirming that this account connection and data access are acceptable for the intended environment.

Risk: First-time setup includes remote installer commands that pipe scripts into a shell.

Mitigation: Manually review and install the oo CLI through a trusted, verifiable method instead of allowing an agent to run remote installer commands.

Risk: Some actions can write to or delete Discord application role-connection data.

Mitigation: Require explicit user approval and confirm the exact payload and target before any action marked write or destructive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-discord)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Discord](https://discord.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.5 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
