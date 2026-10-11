## Description:

Generates verified business metrics, charts, and reports from CSV or XLSX data, with explanations limited to validated figures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and analysts use this skill to inspect spreadsheets, generate verified metrics and charts, and export business reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected CSV or XLSX business data is sent to an external service.

Mitigation: Upload only data approved for that service; avoid highly sensitive spreadsheets unless permitted.

Risk: Exposed API keys or an unreviewed API base URL could disclose credentials or route data elsewhere.

Mitigation: Keep REPORT_GENERATION_API_KEY secret and review AI_SKILLS_API_URL before use.

## Reference(s):

- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/report-generation/API-KEY.md)
- [HTTP requests and task polling](https://ai-skills.open-idea.net/skill-docs/report-generation/HTTP-REQUESTS.md)
- [Metrics and exports](https://ai-skills.open-idea.net/skill-docs/report-generation/OPERATIONS.md)
- [Verification and interpretation rules](https://ai-skills.open-idea.net/skill-docs/report-generation/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Report text and optional Markdown, XLSX, PNG, or PDF exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes validated metrics and charts; partial results are identified and exports are private to the current user.]

## Skill Version(s):

1.0.0 (source: skill metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
