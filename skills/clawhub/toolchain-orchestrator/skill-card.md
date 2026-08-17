## Description:

A multi-step toolchain orchestration skill that helps agents define shell-command workflows as dependency DAGs, validate them, execute them in topological order with upstream output injection, resume failed steps, and export Graphviz DOT views.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan and run repeatable multi-command workflows where steps have explicit dependencies, captured outputs, resumable failure handling, and optional dependency visualization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chain files can execute arbitrary local shell commands with the agent's privileges.

Mitigation: Only run chain files that were written or reviewed by the user, validate the workflow before execution, and execute it in a least-privileged workspace.

Risk: Persistent learning data can retain sensitive notes, credentials, or private paths if they are recorded during use.

Mitigation: Do not store secrets or sensitive incident details in learner notes or preferences, and inspect or delete learned_patterns.json when persistent local history is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/toolchain-orchestrator)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation of chain definitions, execution logs, captured step output, and Graphviz DOT files when the orchestration scripts are run.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
