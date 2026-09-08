## Description:

上传招标/投标文件，AI 一站式完成智能解读（废标红线/评分标准/控标洞察）、成品投标文件(.docx)生成、标书审查（分级风险+雷同检测）和标书查重（2-3份投标文件相似/雷同风险检查）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business teams use this skill to analyze tender files, generate editable bid documents, review bid compliance, and compare multiple bid files for similarity risk before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain confidential business, pricing, and personal information and are uploaded to the third-party service for processing.

Mitigation: Use the skill only when the user accepts the cloud processing and retention model for those documents.

Risk: The skill depends on a locally stored API key for the third-party service.

Mitigation: Have the user configure the key locally, do not request or echo it in chat, and rotate the key if exposure is suspected.

Risk: Bid generation consumes the service account's available word balance.

Mitigation: Confirm the user intends to generate a bid document and understands the billing impact before starting generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-assistant-business)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)
- [API contract reference](references/api.md)
- [Usage guide](references/usage.md)
- [Knowledge-base fields](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, configuration, guidance]

**Output Format:** [Chinese-language summaries and guidance, JSON result details, HTML or Word reports, and generated DOCX bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated bid documents may include placeholders for information the service cannot confirm; reports and results are tied to the user's third-party service account.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
