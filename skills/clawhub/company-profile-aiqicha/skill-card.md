## Description: <br>
Generates company intelligence reports from tendering and bidding evidence, including business focus, award strength, customers, suppliers, competitors, public-risk notes, and optional two-company comparisons. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business analysts use this skill to investigate a company from a tendering perspective, producing single-company due diligence reports or two-company comparisons based on public procurement and vendor API data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill calls vendor APIs and sends company search terms or report parameters outside the local environment. <br>
Mitigation: Use it only when vendor API use is acceptable, and avoid entering confidential company or project information unless approved. <br>
Risk: The skill stores API credentials locally and can provision a trial account after collecting device-fingerprint signals. <br>
Mitigation: Prefer a preconfigured ZLBX_API_KEY where possible, review the local credential file, and require explicit user consent before auto-registration. <br>
Risk: Generated HTML reports and platform links may include signed access URLs suitable for sharing. <br>
Mitigation: Treat generated report files and signed links as sensitive and share them only with intended recipients. <br>
Risk: Optional contact lookup may expose contact data returned by the vendor service. <br>
Mitigation: Request contact lookup only when needed, preserve vendor-provided masking, and avoid bulk exporting contact lists. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/company-profile-aiqicha) <br>
- [API quick reference](artifact/references/api-quick.md) <br>
- [Workflow guide](artifact/references/workflow.md) <br>
- [Report template](artifact/references/report-template.md) <br>
- [Auto-registration flow](artifact/references/auto-register.md) <br>
- [Zhiliaobiaoxun API endpoint pattern](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool_name}) <br>
- [Zhiliaobiaoxun user portal](https://agent.zhiliaobiaoxun.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown reports with optional generated HTML files and concise user guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses vendor API calls, may write local report files, and requires or can provision a ZLBX_API_KEY after user consent.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
