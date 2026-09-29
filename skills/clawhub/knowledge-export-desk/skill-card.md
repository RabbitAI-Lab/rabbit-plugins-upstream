## Description:

Plans a knowledge-base placement path and writes a workspace export file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Knowledge-base maintainers use this skill to plan an archive path for a note or article and optionally write a CSV export to a chosen workspace directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The downstream operation writes a CSV beneath a user-chosen output directory.

Mitigation: Choose a dedicated writable output directory rather than a broad or sensitive path.

## Reference(s):

- [Knowledge Export Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/knowledge-export-desk)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON response and CSV file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The upstream operation returns an archive path; the downstream operation writes a local CSV and returns its recorded path and effect receipt.]

## Skill Version(s):

3.0.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
