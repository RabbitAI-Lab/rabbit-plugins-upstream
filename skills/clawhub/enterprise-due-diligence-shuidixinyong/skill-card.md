## Description: <br>
Enterprise due diligence assistant for light pre-cooperation checks on companies, using bidding records, customer and supplier relationships, competitor overlap, and sourced public risk signals to produce single-company or two-company comparison reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business users and agents use this skill before cooperation, signing, credit terms, or supplier selection to generate a light due diligence report on a company. The skill supports single-company reports and two-company comparisons based on Zhiliaobiaoxun bidding data plus sourced public risk information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts zhiliaobiaoxun.com services and can consume paid or trial credits. <br>
Mitigation: Confirm the expected credit cost before running a report and stop for user approval before exceeding the documented budget. <br>
Risk: The skill checks and may store a service API key in ~/.zlbx/config.json. <br>
Mitigation: Prefer a user-provided ZLBX_API_KEY when available, do not expose credentials in conversation, and review local credential storage before deployment. <br>
Risk: Generated Markdown and HTML reports may contain signed免登录 links that can work for anyone who receives the file or URL. <br>
Mitigation: Treat generated reports as sensitive business documents, store them in controlled locations, and avoid public sharing of report files or signed links. <br>
Risk: Automatic registration collects device characteristics for trial-account deduplication. <br>
Mitigation: Run automatic registration only after explicit user consent and limit collection to the documented platform, architecture, and hashed MAC fields. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/dragonzu/skills/enterprise-due-diligence-shuidixinyong) <br>
- [Workflow guide](artifact/references/workflow.md) <br>
- [API quick reference](artifact/references/api-quick.md) <br>
- [Report template](artifact/references/report-template.md) <br>
- [Automatic registration flow](artifact/references/auto-register.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown due diligence report with an optional self-contained HTML report file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZLBX_API_KEY or explicit-consent automatic registration; may use paid or trial credits; generated reports may include shareable signed links and are saved under ~/zlbx-company-intel-files/.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
