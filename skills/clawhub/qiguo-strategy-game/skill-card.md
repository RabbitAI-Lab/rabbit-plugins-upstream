## Description:

This skill launches the single-file HTML strategy game 七国群雄传 (Seven Kingdoms Tactics), a 三国群英传-style isometric turn-based wargame.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to open and play a bundled browser-based strategy wargame, choosing campaign or skirmish mode with AI, same-device hotseat, or optional network play.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release includes optional online multiplayer despite offline-oriented launch language.

Mitigation: Use AI, hotseat, or same-browser tab play when offline behavior is desired; run net-server.js only when cross-device multiplayer is intentionally needed.

Risk: The WebSocket relay uses room names for convenience rather than strong access control.

Mitigation: Run the relay only on a trusted network, restrict exposure with firewall or bind settings, and avoid treating room names as private authentication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/hmily741963/skills/qiguo-strategy-game)
- [Publisher Profile](https://clawhub.ai/user/hmily741963)
- [Artifact Skill Definition](artifact/SKILL.md)
- [Campaign Mode HTML](artifact/assets/campaign-mode.html)
- [Skirmish Mode HTML](artifact/assets/skirmish-mode.html)
- [Optional WebSocket Relay](artifact/net-server.js)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Markdown guidance with copied local HTML game files and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The primary outputs are self-contained browser game files; cross-device multiplayer can additionally use the bundled WebSocket relay.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
