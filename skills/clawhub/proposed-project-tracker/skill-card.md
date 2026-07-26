## Description: <br>
拟建项目跟踪与早期商机发现助手，用于查询发改立项/审批公示阶段项目、采购意向和临期续约机会，并输出按价值排序的商机清单。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business development and sales teams use this skill to find early public-sector and enterprise opportunity signals by industry, product, region, budget threshold, and project stage. It scans proposed projects, purchase intentions, and expiring contracts, then prepares a prioritized opportunity report with follow-up actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends opportunity-search keywords and regional filters to the Zhiliaobiaoxun API. <br>
Mitigation: Use it only for queries acceptable to share with that service, and avoid entering confidential customer strategy or private deal information. <br>
Risk: The skill can persist an API key in ~/.zlbx/config.json and uses ZLBX_API_KEY when provided. <br>
Mitigation: Protect the local config file, avoid pasting API keys into chat, and rotate the key if it is exposed. <br>
Risk: Generated reports and opportunity links may include signed sk parameters that can bypass login for details pages. <br>
Mitigation: Treat exported reports and links as private access material, and review URLs before forwarding or publishing reports. <br>
Risk: Opportunity reports are generated from third-party API data that can be incomplete, delayed, or commercially sensitive. <br>
Mitigation: Validate high-value opportunities against source records before outreach or bidding decisions, and keep the report disclaimer with exported files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/proposed-project-tracker) <br>
- [Publisher profile](https://clawhub.ai/user/dragonzu) <br>
- [Workflow reference](references/workflow.md) <br>
- [API quick reference](references/api-quick.md) <br>
- [Report template reference](references/report-template.md) <br>
- [Auto-registration reference](references/auto-register.md) <br>
- [Zhiliaobiaoxun API endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{工具名}) <br>
- [Zhiliaobiaoxun agent portal](https://agent.zhiliaobiaoxun.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, HTML files, API calls, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown opportunity lists and optional locally generated HTML reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved auto-registration; reports may include API-returned signed links and are written under ~/zlbx-opportunity-radar-files/.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
