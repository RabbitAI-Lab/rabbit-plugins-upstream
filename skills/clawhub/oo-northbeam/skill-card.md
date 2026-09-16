## Description:

Provides agent guidance for using the OOMOL-connected Northbeam connector to inspect schemas and read Northbeam attribution, breakdown, metric, and spend data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to let an agent query Northbeam through the OOMOL-connected oo CLI for attribution models, breakdowns, metrics, daily spend, and hourly spend.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can execute remote installer scripts that modify the user's machine.

Mitigation: Install the oo CLI only through a trusted source and verification process, and require explicit user approval before running installer commands.

Risk: The connector depends on server-side credentials and an active Northbeam connection through OOMOL.

Mitigation: Use the documented setup flow only after an auth or connection failure, and avoid handling raw Northbeam API tokens in the agent session.

## Reference(s):

- [Northbeam ClawHub skill page](https://clawhub.ai/oomol/skills/oo-northbeam)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Northbeam homepage](https://www.northbeam.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector responses as JSON when actions are executed with --json.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
