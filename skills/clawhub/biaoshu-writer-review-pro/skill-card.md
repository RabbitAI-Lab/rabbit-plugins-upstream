## Description:

凭 App Key 调用百炼®标书开放 API，帮助代理完成招标文件智能解读、分包抽取、投标文件生成和可选合规审查，并明确提示文件上传、凭证保护和积分消耗。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid-writing users and their agents use this skill to analyze tender files, generate editable bid documents, and review bid submissions for compliance risks through the 百炼®标书 cloud API. The workflow is designed for user-provided local files and App Key based account access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to the 百炼®标书 cloud service.

Mitigation: Confirm user consent before upload and limit processing to user-provided local files sent to the documented 百炼®标书 API domain.

Risk: The App Key is a full account credential and may expose billing or account access if shared in chat or links.

Mitigation: Have the user store the App Key locally in config.json, do not request or echo it in conversation, and avoid forwarding URLs that contain key or bind_key parameters.

Risk: Bid-document generation consumes the App Key account's points and long-running generation can be accidentally resubmitted.

Mitigation: Check balance before generation, explain that generation is the paid step, and use job status or idempotency handling instead of resubmitting interrupted jobs.

Risk: Generated bid text, extracted requirements, and compliance findings can be incomplete or require judgment.

Mitigation: Preserve uncertain fields as 待填项, report partial semantic review status when applicable, and require human review before bid submission.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-review-pro)
- [百炼®标书 Platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API Contract Reference](references/api.md)
- [Usage Guide](references/usage.md)
- [Knowledge Base Field Reference](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown or plain text guidance, JSON API results, HTML or Word reports, and editable .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include absolute local file paths for generated reports or bid documents; reports use zh-CN procurement labels.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
