## Description: <br>
员工持股平台（有限合伙/公司型/资管型）财税合规专项助手，帮助 users analyze ESOP platform tax compliance, deferred taxation, partnership-platform tax treatment, dividend retention, share-based payment, nominee-shareholding, listing-review, reduction-sale, reporting, risk, and practical calculation scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax professionals, finance teams, and company operators use this skill to draft ESOP-platform tax analyses, compare platform structures, identify compliance risks, prepare report-style guidance, and run lightweight tax calculations for Chinese employee shareholding scenarios. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax, compensation, equity-plan, and listing-preparation questions may be sent to the aitaxs.top tax-policy backend. <br>
Mitigation: Avoid entering confidential identifiers or sensitive deal details unless the provider's data handling has been reviewed and approved. <br>
Risk: Local MCP client setup can modify user configuration when automatic setup is enabled. <br>
Mitigation: Do not enable TAX_ENABLE_AUTOSETUP unless local MCP client configuration changes are intended; review backups and generated configuration before use. <br>
Risk: The skill includes under-disclosed local logging, stored-key, and fallback web-search behavior. <br>
Mitigation: Check ~/.tax-policy-client for stored keys or logs and disable or review fallback web search before using the skill for sensitive scenarios. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-esop-platform) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [ESOP self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_esop.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, plain text, generated report text, Python or shell snippets, and configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include compliance checklists, tax-comparison tables, risk summaries, report outlines, offline fallback outputs, and links to web workflows.] <br>

## Skill Version(s): <br>
3.15.10 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
