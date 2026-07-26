## Description: <br>
通联刷卡手续费发票申请流程：读取客户账单计算上月手续费，填写手续费应收明细和通联发票申请模板，并在用户确认后发送申请邮件。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shouqianba](https://clawhub.ai/user/shouqianba) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Finance and operations users use this skill to prepare Allinpay card-processing fee invoice applications from customer bills, generate the required spreadsheets, and send the request email after review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Externally looked-up or extracted tax and invoice details may be incorrect. <br>
Mitigation: Review the generated spreadsheets and email before sending, especially tax numbers, invoice amounts, invoice type, and customer details. <br>
Risk: Invoice request email could be sent with the wrong recipient or missing attachments. <br>
Mitigation: Confirm the recipient, both attachments, invoice amount, invoice type, and customer details before allowing the agent to send. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shouqianba/skills/tonglian-fee-invoice-apply) <br>
- [Publisher profile](https://clawhub.ai/user/shouqianba) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Text, API Calls, Guidance] <br>
**Output Format:** [Filled spreadsheet files plus confirmation summaries, email subject/body text, and tool-mediated email actions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation before sending email and depends on user-supplied bill data for invoice amounts and recipient details.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
