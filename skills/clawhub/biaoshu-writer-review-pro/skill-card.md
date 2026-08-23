## Description:

凭 App Key 调用百炼®标书开放 API，完成「招标文件智能解读 → 抽取分包 → 生成成品投标文件(.docx) → 可选合规审查」的端到端标书制作。当用户明确提供招标文件并希望生成投标文件/标书、对已生成标书做合规检查、或询问百炼®标书相关能力时使用。注意：招标/投标文件会上传到百炼®标书云端 API 处理，标书生成消耗账户积分；使用前请确认用户知悉。本 skill 是百炼®标书线上接口的轻客户端，不复刻其算法。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid teams use this skill to analyze mainland-China tender documents, extract package information, generate editable bid documents, and review submitted bid files for compliance risks through the BaiLian bidding API. It is intended for workflows where the user knowingly uploads tender or bid files to the stated third-party service.

### Deployment Geography for Use:

Global, with primary language and workflow fit for mainland-China bidding processes and Simplified Chinese tender documents.

## Known Risks and Mitigations:

Risk: Sensitive tender and bid files, plus the App Key, may be sent to an unexpected endpoint if the API base override is misconfigured.

Mitigation: Before running tasks, verify ZCM_BASE and any saved base setting are unset or point to the official https://biaoshu.zhiliaobiaoxun.com API.

Risk: Tender and bid files commonly contain commercial, pricing, and personal information and are uploaded to the stated third-party service for processing.

Mitigation: Use the skill only after the user understands and agrees to upload those files, and avoid using it for material that should not leave the local environment.

Risk: The App Key is a full account credential and could be exposed through chat, logs, screenshots, or forwarded account links.

Mitigation: Keep the App Key in the local config file only, do not paste or repeat it in conversation, and do not forward links containing App Key or bind_key parameters.

Risk: Uploaded files, generated bid documents, and results are retained by the service for the period described by the skill.

Mitigation: Plan for server-side retention and local output files before use, and manage historical data through the service account when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-review-pro)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼标书 API contract reference](references/api.md)
- [Skill usage guide](references/usage.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Files, Configuration]

**Output Format:** [Markdown responses with background API task execution and generated .docx, HTML, Word, and JSON-style result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated artifacts may include bid documents, interpretation reports, compliance reports, local project cache entries, and paths to saved outputs.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
