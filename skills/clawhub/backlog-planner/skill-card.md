## Description:

Turn a feature idea, conversation context, or rough notes into researched, detailed, dependency-ordered checkbox tasks appended to the project's roadmap/backlog file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to convert feature ideas, notes, or conversation context into PR-sized backlog or roadmap tasks that are grounded in the current codebase and ready for later execution by a human or agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may append backlog tasks that misstate project intent or implementation details if the source request is ambiguous.

Mitigation: Review the appended task block, especially assumptions, verified file references, acceptance criteria, and verification commands, before using the tasks for execution.

Risk: The skill reads relevant project files and may create or append a roadmap, backlog, or todo file in the active workspace.

Mitigation: Run it only in the intended repository and review file changes before committing or handing the backlog to an execution agent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/backlog-planner)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown checklist tasks with plain-text sub-bullets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Appends or creates a roadmap, backlog, or todo file; tasks include context, acceptance criteria, verified files, assumptions, and a verification command.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
