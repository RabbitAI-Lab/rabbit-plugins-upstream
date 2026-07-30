## Description: <br>
Tax Invoice Compliance helps agents provide Chinese digital invoice compliance self-checks, false-invoice risk screening, four-flow consistency checks, abnormal voucher response guidance, and remediation checklists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax compliance staff, and agent operators use this skill to triage Chinese digital invoice compliance questions, screen supplier and invoice risk, prepare self-check workflows, and draft compliance reports or remediation guidance. It is a support tool for review and documentation, not a substitute for tax authority determinations or licensed professional advice. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Cloud MCP and web self-check flows may process sensitive tax, invoice, supplier, or dispute information through mcp.aitaxs.top. <br>
Mitigation: Review the provider and data-handling terms before use, avoid entering sensitive identifiers unless necessary, and use offline workflows for reduced local guidance when cloud processing is not acceptable. <br>
Risk: The client can store service credentials, cache state, and diagnostic logs locally, including tax question text or risk scenarios. <br>
Mitigation: Run in a controlled user profile, inspect or clear local client data after sensitive work, and avoid shared machines for confidential client or dispute matters. <br>
Risk: Optional auto-setup can modify MCP client configuration when explicitly enabled. <br>
Mitigation: Keep auto-setup in dry-run mode unless configuration changes are intended, review generated MCP entries and backups, and restrict configuration writes in managed environments. <br>
Risk: Tax compliance guidance can be incomplete, time-sensitive, or unsuitable for a final filing, audit, or legal position. <br>
Mitigation: Treat outputs as screening and drafting assistance, verify cited policy positions against official tax authority sources, and involve qualified tax or legal professionals for material decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-invoice-compliance) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Interactive invoice compliance workflow](https://mcp.aitaxs.top/web/topic_workflow_invoice_compliance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Remote MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown-style answers, structured JSON tool results, plain-text compliance reports, and optional shell command output from offline workflows.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP or web services for policy answers, risk checks, calculations, and self-check workflows; offline workflows provide reduced local guidance when remote services are unavailable.] <br>

## Skill Version(s): <br>
3.15.5 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
