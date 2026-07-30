## Description: <br>
A tax compliance assistant for specialized and innovative SMEs that helps agents provide structured self-checks, tax treatment guidance for government grants, R&D and high-tech qualification checks, pre-listing tax planning, related-party transaction review, and remediation planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax, finance, and compliance users use this skill to ask SME-focused Chinese tax compliance questions and receive structured guidance, risk checks, self-check workflows, and remediation-oriented outputs. It is intended for planning and review support, with final policy positions verified against official sources or qualified professionals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses cloud processing by mcp.aitaxs.top for online tax policy, risk-check, and calculation workflows. <br>
Mitigation: Review before installing in environments that handle confidential tax, payroll, financing, listing, or related-party information, and avoid submitting sensitive client data unless cloud processing is approved. <br>
Risk: The artifact can store credentials and logs locally, including browser localStorage tokens for the web workflow and plaintext local client files. <br>
Mitigation: Use a dedicated test profile or controlled workspace, inspect stored tokens and logs after use, and clear local browser or client storage where required by policy. <br>
Risk: The skill includes optional MCP client configuration changes through config/init_agent.py. <br>
Mitigation: Do not run config/init_agent.py directly unless MCP configuration changes are intended; review generated MCP settings before enabling automatic setup. <br>
Risk: Fallback search behavior may query public search engines. <br>
Mitigation: Avoid entering confidential facts into fallback searches and prefer verified official tax sources for final decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zxj2devs/skills/tax-sme-specialized) <br>
- [Interactive SME Tax Compliance Workflow](https://mcp.aitaxs.top/web/topic_workflow_sme_specialized.html) <br>
- [Tax Compliance Self-Check Portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Comprehensive Tax Policy Knowledge Skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [High-Tech Enterprise and R&D Super Deduction Skill](https://skillhub.cn/skills/tax-high-tech-rd) <br>
- [IPO Tax Compliance Skill](https://skillhub.cn/skills/tax-ipo-compliance) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown or plain text guidance with optional structured checklists, reports, links, and Python command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct users to a web workflow and may use remote MCP tools or offline fallback scripts depending on availability.] <br>

## Skill Version(s): <br>
3.15.4 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
