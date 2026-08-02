## Description: <br>
tax-industry-tax-risk helps users map and self-check tax risks in high-risk industry scenarios, including fuel invoice manipulation, network freight false invoicing, logistics tax risks, commodity circular trading, and tax-incentive-zone compliance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external tax and compliance professionals, and developers use this skill to ask tax-risk questions, run structured self-checks, and generate checklist-style guidance for industry tax compliance scenarios. The outputs are advisory and should be checked against current official rules and qualified professional advice before use in material decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, scenarios, and self-check data may be sent to mcp.aitaxs.top and possibly to search engines during fallback. <br>
Mitigation: Do not enter confidential taxpayer, customer, or transaction data unless that remote transmission is approved for the intended environment. <br>
Risk: API keys, identifiers, logs, and health or cache state may persist in ~/.tax-policy-client or browser localStorage. <br>
Mitigation: Clear ~/.tax-policy-client and relevant browser localStorage when removing the skill or when persisted state is no longer appropriate. <br>
Risk: Running config/init_agent.py directly can modify MCP client configuration. <br>
Mitigation: Review the configuration changes first and keep setup in dry-run mode unless MCP client modification is intended. <br>
Risk: Tax-risk outputs are advisory and may be incomplete, outdated, or inapplicable to a specific jurisdiction or fact pattern. <br>
Mitigation: Confirm material conclusions against current official tax rules and qualified tax or legal professionals before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-industry-tax-risk) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Industry tax-risk self-check page](https://mcp.aitaxs.top/web/topic_workflow_industry_tax_risk.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured text with optional code, shell-command, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote MCP endpoints and provide offline fallback guidance; outputs are advisory, not legal or tax opinions.] <br>

## Skill Version(s): <br>
3.15.7 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
