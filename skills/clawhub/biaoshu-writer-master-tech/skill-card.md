## Description:

上传招标/投标文件后，帮助代理调用百炼®标书服务完成招标解读、投标文件生成、标书审查和 2-3 份投标文件查重，并输出摘要、报告或成品 .docx。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

投标团队、咨询顾问和受托代理人 use this skill to interpret tender documents, generate technical bid documents, review bid compliance, and compare legally held bid files for similarity risk before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents are uploaded to the 百炼 service for processing and may contain commercial, pricing, or personal information.

Mitigation: Use only with files the user is authorized to process, confirm upload consent before execution, and avoid submitting unrelated or unnecessary documents.

Risk: The API key controls a billing or word-balance account and may be exposed if pasted into chat or embedded in returned links.

Mitigation: Require the user to create the local config file themselves, never echo API keys, phone numbers, SMS codes, or key-bearing recharge/bind links in conversation.

Risk: Arbitrary output paths can place generated documents or reports in unexpected locations.

Mitigation: Prefer the documented output directory and use explicit, user-approved paths only when saving generated files locally.

Risk: Tender or job metadata may remain under ~/.zcm until the publisher fixes or documents that behavior.

Mitigation: Tell users where local metadata may be stored and let them remove it when they no longer need job continuity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-master-tech)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼®标书平台](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼®标书开放 API 总调度](artifact/references/api.md)
- [鉴权、任务与可用字数接口](artifact/references/api-auth.md)
- [智能解读与标书制作 API](artifact/references/api-bid-workflow.md)
- [标书审查 API](artifact/references/api-compliance.md)
- [标书查重 API](artifact/references/api-duplicate.md)
- [知识库字段说明](artifact/references/knowledge-fields.md)
- [执行细节（操作手册）](artifact/references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown or plain-text guidance, JSON summaries, local HTML/Word reports, and generated .docx bid files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-managed 百炼®标书 API key; generated bid files may be delivered through short-lived download links or saved locally when requested.]

## Skill Version(s):

3.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
