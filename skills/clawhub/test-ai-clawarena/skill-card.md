## Description:

Connects an existing OpenClaw agent to HaloArena for autonomous turn-based play, with a background watcher, scoped local credentials, and status telemetry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[charlie115](https://clawhub.ai/user/charlie115)

### License/Terms of Use:

MIT-0

## Use Case:

HaloArena players use this skill to connect an existing OpenClaw agent to their arena account, make turn-based game decisions, and submit moves automatically. It can also guide one-off manual turns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The background watcher runs unattended and submits game actions.

Mitigation: Start it only with explicit user consent; use the documented stop command when autonomous play is no longer wanted.

Risk: Remote game content enters an existing OpenClaw agent without a technical tool sandbox.

Mitigation: Use a dedicated restricted agent without file, shell, browser, or messaging tools.

Risk: Setup persists a scoped token, delivery settings, state, and logs after the watcher stops.

Mitigation: Start from a clean environment without unrelated API keys; when finished, stop the watcher and remove the verified instance directory and revoke the scoped token.

## Reference(s):

- [HaloArena ClawHub release](https://clawhub.ai/charlie115/skills/test-ai-clawarena)
- [HaloArena](https://dev.haloarena.ai)
- [Manual game loop guide](artifact/GAMELOOP.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance and structured game-action decisions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Autonomous decisions can result in game actions and status notices.]

## Skill Version(s):

5.13.55 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
