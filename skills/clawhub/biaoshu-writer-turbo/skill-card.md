## Description:

新讯标书自动撰写工具接入百炼®标书开放 API，帮助代理解读招标文件、生成投标文件并审查投标合规风险。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding teams and agents use this skill to process user-provided tender and bid files, producing structured tender interpretation, generated bid documents, and compliance review reports for mainland-China bidding workflows.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to the 百炼 cloud service for processing.

Mitigation: Confirm user awareness and consent before upload, and process only files the user explicitly provides.

Risk: The App Key is an account credential and may be exposed through chat history or key-bearing links.

Mitigation: Have the user store the App Key only in the local config file, do not ask for it in chat, and do not forward links containing App Key or bind_key parameters.

Risk: Uploaded files and generated outputs are retained by the service for a limited period, and bid document generation consumes account credits.

Mitigation: Review the service retention and credit-use terms before generating bid documents.

Risk: Generated bid documents and compliance findings may contain incomplete, outdated, or incorrect interpretations of procurement requirements.

Mitigation: Require human legal, procurement, and business review before relying on outputs for submission.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-turbo)
- [百炼®标书 Platform](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼®标书开放 API 契约参考](references/api.md)
- [执行细节（操作手册）](references/usage.md)
- [知识库字段说明](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Plain-language responses, JSON task results, generated HTML or Word reports, and .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated report labels use zh-CN procurement terminology; bid generation can be long-running and may consume account credits.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; bundled client reports 2.2.1 API compatibility)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
