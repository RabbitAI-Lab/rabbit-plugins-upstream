## Description: <br>
Tax Compliance Dispute helps users assess Chinese tax compliance, liquidation, audit, invoice, contract tax-clause, and tax-dispute risks and generate practical remediation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business professionals use this skill to ask tax compliance and dispute questions, perform structured self-checks, review high-risk tax scenarios, and prepare practical response or remediation steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive company, tax audit, invoice, dispute, or legal facts may be sent to cloud MCP services or the web self-check workflow. <br>
Mitigation: Review the skill before installation and avoid entering sensitive identifiers or confidential facts unless external processing is acceptable. <br>
Risk: Fallback behavior may send user questions to public search engines when the primary cloud service is unavailable. <br>
Mitigation: Use the offline reference workflow for confidential scenarios or avoid submitting confidential details when fallback search may be triggered. <br>
Risk: Local logs, configuration, and API keys may be stored under ~/.tax-policy-client, and the web workflow stores an API key in browser local storage. <br>
Mitigation: Use trusted devices, periodically review or clear local skill data and browser storage, and avoid shared environments for sensitive work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-compliance-dispute) <br>
- [Structured compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_dispute.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text, Configuration, Shell commands] <br>
**Output Format:** [Markdown text with structured checklists, risk ratings, links, and optional shell-tool output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use cloud MCP services and a web self-check workflow when online; includes offline reference scripts for limited local guidance.] <br>

## Skill Version(s): <br>
3.15.8 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
