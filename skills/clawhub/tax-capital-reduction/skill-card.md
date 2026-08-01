## Description: <br>
This skill helps users assess China personal income tax and compliance risks for company capital reductions, shareholder withdrawals, unpaid-capital reductions, targeted reductions, loss-offset reductions, and New Company Law process alignment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, corporate tax teams, and compliance staff use this skill to triage capital-reduction tax questions, calculate potential individual income tax exposure, identify procedural risks, and draft practical self-check or remediation guidance. It is oriented to China tax and company-law scenarios and does not replace professional tax, legal, filing, or registration services. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, scenarios, and self-check data may be sent to mcp.aitaxs.top or handled through public-search fallback paths. <br>
Mitigation: Use anonymized or minimized facts for sensitive matters, avoid highly sensitive personal or company details unless the data flow is acceptable, and verify important conclusions against official sources or a qualified adviser. <br>
Risk: The skill can create local API-key, configuration, cache, or log files under the user's home directory or browser storage. <br>
Mitigation: Review local files and browser storage after use, clear them on shared devices, and avoid installing where persistent local credentials are not acceptable. <br>
Risk: Optional setup paths can modify MCP client configuration when explicitly enabled or when setup scripts are run directly. <br>
Mitigation: Keep setup in dry-run mode unless the configuration change is intended, review client configuration before and after enabling setup, and rely on backups where available. <br>
Risk: The skill provides tax compliance analysis and calculations that may depend on changing policy or local enforcement practice. <br>
Mitigation: Treat outputs as preliminary guidance, confirm current rules and local practice before acting, and escalate material transactions to a qualified tax or legal professional. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zxj2devs/skills/tax-capital-reduction) <br>
- [Capital Reduction Self-Check Workflow](https://mcp.aitaxs.top/web/topic_workflow_capital_reduction.html) <br>
- [Tax Compliance Self-Check Portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax Policy Knowledge Skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown and structured text with optional copied report or prompt content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include tax calculations, risk self-check findings, remediation suggestions, links to self-check workflows, and MCP/client configuration guidance.] <br>

## Skill Version(s): <br>
3.15.6 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
