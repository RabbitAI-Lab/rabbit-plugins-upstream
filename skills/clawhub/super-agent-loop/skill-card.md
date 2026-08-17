## Description:

Super-agent-loop orchestrates long-running DAG tasks by executing ready steps, gating results with caller-provided verification, writing successful outputs to memory, and producing reflection when failures or blocked nodes occur.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to run long-running, multi-step workflows that require dependency-aware execution, verification gates, shared memory, and failure reflection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can execute caller-provided shell commands through loop definitions.

Mitigation: Treat loop and graph definitions as trusted code, review commands before execution, prefer dry-run first, and add sandboxing, command allowlists, and explicit approval before real execution.

Risk: The skill can write local state such as memory and summary files.

Mitigation: Run it in a scoped workspace or dedicated output directory and avoid sensitive workspaces unless local writes are sandboxed.

Risk: Cyclic or poorly formed dependency graphs can leave work blocked or produce incomplete runs.

Mitigation: Validate inputs as DAGs before execution and require deterministic action and verification functions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/super-agent-loop)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Guidance]

**Output Format:** [CLI text with JSON reports and local output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write memory.json and summary.json when an output directory is provided.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
