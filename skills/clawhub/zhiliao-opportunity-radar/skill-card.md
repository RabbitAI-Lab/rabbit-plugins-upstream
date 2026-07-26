## Description: <br>
商机雷达 helps users discover early business opportunities from proposed projects, procurement intentions, and expiring contracts, then ranks the results and provides next-step actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business-development, sales, and market-research users can scan an industry, product, and region for earlier-stage public-sector and enterprise opportunities. The skill produces ranked opportunity lists with source links, estimated API-credit usage, recommended follow-up actions, and optional local HTML reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: If no API key is configured, the skill may automatically register a trial account using device features and persist the returned key locally. <br>
Mitigation: Review the registration behavior before installation and set ZLBX_API_KEY yourself to avoid automatic registration and local key creation. <br>
Risk: Opportunity-search terms are sent to zhiliaobiaoxun.com services. <br>
Mitigation: Avoid submitting confidential search terms unless the vendor relationship and data handling are acceptable. <br>
Risk: The skill writes HTML reports under the user's home directory and stores credentials in ~/.zlbx/config.json when using local configuration. <br>
Mitigation: Protect or remove generated reports and credential files according to the user's endpoint security policy. <br>
Risk: Ranked opportunity recommendations may influence sales or market decisions. <br>
Mitigation: Review source links, dates, budgets, and data gaps before acting on the generated opportunity list. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/zhiliao-opportunity-radar) <br>
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun) <br>
- [Workflow reference](artifact/references/workflow.md) <br>
- [API quick reference](artifact/references/api-quick.md) <br>
- [Auto-registration reference](artifact/references/auto-register.md) <br>
- [Report template](artifact/references/report-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Files, Shell commands, Configuration] <br>
**Output Format:** [Markdown opportunity list plus optional locally written HTML report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZLBX_API_KEY or uses the vendor's documented automatic registration flow; full scans are documented as consuming about 8-15 API credits.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
