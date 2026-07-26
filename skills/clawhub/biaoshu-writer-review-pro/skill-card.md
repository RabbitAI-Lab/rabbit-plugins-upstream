## Description: <br>
凭 App Key 调用百炼®标书开放 API，完成招标文件智能解读、分包抽取、成品投标文件生成和可选合规审查。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business proposal teams use this skill to process local tender documents, generate editable bid documents, and review bid files for compliance risks through the BaiLian bid-document service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid documents may contain commercial, pricing, and personal information and are uploaded to the BaiLian service for processing. <br>
Mitigation: Use the skill only after the user understands and consents to the upload, and submit only intended local files. <br>
Risk: The App Key controls access to billable account credits and is stored locally. <br>
Mitigation: Keep config.json private, avoid pasting the App Key into chat, and do not share links that contain App Key or bind_key parameters. <br>
Risk: Bid-document generation consumes account credits. <br>
Mitigation: Check the account balance before submitting generation jobs and confirm the user expects credit usage. <br>
Risk: Optional endpoint overrides could route traffic away from the production BaiLian API. <br>
Mitigation: Review ZCM_BASE before use and leave it unset when production API routing is required. <br>
Risk: Generated bid documents and compliance reports may require business and legal review before use. <br>
Mitigation: Treat generated files and risk findings as drafting and review aids, and have qualified staff verify final submissions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-review-pro) <br>
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666) <br>
- [BaiLian bid-document service](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [API contract reference](references/api.md) <br>
- [Usage guide](references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance, progress text, JSON results, .docx bid documents, and HTML or Word reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include local absolute file paths for generated reports and bid documents.] <br>

## Skill Version(s): <br>
1.0.11 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
