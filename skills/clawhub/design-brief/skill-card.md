## Description:

Turns vague feature ideas into approved Markdown design briefs that record intent, decisions, scope, interfaces, constraints, precedent, alternatives, and open questions before implementation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and planning agents use this skill to turn an undecided feature idea or architectural task into a concrete, approved design brief before implementation or task planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create or update draft design brief files under .claude/design-briefs/ as part of normal use.

Mitigation: Review generated brief files before committing them or using them as downstream implementation specifications.

Risk: Broad feature-planning phrases such as "how should we build" may trigger the workflow.

Mitigation: Confirm that the user wants a design-brief workflow before relying on the generated brief.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/design-brief)
- [Publisher profile](https://clawhub.ai/user/dennisrongo)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown design brief file plus concise approval guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write project-scoped brief files under .claude/design-briefs/.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
