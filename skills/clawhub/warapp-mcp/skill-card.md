## Description:

This skill advises users on war.app (Warzone) multiplayer games, including game status, map strategy, picks, turns, and chat.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Warzone players use the skill to check multiplayer game status, understand maps and opponents, plan picks and turns, and review proposed game actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports a surrender-acceptance instruction that could act without user approval and an unpinned package install command; scan coverage was incomplete.

Mitigation: Review the reported behaviors before use, require explicit approval for surrender decisions, and pin the package version before installing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/warapp-mcp)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, API Calls]

**Output Format:** [Natural-language guidance with structured tool arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include game summaries, recommendations, and proposed actions for user review.]

## Skill Version(s):

0.11.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
