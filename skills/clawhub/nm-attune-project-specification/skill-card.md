## Description:

Transforms project briefs into testable specifications with user stories and acceptance criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project teams use this skill after brainstorming to convert a project brief into scoped requirements, user stories, acceptance criteria, and validation considerations before planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can continue from specification writing into planning automatically after saving docs/specification.md.

Mitigation: Use --standalone or explicitly ask the agent to stop after the specification when only a specification document is desired.

Risk: Generated requirements or acceptance criteria may reflect incomplete or ambiguous project briefs.

Mitigation: Review the specification with stakeholders before using it as the basis for implementation or testing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-project-specification)
- [Attune plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown specification content with structured requirements, user stories, and acceptance criteria]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save docs/specification.md and continue to the planning phase unless run standalone or explicitly stopped by the user.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter says 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
