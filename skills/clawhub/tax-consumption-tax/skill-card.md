## Description: <br>
电池消费税合规与政策指引 helps users understand battery consumption tax rates, exemption conditions, CMA report prerequisites, processing/import deductions, self-use filing, compliance self-checks, and risk scans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, compliance, and finance users use this skill to ask battery consumption tax questions and receive checklist-style guidance for rates, exemptions, CMA evidence, tax deduction accounting, and transfer-use filing. It also supports lightweight compliance self-checks, risk scans, and report-oriented follow-up prompts. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The security summary identifies a cloud-backed tax service with under-disclosed remote service behavior. <br>
Mitigation: Use the skill only when remote processing is acceptable, and avoid confidential company identifiers or sensitive tax scenarios unless the remote data flow is understood. <br>
Risk: The security summary identifies local credential and log storage. <br>
Mitigation: Review local files under ~/.tax-policy-client during use and remove stored credentials or logs when they are no longer needed. <br>
Risk: The security summary identifies configuration-change and related skill installation behavior. <br>
Mitigation: Review added MCP settings and files under ~/.skills after installation or invocation, and remove unwanted configuration if uninstalling. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-consumption-tax) <br>
- [Battery consumption tax self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_consumption_tax.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with links, checklists, structured guidance, optional shell commands, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce compliance self-check summaries, risk scan guidance, and report-oriented follow-up prompts.] <br>

## Skill Version(s): <br>
3.15.3 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
