## Description:

Intuiface helps an agent operate Intuiface through an OOMOL-connected account, including listing available running experiences and sending Web Trigger messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate connected Intuiface experiences through the OOMOL oo CLI, inspect action schemas, list running experiences, and send Web Trigger messages when authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include remote installer commands that run scripts directly in a shell.

Mitigation: Review setup commands before installing; prefer verified, version-pinned installation methods or official documentation, and do not run remote installers automatically.

Risk: The send_message action can change Intuiface state by sending Web Trigger messages to running experiences.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Intuiface ClawHub skill page](https://clawhub.ai/oomol/skills/oo-intuiface)
- [Intuiface homepage](https://www.intuiface.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action payload construction; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
