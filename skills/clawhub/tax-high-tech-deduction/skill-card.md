## Description: <br>
高企认定与研发费用加计扣除专项助手，面向企业高企指标测算、研发费用归集、双口径协同、风险自查、合规报告和资格维持提供政策化 guidance。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, finance, compliance, and enterprise R&D management users use this skill to assess China high-tech enterprise qualification and R&D super-deduction readiness, organize supporting evidence, identify tax-compliance risks, and draft actionable checklists or reports. It supports advisory workflows but does not replace review by qualified tax, legal, or government authorities. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Inputs may be routed to a cloud-backed tax service during policy Q&A, risk checks, calculations, and web self-check workflows. <br>
Mitigation: Use only authorized business data, avoid unnecessary personal, payroll, employee time-clock, or confidential R&D details, and confirm the service's retention and deletion practices before entering sensitive information. <br>
Risk: The client may create persistent local API credentials, cache files, and prompt/action logs. <br>
Mitigation: Protect and periodically review the local client data directory, remove stored credentials or logs when no longer needed, and avoid sharing local support bundles that may contain prompts or business context. <br>
Risk: MCP client configuration can be modified when setup is explicitly enabled or the initialization script is run. <br>
Mitigation: Keep automatic setup disabled unless needed, review proposed MCP configuration entries before enabling them, and verify any generated backups or client config changes. <br>
Risk: Tax conclusions, thresholds, and filing advice are time-sensitive and may be incorrect or incomplete for a specific taxpayer. <br>
Mitigation: Verify outputs against current official policy, competent tax authority guidance, and qualified professional review before filing, claiming incentives, or making compliance decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-high-tech-deduction) <br>
- [High-tech enterprise and R&D deduction interactive workflow](https://mcp.aitaxs.top/web/topic_workflow_high_tech.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Related tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Related tax audit skill](https://skillhub.cn/skills/tax-tax-audit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown text with optional JSON/tool results, checklists, calculation summaries, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include policy citations, risk levels, self-check results, evidence-chain summaries, and draft compliance reports.] <br>

## Skill Version(s): <br>
3.15.6 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
