## Description: <br>
Generates company background-check reports from a bidding and tendering perspective, including business profile, customers and suppliers, bidding strength, competitors, public risk signals, and optional company comparisons. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business users, procurement teams, sales teams, and agents use this skill to investigate a named company through public bidding and tendering data. It is suited for single-company diligence, supplier review, competitor context, and two-company comparisons. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Company queries are sent to the third-party 知了标讯 service and may consume account credits. <br>
Mitigation: Use only for company queries the user is comfortable sharing with the service, and disclose expected credit use before starting a report. <br>
Risk: Generated reports and returned platform links may contain signed access parameters such as sk or sid. <br>
Mitigation: Treat exported reports and signed links as sensitive, and share them only with recipients who should have equivalent access. <br>
Risk: The skill can store credentials and generated reports locally. <br>
Mitigation: Protect ~/.zlbx/config.json and the local report output directory, and avoid committing exported reports or credentials to shared repositories. <br>
Risk: Company diligence reports may be incomplete or misleading if public bidding data, public web sources, or scanner-visible evidence are incomplete. <br>
Mitigation: Keep conclusions tied to cited data, state data gaps clearly, and verify important findings through official or primary sources before business decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dragonzu/skills/company-background-check-qixinbao) <br>
- [Workflow Guide](artifact/references/workflow.md) <br>
- [API Quick Reference](artifact/references/api-quick.md) <br>
- [Report Template](artifact/references/report-template.md) <br>
- [Automatic Registration Flow](artifact/references/auto-register.md) <br>
- [知了标讯 API Endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/) <br>
- [知了标讯 Registration and Recharge](https://ai.zhiliaobiaoxun.com/?ch=s114) <br>
- [知了商机大师](https://agent.zhiliaobiaoxun.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown company intelligence report with an optional self-contained HTML report file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-approved trial registration; generated reports may be written under ~/zlbx-company-intel-files/.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
