## Description:

Provides document release guidance and selects a version within a requested major release line.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Document managers and developers use this skill to derive release-selection guidance and select a document version from the available records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A selection may not reflect the actual candidate versions or approval states.

Mitigation: Provide and verify the current candidate data; treat the selection as advisory until checked.

Risk: The downstream operation creates or updates a local Markdown result file.

Mitigation: Choose a writable output directory and review the resulting file before relying on it.

## Reference(s):

- [Document Release Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/document-release-desk)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [JSON result and local Markdown artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Upstream returns selection guidance; downstream returns a selection result and writes a local artifact under the chosen output directory.]

## Skill Version(s):

3.0.0 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
