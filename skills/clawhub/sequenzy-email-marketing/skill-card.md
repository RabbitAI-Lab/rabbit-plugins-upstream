## Description: <br>
Primary agent guide for operating Sequenzy as an email-marketing platform across authentication, subscribers, campaigns, sequences, templates, team operations, webhooks, transactional email, stats, and supported-workflow checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[polnikale](https://clawhub.ai/user/polnikale) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and marketing teams use this skill to guide an agent through Sequenzy email-marketing workflows, including account checks, subscriber management, campaign and sequence creation, lifecycle control, delivery stats, webhooks, API keys, and product feedback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives agents broad production email-marketing powers, including subscriber changes, campaign lifecycle control, webhooks, API-key creation, team invitations, product uploads, and feedback submission. <br>
Mitigation: Require explicit user approval before campaign cancel/delete, scheduling sends, team invitations, API-key creation, webhook changes, subscriber bulk changes, product file uploads, or feedback submissions. <br>
Risk: Campaign cancellation can stop scheduled, paused, waiting-approval, or sending campaigns immediately without a confirmation prompt. <br>
Mitigation: Inspect the target campaign and confirm the intended action with the user before running cancellation or other destructive lifecycle commands. <br>
Risk: Generated API keys and webhook signing secrets are sensitive one-time outputs. <br>
Mitigation: Store generated secrets only in an approved secret manager or non-versioned local file, and redact raw values from chat, logs, tickets, and public transcripts. <br>


## Reference(s): <br>
- [Sequenzy skill page](https://clawhub.ai/polnikale/skills/sequenzy-email-marketing) <br>
- [Command reference](references/command-reference.md) <br>
- [Use cases](references/use-cases.md) <br>
- [Sequenzy application](https://sequenzy.com) <br>
- [Sequenzy API](https://api.sequenzy.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, markdown] <br>
**Output Format:** [Markdown guidance with CLI and MCP command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include dashboard URLs, JSON-oriented command flags, and redacted handling notes for sensitive outputs.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
