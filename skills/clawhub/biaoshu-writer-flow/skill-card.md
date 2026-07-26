## Description: <br>
简单直接的投标文件生成器：解析招标文件、生成技术标与商务标 .docx、排查废标风险并做合规审查，三步出稿。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and bid-writing teams use this skill to interpret tender documents, generate technical and commercial bid .docx files, and review bid documents for compliance and disqualification risk. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid files may contain commercial, pricing, or personal information and are uploaded to the 百炼®标书 service for processing. <br>
Mitigation: Confirm the user knows and agrees before upload; use only user-provided local files and do not fetch cloud links. <br>
Risk: The App Key is a full account credential and billing authority for generated bid work. <br>
Mitigation: Have the user create the local config file themselves, never paste the key into chat, keep the credentials file permission-restricted, and do not forward links containing key or bind_key parameters. <br>
Risk: Generated bid content and compliance findings may be incomplete or unsuitable for final submission without review. <br>
Mitigation: Treat generated documents and reports as drafting and review aids; a qualified human should verify them against the tender before submission. <br>
Risk: Uploaded files and generated results may remain available on the service for the disclosed retention period. <br>
Mitigation: Tell users that task results and generated .docx files may persist for about seven days and can be managed through the service account. <br>


## Reference(s): <br>
- [百炼®标书开放 API 契约参考](references/api.md) <br>
- [执行细节（操作手册）](references/usage.md) <br>
- [百炼®标书平台](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-flow) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Chinese Markdown/status text plus generated HTML reports, Word .docx reports, and bid .docx files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include absolute local file paths for generated artifacts; bid generation and service-side processing use the configured App Key account.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
