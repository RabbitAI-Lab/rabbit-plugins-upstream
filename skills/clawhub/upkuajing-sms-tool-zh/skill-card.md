## Description: <br>
对接全球通信运营商发送批量跨境短信，实时查看每条短信的发送状态，助力外贸从业者开展海外营销推广、订单物流通知以及客户精细化触达。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, sales, operations, and customer support teams use this skill to send batch international SMS campaigns or transactional messages and to review task-level and recipient-level delivery status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SMS sending can incur charges and may contact real recipients. <br>
Mitigation: Confirm costs, recipient consent, message content, and recipient lists before any send operation. <br>
Risk: Recipient phone numbers, message content, delivery records, balances, payment links, and the API key are sensitive. <br>
Mitigation: Protect UPKUAJING_API_KEY and ~/.upkuajing/.env, avoid exposing SMS data in shared logs or transcripts, and keep payment links private. <br>
Risk: The skill can request a new API key and create recharge payment orders for the third-party service. <br>
Mitigation: Ask for explicit user confirmation before creating credentials or recharge orders. <br>


## Reference(s): <br>
- [短信发送 API 参考](references/sms-send-api.md) <br>
- [短信任务列表 API 参考](references/sms-task-list-api.md) <br>
- [短信任务明细列表 API 参考](references/sms-task-record-list-api.md) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing SMS pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/upkuajing-sms-tool-zh) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires UPKUAJING_API_KEY; SMS send operations may incur charges.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release and frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
