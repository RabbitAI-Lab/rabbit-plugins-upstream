## Description:

Use Polar through an OOMOL-connected account to read, create, and update Polar data via the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with Polar customers, orders, organizations, products, and subscriptions through an OOMOL-connected Polar account. The skill is intended for agent workflows that inspect the live connector schema before running read, write, or destructive Polar actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup recommends running remote installer scripts directly.

Mitigation: Independently verify the installer source and integrity before running curl | bash or irm | iex commands.

Risk: Write or destructive Polar actions can change or remove Polar data if the payload is wrong.

Mitigation: Inspect the live action schema and confirm the exact payload and intended effect before execution.

Risk: The skill depends on an OOMOL account connected to Polar.

Mitigation: Confirm the OOMOL account, Polar connection, required scopes, and billing status before retrying failed connector actions.

## Reference(s):

- [Polar homepage](https://polar.sh)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-polar)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and may return JSON connector responses containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
