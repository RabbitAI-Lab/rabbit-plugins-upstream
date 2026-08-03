## Description: <br>
Tax Crossborder helps users assess cross-border e-commerce and trade tax compliance, including import/export tax, export refunds, withholding tax, CRS checks, foreign tax credits, beneficial-owner questions, Hainan Free Trade Port rules, and VIE or red-chip structure tax risks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax teams, finance teams, and compliance reviewers use this skill to get structured cross-border tax guidance, risk self-checks, calculation support, and report-style action lists. The skill is advisory and should be reviewed against official tax authority guidance and qualified professional advice before filing or making material tax decisions. <br>

### Deployment Geography for Use: <br>
China and cross-border transactions involving China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax questions and self-check metrics may be sent to the provider's cloud service. <br>
Mitigation: Avoid entering confidential company, identity, ownership, transaction, or filing details unless the publisher clarifies retention, search fallback, log handling, and the tax-policy-knowledge backend relationship. <br>
Risk: The skill can store local API credentials and logs. <br>
Mitigation: Review local credential and log storage before use in managed environments, restrict file access, and rotate or remove stored keys and logs when no longer needed. <br>
Risk: Optional setup behavior can change local MCP client configuration. <br>
Mitigation: Leave automatic setup disabled unless the configuration change has been reviewed, and inspect backups plus MCP client settings before enabling it. <br>
Risk: Tax calculations, policy answers, and risk scores may be incomplete or stale for a specific taxpayer, region, or transaction. <br>
Mitigation: Treat outputs as advisory triage, verify important conclusions against official tax authority sources, and consult qualified tax or legal professionals before filing or executing a material plan. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-crossborder) <br>
- [Cross-border tax compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_crossborder.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Related tax-policy-knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with optional structured tax calculations, risk checks, checklists, links, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route users to a hosted self-check page and may provide offline fallback guidance when cloud services are unavailable.] <br>

## Skill Version(s): <br>
3.15.8 (source: frontmatter and server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
