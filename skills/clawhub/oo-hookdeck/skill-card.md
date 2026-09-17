## Description:

Hookdeck (hookdeck.com) helps an agent read, create, update, and delete Hookdeck resources through OOMOL connector actions instead of calling the Hookdeck API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Hookdeck sources, destinations, and connections from an agent session. It supports read, list, create, update, and delete workflows while requiring live action schema inspection before connector actions are run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to pipe remote installer scripts directly into a shell.

Mitigation: Review the installer path before installing and prefer a signed or otherwise verifiable oo CLI release.

Risk: Hookdeck actions are brokered through an OOMOL-connected account.

Mitigation: Connect the OOMOL Hookdeck integration only when the user accepts OOMOL brokering Hookdeck actions for the account.

Risk: Create, update, and delete actions can change or remove Hookdeck resources.

Mitigation: Inspect the live action schema and confirm exact targets, payloads, and effects with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-hookdeck)
- [Hookdeck Homepage](https://hookdeck.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
