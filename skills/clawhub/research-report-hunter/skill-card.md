## Description:

Discovers and prioritizes industry reports and white papers, delivering sourced reading lists with inspected findings, dates, links, and clear access labels retained in JishuDB.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and other readers use this skill to find and compare relevant industry reports, with citations and honest distinctions between metadata, summaries, and accessible full text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The required JishuDB setup may install software and change the agent client's connection configuration.

Mitigation: Review the proposed release, destinations, configuration target, local connection URL, and Windows unsigned-installer notice; approve the specific plan before execution or decline setup.

Risk: Source imports and generated report records persist in JishuDB.

Mitigation: Confirm the destination and retention scope before transferring sources or saving outputs; keep private material out of public searches.

Risk: Search results and restricted reports may not support claimed findings or full-text access.

Mitigation: Label what was actually inspected, cite public sources, and do not imply unrestricted access to PDFs or unread content.

## Reference(s):

- [Research Report Hunter release](https://clawhub.ai/bowen-aijishu/skills/research-report-hunter)
- [Research Report Hunter project page](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/research-report-hunter)
- [Evidence and access contract](artifact/references/evidence-contract.md)
- [JishuDB setup guide](artifact/references/jishudb-setup/setup.md)
- [199IT report category](https://www.199it.com/archives/category/report)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [Markdown reading list, report cards, citations, discovery log, and revision notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Source records and output are retained in an authorized JishuDB knowledge base; report access and inspection limits are labeled.]

## Skill Version(s):

0.1.8 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
