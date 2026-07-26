## Description: <br>
通联终端申请（增终）和通联增商（新增子商户）工作流。当有新门店需要申请刷卡终端，或集团商户下需要新增子商户时使用。流程：查询通联商户号、制作申请表、生成邮件，并在用户确认后发送给毛晓丽。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shouqianba](https://clawhub.ai/user/shouqianba) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business operations employees use this skill to prepare Tonglian terminal and sub-merchant application materials, generate standardized email text, and send the request only after user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated spreadsheets and email drafts may contain merchant numbers, store details, addresses, contact names, and phone numbers. <br>
Mitigation: Review all generated files and email text before approving the send action. <br>
Risk: The workflow can transmit business application materials to an external recipient. <br>
Mitigation: Send email only after the user explicitly confirms that the attachments, recipient, and message are correct. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shouqianba/skills/tonglian-terminal-application) <br>
- [Publisher profile](https://clawhub.ai/user/shouqianba) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files] <br>
**Output Format:** [Markdown guidance, email draft text, and prepared spreadsheet files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user review and explicit confirmation before sending email.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
