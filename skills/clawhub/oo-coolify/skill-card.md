## Description:

Coolify support for reading, creating, updating, deleting, and deploying Coolify resources through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Coolify projects, applications, deployments, and application lifecycle actions from an agent through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger state-changing or destructive Coolify actions such as deployments, restarts, stops, cancellations, and resource pruning.

Mitigation: Require explicit user confirmation for deployments, restarts, stops, cancellations, and any destructive Coolify action before running the command.

Risk: The one-time oo CLI installer is a piped install command and the workflow depends on trusting OOMOL as a broker for the user's Coolify account.

Mitigation: Review the oo CLI installer before running it and install the skill only when OOMOL is trusted to broker the connected Coolify account.

## Reference(s):

- [ClawHub Coolify skill page](https://clawhub.ai/oomol/skills/oo-coolify)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Coolify homepage](https://coolify.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run oo CLI connector commands that return JSON data from Coolify.]

## Skill Version(s):

1.0.1 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
