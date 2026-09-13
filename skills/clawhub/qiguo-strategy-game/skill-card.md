## Description:

This skill launches the bundled HTML5 Canvas strategy game 七国群雄传 (Seven Kingdoms Tactics), offering campaign and skirmish modes with AI, hotseat, and optional network play.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to copy and open a self-contained browser strategy game in the workspace. It supports campaign and skirmish play with AI, same-device hotseat, same-browser play, and optional cross-device multiplayer through a relay.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional online multiplayer relay has network-safety weaknesses and is inconsistently disclosed.

Mitigation: Prefer local AI, hotseat, or same-browser play; avoid exposing net-server.js to a LAN or the internet.

Risk: Anyone who can reach the relay and guess the room can interfere with the match and potentially affect the game page.

Mitigation: Use the relay only in trusted local conditions, share room details only with the intended player, and stop the relay when play ends.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hmily741963/skills/qiguo-strategy-game)

## Skill Output:

**Output Type(s):** [files, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and copied HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Copies selected self-contained HTML game files into the workspace; cross-device multiplayer optionally uses the bundled net-server.js relay.]

## Skill Version(s):

1.5.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
