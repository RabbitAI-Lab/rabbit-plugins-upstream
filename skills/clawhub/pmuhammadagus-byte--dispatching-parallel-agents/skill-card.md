## Description:

Helps agents split independent debugging or test-failure investigations into focused parallel subagent tasks and verify returned work before integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill when three or more unrelated bugs, test failures, or subsystem issues can be investigated independently. It guides the coordinator to create scoped subagent briefs, run them in parallel, review results, and verify the combined outcome.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Parallel subagents can produce conflicting or overlapping changes when tasks are not truly independent.

Mitigation: Scope each task to separate files or subsystems, then review returned changes for conflicts before integration.

Risk: Returned fixes or recommendations can be incorrect even when the skill itself is clean.

Mitigation: Review each result independently and run the relevant tests or full suite before treating the combined work as complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/dispatching-parallel-agents)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with optional text task briefs and shell command suggestions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose one focused brief per independent task and requires coordinator verification before integration.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact metadata.openclaw.version is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
