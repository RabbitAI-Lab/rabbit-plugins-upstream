## Description: <br>
建筑工程商机雷达 helps agents find early construction and infrastructure opportunities by searching proposed projects, procurement intents, and expiring service contracts, then ranking opportunities with follow-up guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business-development, sales, and construction-market users use this skill to discover earlier-stage engineering opportunities by region, sector, budget threshold, and project maturity. It produces prioritized opportunity lists with objective next steps for proposed projects, procurement intents, and contract-renewal windows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms, regions, and opportunity criteria are sent to the vendor API. <br>
Mitigation: Use the skill only when that disclosure is acceptable, and avoid entering confidential bid strategy or customer-sensitive context as search input. <br>
Risk: Automatic trial registration may send a hashed MAC-based device identifier and persist credentials locally. <br>
Mitigation: Prefer manually setting ZLBX_API_KEY; if using auto-registration, review the consent prompt and local credential file handling. <br>
Risk: Generated HTML reports and returned sk links may provide direct access to opportunity details. <br>
Mitigation: Treat reports and links as sensitive business documents and do not publish or forward them broadly. <br>
Risk: Scheduled monitoring can continue to consume account credits and repeatedly send search criteria. <br>
Mitigation: Disable cron or /loop schedules when monitoring is no longer needed and review expected credit use before scans. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/construction-project-opportunity-radar) <br>
- [Workflow Manual](references/workflow.md) <br>
- [API Quick Reference](references/api-quick.md) <br>
- [Report Template](references/report-template.md) <br>
- [Auto-Registration Flow](references/auto-register.md) <br>
- [Zhiliaobiaoxun API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool}) <br>
- [Zhiliaobiaoxun Opportunity Platform](https://agent.zhiliaobiaoxun.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown opportunity list, optional self-contained HTML report, and concise guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include ranked opportunity tables, data-source notes, API-derived links, and optional report files.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
