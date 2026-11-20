## Description:

Read war.app (Warzone) game and player data from a shell through the GameFeed API and a signed-in browser tab without submitting orders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and players use the skill to inspect Warzone games, maps, settings, player status, and opponent statistics from scripts or one-off shell sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads war.app credentials and sends them with GameFeed requests; the security review was benign with medium confidence and partial component coverage.

Mitigation: Use only if you trust war.app to receive the credentials, keep the configured .env file private, and never print or commit the token.

## Reference(s):

- [war.app](https://war.app)
- [fpx CLI (@fetchproxy/cli)](https://www.npmjs.com/package/@fetchproxy/cli)
- [ClawHub warapp-api release](https://clawhub.ai/chrischall/skills/warapp-api)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands]

**Output Format:** [JSON game and player data, with shell commands for retrieval and optional text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only inspection; game data is limited to the authenticated player's view.]

## Skill Version(s):

0.6.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
