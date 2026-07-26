## Description: <br>
This skill helps bid teams interpret tender documents, draft finished .docx bid files, format bid responses, and review submissions for compliance through the 百炼标书 API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External bid teams and agent users use this skill to analyze tender requirements, generate editable bid documents, and check bid submissions for disqualification or compliance risks. It is intended for workflows where users explicitly provide local tender or bid files and authorize processing by the 百炼标书 service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid files may contain commercial, pricing, or personal information and are uploaded to the 百炼标书 service for processing. <br>
Mitigation: Confirm user consent before upload and use the skill only for files the user is authorized to send to that service. <br>
Risk: Uploaded files and generated results are retained under the user's App Key account for about 7 days. <br>
Mitigation: Use the skill only when that retention is acceptable, and direct users to manage history through the service account when needed. <br>
Risk: The App Key is a full account credential for the service. <br>
Mitigation: Keep the App Key out of chat and store it only in the local config file as instructed by the release evidence. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-corp-pro) <br>
- [API contract reference](references/api.md) <br>
- [Usage and operations guide](references/usage.md) <br>
- [百炼标书 service](https://biaoshu.zhiliaobiaoxun.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text or Markdown guidance, progress/status text, generated .docx bid documents, and HTML or Word reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated bid documents and reports are file outputs; cloud-side task results are retained by the service for about 7 days under the user's App Key account.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
