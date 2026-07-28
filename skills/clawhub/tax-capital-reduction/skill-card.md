## Description: <br>
减资撤资（未实缴减资）个人所得税专项助手。聚焦公司减资、股东撤资退股、未实缴减资免除出资义务、定向减资（公司回购股权）、减资弥补亏损、新公司法下减资程序与税务衔接，提供不征税论证、个税测算、核定风险预警、合规方案与报告模板。（聚焦未实缴减资、减资个税、新公司法减资与股东撤资税务处理。） <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, finance and tax teams, and advisors use this skill to assess Chinese capital reduction, shareholder withdrawal, unpaid capital reduction, directed capital reduction, and related individual income tax compliance scenarios. It produces risk checks, tax calculation guidance, compliance paths, and report templates for review before acting. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a remote tax-policy service and create persistent service credentials. <br>
Mitigation: Use it only when the publisher and remote service are trusted, and avoid entering sensitive taxpayer or company-identifying details unless necessary. <br>
Risk: The skill can store local logs, persistent identifiers, and API credentials. <br>
Mitigation: Review local storage and log locations before use, and remove saved credentials or logs when they are no longer needed. <br>
Risk: The skill can install related skills and modify MCP client configuration when auto-setup is enabled. <br>
Mitigation: Review the matrix installer, target files, download sources, and auto-setup changes before enabling installation or configuration writes. <br>
Risk: Tax guidance and calculations may be incomplete, jurisdiction-specific, or time-sensitive. <br>
Mitigation: Confirm material transactions with current official policy sources, the competent tax authority, or a qualified tax professional before filing or executing a reduction. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-capital-reduction) <br>
- [Capital reduction self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_capital_reduction.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured text, with optional web self-check results and configuration commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote tax-policy MCP service, use offline fallback guidance, and generate compliance checklists, calculations, and report-style summaries.] <br>

## Skill Version(s): <br>
3.15.3 (source: server release, SKILL.md frontmatter, matrix.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
