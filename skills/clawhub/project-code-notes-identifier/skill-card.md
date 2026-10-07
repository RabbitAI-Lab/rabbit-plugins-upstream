## Description:

Prepares project context from an intake note by extracting a project code, source title, and note digest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Project delivery teams use this skill to turn a supplied intake note into a structured project context for a handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill extracts SEC-prefixed credential-like markers from supplied notes and returns them as project codes, potentially exposing sensitive identifiers.

Mitigation: Do not use notes containing credentials, secrets, or sensitive identifiers unless this extraction is explicitly intended; review the result before sharing it.

## Reference(s):

- [Project Intake Identifier on ClawHub](https://clawhub.ai/wxt-ai/skills/project-code-notes-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON object containing project_context]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes project_code, source_title, and note_digest; requires an SEC-prefixed marker in the note.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
