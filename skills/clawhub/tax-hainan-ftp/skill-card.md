## Description: <br>
Helps assess Hainan Free Trade Port tax incentives, substantive-operation requirements, and compliance risks for self-checks, reports, and remediation planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, finance, and compliance users can use this skill to ask Hainan Free Trade Port tax-policy questions, run lightweight risk self-checks, and generate practical compliance checklists or self-assessment reports. It is supporting guidance and does not replace review by tax authorities, certified tax advisers, lawyers, or auditors. <br>

### Deployment Geography for Use: <br>
China (Hainan Free Trade Port tax context) <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, scenarios, or self-check metrics may be sent to the remote service at mcp.aitaxs.top. <br>
Mitigation: Use anonymized or minimized scenarios unless the organization has approved that data flow; avoid confidential taxpayer, payroll, transaction, and corporate-structure details when approval is absent. <br>
Risk: The client can persist API credentials, cache files, and logs locally under the user's tax-policy client data directory. <br>
Mitigation: Review and protect the local data directory, rotate or remove credentials when no longer needed, and clear logs before using shared or unmanaged machines. <br>
Risk: Optional setup code can modify local MCP client configuration. <br>
Mitigation: Keep setup in dry-run mode until reviewed, enable automatic configuration only intentionally, and inspect created backups and MCP entries after setup. <br>
Risk: Tax calculations, risk ratings, and policy explanations may be incomplete or become outdated. <br>
Mitigation: Treat outputs as supporting material and confirm material filing, audit, dispute, or planning decisions with current official sources and qualified tax or legal professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-hainan-ftp) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Hainan FTP self-check page](https://mcp.aitaxs.top/web/topic_workflow_hainan_ftp.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge hub](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown and plain text responses, with optional JSON tool results and copied or exported self-check reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include risk levels, checklists, policy references, remediation steps, MCP setup snippets, and offline fallback guidance.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
