## Description:

Inspects CSV and XLSX files, previews rule-based cleaning with change samples, and delivers cleaned files only after user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

People working with CSV or XLSX spreadsheets use this skill to inspect data and review the effects of explicit cleaning rules before authorizing a cleaned file. It provides change samples, impact counts, and an audit summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded spreadsheets may contain sensitive information processed by an external service.

Mitigation: Upload only files approved for this service, and check its privacy and retention terms before using sensitive spreadsheets.

Risk: Preview and execution can incur usage charges.

Mitigation: Review the published pricing and previewed changes before explicitly confirming execution.

## Reference(s):

- [ClawHub data-cleaning release](https://clawhub.ai/youteacher/skills/data-cleaning)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [Data-cleaning product and pricing](https://ai-skills.open-idea.net/skills/data-cleaning)
- [API key and pricing guide](https://ai-skills.open-idea.net/skill-docs/data-cleaning/API-KEY.md)
- [HTTP requests and task polling](https://ai-skills.open-idea.net/skill-docs/data-cleaning/HTTP-REQUESTS.md)
- [Cleaning operations and rules](https://ai-skills.open-idea.net/skill-docs/data-cleaning/OPERATIONS.md)
- [Safety and confirmation rules](https://ai-skills.open-idea.net/skill-docs/data-cleaning/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Human-readable preview and audit summary with private CSV or XLSX file links after confirmation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports affected rows, changed cells, representative samples, and unresolved risks; execution requires explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: release metadata and skill packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
