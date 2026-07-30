## Description: <br>
A VAT law compliance assistant for China-focused VAT implementation questions, input deduction checks, deemed taxable transaction handling, mixed sales accounting, refund risk review, and structured self-check reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax, finance, and compliance teams use this skill to ask VAT implementation questions, run lightweight self-checks, identify common VAT risk areas, and produce draft compliance guidance or reports for review. <br>

### Deployment Geography for Use: <br>
Global; content is focused on China VAT compliance. <br>

## Known Risks and Mitigations: <br>
Risk: Tax queries and self-check data may be sent to the mcp.aitaxs.top service. <br>
Mitigation: Avoid entering sensitive business details until the remote-service trust, retention, and access model has been reviewed. <br>
Risk: The client can store credentials locally. <br>
Mitigation: Review local credential storage before use and rotate or remove credentials when the skill is no longer needed. <br>
Risk: Optional setup code can modify agent MCP configuration files. <br>
Mitigation: Run configuration setup only when MCP registration is intended; keep dry-run behavior for review before enabling write mode. <br>
Risk: The security scan verdict is suspicious because remote-service use, credential storage, and configuration changes are not clearly disclosed. <br>
Mitigation: Perform a security review before deployment and restrict use to environments where these behaviors are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-vat-law) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [VAT law self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_vat_law.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>
- [Tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Invoice compliance skill](https://skillhub.cn/skills/tax-invoice-compliance) <br>
- [Tax judicial cases skill](https://skillhub.cn/skills/tax-tax-judicial) <br>
- [Tax restructuring skill](https://skillhub.cn/skills/tax-restructuring) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance, JSON tool results, shell/configuration snippets, copied report text, and web self-check prompts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote MCP service, store local client credentials, register MCP configuration when explicitly enabled, and fall back to local reference workflows when offline.] <br>

## Skill Version(s): <br>
3.15.4 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
