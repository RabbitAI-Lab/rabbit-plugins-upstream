## Description:

Finds and prioritizes industry reports, market studies, and white papers, providing a sourced reading list with inspected key points and clear access limits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and other readers use this skill to find and rank relevant industry reports, check dates and access, and review points supported by inspected sources. It saves the reading list and source records in JishuDB rather than writing a new industry report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saving report searches and source records grants the skill write access to the selected JishuDB knowledge base.

Mitigation: Approve only the intended knowledge base and retention scope; review saved records and access permissions.

Risk: Optional JishuDB Desktop setup can change local application, data, and client connection settings.

Mitigation: Approve setup only after checking the app and data paths, MCP URL, client configuration target, and publisher or signing information.

Risk: The default search starts with mainland China and may not match the reader's intended market.

Mitigation: Specify or adjust the report-search geography before relying on the reading list.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bowen-aijishu/skills/research-report-hunter)
- [Author-declared skill homepage](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/research-report-hunter)
- [Report discovery and evidence contract](references/evidence-contract.md)
- [199IT report category](https://www.199it.com/archives/category/report)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown files and JishuDB records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ranked reading list, report cards, citations, discovery log, and revision record with access and coverage labels.]

## Skill Version(s):

0.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
