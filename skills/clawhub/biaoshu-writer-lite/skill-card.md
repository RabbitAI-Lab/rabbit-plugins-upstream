## Description:

投标文件一键生成工具，凭 App Key 调用开放 API 让用户完成招标文件解读、成品投标文件生成、自动排版、待填项引导和生成后合规自查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bidding teams use this skill to interpret tender files, generate editable bid documents, and review bid submissions for compliance issues before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files may contain commercial, pricing, or personal information and are uploaded to the 百炼标书 service for processing.

Mitigation: Confirm user consent before upload and use the skill only for files the user explicitly provides for this workflow.

Risk: The App Key grants access to the user's account and billing balance.

Mitigation: Keep the App Key out of chat, store it only in the local config file, and do not forward links that contain key or bind_key parameters.

Risk: Generated server-side task results and documents are disclosed as retained by the service for about 7 days.

Mitigation: Tell users that results remain available under their App Key account for the disclosed retention period and should be managed through the service account.

Risk: Bid document generation consumes account points.

Mitigation: Check account balance before generation and make clear that generation is the billable step.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-lite)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage guide](references/usage.md)
- [Knowledge field reference](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Files]

**Output Format:** [Markdown guidance with local command orchestration and generated HTML, Word, and DOCX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include structured tender interpretation, compliance findings, exported reports, and editable bid document files.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
