## Description:

Builds presentation decks locally as self-contained HTML, or through OnePress for researched decks and downloadable presentation exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[getonepress](https://clawhub.ai/user/getonepress)

### License/Terms of Use:

MIT

## Use Case:

Employees, creators, and developers use this skill to prepare investor updates, lessons, research briefings, and other presentations. It builds a local HTML deck without an account or uses a connected OnePress account for research and additional exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local mode writes a deck file in the current working directory.

Mitigation: Review the output location and deck contents before sharing or overwriting local files.

Risk: Connected mode sends deck prompts and uploaded files to OnePress, where they may remain in its workspace.

Mitigation: Avoid secrets, regulated data, and confidential files unless your organization approves OnePress for that data.

## Reference(s):

- [OnePress Deck on ClawHub](https://clawhub.ai/getonepress/skills/onepress-deck)
- [OnePress](https://www.getonepress.com)

## Skill Output:

**Output Type(s):** [Code, Files, Text guidance]

**Output Format:** [Self-contained HTML deck in local mode; downloaded presentation files and text summaries in connected mode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connected mode can produce PDF, editable PPTX, and narrated video; local mode writes an HTML deck to the working directory.]

## Skill Version(s):

3.1.2 (source: frontmatter, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
