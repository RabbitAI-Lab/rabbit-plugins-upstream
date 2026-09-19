## Description:

Configure and operate the GameLearningRuntime agent-first CLI for bridge startup, bounded goal-driven research and training, concurrent review capture, run queries, spatial knowledge transfer, and verified model playback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to operate an existing GLR project through the `glr` CLI, including project validation, runtime startup, bounded training and goal runs, telemetry review, capture verification, packaging, backup, and model playback. It helps agents keep CLI actions scoped to project manifests, explicit user requests, and authoritative run evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GLR update operations can modify GLR binaries or project skill copies when explicitly run.

Mitigation: Run `glr update` only after an explicit update request; use `glr update --check` for read-only version checks and review the selected project or skills directory before applying changes.

Risk: Project workflows may execute configured runtime, training, recording, or task commands from a trusted project manifest.

Mitigation: Install and use the skill only with trusted GLR projects, inspect manifests and task definitions first, and rely on `glr --project . --json doctor` plus bounded budgets before running project roles.

Risk: Telemetry or project evidence can contain local paths, tokens, private traces, or machine-local binding details.

Mitigation: Keep telemetry tokens, local runtime identifiers, credentials, private traces, and source-machine paths out of public artifacts and source packages; publish only reviewed, portable evidence.

Risk: Video, process exit, model hash, or package validity can be mistaken for gameplay success or training-ready data.

Mitigation: Require authoritative run metrics, checked capture manifests, synchronized `glr.capture-frame.v1` indexes, and evaluator evidence before claiming gameplay success, reproduction, or training readiness.

## Reference(s):

- [GLR CLI command and contract reference](references/commands.md)
- [Collect, render, and trace training data](references/data-collection.md)
- [Offline source packages](references/packages.md)
- [VX recording and acceptance contract](references/recording.md)
- [ClawHub skill page](https://clawhub.ai/loonghao/skills/glr-cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code snippets]

**Output Format:** [Markdown with inline shell, JSON, TOML, and Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is scoped to existing GLR projects, explicit project manifests, run contexts, receipts, and verified artifacts.]

## Skill Version(s):

0.22.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
