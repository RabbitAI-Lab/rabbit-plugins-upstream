## Description:

Wire2Air enables an agent to list inbound SMS and MMS messages and send single or bulk SMS messages through an OOMOL-connected Wire2Air account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when an agent needs to work with Wire2Air messaging workflows, including reading inbound inbox messages and queuing outbound SMS messages. Write actions should be confirmed with the user before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that could execute unverified code.

Mitigation: Review the setup path before installing and independently verify the installer source before running remote installer commands.

Risk: The send_message action can queue outbound SMS messages and may affect users or incur cost.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [Wire2Air skill page](https://clawhub.ai/oomol/skills/oo-wire2air)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Wire2Air homepage](https://www.wire2air.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI schema-inspection commands, connector execution commands, and user-confirmation guidance for write actions.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
