## Description:

上传招标/投标文件，AI 一站式完成智能解读（废标红线/评分标准/控标洞察）、成品投标文件(.docx)生成、标书审查（分级风险+雷同检测）和标书查重（2-3份投标文件相似/雷同风险检查）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams and procurement contributors use this skill to interpret tender files, generate editable bid documents, review bid compliance, and compare legally held bid files for similarity before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents can contain sensitive commercial, pricing, and personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Confirm user awareness and consent before upload, process only files the user explicitly provides, and avoid using the skill for documents that cannot be shared with that service.

Risk: The API key grants account access and can be exposed through chat logs or parameterized account links.

Mitigation: Keep the key in the local config file, do not paste or echo it in chat, and do not forward service links that contain key or bind_key parameters.

Risk: Generated bid documents, compliance findings, and duplicate-check results may be incomplete or incorrect and duplicate checks are not legal determinations.

Mitigation: Have qualified bid, procurement, or legal reviewers check outputs before submission and treat similarity findings as internal review signals.

Risk: Bid generation consumes account word balance and repeated submissions can create avoidable cost.

Mitigation: Use the stored job and progress flow for long-running tasks, avoid resubmitting the same generation task, and verify account balance before generation.

## Reference(s):

- [Open API contract reference](references/api.md)
- [Usage guide](references/usage.md)
- [Knowledge fields reference](references/knowledge-fields.md)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Chinese-language guidance, JSON summaries, HTML/Word reports, and generated .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-selected local tender or bid files and a 百炼®标书 API key; generated bid documents may be delivered as short-lived download links or saved local .docx files.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
