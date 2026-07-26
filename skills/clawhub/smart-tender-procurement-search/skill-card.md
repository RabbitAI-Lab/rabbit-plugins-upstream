## Description: <br>
Searches tender and procurement information across announcements using keywords, geography, amount, time, industry, advanced logic, bid details, company analysis, and market analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and business users use this skill to retrieve tender notices, procurement details, expiring recurring projects, company intelligence, and market summaries from Zhiliaobiaoxun APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: First use without a configured ZLBX_API_KEY can automatically register the device, send local device and user metadata to a remote service, and store an API key under ~/.zlbx/config.json. <br>
Mitigation: Configure a user-managed ZLBX_API_KEY before use when automatic registration or local credential persistence is not acceptable. <br>
Risk: Company-intelligence and contact features can return business relationship and project contact information that may be sensitive in some environments. <br>
Mitigation: Review whether contact lookup and company-intelligence workflows are appropriate for the deployment environment before enabling the skill. <br>
Risk: The authoritative security verdict marks the release as suspicious because of automatic registration, remote identifier transmission, and credential storage. <br>
Mitigation: Review the skill before installing, and limit deployment to environments where those behaviors are understood and approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/smart-tender-procurement-search) <br>
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun) <br>
- [Tender search API details](references/api-search.md) <br>
- [Company analysis API details](references/api-company.md) <br>
- [Market analysis API details](references/api-market.md) <br>
- [Auto-registration flow](references/auto-register.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration, guidance] <br>
**Output Format:** [Markdown summaries with JSON API request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or read a local API key configuration and call remote Zhiliaobiaoxun services.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
