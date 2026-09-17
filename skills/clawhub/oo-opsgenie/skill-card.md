## Description:

Opsgenie lets agents read, create, and update Opsgenie alerts through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to operate Opsgenie alerts from an agent, including creating, acknowledging, closing, fetching, listing, and checking asynchronous request status. The skill is intended for OOMOL-connected Opsgenie accounts and directs the agent to inspect live connector schemas before constructing payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change Opsgenie alert state, including acknowledge, close, and create workflows.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: The skill relies on an external oo CLI controlling a connected Opsgenie account.

Mitigation: Install and use the skill only when the OOMOL account connection and requested Opsgenie scope are trusted.

Risk: The setup guidance includes remote installer commands that execute downloaded scripts.

Mitigation: Prefer the install guide or independently verify the installer source before using pipe-to-shell commands.

## Reference(s):

- [ClawHub Opsgenie skill page](https://clawhub.ai/oomol/skills/oo-opsgenie)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [Opsgenie homepage](https://www.atlassian.com/software/opsgenie)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, PowerShell, JSON, and text snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas and JSON payloads for Opsgenie actions; command responses may include asynchronous execution IDs.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
