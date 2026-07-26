## Description: <br>
Generates company background-investigation reports from a tendering and procurement perspective, using Zhiliao Biaoxun bid data to summarize business focus, customer and supplier relationships, winning history, competitors, and public-risk notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement, sales, due-diligence, and analyst users provide one or two company names and receive a tender-data-based company intelligence report. The skill supports single-company reports, two-company comparisons, optional contact lookup, and local HTML report generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A third-party provider receives submitted company queries. <br>
Mitigation: Use the skill only for company lookups approved for processing by Zhiliao Biaoxun, and review the provider relationship before installation. <br>
Risk: The skill stores API credentials locally. <br>
Mitigation: Prefer a managed ZLBX_API_KEY where available, restrict local credential-file access, and rotate the key if logs or reports expose account details. <br>
Risk: Automatic free-trial registration uses device-hash signals. <br>
Mitigation: Decline automatic registration or preconfigure ZLBX_API_KEY if device-based trial registration is not acceptable. <br>
Risk: Generated HTML reports can contain shareable signed links. <br>
Mitigation: Avoid sharing generated reports, screenshots, or logs unless recipients are allowed to access embedded signed links. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/zhiliao-company-intel) <br>
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun) <br>
- [API quick reference](artifact/references/api-quick.md) <br>
- [Seven-step workflow](artifact/references/workflow.md) <br>
- [Report template](artifact/references/report-template.md) <br>
- [Automatic registration workflow](artifact/references/auto-register.md) <br>
- [Zhiliao Biaoxun API endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool}) <br>
- [Zhiliao Business Platform](https://agent.zhiliaobiaoxun.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown company intelligence report plus a local self-contained HTML report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved automatic registration; generated reports may include shareable signed links.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
