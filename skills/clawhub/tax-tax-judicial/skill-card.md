## Description: <br>
A tax judicial-case and dispute-ruling guidance skill focused on Chinese tax crime, false VAT invoice sentencing and non-criminalization rules, downstream invoice recipient appeal rights, mechanical tax assessment challenges, and structured tax dispute self-checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and tax-compliance practitioners use this skill to ask Chinese tax judicial and dispute questions, run lightweight risk self-checks, and produce practical guidance for evidence preparation, review, appeal, litigation, and internal remediation workflows. It is guidance-oriented and does not replace licensed legal, tax, criminal-defense, or litigation representation. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive taxpayer, company, dispute, or criminal-risk facts may be sent to remote MCP services or public search fallback paths. <br>
Mitigation: Use anonymized prompts, avoid privileged case details, and review the skill before using it with real matters. <br>
Risk: Local API credentials, cache, health state, and logs are stored under the user's tax policy client data directory. <br>
Mitigation: Treat those local files as sensitive, restrict access, and rotate or remove credentials when the skill is no longer needed. <br>
Risk: The optional setup path can change MCP client configuration when explicitly enabled. <br>
Mitigation: Do not enable TAX_ENABLE_AUTOSETUP or run setup directly unless the user accepts the configuration changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-tax-judicial) <br>
- [Tax judicial workflow page](https://mcp.aitaxs.top/web/topic_workflow_tax_judicial.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge MCP endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance, JSON-like MCP tool results, optional console text, and copied self-check report text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP tools, a browser workflow page, or offline reference scripts depending on availability.] <br>

## Skill Version(s): <br>
3.15.8 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
