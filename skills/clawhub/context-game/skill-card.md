## Description:

Context Game is a multi-genre open-world dialogue game skill where the agent acts as the game engine, narrator, world simulator, and adjudicator for free-text player actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[charlesresearch001](https://clawhub.ai/user/charlesresearch001)

### License/Terms of Use:

MIT-0

## Use Case:

External users and game-focused agent operators use this skill to run the Chinese-language open-world game '上下文' through free-text role-play, state tracking, dice adjudication, and save-file management. The skill supports new games, resumed saves, status checks, world selection, custom world setup, and retirement summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A malicious or untrusted save-slot name could lead to unintended shell command execution when an agent interpolates it into a command.

Mitigation: Use trusted save-slot names only, restrict slots to letters, numbers, underscores, and hyphens, and call scripts/save.py with structured arguments rather than shell-interpolated strings.

Risk: Normal gameplay writes state, memory, world, archive, and dice-log files in the workspace.

Mitigation: Install and run the skill only in workspaces where game save-file writes are expected and acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/charlesresearch001/skills/context-game)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)
- [Core rules](artifact/rules/rules.md)
- [Event rules](artifact/rules/events.md)
- [Suspicion module](artifact/rules/suspicion.md)
- [World library](artifact/world/README.md)
- [World generation protocol](artifact/world/world-gen-protocol.md)
- [Save engine](artifact/scripts/save.py)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, files, guidance]

**Output Format:** [Markdown/plain-text game narration with shell command calls and JSON/Markdown save artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains game state in save files and dice logs; requires Python 3.8+ and filesystem access for normal play.]

## Skill Version(s):

0.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
