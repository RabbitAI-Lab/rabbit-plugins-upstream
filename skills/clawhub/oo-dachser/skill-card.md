## Description:

DACHSER (dachser.com). Use this skill for DACHSER requests that read, create, or update data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to operate DACHSER shipment and delivery-order workflows through the OOMOL oo CLI. It helps agents inspect live action schemas, run connector actions, retrieve shipment status and history, and request confirmation before write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that directly execute downloaded scripts.

Mitigation: Review official installation instructions, verify the source before running installers, and prefer an audited installation path where required.

Risk: Some DACHSER actions may change state or have operational effects.

Mitigation: Inspect the live action schema first and require explicit user confirmation for actions tagged as write or destructive.

## Reference(s):

- [ClawHub DACHSER skill page](https://clawhub.ai/oomol/skills/oo-dachser)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [DACHSER homepage](https://www.dachser.com/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, OOMOL sign-in, and a connected DACHSER account; connector responses are JSON with data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
