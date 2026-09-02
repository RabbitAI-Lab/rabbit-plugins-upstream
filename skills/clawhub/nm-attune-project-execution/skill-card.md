## Description:

Executes implementation plans with progress tracking, checkpoint validation, and quality gates after planning is complete and tasks are ready to implement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill after an implementation plan exists to execute tasks, track progress, validate checkpoints, and prepare completion reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project-specific make, test, deployment, or staging commands may run with the same authority as the local project environment.

Mitigation: Review those commands and their target environment before allowing the agent to execute them.

Risk: Execution guidance can produce incorrect or misleading implementation changes if the project plan, dependencies, or acceptance criteria are outdated.

Mitigation: Confirm the implementation plan, dependency state, acceptance criteria, and quality gates before task execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-attune-project-execution)
- [Attune Project Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Text and Markdown with inline code, shell commands, checklists, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce progress updates, execution-state JSON, validation commands, quality-gate checklists, and mission reports.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
