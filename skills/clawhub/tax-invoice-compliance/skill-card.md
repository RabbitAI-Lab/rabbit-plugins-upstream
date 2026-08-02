## Description: <br>
Assists with China digital invoice compliance, false-invoice risk screening, four-flow consistency checks, abnormal voucher response, and practical self-check reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, finance teams, tax staff, and developers use this skill to ask invoice-compliance questions, run invoice risk self-checks, and produce practical remediation guidance for supplier screening, four-flow validation, abnormal voucher handling, and archiving. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan verdict is suspicious because the skill uses cloud-backed tax-policy processing and local client integration beyond the core invoice-compliance guidance. <br>
Mitigation: Install only when the user trusts the mcp.aitaxs.top service and understands that tax questions or self-check data may be processed by that service. <br>
Risk: The packaged client can store local credentials, cache data, and logs for MCP service access. <br>
Mitigation: Avoid submitting confidential invoice, supplier, or tax-investigation details unless the service and local storage behavior are acceptable for the deployment. <br>
Risk: The initialization code can modify MCP client configuration when explicitly run or when TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Do not run config/init_agent.py or set TAX_ENABLE_AUTOSETUP unless configuration changes are intentional and have been reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-invoice-compliance) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Invoice compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_invoice_compliance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Cloud MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, API Calls, Configuration] <br>
**Output Format:** [Markdown and structured text, with optional JSON responses from MCP-backed tools] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return compliance checklists, risk summaries, tax-policy answers, calculation results, and configuration guidance.] <br>

## Skill Version(s): <br>
3.15.7 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
