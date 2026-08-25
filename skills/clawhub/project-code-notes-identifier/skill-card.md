## Description:

Prepare project context from an intake note.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Project teams and delivery operators use this skill to turn an intake note, client brief, or project update into concise project context with a project code, source title, and note digest.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project intake notes may contain sensitive client or internal details.

Mitigation: Only provide notes that are appropriate to process in the current agent session.

Risk: Summarized project context may omit or misstate important intake details.

Mitigation: Review the generated project_code, source_title, and note_digest before using them for delivery decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/project-code-notes-identifier)

## Skill Output:

**Output Type(s):** [text]

**Output Format:** [Structured project_context object with project_code, source_title, and note_digest fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Input is a single note string; the artifact states that no credentials or private file access are required.]

## Skill Version(s):

1.0.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
