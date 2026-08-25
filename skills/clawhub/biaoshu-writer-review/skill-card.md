## Description:

凭 App Key 调用百炼®标书开放 API，完成招标文件智能解读、分包抽取、成品投标文件生成和可选合规审查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and bid-writing teams use this skill to analyze tender documents, generate editable bid documents, and review submitted bids for compliance risks. Agents use it as a light client for the 百炼®标书 cloud API while keeping users informed about upload, credential, and billing implications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files can contain commercial, pricing, or personal information and are uploaded to the 百炼®标书 cloud service for processing.

Mitigation: Use the skill only with user-provided local files after confirming upload consent, and keep network use limited to biaoshu.zhiliaobiaoxun.com.

Risk: The App Key is an account credential and bid generation can spend account credits.

Mitigation: Have the user write the key directly to the local config file, never paste or echo it in chat, avoid forwarding key-bearing links, and use logout or file deletion when access is no longer needed.

Risk: Uploaded files and generated results are retained under the App Key account for a limited period, and local project state can reveal tender filenames.

Mitigation: Tell users about cloud retention, direct them to manage history on the platform, and clear local config or project state when filenames or account context are sensitive.

Risk: Generated bid documents and compliance findings may be incomplete, partially semantic, or require professional judgment before submission.

Mitigation: Review reports and .docx outputs before filing, surface high-risk and partial-review status clearly, and leave uncertain knowledge-base fields as待填项 instead of inventing values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-review)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [Usage guide](references/usage.md)
- [Open API contract](references/api.md)
- [Knowledge field guide](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Agent-facing instructions and command workflows that produce JSON results, HTML or Word reports, and .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated artifacts use zh-CN procurement labels; outputs may include absolute local file paths and account balance status.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
