## Description: <br>
Provides digital tax invoice compliance guidance, shell-company false-invoice risk checks, recipient-side supplier screening, four-flow consistency review, abnormal voucher response guidance, and good-faith acquisition defense support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and tax-compliance teams use this skill to assess digital invoice compliance scenarios, screen supplier and transaction evidence, identify false-invoice indicators, and generate practical self-check or remediation guidance. It also helps agents route questions to cloud MCP tax-policy tools or offline fallback workflows when remote service is unavailable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill routes policy questions and risk scenarios to a remote MCP service and may process sensitive invoice, supplier, contract, or tax-risk details. <br>
Mitigation: Use it only in environments where remote processing through mcp.aitaxs.top is approved; redact confidential invoice, supplier, and contract details before use. <br>
Risk: The client persists an API key and local logs under the user's tax-policy client data directory. <br>
Mitigation: Review local storage policies before installation, restrict file permissions where needed, and avoid running the skill on shared workstations with sensitive tax data. <br>
Risk: Setup code can modify MCP client configuration when write mode is explicitly enabled. <br>
Mitigation: Run setup in dry-run mode first and review any proposed MCP configuration changes before enabling write mode. <br>
Risk: Tax guidance can become outdated or may not fit the user's jurisdiction, facts, or formal filing posture. <br>
Mitigation: Treat outputs as compliance support, verify against current tax authority materials and professional advice, and retain source evidence for any filing or audit response. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-invoice-compliance) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Invoice compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_invoice_compliance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [VAT law skill](https://skillhub.cn/skills/tax-vat-law) <br>
- [Tax judicial cases skill](https://skillhub.cn/skills/tax-tax-judicial) <br>
- [Tax compliance dispute skill](https://skillhub.cn/skills/tax-compliance-dispute) <br>
- [Listed-company tax advisory skill](https://skillhub.cn/skills/tax-listed-advisory) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands] <br>
**Output Format:** [Markdown and plain-text guidance with links, structured checklists, risk summaries, and optional configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote MCP tax-policy tools, provide offline fallback guidance, and copy or generate compliance report text for the user.] <br>

## Skill Version(s): <br>
3.15.10 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
