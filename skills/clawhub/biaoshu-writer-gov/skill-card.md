## Description: <br>
AI 投标文件写作围绕「看懂—写出—查错」三步展开：读招标文件时提炼评分点和硬性门槛，写作时按章节生成可交付的投标文件(.docx)，收尾时做合规与雷同自查、规避低级废标。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business proposal teams use this skill to interpret tender documents, generate editable bid documents, and review bid submissions for compliance and similarity risks through the disclosed 百炼®标书 API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and proposal files can contain confidential business, pricing, and personal information and are uploaded to the disclosed 百炼®标书 service. <br>
Mitigation: Use the skill only after the user understands and accepts the upload; share only files intended for processing by that service. <br>
Risk: Generated results and uploaded files are retained under the App Key account for about 7 days. <br>
Mitigation: Review account retention expectations before use and manage historical data through the service account when needed. <br>
Risk: The local App Key is a credential for the linked account. <br>
Mitigation: Have the user create the local config file themselves, keep the key out of chat, and rotate it from the service if exposed. <br>
Risk: Bid document generation may consume account credits. <br>
Mitigation: Check the linked account balance before generation and confirm paid actions before submitting long-running jobs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-gov) <br>
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666) <br>
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [百炼®标书开放 API 契约参考](references/api.md) <br>
- [执行细节（操作手册）](references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, structured status text, and generated DOCX/HTML/Word files with absolute file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a locally configured App Key; generation may bill the linked account and can take more than 10 minutes.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
