## Description: <br>
各类型拟上市与上市公司全生命周期财税顾问与内控框架专项助手。覆盖板块定位与上市路径论证、上市前财税规范与历史清理、内控框架设计与内控鉴证、股改涉税、资本运作涉税、境外架构与外汇登记、持续督导与定期报告涉税披露、股权激励与员工持股平台。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business users and professional advisers use this skill to structure tax, internal-control, disclosure, listing-path, restructuring, cross-border, and equity-incentive guidance for listed and listing-preparation companies. It is intended to support analysis, checklists, calculations, report-style outputs, and implementation guidance, not to replace licensed audit, tax, legal, or regulatory filings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud-backed tax assistance can transmit sensitive company, shareholder, financing, tax audit, or internal-control details to mcp.aitaxs.top. <br>
Mitigation: Avoid entering confidential or regulated details unless transmission to the remote service has been approved; redact or generalize sensitive facts before use. <br>
Risk: The security evidence notes local logging and credential storage under ~/.tax-policy-client. <br>
Mitigation: Review local retention expectations before installation, restrict access to the user data directory, and clear logs or cached configuration under the user's retention policy. <br>
Risk: Optional auto-setup behavior can persist MCP configuration changes in supported AI clients when explicitly enabled. <br>
Mitigation: Keep setup in dry-run mode unless intentional; enable TAX_ENABLE_AUTOSETUP or write-mode setup only after reviewing the target client configuration. <br>
Risk: Tax and listing guidance may be incomplete or unsuitable for a specific issuer, transaction, or jurisdiction. <br>
Mitigation: Treat outputs as advisory drafts and have qualified tax, audit, legal, or regulatory professionals review conclusions before filing, disclosure, or execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-listed-advisory) <br>
- [Interactive listed-company tax workflow](https://mcp.aitaxs.top/web/topic_workflow_listed_advisory.html) <br>
- [Tax compliance topic portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON-like structured results, plain text guidance, Python code, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call cloud-backed MCP tools and may provide offline fallback workflow guidance when the remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.8 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
