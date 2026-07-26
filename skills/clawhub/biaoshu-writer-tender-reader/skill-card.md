## Description: <br>
基于百炼®标书开放 API 的招投标全流程助手，上传招标文件后生成结构化智能解读报告，并可生成投标文件或审查投标文件合规性。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business users, tender teams, and bid writers use this skill to analyze tender documents, identify disqualification risks and scoring criteria, generate bid documents, and review bid submissions before filing. It requires a百炼®标书 App Key and sends user-selected tender or bid files to the百炼®标书 cloud service for processing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com under the user's App Key account. <br>
Mitigation: Confirm the user understands and agrees before upload, and avoid installing or using the skill unless that cloud processing and retention model is acceptable. <br>
Risk: The App Key is a full account credential and can be exposed if pasted into chat or shared through links that contain key parameters. <br>
Mitigation: Keep the App Key in the local config file only, do not paste it into conversations, and never forward links that include App Key or bind_key parameters. <br>
Risk: Custom API base settings can redirect document uploads and credentials to a different endpoint. <br>
Mitigation: Use the default biaoshu.zhiliaobiaoxun.com endpoint unless the user explicitly trusts the configured alternative. <br>
Risk: Bid document generation consumes account points and long-running jobs can continue after a local client timeout. <br>
Mitigation: Check balance before generation, track existing job IDs, and resume polling instead of resubmitting generation requests. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-tender-reader) <br>
- [百炼®标书 Platform](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [API Contract Reference](references/api.md) <br>
- [Usage and Operations Guide](references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance plus generated HTML, Word, DOCX, and JSON-backed report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include structured tender interpretation, risk summaries, bid document files, compliance reports, progress updates, and absolute local file paths.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
