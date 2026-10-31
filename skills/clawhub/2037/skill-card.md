## Description:

A Chinese-language Earth2037 player assistant that uses the updated account center and game MCP/CLI to inspect cities, buildings, heroes, tasks, troops, and maps, and carry out player-authorized game actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[windinwing](https://clawhub.ai/user/windinwing)

### License/Terms of Use:

MIT-0

## Use Case:

External players use this skill to connect an assistant to their Earth2037 account, inspect their characters and game state, and carry out specifically authorized in-game actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enabling writes exposes a broad command catalog, including account-deletion and payment-related protocol commands; some raw commands do not provide previews.

Mitigation: Keep read-only mode enabled until the player authorizes specific actions. Use the documented prepare and preview flow where available, and limit raw commands to clearly authorized requests.

Risk: The local credential file contains a password and rotating authentication tokens, and an unverified replacement account endpoint could expose them.

Mitigation: Protect the credential file and its directory with the documented private permissions, and verify any replacement account endpoint before use.

Risk: Entering a character replaces that character's current phone or web client session.

Mitigation: Enter only the explicitly selected server and character when session takeover is intended; stop after a forced logout instead of reconnecting automatically.

## Reference(s):

- [Setup, permissions, and migration](references/SETUP.md)
- [Player workflows](references/WORKFLOWS.md)
- [Earth2037 AI assistant page](https://www.earth2037.com/ai/index-cn.html)
- [2037 ClawHub release](https://clawhub.ai/windinwing/skills/2037)

## Skill Output:

**Output Type(s):** [JSON, Guidance, Shell commands, Configuration instructions]

**Output Format:** [JSON MCP requests and responses, CLI text, and Markdown setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only by default; game actions require explicit write enablement and player authorization. Large responses may be paginated.]

## Skill Version(s):

2.0.3 (source: package.json, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
