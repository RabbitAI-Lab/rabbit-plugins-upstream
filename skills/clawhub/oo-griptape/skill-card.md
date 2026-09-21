## Description:

Use this skill to operate Griptape through an OOMOL-connected account for reading, creating, updating, and deleting Griptape Cloud data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Griptape Cloud assistants, runs, organizations, and related account resources through the OOMOL `oo` CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote shell installers for the `oo` CLI.

Mitigation: Review installer contents or use official package instructions before running installation commands.

Risk: Create, update, cancel, and delete actions can change Griptape resources accessible to the connected account.

Mitigation: Confirm the exact target, payload, and expected effect with the user before approving state-changing actions.

Risk: The skill depends on OOMOL as the CLI and credential broker for the user's Griptape account.

Mitigation: Install and use the skill only when the user trusts OOMOL to broker Griptape access.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-griptape)
- [Griptape Homepage](https://www.griptape.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands that read from or change Griptape Cloud resources through the connected OOMOL account.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
