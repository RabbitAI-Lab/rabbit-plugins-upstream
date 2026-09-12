## Description:

Use when starting a new .NET/Blazor/Angular MVP project in an empty repository.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to bootstrap a new MVP repository for .NET, Blazor, Angular, or MAUI-oriented products after a SPEC has been approved or when a quick MVP start is explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or modify repository scaffolding, dependencies, lockfiles, local service stubs, agent harness files, and an initial git commit.

Mitigation: Run it only in an intended empty repository, review generated agent harness files, rules, hooks, and dependency changes, and verify build or type checks before relying on the scaffold.

Risk: The workflow includes Portuguese confirmation prompts, which may be unclear for teams expecting English-only operation.

Mitigation: Ask the agent to use the team's preferred language before approving stack and scaffold decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/scaffold-mvp)
- [Repository URL from skill metadata](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with generated repository files, code, shell commands, configuration, and documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create repository-local agent harness files, project skeletons, dependency lockfiles, local service stubs, documentation, and an initial git commit after user approval.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
