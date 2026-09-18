## Description:

TheirStack (theirstack.com). Use this skill for searching and reading TheirStack data through the OOMOL `oo` CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect TheirStack action schemas and run read-oriented company, job, technographic, and credit-balance queries through an OOMOL-connected TheirStack account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in setup instructions can execute downloaded code on the user's machine.

Mitigation: Install the OOMOL CLI from official, verifiable releases or a trusted package manager, and review setup commands before execution.

Risk: The skill queries TheirStack data through the user's OOMOL-connected TheirStack account.

Mitigation: Confirm the account connection and requested query scope before running connector actions that access account data.

## Reference(s):

- [TheirStack homepage](https://theirstack.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-theirstack)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return TheirStack connector responses as JSON from the `oo` CLI.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
