## Description: <br>
企业出海全球合规指引专项助手，帮助中国企业梳理主要海外投资目的地的用工、薪酬、税务、转让定价、数据跨境、反洗钱、反腐败、知识产权和外资安全审查等合规事项。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business, tax, legal, HR, and compliance teams use this skill to ask scenario-based questions about overseas expansion and to draft practical checklists for country labor rules, payroll and tax, transfer pricing, data export, investment entry, anti-corruption, anti-money-laundering, and IP risk. It is a guidance aid and should be reviewed against current official sources and qualified local professional advice before action. <br>

### Deployment Geography for Use: <br>
Global, with source material focused on China outbound investment and examples for the United States, Saudi Arabia, Indonesia, Mexico, and Brunei. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send compliance, tax, payroll, and business-risk questions to a third-party backend at mcp.aitaxs.top. <br>
Mitigation: Use it only when that data handling is acceptable for the organization; avoid entering sensitive company identifiers or confidential facts unless approved. <br>
Risk: The skill stores API credentials locally under the tax policy client configuration area. <br>
Mitigation: Review local credential storage before installation, restrict access to the user profile, and remove stored credentials when the skill is no longer used. <br>
Risk: The init_agent.py helper can modify MCP client configuration when run intentionally or when TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Do not run config/init_agent.py or set TAX_ENABLE_AUTOSETUP=1 unless client configuration changes are intended; review backups and resulting MCP server entries. <br>
Risk: Cross-border compliance guidance may be incomplete or outdated for a specific jurisdiction or transaction. <br>
Mitigation: Verify outputs against current official sources and qualified local legal, tax, HR, or compliance advisers before operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-global-compliance) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [SkillHub topic workflow](https://skillhub.cn/skills/tax-global-compliance) <br>
- [Tax policy knowledge matrix](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration, Shell commands] <br>
**Output Format:** [Conversational text and Markdown checklists, with optional local configuration snippets or shell commands for MCP setup.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a third-party MCP service for policy Q&A, risk checks, tax calculations, and knowledge-base metadata; includes offline reference scripts for limited fallback guidance.] <br>

## Skill Version(s): <br>
3.14.38 (source: frontmatter and server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
