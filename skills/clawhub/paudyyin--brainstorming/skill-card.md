## Description:

A Chinese-language brainstorming and design-approval workflow that helps agents explore requirements, refine ideas, evaluate options, and gate implementation until design approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paudyyin](https://clawhub.ai/user/paudyyin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and agent operators use this skill to structure feature ideation, clarify requirements, pressure-test assumptions, and document an approved design before code changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can activate on broad design or idea-related requests.

Mitigation: Opt out explicitly when the task is casual discussion, pure analysis, or does not need the design-approval workflow.

Risk: The workflow may create or update repository documentation files.

Mitigation: Review proposed documentation changes before accepting them, especially .superpowers/design-approval.md and record.md.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/paudyyin/skills/brainstorming)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown and conversational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation or update of repository documentation files such as .superpowers/design-approval.md and record.md.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
