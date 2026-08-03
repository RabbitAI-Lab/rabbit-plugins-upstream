## Description: <br>
Provides Chinese tax policy Q&A, compliance risk screening, tax calculations, contract and invoice review guidance, templates, and report-style remediation guidance backed by a cloud tax knowledge service with offline fallback tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax practitioners, consultants, finance teams, and developers use this skill to ask tax policy questions, screen business scenarios for tax and invoice compliance risk, calculate common tax items, and generate practical compliance guidance or templates. <br>

### Deployment Geography for Use: <br>
Global, with substantive content focused on China tax and compliance topics. <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax, payroll, invoice, contract, or client data may be sent to cloud and search services. <br>
Mitigation: Review the skill before installing it in confidential environments, disclose the cloud service behavior to users, and avoid sending sensitive client data unless the environment is approved for that use. <br>
Risk: First use can create and store a local API key, device ID, cache, and logs. <br>
Mitigation: Restrict local profile access, review the local client data directory after use, and clear stored credentials or logs when operating on shared or regulated machines. <br>
Risk: Enabling TAX_ENABLE_AUTOSETUP can modify local MCP or client configuration files. <br>
Mitigation: Leave automatic setup disabled unless configuration changes are intended, and review generated backups and MCP entries before continuing. <br>
Risk: Fallback search results may be incomplete or unsuitable as authoritative tax advice. <br>
Mitigation: Verify fallback guidance against official tax policy sources or qualified professional review before relying on it for compliance decisions. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/zxj2devs/skills/tax-policy-knowledge) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Tax compliance topic portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-like structured tool responses with optional Python scripts and MCP configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote MCP tools for policy answers, risk checks, tax calculations, and knowledge-base listings; includes local offline reference workflows for limited fallback guidance.] <br>

## Skill Version(s): <br>
3.15.8 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
