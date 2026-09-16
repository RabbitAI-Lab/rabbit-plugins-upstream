## Description:

Screendesk enables agents to read, list, search, and update Screendesk recordings and workspace users through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with Screendesk recordings, transcripts, and workspace users from an OOMOL-connected account. It supports read actions and guarded updates to recording titles, summaries, and descriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can execute remote installer scripts without an included checksum or signature verification step.

Mitigation: Review the installer path before use and prefer signed, versioned, or checksum-verified installation methods.

Risk: The update_recording action changes Screendesk recording metadata.

Mitigation: Require explicit user confirmation of the exact recording and payload before running any update action.

## Reference(s):

- [Screendesk homepage](https://screendesk.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-screendesk)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schemas before action execution and returns connector responses as JSON when commands are run.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
