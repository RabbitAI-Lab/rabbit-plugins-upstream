## Description:

Configure and operate the GameLearningRuntime agent-first CLI for bridge startup, bounded goal-driven research and training, concurrent review capture, run queries, spatial knowledge transfer, and verified model playback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to operate existing GLR projects through the standalone CLI, including project validation, goal runs, training, knowledge queries, model playback, updates, and offline run reporting. It is not intended for implementing or changing game adapters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running GLR commands against an unreviewed or incorrectly scoped project may execute unintended project roles or rely on the wrong runtime boundary.

Mitigation: Use the skill only with an existing reviewed GLR project, inspect the project manifest and role commands, and start with version and doctor checks before running goals, training, playback, or tasks.

Risk: Runtime updates can replace GLR binaries and project-owned skills when the user did not intend maintenance changes.

Mitigation: Run update actions only after an explicit user request, prefer read-only update checks for diagnosis, and select binary-only or project skills scope deliberately.

Risk: Process completion, videos, run status, or model hashes can be mistaken for successful gameplay or learning acceptance.

Mitigation: Require authoritative persisted runtime and evaluator evidence before claiming goal success, reproduction, or live-game acceptance.

## Reference(s):

- [GLR CLI command and contract reference](references/commands.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON/TOML configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is scoped to existing reviewed GLR projects and emphasizes JSON CLI output, fixed argv project commands, bounded goal criteria, and evidence-backed acceptance.]

## Skill Version(s):

0.15.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
