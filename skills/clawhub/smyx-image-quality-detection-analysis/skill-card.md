## Description:

Analyzes camera images and video for black or white screens, color casts, stripes, noise, and blur, then returns a structured quality report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Security camera operators and maintenance teams use the skill to check still images or video for quality problems and review analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The analyzer can create cloud accounts, persist login tokens, and upload footage despite its advertised export-only option.

Mitigation: Confirm the provider may receive footage; ask for the export-only behavior to be fixed and credentials restricted to approved HTTPS destinations. Avoid sensitive footage and shared workspaces until account storage and deletion controls are documented.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-image-quality-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Structured analysis reports and JSON report-list data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include detected quality issues and recommendations; history lookup returns report records and links.]

## Skill Version(s):

1.0.15 (source: server-resolved release; packaged frontmatter reports 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
