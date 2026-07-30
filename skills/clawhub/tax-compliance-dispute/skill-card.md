## Description: <br>
Provides tax compliance and dispute-resolution assistance for internal tax controls, company liquidation and deregistration, audit response, tax administrative remedies, contract tax-clause review, invoice compliance checks, and related criminal tax-risk self-assessment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and advisors use this skill to triage tax compliance questions, prepare self-checklists, understand dispute-response paths, and generate structured compliance guidance before consulting qualified tax or legal professionals for high-stakes matters. <br>

### Deployment Geography for Use: <br>
Global; content focuses on China tax compliance and dispute workflows. <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and self-check metrics may be sent to mcp.aitaxs.top. <br>
Mitigation: Use minimized or anonymized facts for exploratory checks, and review the publisher and data-handling expectations before entering real company identifiers or highly sensitive dispute details. <br>
Risk: The client stores API credentials and logs in plaintext under the user profile. <br>
Mitigation: Treat the local profile storage as sensitive, restrict filesystem access, and remove or rotate stored credentials and logs when the skill is no longer needed. <br>
Risk: Optional setup code can register an MCP endpoint in supported AI clients. <br>
Mitigation: Keep setup in dry-run mode unless registration is intended, and review client configuration changes and backups before enabling persistent MCP integration. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-compliance-dispute) <br>
- [Tax compliance dispute self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_dispute.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown and structured text with checklists, risk classifications, workflow steps, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP-backed tax policy, risk-check, calculation, and knowledge-list tools with offline fallback guidance when the service is unavailable.] <br>

## Skill Version(s): <br>
3.15.4 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
