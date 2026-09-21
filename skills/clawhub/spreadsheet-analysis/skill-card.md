## Description:

Analyzes XLSX and UTF-8 CSV files, summarizes tables, answers questions from cell contents, compares spreadsheets, and can export results with worksheet and row evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect, summarize, question, compare, and export evidence-backed findings from spreadsheet files. It is not intended for legacy XLS files, encrypted spreadsheets, macro execution, or non-UTF-8 CSV input.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Extracted spreadsheet text and row evidence are sent to ai-skills.open-idea.net for processing and billing.

Mitigation: Use the skill only on spreadsheets the user is authorized to process, and avoid confidential, regulated, or personal data unless the platform's data handling terms are acceptable.

Risk: Spreadsheet cell contents, formulas, and macros can contain untrusted instructions or misleading data.

Mitigation: Treat spreadsheet contents only as evidence, do not execute macros or formulas, and verify cited findings against the referenced worksheet rows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/spreadsheet-analysis)
- [AI Skills platform homepage](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/spreadsheet-analysis/API-KEY.md)
- [Local spreadsheet extraction](https://ai-skills.open-idea.net/skill-docs/spreadsheet-analysis/LOCAL-EXTRACTION.md)
- [HTTP requests](https://ai-skills.open-idea.net/skill-docs/spreadsheet-analysis/HTTP-REQUESTS.md)
- [Operations](https://ai-skills.open-idea.net/skill-docs/spreadsheet-analysis/OPERATIONS.md)
- [Evidence and safety rules](https://ai-skills.open-idea.net/skill-docs/spreadsheet-analysis/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown and JSON with worksheet and row evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a local extraction script for XLSX and UTF-8 CSV files, then sends extracted cell text and row locations to the platform API.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
