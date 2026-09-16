## Description:

ApiFlash (apiflash.com). Use this skill for ApiFlash screenshot capture, quota retrieval, and screenshot metadata requests through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate ApiFlash through an OOMOL-connected account, including capturing website screenshots, checking screenshot quota, and reading screenshot metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance includes remote installer commands that execute downloaded scripts directly.

Mitigation: Use a safer installation path where available, such as a signed or checksum-verified release, and run installer commands only after trusting OOMOL's delivery path.

Risk: Connector actions can interact with an ApiFlash account and should stay limited to user-requested ApiFlash work.

Mitigation: Inspect the live action schema before constructing payloads and confirm any state-changing action with the user before execution.

## Reference(s):

- [ApiFlash homepage](https://apiflash.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-apiflash)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId when actions are run with --json.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
