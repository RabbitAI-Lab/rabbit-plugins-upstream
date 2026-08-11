## Description:

Use when the user runs /wdp-prd-en to discuss or record new requirements, view the backlog, or dispatch confirmed requirements to background subagents for parallel implementation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckystar513](https://clawhub.ai/user/luckystar513)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to maintain a project requirements backlog, discuss and record requirement cards, schedule work by dependency and conflict state, and dispatch confirmed requirements to implementation subagents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent requirement storage can write backlog files, execution plans, and pointer files outside the current project directory when PRD_ROOT is configured.

Mitigation: Review PRD_ROOT and the project pointer before use, and confirm the selected storage location matches the project workflow.

Risk: Parallel dispatch can create implementation work in background subagents and later merge changes into the current branch.

Mitigation: Use the documented confirmation, full integration test, code review, and user acceptance gates before marking work done or merging results.

Risk: A non-git project cannot provide worktree isolation for dispatched implementation work.

Mitigation: Follow the skill's non-git fallback: warn clearly and ask whether to continue serially without isolation or abandon dispatch.

## Reference(s):

- [Requirement Card Template](references/card-template.md)
- [wdp-prd-en Test Scenarios](references/test-scenarios.md)
- [ClawHub skill release page](https://clawhub.ai/luckystar513/skills/wdp-prd-en)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown requirement cards, backlog summaries, scheduling status reports, implementation summaries, and guided command instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates and updates local project backlog files, execution plans, and implementation-plan archives; may dispatch background implementation subagents when the user confirms.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
