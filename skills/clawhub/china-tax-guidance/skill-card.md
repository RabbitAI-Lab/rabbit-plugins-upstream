## Description: <br>
Provides China tax filing and compliance guidance for electronic tax bureau workflows, declarations, invoices, tax cancellation, credit repair, calendars, forms, and common questions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax, finance, and operations staff use this skill to ask China tax filing questions and receive step-by-step filing paths, document checklists, form guidance, deadlines, and risk self-check prompts. It is intended as guidance for preparing tax work, not as a substitute for official tax authority instructions or professional representation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and scenarios may be sent to mcp.aitaxs.top, and fallback behavior may send queries to public search engines. <br>
Mitigation: Avoid entering sensitive personal or business tax data; anonymize scenarios before use and review network exposure before deployment. <br>
Risk: The skill includes setup behavior that can modify local MCP client configuration when explicitly enabled. <br>
Mitigation: Do not enable TAX_ENABLE_AUTOSETUP or run setup scripts unless configuration changes are intended; review client configuration backups after testing. <br>
Risk: The skill may store credentials and logs under ~/.tax-policy-client. <br>
Mitigation: Inspect that directory after testing, protect any stored credentials, and remove logs that contain sensitive tax questions. <br>
Risk: Security evidence marks the release suspicious because remote service setup, local configuration changes, credential storage, public-search fallback, and logging are under-disclosed. <br>
Mitigation: Review the security summary before installation and restrict use in environments that handle sensitive tax or business data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/china-tax-guidance) <br>
- [Tax compliance portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Local tax guidance prompt helper](web/topic_workflow_china_tax_guidance.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands, configuration] <br>
**Output Format:** [Markdown or plain text guidance with optional checklists, prompts, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include tax process steps, risk self-check summaries, document lists, filing deadlines, and prompts for deeper analysis.] <br>

## Skill Version(s): <br>
3.15.4 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
