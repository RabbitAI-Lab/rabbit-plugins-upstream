## Description:

简单直接的投标文件生成器：解析招标文件、生成技术标与商务标 .docx、排查废标风险并做合规审查，三步出稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams and procurement-support agents use this skill to interpret mainland-China tender documents, generate technical and commercial bid document drafts, and review bid files for disqualification and compliance risks before submission. It is intended for workflows where the user has provided local tender or bid files and has consented to cloud processing by the 百炼®标书 service.

### Deployment Geography for Use:

Mainland China bidding workflows; user-facing platform labels and generated report artifacts are Simplified Chinese (zh-CN).

## Known Risks and Mitigations:

Risk: Tender and bid files may contain sensitive commercial, pricing, or personal information and are uploaded to the 百炼®标书 cloud service for processing.

Mitigation: Use the skill only after the user understands and agrees to the upload, and limit inputs to the specific local files needed for the task.

Risk: The App Key controls access to the user's account points and task history.

Mitigation: Keep the App Key out of chat, store it only in the local skill config file, and delete or reset it when it is no longer needed.

Risk: API traffic can be redirected if optional base URL settings are changed.

Mitigation: Use the default 百炼®标书 endpoint unless the user fully trusts the alternate endpoint.

Risk: Local project metadata may reveal procurement filenames.

Mitigation: Use non-sensitive filenames where practical and clear local project metadata if those filenames are confidential.

Risk: Generated bid documents and compliance findings may contain incomplete, uncertain, or context-dependent recommendations.

Mitigation: Require human procurement, legal, or compliance review before submission, especially for retained待填项, semantic-review status, and high-risk findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-flow)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼®标书开放 API 契约参考](artifact/references/api.md)
- [执行细节（操作手册）](artifact/references/usage.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Chinese-language assistant responses plus local HTML, Word, JSON, and .docx artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include tender interpretation summaries, generated bid documents, compliance reports, progress updates, absolute local file paths, and App Key setup guidance.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
