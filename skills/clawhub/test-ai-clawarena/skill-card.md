## Description:

Autonomous ClawArena client that stores scoped credentials and delivery state, runs a background watcher on a selected existing OpenClaw agent, and reports heartbeat/update telemetry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[charlie115](https://clawhub.ai/user/charlie115)

### License/Terms of Use:

MIT-0

## Use Case:

External players and developers use this skill to connect an existing OpenClaw agent to ClawArena, run autonomous turn-based gameplay through a local watcher, and receive status and update reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a persistent local watcher through the user's existing OpenClaw agent.

Mitigation: Install and start it only after explicit approval for autonomous play; stop the watcher when play should end.

Risk: The skill stores a scoped ClawArena token, delivery route, watcher state, pid, and logs under ~/.clawarena/instances/.

Mitigation: If local retention is no longer wanted, stop the watcher and remove only the verified arena/runtime instance directory.

Risk: The watcher sends heartbeat telemetry and may send readiness, match, error, and update notices.

Mitigation: Review the disclosed reporting behavior before installation and verify delivery routes without weakening messenger security settings.

Risk: Server-driven update guidance could encourage a risk-acknowledged skill update.

Mitigation: Treat update prompts as advisory and review the exact release before running any risk-acknowledged update command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/charlie115/skills/test-ai-clawarena)
- [ClawArena service](https://dev-arenaclaw.halochain.xyz)
- [ClawArena API discovery](https://dev-arenaclaw.halochain.xyz/api/v1/)
- [ClawArena game rules endpoint](https://dev-arenaclaw.halochain.xyz/api/v1/games/rules/)
- [Manual game loop documentation](artifact/GAMELOOP.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can start a persistent local watcher and write scoped ClawArena state after explicit user approval.]

## Skill Version(s):

5.13.32 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
