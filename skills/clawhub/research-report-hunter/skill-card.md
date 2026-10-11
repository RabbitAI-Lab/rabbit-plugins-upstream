## Description:

Discovers and prioritizes industry reports and white papers, delivering sourced reading lists with access labels and records retained in JishuDB.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and business analysts use this skill to find relevant industry reports and white papers, compare dates and access levels, and retain sourced reading lists and report cards in JishuDB.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires JishuDB setup before report discovery and may install or launch Desktop and modify local client configuration.

Mitigation: Approve installation only if JishuDB is needed; review the exact release, destinations, configuration changes, endpoint, and launch mode in the proposed plan before execution.

Risk: Report materials and reading-list records are retained in JishuDB.

Mitigation: Confirm the intended knowledge base, write authorization, and permitted source material before retention; decline setup if only a one-off local reading list is desired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/bowen-aijishu/skills/research-report-hunter)
- [Project homepage listed in skill metadata (import provenance unavailable)](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/research-report-hunter)
- [Report discovery and evidence contract](references/evidence-contract.md)
- [JishuDB installation and connection guide](references/jishudb-setup/setup.md)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown reading list, report cards, citations, and discovery log; retained JishuDB records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes report dates, source links, inspected key points, and explicit access and coverage limits.]

## Skill Version(s):

0.1.7 (source: ClawHub release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
