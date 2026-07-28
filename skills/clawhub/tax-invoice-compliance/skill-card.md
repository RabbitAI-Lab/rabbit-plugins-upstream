## Description: <br>
数电票合规与空壳虚开防范专项助手，帮助用户完成供应商筛查、四流一致校验、异常凭证应对、善意取得抗辩和发票合规自检。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and tax or compliance teams use this skill to ask invoice-risk questions, run structured self-checks, and prepare practical remediation guidance for digital invoices, suspected false invoicing, abnormal vouchers, fund-flow consistency, and archive readiness. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, scenarios, and self-check metrics may be sent to the remote service and, in fallback paths, public search engines. <br>
Mitigation: Do not enter confidential invoice, supplier, dispute, or taxpayer details unless those data flows are approved for the environment. <br>
Risk: Credentials, cache, and logs may be stored locally under ~/.tax-policy-client. <br>
Mitigation: Review local storage practices before managed deployment, protect generated API keys, and clear local data according to organizational policy. <br>
Risk: Setup and installer tooling can make persistent MCP configuration changes or bulk-install related skills into ~/.skills. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP disabled and avoid installer/setup scripts unless persistent changes are intended and reviewed. <br>
Risk: Tax guidance is time-sensitive and does not determine audit, penalty, or litigation outcomes. <br>
Mitigation: Confirm material conclusions against current tax authority guidance or qualified professional advice before filing, dispute response, or remediation decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-invoice-compliance) <br>
- [Invoice compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_invoice_compliance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown and plain text responses, with JSON for tool responses and local configuration when setup is enabled] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can produce self-check reports, risk summaries, remediation checklists, MCP configuration guidance, and offline fallback guidance.] <br>

## Skill Version(s): <br>
3.15.3 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
