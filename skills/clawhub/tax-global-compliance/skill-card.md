## Description: <br>
Tax Global Compliance helps organizations assess overseas employment, payroll, tax, transfer-pricing, data-transfer, and related compliance risks for Chinese companies expanding abroad. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business, tax, legal, and compliance teams use this skill to ask scenario-based questions, run self-checks, identify cross-border compliance gaps, and prepare practical next steps before overseas market entry or operations. <br>

### Deployment Geography for Use: <br>
Global, with source material focused on China outbound operations and selected destination countries. <br>

## Known Risks and Mitigations: <br>
Risk: Compliance questions and tool inputs may be sent to a third-party cloud tax service. <br>
Mitigation: Use only with organization-approved data handling, and avoid entering confidential payroll, tax, employee, investment, or cross-border transaction details unless approved. <br>
Risk: The skill can store a local API key and logs under the user's home directory. <br>
Mitigation: Review local storage policy before use, restrict file access where needed, and remove or rotate stored credentials if the skill is no longer approved. <br>
Risk: Optional setup code can modify MCP client configuration files. <br>
Mitigation: Run setup in dry-run mode first, inspect proposed configuration changes, and rely on backups before enabling automatic writes. <br>
Risk: Fallback public search can provide less authoritative or less current tax guidance than the cloud knowledge service. <br>
Mitigation: Treat fallback output as preliminary and verify material compliance decisions against official sources or qualified local professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-global-compliance) <br>
- [Enterprise overseas compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_global_compliance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge MCP service](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown and structured text, with optional local helper output as plain text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route questions to a cloud MCP service and may use local offline fallback guidance when the service is unavailable.] <br>

## Skill Version(s): <br>
3.15.10 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
