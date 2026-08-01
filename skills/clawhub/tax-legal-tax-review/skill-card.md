## Description: <br>
Guides Chinese tax and legal review workflows for pre-transaction tax due diligence, tax clauses in deal documents, tax-related legal templates, Audit Standard 1142 tax procedures, forensic accounting quality control, and integrated legal-finance-tax review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business, legal, finance, tax, and compliance users use this skill to structure Chinese tax due diligence, draft or review tax-related deal documents, run legal-tax self-checks, and produce risk-focused compliance guidance. It is advisory support and does not replace licensed tax, audit, or legal professionals. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax or legal questions and self-check values may be sent to mcp.aitaxs.top. <br>
Mitigation: Use the skill only after organizational approval of that endpoint and avoid confidential deal, litigation, tax exposure, or client-identifying facts. <br>
Risk: Local and browser credentials or identifiers may be stored for MCP access. <br>
Mitigation: Review the local and browser storage model before use, restrict access to stored credentials, and clear them when the skill is no longer needed. <br>
Risk: Optional setup can modify local MCP client configuration. <br>
Mitigation: Do not enable TAX_ENABLE_AUTOSETUP or run config/init_agent.py directly unless the configuration change is intentional and reviewed. <br>
Risk: Fallback search and advisory outputs may be incomplete or out of date for high-stakes tax and legal decisions. <br>
Mitigation: Confirm material conclusions against current official sources and licensed tax, audit, or legal professionals before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-legal-tax-review) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Legal-tax review self-check page](https://mcp.aitaxs.top/web/topic_workflow_legal_tax_review.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON-like structured results, plain text guidance, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote MCP service for policy answers, risk checks, tax calculations, and knowledge-base metadata; includes local and browser self-check flows.] <br>

## Skill Version(s): <br>
3.15.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
