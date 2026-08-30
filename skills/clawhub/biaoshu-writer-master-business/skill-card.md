## Description:

基于百炼®标书开放 API 的商务标生成工具，同一 App Key 也支持招标文件解读与合规审查。当用户明确提供招标文件并要求撰写商务标、整理商务响应、生成商务标成品投标文件(.docx)时使用；仅咨询一般性招投标问题、未提供文件时不必调用本 SKILL。注意：文件会上传百炼®标书云端处理、标书生成消耗积分，使用前请确认用户知悉。需 App Key（官网注册赠积分）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding teams and business proposal staff use this skill to interpret tender documents, generate commercial bid documents, and review bid files for compliance through the 百炼®标书 service after confirming upload, credential, and account-balance requirements.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid files may contain confidential business, pricing, or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Confirm user awareness and consent before upload, limit inputs to user-provided files, and disclose that uploaded files and generated results are retained under the App Key account for the service retention window.

Risk: The App Key controls account access and balance use.

Mitigation: Have the user store the App Key only in the local config file, never request or echo it in chat, and never share links that include App Key or bind_key parameters.

Risk: Bid generation consumes account points and long-running jobs can create cost or duplication risk if resubmitted unnecessarily.

Mitigation: Check balance before generation, explain that generation is the point-consuming step, and resume existing jobs rather than submitting duplicate generation requests.

Risk: Generated bid content and compliance findings may be incomplete or incorrect if source documents or company knowledge-base data are missing or ambiguous.

Mitigation: Require human review against the tender source, preserve uncertain fields as placeholders, and avoid inventing company facts or financial data.

Risk: Knowledge-base lookup can expose tenant-scoped company profile, qualification, performance, and financial-report category information.

Mitigation: Use only the scoped fields returned for the App Key tenant, avoid cross-tenant assumptions, and do not infer attachment contents or unavailable financial details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-master-business)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](artifact/references/api.md)
- [Usage reference](artifact/references/usage.md)
- [Knowledge-base field reference](artifact/references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance plus generated .docx bid documents and HTML or Word interpretation and compliance reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-facing labels and report terminology are primarily Simplified Chinese; generated outputs depend on user-provided tender or bid files and the configured App Key account.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
