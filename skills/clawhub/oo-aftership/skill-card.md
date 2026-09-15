## Description:

The AfterShip skill helps agents read, create, update, and delete shipment tracking data through an OOMOL-connected AfterShip account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate AfterShip through an OOMOL-connected account, including shipment tracking, courier lookup, and tracking lifecycle actions. The skill supports both read workflows and state-changing AfterShip operations through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs agents toward remote installer commands for the oo CLI.

Mitigation: Review installation commands before execution and prefer a reviewed, version-pinned, or otherwise verifiable installation method.

Risk: Write and destructive AfterShip actions can change or delete shipment tracking records.

Mitigation: Confirm the exact action, target tracking record, payload, and expected effect with the user before running state-changing commands.

Risk: Using the connector relies on OOMOL as an intermediary for AfterShip actions.

Mitigation: Install only when this intermediary model is acceptable for the user's account and data handling requirements.

## Reference(s):

- [ClawHub AfterShip skill page](https://clawhub.ai/oomol/skills/oo-aftership)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [AfterShip homepage](https://www.aftership.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
