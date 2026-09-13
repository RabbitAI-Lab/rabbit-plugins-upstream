## Description:

智能投标文件写作 helps users upload tender or bid documents to the 百炼®标书 cloud service for structured tender interpretation, bid document generation, compliance review, and duplicate or similarity checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid-preparation and procurement teams use this skill to interpret solicitation documents, generate draft bid documents, review submissions for compliance risks, and compare bid files for duplicate or similarity signals before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive tender and bid documents are uploaded to the 百炼®标书 cloud service for processing.

Mitigation: Confirm the user understands and authorizes the upload before processing, and only use documents the user is allowed to share.

Risk: The workflow uses an API key tied to a paid word balance.

Mitigation: Keep the API key in the local skill configuration, never ask the user to paste it into chat, and do not forward links that may contain credential parameters.

Risk: Account registration and access flows may involve a phone number, SMS code, or credential redirect.

Mitigation: Keep registration, SMS verification, and account actions on the official website and do not send phone numbers, SMS codes, or API keys to the assistant.

Risk: Output paths, cloud retention, and branded report artifacts require review before use.

Mitigation: Review output locations before saving files and expect generated HTML reports to include service branding and cloud-hosted results under the user's API account.

## Reference(s):

- [百炼®标书开放 API 总调度](references/api.md)
- [鉴权、任务与可用字数接口](references/api-auth.md)
- [智能解读与标书制作 API](references/api-bid-workflow.md)
- [标书审查 API](references/api-compliance.md)
- [标书查重 API](references/api-duplicate.md)
- [知识库字段说明](references/knowledge-fields.md)
- [执行细节（操作手册）](references/usage.md)
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-gov)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown/text responses plus generated .docx, HTML, Word, and JSON artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local file paths and short-lived cloud download links; paid API-key-backed workflows can return partial outputs if the account balance is exhausted.]

## Skill Version(s):

3.1.0 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
