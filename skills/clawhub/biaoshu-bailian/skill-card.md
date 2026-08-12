## Description:

凭 App Key 调用百炼标书开放 API，完成招标文件智能解读、分包抽取、成品投标文件生成和可选合规审查的端到端标书制作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams and procurement-support users use this skill to analyze tender files, generate editable bid documents, and review submitted bid files for compliance risks through the 百炼标书 cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to a third-party cloud API for processing.

Mitigation: Confirm user consent before upload, use only files the user explicitly provides, and install only when the organization accepts processing by the 百炼标书 cloud service.

Risk: The App Key is a full account credential and leakage could expose account access or billing actions.

Mitigation: Keep the App Key out of chat, store it only in the local skill config file with restricted permissions, and do not forward links that embed the key.

Risk: Bid-document generation consumes account credits and long-running generation may still continue after a local command times out.

Mitigation: Check balance before generation, confirm expected credit use, and resume existing jobs instead of resubmitting generation requests.

Risk: Changing the API base URL could send sensitive files to an unintended service.

Mitigation: Use the default 百炼标书 endpoint unless there is an intentional, reviewed configuration change.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-bailian)
- [百炼标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼标书 API contract](references/api.md)
- [Execution and usage guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [User-facing Chinese guidance plus generated HTML, Word, JSON, and .docx bid-document files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uploads user-provided tender or bid files to the 百炼标书 cloud API; generated reports and bid documents are saved locally and may also remain available in the service account for about 7 days.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
