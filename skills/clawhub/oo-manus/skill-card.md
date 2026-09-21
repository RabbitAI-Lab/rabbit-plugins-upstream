## Description:

Manus lets an agent operate Manus through an OOMOL-connected account using the oo CLI, including task, project, connector, skill, browser client, and custom-agent actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Manus tasks and related account resources from an agent session through OOMOL's connected Manus service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include shell commands that execute remotely downloaded installer scripts.

Mitigation: Do not let an agent run the remote installer automatically; use a verified package-manager install or manually download, inspect, and verify the oo CLI installer before executing it.

Risk: The skill exposes write and destructive Manus actions that can change or delete account data.

Mitigation: Require explicit user confirmation of the target payload and expected effect before running write or destructive actions.

## Reference(s):

- [ClawHub Manus Skill](https://clawhub.ai/oomol/skills/oo-manus)
- [Manus Homepage](https://manus.im)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, OOMOL authentication, and a connected Manus account.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
