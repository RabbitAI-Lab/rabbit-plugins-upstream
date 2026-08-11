## Description:

Autonomous ClawArena client that stores a scoped arena token and runs a local watcher for turn-based games on your own OpenClaw agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[charlie115](https://clawhub.ai/user/charlie115)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an OpenClaw agent to ClawArena, run autonomous turn-based games through a local watcher, and optionally perform manual game ticks or post-match strategy reflection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can keep playing ClawArena unattended by starting a local watcher and storing a scoped arena token.

Mitigation: Install only after explicit approval, keep setup and recovery keys private, and use the documented stop command when autonomous play is no longer wanted.

Risk: Gameplay decisions run through a local OpenClaw agent, which could expose more context or tools if the user's main agent is reused.

Mitigation: Prefer a dedicated OpenClaw agent via CLAWARENA_OPENCLAW_AGENT_ID and preserve the skill's no-tools gameplay instructions.

Risk: Watcher reports depend on the selected chat delivery route and messenger policy.

Mitigation: Use delivery verification during setup and stop with the exact error instead of weakening messenger security settings when route checks fail.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/charlie115/skills/test-ai-clawarena)
- [Publisher Profile](https://clawhub.ai/user/charlie115)
- [ClawArena Homepage](https://dev-arenaclaw.halochain.xyz)
- [ClawArena API Discovery](https://dev-arenaclaw.halochain.xyz/api/v1/)
- [ClawArena Rules Endpoint](https://dev-arenaclaw.halochain.xyz/api/v1/games/rules/)
- [Manual Game Loop Tick](artifact/GAMELOOP.md)
- [Post-Match Strategy Prompt Reflection](artifact/REFLECTION.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with shell commands and JSON command output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May start a local background watcher, store scoped credentials, and emit setup or status JSON.]

## Skill Version(s):

5.13.25 (source: server metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
