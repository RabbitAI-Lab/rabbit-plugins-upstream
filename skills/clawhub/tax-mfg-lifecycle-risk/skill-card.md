## Description: <br>
A ClawHub skill that provides manufacturing lifecycle tax-risk self-checks and guidance for entity formation, operations, R&D deductions, accelerated depreciation, environmental and resource taxes, restructuring, expansion, liquidation, and deregistration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax teams, and compliance reviewers use this skill to ask manufacturing tax questions, run lifecycle risk self-checks, and produce practical checklists for China-focused tax compliance scenarios. Users should verify policy details with official sources before relying on outputs for filing, restructuring, or audit-sensitive decisions. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The release is a cloud-connected tax MCP integration and may transmit company tax facts, restructuring details, tax positions, or audit-sensitive prompts to the aitaxs.top service. <br>
Mitigation: Avoid entering confidential or audit-sensitive information unless the user or administrator accepts that transmission path and has reviewed the service, retention, and access controls. <br>
Risk: The release can persist credentials, browser localStorage values, and JSONL logs related to tax prompts and API use. <br>
Mitigation: Inspect and manage local credential files, browser localStorage credentials, and JSONL logs before use in enterprise or sensitive tax environments. <br>
Risk: The release can modify local MCP client configuration through its auto-setup path when explicitly enabled. <br>
Mitigation: Administrators should inspect or disable auto-setup and review MCP client configuration changes before deploying the skill. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/zxj2devs/skills/tax-mfg-lifecycle-risk) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Manufacturing lifecycle self-check page](https://mcp.aitaxs.top/web/topic_workflow_mfg_lifecycle.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Remote MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with structured checklists, risk summaries, report-style guidance, code snippets, shell commands, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a cloud-connected MCP service and local fallback workflows; users should review any generated guidance before acting on it.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
