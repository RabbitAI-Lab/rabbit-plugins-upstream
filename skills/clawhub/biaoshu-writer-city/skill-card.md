## Description: <br>
应答与排版一体的生成器。输入招标文件，它解析评分点、生成投标应答、自动编排目录与格式，产出可直接提交的投标标书(.docx)，并附带废标风险与合规审查。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External bid teams and procurement-support agents use this skill to interpret tender documents, draft formatted bid documents, and review bid submissions for rejection and compliance risks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing. <br>
Mitigation: Confirm user consent before upload and install only when the organization accepts processing by the disclosed third-party service. <br>
Risk: The App Key can consume account credits and access account-scoped data. <br>
Mitigation: Store the key in the local credential file or approved environment variable, avoid pasting it into chat, and rotate it if exposed. <br>
Risk: Changing the API base URL can redirect sensitive documents and credentials to a different endpoint. <br>
Mitigation: Avoid custom ZCM_BASE values unless the endpoint is explicitly trusted. <br>
Risk: Generated files and task results may remain available on the service for about 7 days. <br>
Mitigation: Treat generated outputs as retained service data during that period and manage historical data through the service account when needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/biaoshu-writer-city) <br>
- [Publisher profile](https://clawhub.ai/user/dragonzu) <br>
- [招采猫开放 API 契约参考](references/api.md) <br>
- [执行细节（操作手册）](references/usage.md) <br>
- [招采猫平台](https://biaoshu.zhiliaobiaoxun.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown/plain text guidance plus generated .docx bid files and HTML or Word reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses an App Key account, uploads user-selected tender and bid documents to the disclosed third-party API, and writes generated artifacts to local files.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
