## Description: <br>
再生资源/资源回收/废旧物资企业财税政策、反向开票（自然人出售者）、资源综合利用即征即退、简易计税、风险指标、真实案例、报告模板与实操指引专题助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Chinese-speaking resource recycling businesses, tax compliance teams, and advisors use this skill to self-check renewable-resource tax risks, reverse invoicing scenarios, VAT preferential treatment, documentation gaps, and remediation plans. It supports practical guidance and report-style outputs, but its tax and legal conclusions should be confirmed with qualified professionals and official authorities. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send tax prompts and self-check data to remote cloud services. <br>
Mitigation: Avoid entering confidential taxpayer, customer, or transaction details unless the remote service is approved for that data. <br>
Risk: The skill stores local API credentials, browser API keys, cache files, and prompt logs. <br>
Mitigation: Protect and periodically review the local client data directory and browser localStorage; clear stored keys and logs on shared or managed machines. <br>
Risk: The matrix installer can download and install related skills in bulk. <br>
Mitigation: Review the matrix manifest and run installer dry-runs before enabling installation in production or managed environments. <br>
Risk: TAX_ENABLE_AUTOSETUP can allow MCP client configuration writes. <br>
Mitigation: Leave automatic setup disabled unless needed, and review generated MCP configuration changes before use. <br>
Risk: Tax guidance may be incomplete, stale, or not tailored to a specific jurisdiction or taxpayer situation. <br>
Mitigation: Validate material conclusions against official tax authority sources and qualified tax or legal professionals before filing, claiming incentives, or responding to enforcement matters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-renewable) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Renewable-resource self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_renewable.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown and structured text responses with checklists, risk summaries, prompts, reports, and optional code or configuration guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call cloud MCP tools, use local fallback workflows, produce browser self-check reports, and guide installation of related tax skills.] <br>

## Skill Version(s): <br>
3.15.3 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
