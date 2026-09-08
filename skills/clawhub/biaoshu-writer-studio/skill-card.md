## Description:

智能标书编制 helps agents upload authorized tender and bid documents to the 百炼®标书 service to interpret requirements, generate .docx bid documents, review bid compliance, and compare 2-3 bid files for similarity risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams and their agents use this skill to process authorized tender and bid files, generate bid documents, produce interpretation and compliance reports, and run similarity checks before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, or personal data and are uploaded to the 百炼®标书 service for processing.

Mitigation: Use the skill only with documents the user is authorized to upload, confirm consent before upload, and avoid including unnecessary sensitive information.

Risk: Credentials or account recovery details could be exposed if phone numbers, SMS codes, API keys, or credential screenshots are shared in chat.

Mitigation: Keep API keys out of conversation history and screenshots; have the user store credentials only in the local config file.

Risk: Local output paths and persistent project metadata may reveal project names or job identifiers.

Mitigation: Keep output paths simple, avoid path characters in report basenames, and review or clear ~/.zcm/projects.json when project metadata is sensitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-studio)
- [百炼®标书开放 API 总调度](artifact/references/api.md)
- [鉴权、任务与可用字数接口](artifact/references/api-auth.md)
- [智能解读与标书制作 API](artifact/references/api-bid-workflow.md)
- [标书审查 API](artifact/references/api-compliance.md)
- [标书查重 API](artifact/references/api-duplicate.md)
- [知识库字段说明](artifact/references/knowledge-fields.md)
- [执行细节（操作手册）](artifact/references/usage.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown/plain text guidance plus generated HTML, Word, JSON, and .docx artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided API key stored in skill-local config.json; uploads authorized documents to the 百炼®标书 service and may consume account word credits. Security evidence verdict: suspicious; review handling of personal data, local paths, output paths, and persistent metadata before use.]

## Skill Version(s):

3.1.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
