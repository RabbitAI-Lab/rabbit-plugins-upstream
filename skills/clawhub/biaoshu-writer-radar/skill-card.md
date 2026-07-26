## Description: <br>
标书智能制作工具，凭 App Key 调用开放 API 完成评分点应答、投标文件生成、合规审查与报告排版。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Bid and proposal teams use this skill to analyze tender requirements, identify disqualification risks, generate editable bid documents, and review submitted bid files against tender criteria. It is intended for workflows where users provide local tender or bid files and consent to processing by the 百炼标书 service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid documents may contain business, pricing, or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing. <br>
Mitigation: Confirm user consent before upload, use only files the user explicitly provides, and avoid processing cloud links directly. <br>
Risk: The App Key is an account credential and may be stored on disk in config.json. <br>
Mitigation: Keep the App Key out of chat, store it only in the local credential file with restricted permissions, and reset it through the provider if exposed. <br>
Risk: Generated reports, DOCX outputs, and task results may remain locally or in the service account history for a limited period. <br>
Mitigation: Tell users where outputs are written, delete local artifacts when no longer needed, and manage server-side history through the provider account. <br>
Risk: Changing the API base can send files and credentials to a non-default endpoint. <br>
Mitigation: Use the default biaoshu.zhiliaobiaoxun.com endpoint unless the user intentionally trusts an alternate endpoint. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-radar) <br>
- [百炼标书 service](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [API contract reference](references/api.md) <br>
- [Usage reference](references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with generated HTML, Word, and DOCX file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local files selected by the user, a local App Key configuration file, and asynchronous API jobs that may incur account-point charges.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
