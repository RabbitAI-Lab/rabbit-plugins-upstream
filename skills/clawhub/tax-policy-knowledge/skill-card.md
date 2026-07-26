## Description: <br>
Provides Chinese tax policy Q&A, tax calculations, invoice and contract compliance review, risk self-checks, and remediation/report guidance for enterprises and tax advisors. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business users, finance teams, CFOs, internal audit teams, tax advisors, and consulting firms use this skill to ask Chinese tax policy questions, calculate common taxes, identify invoice, contract, and operating-compliance risks, and produce self-check reports, remediation checklists, and contract templates. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, risk scenarios, and calculation inputs may be sent to the provider cloud endpoint and possibly to public search engines during fallback. <br>
Mitigation: Redact or anonymize client, payroll, invoice, bank, investigation, and other confidential details, and review the provider's privacy and retention practices before use. <br>
Risk: Credentials and raw prompts may be stored locally. <br>
Mitigation: Treat local configuration and log locations as sensitive, avoid shared machines for confidential work, and rotate or revoke API keys if exposure is suspected. <br>
Risk: The matrix installer and auto-setup features can modify local MCP or client configuration. <br>
Mitigation: Run setup in dry-run mode first, verify download sources, and enable TAX_ENABLE_AUTOSETUP only when local configuration changes are intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-policy-knowledge) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Tax compliance web portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax Policy Knowledge MCP endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown or plain text responses with optional structured lists, tables, calculations, reports, contract templates, configuration guidance, and shell commands for setup workflows.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a provider cloud MCP endpoint and may fall back to local web search when the remote service or API key is unavailable.] <br>

## Skill Version(s): <br>
3.14.38 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
