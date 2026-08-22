## Description:

凭 App Key 调用百炼®标书开放 API，完成招标文件智能解读、分包抽取、成品投标文件生成和可选合规审查的端到端标书制作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bidding teams use this skill to analyze mainland-China tender documents, generate editable bid documents, and review bid files for compliance risks before submission.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain confidential business, pricing, or personal information and are uploaded to the vendor cloud service for processing.

Mitigation: Use the skill only with documents the user is willing to upload, and confirm user consent before the first upload.

Risk: The security scan reports that the API base can be redirected, which could send uploaded files or credentials to an unintended endpoint.

Mitigation: Avoid setting ZCM_BASE or login --base unless the endpoint is intentionally trusted to receive both files and credentials.

Risk: The App Key controls account access and billing, and keyed recharge or bind links could leak that credential.

Mitigation: Keep the App Key out of chat, store it only in the local config.json file, and do not forward links containing bind_key or App Key parameters.

Risk: Generated bid documents and compliance findings can be incomplete or incorrect for a procurement submission.

Mitigation: Require human procurement or legal review before submitting any generated bid package or acting on compliance findings.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-smart-pro)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼®标书开放 API 契约参考](references/api.md)
- [执行细节（操作手册）](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with local command execution and generated .docx, HTML, Word, and JSON artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs use Simplified Chinese labels for bidding workflow terms; generated artifacts are written under biaoshu-bailian-files/.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
