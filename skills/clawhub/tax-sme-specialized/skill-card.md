## Description: <br>
Provides China-focused tax compliance guidance for specialized and innovative SMEs, including recognition data consistency, R&D expense treatment, fiscal subsidy tax handling, listing-related tax planning, qualification maintenance, related-party pricing, self-checks, and remediation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, finance teams, tax practitioners, and compliance reviewers use this skill to ask China SME tax questions, run structured self-checks, review risk indicators, and draft compliance-oriented guidance or reports for professional review. <br>

### Deployment Geography for Use: <br>
Global, for China-focused tax compliance scenarios <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax, transaction, R&D, related-party, or listing-planning details may be processed by remote services. <br>
Mitigation: Use sanitized prompts or non-confidential examples unless remote processing by mcp.aitaxs.top and fallback searches are approved for the environment. <br>
Risk: The skill creates persistent local credentials and client state under ~/.tax-policy-client. <br>
Mitigation: Review local credential storage before installation, restrict filesystem access where needed, and remove or rotate credentials when the skill is no longer approved. <br>
Risk: MCP client configuration may be changed during setup. <br>
Mitigation: Inspect MCP configuration changes before enabling setup in a business environment and keep backups of existing client configuration. <br>
Risk: Tax guidance and calculations can be incomplete, stale, or unsuitable for a specific filing position. <br>
Mitigation: Verify conclusions against current official sources and obtain qualified professional review before taking tax, legal, financing, or listing-related action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-sme-specialized) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [SME tax compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_sme_specialized.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge matrix](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Remote MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Natural-language text and Markdown, with JSON responses from MCP tools and optional configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP tools and offline fallback workflows; outputs should be reviewed before tax, legal, or business action.] <br>

## Skill Version(s): <br>
3.15.7 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
