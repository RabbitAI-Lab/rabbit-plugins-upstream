## Description:

Read Warzone game state, maps, standings, and opponent statistics from a shell or signed-in war.app browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and players use this skill to inspect Warzone games, map details, player status, and opponent records. It returns read-only information for questions, scripts, or one-off checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends account credentials with requests to war.app, and its security scan advises considering whether that service is trusted.

Mitigation: Use credentials only for the intended war.app account, keep the credentials file private, and do not print or commit the token.

Risk: The security analysis was partial: one of three components was fully inspected and two were partially inspected.

Mitigation: Review the skill files before installation and deployment, especially when changing the helper or scouting behavior.

## Reference(s):

- [War.app GameFeed API](https://war.app/API/GameFeed)
- [FetchProxy CLI](https://www.npmjs.com/package/@fetchproxy/cli)
- [Opponent scouting reference script](artifact/references/scout.mjs)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/warapp-api)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Structured game and player data with concise text summaries; shell recipes use curl and jq.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only game and player information; account access and fog of war limit returned data.]

## Skill Version(s):

0.7.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
