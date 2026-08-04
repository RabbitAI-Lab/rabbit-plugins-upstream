## Description: <br>
Tax Policy Knowledge helps agents answer Chinese tax-policy questions, assess compliance risks, calculate taxes, and generate checklists, templates, and reports using a cloud-backed tax knowledge service with local fallback guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users can use this skill to support Chinese tax-policy Q&A, tax calculations, compliance self-checks, invoice and contract risk review, and generation of practical checklists or report drafts. It is suited to tax, finance, compliance, and advisory workflows where outputs should be reviewed against official policy and qualified professional judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax, payroll, contract, and business-risk details may be sent to the publisher's cloud service. <br>
Mitigation: Use the skill only with data the organization is approved to send to that service, and avoid confidential client data unless appropriate approvals are in place. <br>
Risk: Raw prompts, local logs, credentials, and API keys may be stored under the local tax-policy client directory. <br>
Mitigation: Review the local ~/.tax-policy-client directory for stored logs and credentials, and apply local retention, access-control, or cleanup practices before production use. <br>
Risk: Optional auto-setup can modify MCP client configuration. <br>
Mitigation: Do not enable TAX_ENABLE_AUTOSETUP or run config/init_agent.py directly unless client configuration changes are intended and have been reviewed. <br>
Risk: The scanner verdict is suspicious because of cloud data transfer, local logging and credential storage, and optional configuration changes. <br>
Mitigation: Perform review before deployment, confirm the publisher's service and data-handling posture, and scan the installed artifact in the target environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-policy-knowledge) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [State Taxation Administration of China](https://www.chinatax.gov.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown text with structured answers, checklists, tax calculations, templates, report drafts, and configuration guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Cloud-backed responses may include policy references, risk levels, and calculations; offline fallback output is limited to local reference and process guidance.] <br>

## Skill Version(s): <br>
3.15.10 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
