## Description: <br>
Provides an industry tax-risk map for identifying, diagnosing, and planning mitigations for high-risk tax scenarios including fuel-station invoice substitution, network freight false invoicing, logistics risk, commodity trade round-tripping, related-party transactions, and tax-preferential-zone substance requirements. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and tax or compliance professionals use this skill to ask scenario-specific questions and run structured self-checks for industry tax risk, with outputs that help identify risk level, supporting evidence gaps, and remediation priorities. It is reference guidance only and does not replace licensed tax, audit, or legal advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and self-check data may be sent to mcp.aitaxs.top cloud services. <br>
Mitigation: Use the skill only where that data flow is acceptable, and do not submit secrets, confidential client data, or regulated personal data. <br>
Risk: Credentials and logs may be stored under ~/.tax-policy-client. <br>
Mitigation: Review and clear stored keys or logs after use, and apply local access controls before using the skill on shared systems. <br>
Risk: Auto-configuration behavior can modify local MCP client settings when explicitly enabled. <br>
Mitigation: Do not enable TAX_ENABLE_AUTOSETUP or run init_agent.py directly unless local MCP configuration changes are intended and reviewed. <br>
Risk: Fallback web searches and tax guidance can be incomplete, outdated, or unsuitable for a specific filing or dispute. <br>
Mitigation: Verify material conclusions against official tax sources and qualified tax, audit, or legal professionals before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-industry-tax-risk) <br>
- [Industry tax-risk self-check page](https://mcp.aitaxs.top/web/topic_workflow_industry_tax_risk.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Comprehensive tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown text with structured risk matrices, checklists, self-check summaries, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use cloud MCP services and fallback web search; outputs are advisory and require professional verification for tax, audit, or legal decisions.] <br>

## Skill Version(s): <br>
3.15.10 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
