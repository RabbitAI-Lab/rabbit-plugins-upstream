## Description:

Shotstack helps agents operate Shotstack through an OOMOL-connected account to check render status and submit asynchronous video, image, or audio render jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage Shotstack render workflows through the oo CLI, including checking render status, retrieving output URLs, and submitting edit payloads after confirming write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes shell commands that pipe downloaded installer scripts directly into Bash or PowerShell.

Mitigation: Review the install step first and prefer a trusted, verifiable oo CLI release path before running installer commands.

Risk: Submitting a Shotstack render edit can create account activity or costs.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions such as render_edit.

Risk: Connector action contracts may change over time.

Mitigation: Inspect the live Shotstack connector schema before building each action payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-shotstack)
- [Shotstack Homepage](https://shotstack.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before building action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
