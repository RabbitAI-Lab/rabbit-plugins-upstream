## Description:

Spreadsheet Analysis helps agents analyze XLSX and UTF-8 CSV files, summarize tables, answer questions from cell content, compare spreadsheets, and export results with worksheet and row evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to extract spreadsheet text locally, submit supported cell content for analysis, ask evidence-grounded questions, compare two or three spreadsheet files, and export completed analysis results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Parsed spreadsheet contents are sent to the configured platform service after local extraction.

Mitigation: Confirm user authorization before processing sensitive spreadsheets and disclose that extracted cell text leaves the local machine.

Risk: A configurable API destination can redirect spreadsheet text and the API key.

Mitigation: Keep AI_SKILLS_API_URL unset or pinned to the intended HTTPS service and protect SPREADSHEET_ANALYSIS_API_KEY from logs and chat output.

Risk: Crafted or unusually compressed XLSX files could exhaust local resources during extraction.

Mitigation: Avoid untrusted XLSX files until archive-expansion limits are added, and enforce the documented 10 MB file-size limit.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/spreadsheet-analysis)
- [AI Skills homepage](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/spreadsheet-analysis/API-KEY.md)
- [Local spreadsheet extraction](https://ai-skills.open-idea.net/skill-docs/spreadsheet-analysis/LOCAL-EXTRACTION.md)
- [HTTP requests](https://ai-skills.open-idea.net/skill-docs/spreadsheet-analysis/HTTP-REQUESTS.md)
- [Operations](https://ai-skills.open-idea.net/skill-docs/spreadsheet-analysis/OPERATIONS.md)
- [Behavior rules](https://ai-skills.open-idea.net/skill-docs/spreadsheet-analysis/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and JSON analysis results with worksheet and row references, plus local extraction commands and configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports XLSX and UTF-8 CSV files up to 10 MB, 2000 non-empty rows, and 120000 extracted characters.]

## Skill Version(s):

1.0.1 (source: server release metadata and artifact metadata.packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
