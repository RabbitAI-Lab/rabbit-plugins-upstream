## Description: <br>
Tax Life Services helps users assess Chinese tax compliance questions for life-service businesses such as medical aesthetics providers and gold or jewelry retailers, including invoicing, revenue recognition, private-account collection risk, self-check reports, and practical remediation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and businesses use this skill to ask tax-policy questions, run lightweight compliance self-checks, identify life-service tax risks, and generate practical tax compliance guidance for medical aesthetics, jewelry retail, prepaid memberships, invoices, and private-account collections. It is advisory support only and does not replace licensed tax, audit, or legal advice. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Cloud-backed tax assistance can send user questions and scenario details to the configured remote MCP service. <br>
Mitigation: Review the remote endpoint before use and avoid entering confidential tax, business, or personal details unless the publisher provides acceptable retention and log-handling terms. <br>
Risk: The client stores local credentials and logs under the user's tax-policy client data directory. <br>
Mitigation: Treat the local data directory as sensitive, restrict access to the user account, and clear stored credentials or logs according to local security policy. <br>
Risk: Setup paths can modify MCP client configuration when automatic setup is enabled. <br>
Mitigation: Leave TAX_ENABLE_AUTOSETUP unset unless configuration changes are intended, and review any generated MCP client configuration before using it. <br>
Risk: Tax outputs may be incomplete, stale, or unsuitable for a specific taxpayer or jurisdictional fact pattern. <br>
Mitigation: Use outputs as advisory self-check material and confirm high-impact filings, disputes, or remediation plans with a qualified tax professional or the competent tax authority. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-life-services) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Life-services self-check page](https://mcp.aitaxs.top/web/topic_workflow_life_services.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown and text responses, with optional JSON-like MCP tool results, copied prompts, reports, configuration snippets, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include policy references, risk levels, remediation checklists, tax calculation results, self-check reports, and MCP setup guidance.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
