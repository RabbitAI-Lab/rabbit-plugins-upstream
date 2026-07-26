## Description: <br>
Queries UpKuaJing customs records by company ID to return trade-partner distribution, HS-code breakdowns, product portfolios, and monthly trade timelines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Export teams, sourcing agents, and trade analysts use this skill to identify trade counterparts, analyze product mix, and map supply-chain relationships from customs data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid API and can initiate account or top-up workflows. <br>
Mitigation: Require explicit user confirmation before fee-incurring queries or payment-related actions, and review pricing with the provided price information command. <br>
Risk: The skill reads and may create an UpKuaJing API key stored in a local plain-text file. <br>
Mitigation: Avoid printing the key file, prefer masked key checks, restrict local file permissions, and revoke or rotate the key when access is no longer needed. <br>
Risk: The skill performs an update check during API requests. <br>
Mitigation: Review network behavior before installation and account for the version-check request in environments with strict outbound-network controls. <br>


## Reference(s): <br>
- [Company Trade Partner Trends API](artifact/references/customs-company-partner-stats-api.md) <br>
- [UpKuaJing homepage](https://www.upkuajing.com) <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-company-partner-stats) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/upkuajing) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns partner distribution, monthly activity, HS-code breakdowns, product distribution, and masked fee information when API calls succeed.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
