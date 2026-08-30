## Description:

Create or maintain a PROJECT.md source-of-truth doc for any project, quiz-first with project-type branches. Use only when the user explicitly asks for project documentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tooled-app](https://clawhub.ai/user/tooled-app)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project maintainers use this skill to create or maintain a root PROJECT.md source-of-truth document after an explicit documentation request. It captures project purpose, stack, build and run details, structure, decisions, changelog entries, gotchas, and a running notes log.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may record sensitive or unintended project details in PROJECT.md.

Mitigation: Review generated or updated documentation before keeping or sharing it, and remove details that should not be preserved.

Risk: The skill writes to the project root and could update the wrong PROJECT.md if the root is ambiguous.

Mitigation: Confirm the intended project root before allowing the skill to create or edit PROJECT.md.

## Reference(s):

- [PROJECT.md Section Templates](references/templates.md)
- [Project Doc Skill Page](https://clawhub.ai/tooled-app/skills/project-doc-skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown PROJECT.md file and concise conversational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read, write, or edit only PROJECT.md at the confirmed project root; does not request shell command execution.]

## Skill Version(s):

1.0.1 (source: server release metadata; SKILL.md frontmatter reports v1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
