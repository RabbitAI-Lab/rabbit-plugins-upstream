## Description: <br>
标书自动撰写工具 helps agents interpret tender files, generate formatted bid documents, and run bid-compliance reviews through the 百炼®标书 cloud service using a locally stored App Key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to process procurement workflows: interpret tender documents, generate editable bid documents, and review bid files for compliance risks. It is intended for users who accept uploading tender and bid files to the 百炼®标书 cloud service and managing an App Key locally. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing. <br>
Mitigation: Use the skill only after the user understands and accepts cloud processing and retention by the service. <br>
Risk: The App Key is a full account credential stored locally by the user. <br>
Mitigation: Do not ask users to paste or repeat the App Key in chat; keep it in local config only and delete or rotate it when no longer needed. <br>
Risk: A malicious or untrusted API base override could redirect sensitive files or credentials. <br>
Mitigation: Avoid untrusted ZCM_BASE overrides and keep network access limited to the declared 百炼®标书 service domain. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-swift) <br>
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666) <br>
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [API contract reference](references/api.md) <br>
- [Usage reference](references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance plus generated local files such as HTML reports, Word reports, and DOCX bid documents.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a locally stored App Key; bid generation consumes account credits and can take more than 10 minutes.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
