## Description:

Task Executor guides an agent through a disciplined single-task workflow: understand the request, inspect relevant files, plan, execute incrementally, validate after each change, and track progress and assumptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to execute a concrete, already-defined task with explicit context gathering, plan approval, incremental implementation, validation after each change, and resumable progress reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can activate for well-defined coding tasks even when it is not named, which may add process overhead to ordinary requests.

Mitigation: Disable or narrow the skill trigger when lightweight handling is preferred.

Risk: The workflow may inspect files, request plan approval, run validations, and delegate read-only exploration to sub-agents.

Mitigation: Use it in workspaces where those actions are acceptable, and review proposed plans and validation steps before approving execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/task-executor)
- [Publisher profile](https://clawhub.ai/user/dennisrongo)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Structured Markdown progress reports with optional code, shell commands, configuration changes, and validation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a strict per-turn Goal / Current understanding / Files to inspect / Plan / Progress / Risks / Assumptions structure.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
