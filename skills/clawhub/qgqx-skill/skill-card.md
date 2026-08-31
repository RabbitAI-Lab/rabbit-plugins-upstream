## Description:

Launches a bundled browser tactics game, 七国群雄传, with campaign and skirmish modes plus AI, same-device hotseat, same-browser, and optional cross-device multiplayer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to open a playable Warring States browser strategy game from bundled HTML assets. It is useful for quick single-player play, same-device two-player matches, and optional live multiplayer when a trusted relay is available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional cross-device multiplayer requires running a WebSocket relay and entering a server URL, which can expose connections outside a purely local play session.

Mitigation: Run net-server.js only on trusted networks, bind or firewall it deliberately, and connect only to trusted relay URLs.

Risk: The artifact documentation includes offline/no-network language even though cross-device multiplayer can use a relay server.

Mitigation: Treat the skill as offline only for AI, hotseat, and same-browser play; review network behavior before enabling cross-device matches.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hmily741963/skills/qgqx-skill)
- [Publisher profile](https://clawhub.ai/user/hmily741963)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and local file references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May copy bundled HTML game files into the workspace and open them in a browser preview; optional cross-device play requires a WebSocket relay URL.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
