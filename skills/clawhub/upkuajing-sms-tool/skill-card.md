## Description: <br>
Send global bulk SMS with two-way replies and monitor delivery status through UpKuaJing task reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, sales, operations, and customer support teams use this skill to send paid cross-border SMS campaigns, enable two-way replies, and check delivery task status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid SMS sending can incur charges. <br>
Mitigation: Confirm pricing and obtain explicit user approval before executing send operations. <br>
Risk: Bulk messaging can create legal, consent, or abuse risk. <br>
Mitigation: Confirm recipient consent, applicable messaging rules, and message content before sending. <br>
Risk: The skill handles phone numbers, message content, delivery records, and an API key. <br>
Mitigation: Limit exposure of recipient data and keep ~/.upkuajing/.env private with restrictive file permissions. <br>


## Reference(s): <br>
- [SMS Send API](references/sms-send-api.md) <br>
- [SMS Task List API](references/sms-task-list-api.md) <br>
- [SMS Task Record List API](references/sms-task-record-list-api.md) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python, httpx, and UPKUAJING_API_KEY for authenticated API calls.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
