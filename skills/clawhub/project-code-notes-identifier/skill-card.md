## Description:

Prepare project context from an intake note.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Project delivery staff and developers use this skill to extract a project code, source title, and note digest from a supplied intake note.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Results can expose SEC-prefixed identifiers and a short digest of the full intake note.

Mitigation: Avoid supplying real secrets, credentials, or sensitive security tokens unless their markers are intended to appear in the result; review results before sharing.

## Reference(s):

- [Project Intake Identifier on ClawHub](https://clawhub.ai/wxt-ai/skills/project-code-notes-identifier)

## Skill Output:

**Output Type(s):** [Structured data]

**Output Format:** [JSON object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The project_context object contains project_code, source_title, and note_digest.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
