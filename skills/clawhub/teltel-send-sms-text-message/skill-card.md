## Description: <br>
Send SMS text messages via TelTel (teltel.io) using the REST API (api.teltel.io). Includes bulk send, delivery report, and bulk sms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[teltel-call-center](https://clawhub.ai/user/teltel-call-center) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to send single or bulk SMS messages through a TelTel account from an agent workflow. It supports TelTel API-key configuration, sender selection, recipient lists, message text, optional callbacks, and dry-run payload inspection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send billable or unintended SMS messages through a TelTel account, especially when used for bulk recipient lists. <br>
Mitigation: Use dry-run or explicit confirmation before bulk sends, confirm recipients and message text, and ensure the TelTel account has appropriate sender verification and spending controls. <br>
Risk: The TelTel API key grants access to the user's messaging account. <br>
Mitigation: Store TELTEL_API_KEY as a sensitive secret, restrict access to the runtime environment, and rotate the key if it is exposed. <br>
Risk: SMS content and recipient numbers may include sensitive personal information. <br>
Mitigation: Send sensitive, regulated, or personal data only when authorized to share it with TelTel and the intended recipients. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/teltel-call-center/skills/teltel-send-sms-text-message) <br>
- [TelTel homepage](https://www.teltel.io/) <br>
- [TelTel API base URL](https://api.teltel.io/v2) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses TELTEL_API_KEY, TELTEL_SMS_FROM, TELTEL_BASE_URL, recipient, message, optional callback, and dry-run controls.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
