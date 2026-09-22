## Description:

Multi-Agent Dev helps developers execute coding plans by decomposing work into task dependencies, dispatching fresh subagents, and applying staged specification and code-quality reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to coordinate multi-task coding work with subagents, including implementation, testing, and staged review. It is intended for clear implementation plans where tasks can be decomposed, sequenced, and selectively parallelized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Subagents may edit files or run commands while implementing coding tasks.

Mitigation: Use the skill only in trusted repositories, start from an explicit plan, and review proposed changes and command output before accepting results.

Risk: Parallel subagent work can create conflicts when tasks touch the same files or have hidden dependencies.

Mitigation: Build a dependency graph first, run shared-file or uncertain tasks serially, and fall back to serial execution when conflicts appear.

Risk: Callback URLs may expose information to the agent platform handling asynchronous notifications.

Mitigation: Avoid callback URLs unless the destination and transmitted data are understood and approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/multi-agent-dev)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce task breakdowns, review findings, implementation guidance, and commands for the active agent environment.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
