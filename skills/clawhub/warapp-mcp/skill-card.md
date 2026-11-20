## Description:

Advises players on Warzone multiplayer games and supports game actions through warapp tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

War.app players use the skill to review games, maps, opponents, and chat, get strategy and turn plans, and carry out requested picks or game actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic surrender decisions can affect the player's game outcome.

Mitigation: Review surrender decisions and require explicit user intent before taking a surrender action.

Risk: The optional migration command installs a package without pinning its version.

Mitigation: Review the package and version before running the migration command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/warapp-mcp)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, API Calls, Text]

**Output Format:** [Conversational text with structured game data, plans, and action previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit requested game actions after review and confirmation.]

## Skill Version(s):

0.6.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
