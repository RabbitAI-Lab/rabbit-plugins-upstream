## Description:

Advises users on Warzone multiplayer games and can carry out selected game actions after review and confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Warzone players use this skill to check game state, assess maps and opponents, and plan picks or turns. It can also submit game actions when the user has reviewed and confirmed them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A surrender-acceptance exception can accept an opponent's surrender without asking when acceptance simply wins the game.

Mitigation: Review the game's surrender preview and use the exception only when accepting the surrender wins the game; otherwise get the player's decision first.

Risk: Migration guidance uses an unpinned package command, so the package version may change.

Mitigation: Review and require a specific package version before following migration instructions.

Risk: The security scan was partial because multiple local references could not be resolved.

Mitigation: Treat the scan as incomplete and review the referenced skill materials before relying on the guidance.

## Reference(s):

- [warapp-mcp on ClawHub](https://clawhub.ai/chrischall/skills/warapp-mcp)
- [war.app API token help](https://war.app/API/GetAPIToken)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [Markdown text with game analysis, strategy advice, and proposed picks or turn orders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May perform selected game actions after review and confirmation.]

## Skill Version(s):

0.7.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
