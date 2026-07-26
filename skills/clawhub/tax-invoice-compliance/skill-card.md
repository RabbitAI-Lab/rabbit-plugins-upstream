## Description: <br>
A digital tax-invoice compliance assistant for identifying shell-company false-invoice risk, checking four-flow consistency, and guiding abnormal voucher response and good-faith defense preparation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Finance, tax, and compliance users use this skill to self-check digital invoice workflows, screen supplier and shell-company invoice risk, verify contract-invoice-fund-logistics consistency, and prepare evidence-oriented next steps for abnormal vouchers. It provides compliance guidance and structured self-checks; final tax positions should be confirmed against current authority guidance and qualified professional advice. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Remote processing by mcp.aitaxs.top may handle invoice, supplier, contract, or tax-investigation details. <br>
Mitigation: Avoid submitting confidential records unless approved for remote processing; use non-sensitive summaries or the offline reference workflows for preliminary review. <br>
Risk: The client can persist API keys, client identifiers, and logs locally, including browser localStorage and the ~/.tax-policy-client directory. <br>
Mitigation: Protect local profiles and clear stored keys or logs when no longer needed, especially on shared or regulated machines. <br>
Risk: Optional matrix installation and auto-setup can modify local skills or MCP/client configuration directories. <br>
Mitigation: Do not run the installer or enable TAX_ENABLE_AUTOSETUP unless those local configuration changes are intended; review dry-run output and target paths first. <br>
Risk: Tax compliance guidance can become outdated or differ by facts and authority interpretation. <br>
Mitigation: Confirm material conclusions against current tax-authority guidance and qualified professional advice before filing, responding to an audit, or taking a legal position. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-invoice-compliance) <br>
- [Interactive invoice compliance self-check](https://mcp.aitaxs.top/web/topic_workflow_invoice_compliance.html) <br>
- [SkillHub tax invoice compliance page](https://skillhub.cn/skills/tax-invoice-compliance) <br>
- [Tax policy knowledge matrix download entry](https://api.skillhub.cn/api/v1/download?slug=tax-invoice-compliance) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown guidance with structured checklists, links, and optional web self-check results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP/API calls for current tax-policy answers and risk checks; includes limited offline reference workflows.] <br>

## Skill Version(s): <br>
3.14.38 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
