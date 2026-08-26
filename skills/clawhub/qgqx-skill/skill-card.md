## Description:

Launches 七国群雄传 (Seven Kingdoms Tactics), a bundled HTML5 Canvas turn-based strategy game with campaign, skirmish, AI, hotseat, and optional network play modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to copy and open a playable browser strategy game from bundled files, choosing campaign or skirmish and optionally using AI, same-device hotseat, or network multiplayer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional cross-device multiplayer uses a relay server that opens a network listener.

Mitigation: Run net-server.js only on trusted networks, bind or firewall it to trusted peers, and stop the process after play.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hmily741963/skills/qgqx-skill)

## Skill Output:

**Output Type(s):** [text, shell commands, files, guidance]

**Output Format:** [Markdown guidance with shell commands and local HTML file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces playable HTML game files in the workspace; optional net-server.js relay can be run for trusted cross-device play.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
