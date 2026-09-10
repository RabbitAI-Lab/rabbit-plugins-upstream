## Description:

Guides agents through Portuguese requirements interviews to create or refine a feature SPEC SDD before implementation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to turn ambiguous feature, bugfix, refactor, API, infrastructure, frontend, or documentation requests into a reviewed SPEC SDD before implementation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A SPEC approval workflow could be treated as permission for implementation, commits, or PR creation.

Mitigation: Before use, instruct the agent to stop after writing or approving the SPEC unless implementation, commits, or PR creation are separately requested.

## Reference(s):

- [SPEC SDD Template](references/spec-sdd-template.md)
- [Publisher-provided project URL](https://github.com/afonsoft/skills)
- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/grill-me-with-spec)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Portuguese question rounds and Markdown SPEC SDD files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Intended to write .specs/SPEC-{YYYYMMDD}-{feature}.md and stop before implementation unless the user separately requests follow-on work.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence; artifact metadata says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
