## Description: <br>
Provides China-focused tax and legal co-review guidance for transaction tax due diligence, tax-related legal documents, audit-standard implementation, forensic accounting quality checks, and integrated legal-finance-tax review workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business, legal, finance, and tax teams use this skill to structure China tax/legal due diligence, draft or review tax-related deal materials, run risk self-checks, and generate compliance-oriented reports. It is a decision-support aid and does not replace licensed tax, audit, or legal advice. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports remote processing by mcp.aitaxs.top for tax, legal, diligence, or transaction data. <br>
Mitigation: Avoid entering privileged client facts or confidential transaction details unless the publisher's data handling terms are acceptable. <br>
Risk: The security review reports persistent local API credentials and logs. <br>
Mitigation: Inspect, restrict, rotate, or remove credentials and logs under ~/.tax-policy-client before and after use in sensitive environments. <br>
Risk: The security review reports optional MCP client configuration changes. <br>
Mitigation: Keep automatic setup disabled unless needed, review TAX_ENABLE_AUTOSETUP before installation, and inspect any generated MCP configuration changes. <br>
Risk: Artifact behavior and skill documentation state that tax calculations, policy guidance, and risk scores are reference material rather than legal, audit, or tax opinions. <br>
Mitigation: Have qualified professionals and official tax authority sources verify conclusions before filings, disputes, transactions, or other high-impact decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zxj2devs/skills/tax-legal-tax-review) <br>
- [Legal Tax Review Self-Check Page](https://mcp.aitaxs.top/web/topic_workflow_legal_tax_review.html) <br>
- [Tax Compliance Self-Check Portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Remote MCP Endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>
- [Tax Policy Knowledge Matrix](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, API Calls, Configuration] <br>
**Output Format:** [Markdown and JSON-like structured tool responses, with optional text reports and local configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses remote MCP tools for policy Q&A, risk checks, tax calculations, and knowledge-base listing; includes local offline reference and fallback guidance.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
