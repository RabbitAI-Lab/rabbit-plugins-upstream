## Description: <br>
Send NEAR reports and alerts via email with SMTP configuration, scheduling, and automatic reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shaiss](https://clawhub.ai/user/shaiss) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and NEAR account operators use this skill to configure SMTP settings, generate NEAR account balance reports, and prepare email-based alerts or scheduled reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SMTP passwords are entered on the command line and saved locally. <br>
Mitigation: Use an app-specific SMTP password, avoid setup on shared machines, clear shell history after using --pass when appropriate, and verify ~/.near-email/config.json permissions. <br>
Risk: Alerts and scheduled reports may not send automatically because the included script notes that these features require additional email or scheduling setup. <br>
Mitigation: Test reports, alerts, and schedules manually before relying on them for operational notifications. <br>


## Reference(s): <br>
- [Near Email Reporter Skill Page](https://clawhub.ai/shaiss/skills/near-email-reporter) <br>
- [Publisher Profile](https://clawhub.ai/user/shaiss) <br>
- [Nodemailer](https://nodemailer.com/) <br>
- [NEAR RPC API](https://docs.near.org/api/rpc) <br>
- [Gmail App Passwords](https://myaccount.google.com/apppasswords) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with CLI commands and generated plain-text NEAR account reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores SMTP configuration in ~/.near-email/config.json and queries NEAR mainnet RPC for account balance reports.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
