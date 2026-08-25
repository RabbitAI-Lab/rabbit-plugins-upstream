## Description:

Write a workspace export file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Knowledge-base contributors and workspace automation users use this skill to record a supplied workspace path for a note or article export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recorded output is derived from a user-supplied workspace path, so an unintended path could be recorded if the input is wrong.

Mitigation: Provide only the workspace path intended for the current note or knowledge-base article and review the recorded_path fields before using the result.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wxt-ai/skills/workspace-note-path-workbench)

## Skill Output:

**Output Type(s):** [text, configuration]

**Output Format:** [Structured object with relative_path, stem, and extension fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output is derived from the user-supplied workspace path.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
