## Description: <br>
个人境外投资合规筹划 helps individuals and tax advisers evaluate China-focused overseas investment tax reporting, foreign tax credit, compliant investment channel, foreign-exchange registration, residency, and CRS consistency questions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and tax advisers use this skill to ask about China-related individual overseas securities, deposits, real estate, residency, foreign tax credit, and compliant investment channel scenarios. It produces policy-grounded guidance, risk self-checks, remediation checklists, and report-style summaries for professional review. <br>

### Deployment Geography for Use: <br>
China-focused <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and self-check metrics may be sent to mcp.aitaxs.top. <br>
Mitigation: Avoid entering personal identifiers, account-level financial details, or unnecessary sensitive facts; review the service destination before use. <br>
Risk: The skill can store an API key and local logs under the user profile. <br>
Mitigation: Treat the local profile data as sensitive, restrict filesystem access, and remove or rotate stored credentials when they are no longer needed. <br>
Risk: Optional matrix installation and client setup code can install related skills or alter supported client configuration. <br>
Mitigation: Run setup or matrix installation only when explicitly intended, review dry-run output first, and keep auto-setup disabled unless configuration changes are desired. <br>
Risk: Tax and compliance outputs may be incomplete or unsuitable for a specific filing or legal dispute. <br>
Mitigation: Use outputs as planning and self-check material, then confirm material tax, foreign-exchange, and legal positions with official sources or qualified professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-individual-overseas) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls] <br>
**Output Format:** [Markdown and plain text guidance, structured JSON from MCP tools, generated checklist/report text, and configuration or shell command snippets when setup workflows are used.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill can use cloud MCP tools for policy answers, risk checks, calculations, and knowledge-base metadata, with local offline reference workflows available when the service is unavailable.] <br>

## Skill Version(s): <br>
3.15.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
