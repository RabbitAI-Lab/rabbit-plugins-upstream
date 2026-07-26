## Description: <br>
一站式覆盖招标文件智能解读、投标应答撰写、成品投标文件生成和废标风险与合规审查。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dragonzu](https://clawhub.ai/user/dragonzu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Bid and proposal teams use this skill to analyze tender documents, draft editable bid documents, and review bid files for compliance risks before submission. It is intended for users who can provide local tender or bid files and an App Key for the 招采猫 service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid files may contain business or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing. <br>
Mitigation: Use the skill only after the user understands and accepts the upload, and avoid submitting files that the user is not authorized to share with that service. <br>
Risk: The App Key controls account access and can consume the account's points. <br>
Mitigation: Keep the App Key out of chat, store it locally as documented, and confirm point balance before generating full bid documents. <br>
Risk: Changing the service base URL could send files or credentials to an unexpected endpoint. <br>
Mitigation: Verify any ZCM_BASE override before use and keep the default service host unless there is a trusted reason to change it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/biaoshu-writer-edu) <br>
- [招采猫平台](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [API contract reference](artifact/references/api.md) <br>
- [Execution usage reference](artifact/references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, document files, reports] <br>
**Output Format:** [Markdown summaries and progress, HTML or Word reports, and editable .docx bid documents] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads user-selected local tender or bid files, writes outputs under the configured local output directory, and uses the user's App Key account for service access.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
