## Description:

This skill operates Eden AI through an OOMOL-connected account, including non-streaming chat completions and model listing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Eden AI action schemas, run Eden AI connector actions, create non-streaming chat completions, and list available models through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions may run downloaded installer scripts for the oo CLI before the tool is available.

Mitigation: Review the installer path first and prefer a trusted, versioned, verifiable oo CLI release channel before installation.

Risk: Chat-completion payloads are sent through OOMOL and Eden AI and may consume account credits.

Mitigation: Confirm the exact payload and expected effect before running write-tagged actions, and avoid sending sensitive content unless the user approves.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-edenai)
- [Eden AI homepage](https://www.edenai.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
