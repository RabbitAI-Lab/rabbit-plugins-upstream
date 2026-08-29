## Description:

通过百炼®标书开放 API 辅助完成招标文件解读、分包抽取、投标文件生成和合规审查，并提醒用户文件会上传到云端且生成标书会消耗账户积分。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

Bid teams and agents use this skill to analyze local tender documents, extract bid packages, generate editable .docx bid documents, and review bid files for compliance through the 百炼®标书 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Install and use only when the user is comfortable with that upload path, and confirm consent before sending tender or bid files.

Risk: The App Key grants access to the user's 百炼®标书 account.

Mitigation: Use the documented local config.json credential flow and do not paste, echo, or forward the App Key in chat.

Risk: Generated results are retained by the service for a limited period and bid generation can consume account credits.

Mitigation: Tell users about retention and credit consumption before generation, and avoid duplicate submissions for long-running jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-smart-pro)
- [百炼®标书平台](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼®标书开放 API 契约参考](references/api.md)
- [执行细节](references/usage.md)
- [知识库字段说明](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Files, Guidance]

**Output Format:** [Plain text summaries, JSON API results, HTML or Word reports, and generated .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports and bid documents are written as local files; cloud results are associated with the user's App Key account and may expire after a limited retention period.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
