## Description: <br>
Tax Compliance Dispute helps users assess Chinese tax compliance risks, liquidation and cancellation issues, tax audits and disputes, tax-sensitive contract terms, invoice red lines, and dispute-resolution paths. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax professionals, business operators, and compliance teams use this skill to triage Chinese tax-compliance questions, plan audit or dispute responses, review tax-sensitive contract and invoice scenarios, and produce practical self-check or remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax and compliance prompts may be sent to mcp.aitaxs.top and, during fallback, possibly to public search engines. <br>
Mitigation: Avoid entering confidential financial records, litigation strategy, invoice details, or client data unless the backend behavior and retention terms have been reviewed. <br>
Risk: The skill stores API keys and logs under ~/.tax-policy-client. <br>
Mitigation: Review local files under ~/.tax-policy-client before and after use, and remove stored credentials or logs when they are no longer needed. <br>
Risk: Optional setup behavior can modify local MCP client configuration when TAX_ENABLE_AUTOSETUP is enabled or config/init_agent.py is run directly. <br>
Mitigation: Leave automatic setup disabled unless configuration changes are intended, and review generated MCP client configuration before using the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-compliance-dispute) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_dispute.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Analysis, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown responses, structured risk results, offline reference text, Python helper code, and MCP configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote MCP service for tax-policy answers, risk checks, tax calculations, and knowledge-base listings; includes local offline fallback guidance when the remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.10 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
