## Description:

Maps a codebase, decomposes requested work into a dependency graph, and runs a test-sandwiched multi-agent software pipeline with isolated worktrees, per-wave regression checks, adversarial review, and an explicit quality rubric.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill for substantial builds, fixes, refactors, migrations, and greenfield package work that benefit from repository mapping, dependency-aware planning, isolated implementation attempts, repeated regression checks, and reviewable branch handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow has broad local mutation authority in the target repository.

Mitigation: Run it only against a backed-up, trusted repository path with filesystem, credential, network, time, and spending limits.

Risk: Unsafe command or path handling could affect repository contents or cleanup behavior.

Mitigation: Review the workflow adapter before use, avoid arbitrary non-Git directories, and inspect generated branches, tags, MAP.md, and cleanup actions before merging.

Risk: Remote mutation can publish integration checkpoints or agent branches.

Mitigation: Keep remote push disabled unless the exact repository and refs have been explicitly authorized.

Risk: Agent-reported tests, scans, grades, and review outcomes may be incomplete or wrong.

Mitigation: Re-run the relevant checks independently on the final integration branch and resolve escalations before merging.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/antreasantoniou/skills/grade-a-pipeline)
- [SKILL.md](SKILL.md)
- [README.md](README.md)
- [Workflow adapter](examples/grade-a-pipeline.workflow.js)
- [Agent Orchestra](https://github.com/AntreasAntoniou/agent-orchestra)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Structured workflow result object with Markdown, Git refs, branch handoff details, test summaries, review findings, grade, escalations, and checkout guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a compatible Workflow host and a target repository path; it can create local Git worktrees, branches, tags, commits, and optional remote pushes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
