## Description: <br>
Helps users identify and self-check industry-specific Chinese tax risk scenarios, including fuel-station invoice changes, freight-platform false invoicing, logistics risks, commodity trading, and tax-incentive-zone compliance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax professionals, finance teams, compliance reviewers, and business operators use this skill to frame Chinese industry tax-risk questions, run self-checks, and receive structured risk indicators, policy-source prompts, case comparisons, and remediation guidance. Its outputs are reference guidance and should be reviewed by qualified tax, audit, or legal professionals before filing, dispute, or enforcement decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, scenarios, self-check data, and metrics may be sent to the remote mcp.aitaxs.top service, and fallback behavior may query public search engines. <br>
Mitigation: Avoid entering confidential taxpayer, employee, transaction, investigation, or filing details unless the user has approval to disclose them to those services. <br>
Risk: The skill stores local configuration, persistent identifiers, API credentials, caches, and raw logs under the user's home directory. <br>
Mitigation: Review and clear ~/.tax-policy-client configuration, cache, and log files according to the user's retention and credential-handling requirements. <br>
Risk: Optional auto-setup can modify AI-client MCP configuration when TAX_ENABLE_AUTOSETUP is enabled or the setup script is run intentionally. <br>
Mitigation: Leave auto-setup disabled unless MCP configuration changes are intended, and review any client configuration backups or merged entries before use. <br>
Risk: Tax-risk answers are reference guidance and may be incomplete, outdated, or unsuitable for a specific filing, audit, dispute, or enforcement matter. <br>
Mitigation: Verify conclusions against official tax authority sources and qualified tax, audit, or legal professionals before acting on material matters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-industry-tax-risk) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance and JSON-like MCP tool responses, with optional shell commands and configuration snippets for MCP setup or offline utilities.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP services, local fallback search summaries, cached responses, and offline tax-rate or risk-keyword references.] <br>

## Skill Version(s): <br>
3.15.4 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
