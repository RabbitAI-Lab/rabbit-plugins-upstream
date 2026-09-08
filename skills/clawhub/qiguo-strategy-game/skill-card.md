## Description:

This skill launches 七国群雄传 (Seven Kingdoms Tactics), a browser-based isometric turn-based strategy game with campaign, skirmish, AI, hotseat, and optional network play modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

External users invoke this skill when they want an agent to open and present the 七国群雄传 browser strategy game for immediate play. The skill is also useful when a user asks for campaign, skirmish, same-device hotseat, or optional network multiplayer setup guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional cross-device multiplayer uses a relay without room authentication or documented exposure limits.

Mitigation: Use offline AI or same-device hotseat by default; only run cross-device multiplayer with trusted participants on a trusted network, and avoid broad exposure of net-server.js.

Risk: Peer-controlled multiplayer messages can affect page updates.

Mitigation: Before relying on multiplayer, validate peer messages, add room authentication and limits, and render peer-derived text safely instead of using unsafe HTML insertion.

Risk: The skill text contains a no-network claim that conflicts with the optional cross-device WebSocket mode.

Mitigation: Treat the game as offline for AI, hotseat, and same-browser play only; clearly document the WebSocket relay scope before enabling cross-device play.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hmily741963/skills/qiguo-strategy-game)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, local file paths, and preview instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Copies bundled self-contained HTML game files into the workspace and may provide local WebSocket relay setup for cross-device multiplayer.]

## Skill Version(s):

1.1.1 (source: server release metadata, artifact package.json, and artifact SKILL.md changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
