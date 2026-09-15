## Description:

Use when the user needs to create or refine a feature SPEC SDD before implementation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to clarify feature, bugfix, refactor, API, infrastructure, frontend, or documentation requests before implementation. It asks structured Portuguese questions, gathers repository facts, and writes a SPEC SDD that must be approved before implementation begins.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect repository files and documentation while gathering facts for a SPEC.

Mitigation: Use it only in workspaces where repository inspection is appropriate, and avoid exposing secrets or sensitive data in prompts, files, or generated SPEC content.

Risk: Generated SPEC content can contain incorrect, incomplete, or overbroad implementation guidance.

Mitigation: Review the generated .specs/SPEC file for scope, security, and technical accuracy before approving any later implementation work.

## Reference(s):

- [SPEC SDD Template](references/spec-sdd-template.md)
- [Publisher Metadata URL](https://github.com/afonsoft/skills)
- [ClawHub Skill Page](https://clawhub.ai/afonsoft/skills/write-specs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Portuguese clarification questions and a Markdown SPEC SDD file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a .specs/SPEC-{YYYYMMDD}-{feature}.md planning document and requires user approval before implementation.]

## Skill Version(s):

1.0.3 (source: server release evidence; artifact metadata reports 1.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
