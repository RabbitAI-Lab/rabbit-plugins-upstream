## Description:

Uploads tender or bid documents to the 百炼®标书 service so an agent can interpret tender requirements, generate .docx bid documents, review bid compliance, and compare 2-3 bid files for duplicate or similarity risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement teams use this skill to analyze tender files, prepare bid documents, check submission risk, and review similarity between bid files before submission. It is intended for users who can provide local tender or bid documents and consent to cloud processing by the 百炼®标书 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents can contain sensitive commercial, pricing, and personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Install and use the skill only after confirming the user understands and consents to cloud processing under their own account.

Risk: The security scan reports that the skill can upload arbitrary local file paths.

Mitigation: Review file paths before execution and upload only files the user explicitly provided and is authorized to process.

Risk: The security scan reports that outputs may be written outside the declared boundary.

Mitigation: Prefer the default output directory and avoid custom output paths unless the user specifically requests and reviews them.

Risk: The security scan reports undeclared local metadata retention for tender filenames.

Mitigation: Periodically delete ~/.zcm/projects.json if local retention of tender filenames is not desired.

Risk: The security scan reports inconsistent account-onboarding guidance, and API keys or account recovery links can expose credentials if shared in chat.

Mitigation: Have users create config.json themselves, never ask for phone numbers, SMS codes, or API keys in chat, and avoid sharing links that contain credential or binding parameters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-master-business)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼®标书开放 API 总调度](artifact/references/api.md)
- [鉴权、任务与可用字数接口](artifact/references/api-auth.md)
- [智能解读与标书制作 API](artifact/references/api-bid-workflow.md)
- [标书审查 API](artifact/references/api-compliance.md)
- [标书查重 API](artifact/references/api-duplicate.md)
- [知识库字段说明](artifact/references/knowledge-fields.md)
- [执行细节（操作手册）](artifact/references/usage.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration guidance]

**Output Format:** [Agent-facing guidance and status text, JSON task results, HTML or Word reports, short-lived download links, and generated .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include cloud-hosted task results and locally written reports; generated bid documents may be delivered by short-lived download URL or saved locally when requested.]

## Skill Version(s):

3.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
