## Description: <br>
A Chinese-language tax compliance assistant for medical beauty, gold and jewelry, and related life-service businesses, covering tax policy, revenue recognition, invoice compliance, private-account collection risks, self-check workflows, case analysis, report templates, and practical remediation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business users, tax practitioners, and agents use this skill to answer life-service tax compliance questions, run structured self-checks, identify risk indicators, and draft compliance or remediation guidance for medical beauty, jewelry, prepaid membership, invoicing, and private-account collection scenarios. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax or business information may be sent to the cloud MCP service or fallback search providers. <br>
Mitigation: Use sanitized scenarios where possible, avoid entering taxpayer IDs, bank details, client names, invoice numbers, and audit-sensitive facts, and confirm that use of the cloud service is acceptable before submitting data. <br>
Risk: The skill stores service credentials and client data locally under user-controlled storage locations. <br>
Mitigation: Review and clear ~/.tax-policy-client and browser localStorage when rotating credentials, uninstalling the skill, or working on shared machines. <br>
Risk: Running the initialization script directly or enabling TAX_ENABLE_AUTOSETUP can modify MCP client configuration. <br>
Mitigation: Keep auto-setup disabled unless intentional, review any generated MCP configuration before use, and rely on dry-run behavior for inspection. <br>
Risk: Tax calculations, policy explanations, and risk scores may be incomplete, outdated, or unsuitable for a specific taxpayer's facts. <br>
Mitigation: Treat outputs as decision support, verify material positions against official tax authority sources, and consult qualified tax or legal professionals for filing, audit, dispute, or high-value matters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-life-services) <br>
- [Life services compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_life_services.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured text, with optional JSON-style tool results, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call cloud MCP tools or local fallback workflows; outputs can include risk ratings, policy references, calculations, self-check reports, and remediation checklists.] <br>

## Skill Version(s): <br>
3.15.8 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
