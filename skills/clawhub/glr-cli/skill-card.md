## Description:

Configure and operate the GameLearningRuntime agent-first CLI for bridge startup, bounded goal-driven research and training, concurrent review capture, run queries, spatial knowledge transfer, and verified model playback. Use for operating an existing GLR project; use glr-adapter-builder when implementing the game adapter itself.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure and operate existing GLR projects through the standalone CLI, including project validation, bounded goal runs, training, run inspection, knowledge transfer, recording checks, updates, and offline source handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill helps an agent operate GLR projects and their configured project roles.

Mitigation: Review the project manifest and role commands before use, run doctor first, and keep goal runs bounded by explicit trial, step, time, and research-source limits.

Risk: Routine GLR commands may perform background release-check requests.

Mitigation: Set GLR_NO_UPDATE_CHECK=1 when background release checks are not desired; CI environments skip automatic checks.

Risk: Recorded video alone can be mistaken for training-ready data.

Mitigation: Require a finalized H.264 MP4 plus a valid checksummed glr.capture-frame.v1 index, decoded media checks, and authoritative runtime evidence before classifying capture as training data.

Risk: An update operation can modify the GLR executable, runtime host, and project skills.

Mitigation: Run glr update only after an explicit user request, use the selected project skills directory or --no-skills intentionally, and rely on exact archive and SHA256SUMS verification.

## Reference(s):

- [GLR CLI command and contract reference](references/commands.md)
- [Offline source packages](references/packages.md)
- [VX recording and acceptance contract](references/recording.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.19.0 (source: ClawHub server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
