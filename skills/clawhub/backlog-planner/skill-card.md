## Description:

Backlog Planner turns feature ideas, rough notes, or conversation context into researched, dependency-ordered checkbox tasks appended to a project's roadmap or backlog file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to convert rough feature requests into self-contained, codebase-grounded backlog items before implementation. It is intended for planning only and does not execute the tasks it writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read project files and create or append ROADMAP.md, BACKLOG.md, or TODO.md.

Mitigation: Run it in the intended workspace, confirm the target backlog file when prompted, and review the appended diff before acting on it.

Risk: Generated backlog tasks may encode incorrect assumptions or stale code references.

Mitigation: Review the generated task block, especially assumptions, file references, acceptance criteria, and verification commands before execution.

## Reference(s):

- [ClawHub backlog-planner skill page](https://clawhub.ai/dennisrongo/skills/backlog-planner)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown checklist with plain sub-bullets, assumptions, acceptance criteria, and verification commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Append-only updates to ROADMAP.md, BACKLOG.md, or TODO.md; does not execute planned tasks.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
