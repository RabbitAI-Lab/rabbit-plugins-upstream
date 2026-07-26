## Description: <br>
This skill lets agents send bulk corporate cold-email campaigns through UpKuaJing and monitor task, delivery, open, click, and read status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sales, export, and sourcing teams use this skill to submit B2B cold-email campaigns and inspect campaign task records and engagement metrics. Agents can also guide users through API-key setup, balance checks, and fee-aware sending workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid bulk-email sends can create unexpected charges or unauthorized outreach. <br>
Mitigation: Confirm campaign purpose, recipient authorization, pricing, account balance, and explicit user approval before any send or top-up action. <br>
Risk: Recipient addresses, message content, reply addresses, account data, and engagement metrics are transmitted to UpKuaJing. <br>
Mitigation: Use the skill only for lawful, authorized B2B campaigns and avoid sending sensitive or unrelated personal data. <br>
Risk: The API key may be stored in plaintext at ~/.upkuajing/.env. <br>
Mitigation: Treat UPKUAJING_API_KEY as a secret, restrict local file permissions, avoid sharing logs or screenshots containing the key, and rotate the key if exposed. <br>
Risk: The skill performs an automatic version check against the UpKuaJing API during requests. <br>
Mitigation: Review network behavior before deployment and account for this outbound check in environments with strict egress controls. <br>


## Reference(s): <br>
- [Email Send API](artifact/references/email-send-api.md) <br>
- [Email Task List API](artifact/references/email-task-list-api.md) <br>
- [Email Task Record List API](artifact/references/email-task-record-list-api.md) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; paid send operations require explicit user confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
