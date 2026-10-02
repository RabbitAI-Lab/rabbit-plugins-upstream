## Description:

Creates a local Markdown release-note entry from a supplied change set and returns a receipt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release coordinators and developers use this skill to turn a structured change set into a local release-note entry and receipt for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A generated release note may overwrite a local file or contain inaccurate release details.

Mitigation: Use a dedicated writable output directory and review the generated note before publishing it externally.

## Reference(s):

- [Release Notes Journal on ClawHub](https://clawhub.ai/wxt-ai/skills/repository-release-changes-workbench)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [JSON receipt with release-note Markdown; local Markdown file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes change ID, title, Markdown, and file count; creates or updates a release-note file under the selected output directory.]

## Skill Version(s):

1.1.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
