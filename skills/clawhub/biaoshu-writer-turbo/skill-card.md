## Description: <br>
新讯标书自动撰写工具通过 App Key 接入百炼标书开放 API，帮助代理解读招标文件、生成投标文件并执行合规审查。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and bid teams use this skill to process local tender and bid documents through the 百炼标书 service for tender interpretation, bid-document drafting, and pre-submission compliance review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing. <br>
Mitigation: Confirm the user understands and agrees to the first-use data disclosure before uploading confidential files. <br>
Risk: Generated bid documents or compliance findings may be incomplete or unsuitable for submission without review. <br>
Mitigation: Have qualified bid staff review generated documents, compliance findings, and any flagged risks before submission. <br>
Risk: The App Key is an account credential and can be exposed through chat, logs, screenshots, or credential-bearing links. <br>
Mitigation: Keep the App Key out of conversation, store it only in the local credential file or approved environment variable, and never forward links that include credential parameters. <br>
Risk: Changing ZCM_BASE can redirect requests to a different endpoint. <br>
Mitigation: Leave ZCM_BASE unset unless the user intentionally trusts the alternate endpoint. <br>
Risk: Uploaded files and generated results are retained under the App Key account for the service's stated retention period. <br>
Mitigation: Use the service account to review and manage retained history, and avoid uploading files unless this retention is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-turbo) <br>
- [百炼标书 platform](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [API contract reference](references/api.md) <br>
- [Usage and operating guide](references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration guidance] <br>
**Output Format:** [Chinese natural-language guidance with local file paths, HTML or Word reports, and .docx bid documents] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-owned App Key; uploads user-selected procurement files to biaoshu.zhiliaobiaoxun.com and writes generated artifacts locally.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
