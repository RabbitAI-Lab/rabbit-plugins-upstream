## Description: <br>
离岸信托与跨境家族财富个人所得税专项助手，帮助用户围绕离岸信托个税新规、居民境外所得申报、受控外国企业规则、CRS 合规、反避税衔接和跨境资产传承税务进行结构化合规自检、风险扫描和闭环实操规划。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax professionals, wealth advisers, and developers use this skill to ask offshore trust tax questions, run personal income tax compliance self-checks, identify cross-border wealth tax risks, and prepare structured follow-up checklists or reports. The skill is especially relevant for scenarios involving Chinese individual income tax, offshore trusts, overseas income reporting, CRS information exchange, CFC analysis, and anti-avoidance review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive offshore trust, beneficiary, residency, account, or family-wealth facts may be processed remotely or persisted locally. <br>
Mitigation: Avoid entering identifying documents or granular personal facts unless remote processing and local persistence are acceptable; disclose what data is transmitted, stored, and logged. <br>
Risk: Fallback to public web search can introduce incomplete, stale, or unverified tax guidance. <br>
Mitigation: Disable public-search fallback by default or clearly label fallback answers and require review against official tax authority guidance before action. <br>
Risk: Setup behavior can write MCP client configuration and local files if enabled. <br>
Mitigation: Keep configuration writes explicitly opt-in, show the target files before writing, and preserve backups for any modified client configuration. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zxj2devs/skills/tax-offshore-trust) <br>
- [Interactive Offshore Trust Self-Check](https://mcp.aitaxs.top/web/topic_workflow_offshore_trust.html) <br>
- [Tax Compliance Topic Portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Remote Tax Policy MCP Service](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown text with structured Q&A, risk self-check results, compliance checklists, report-style guidance, and optional setup snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can use remote MCP tools or local fallback/search paths and should be reviewed against current official tax guidance before action.] <br>

## Skill Version(s): <br>
3.15.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
