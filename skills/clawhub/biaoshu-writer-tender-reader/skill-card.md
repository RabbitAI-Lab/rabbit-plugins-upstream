## Description:

基于百炼®标书开放 API，帮助用户在明确提供招标或投标文件后生成招标文件解读、投标文件草稿和合规审查结果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement teams use this skill to analyze tender files, identify disqualification risks and scoring criteria, generate editable bid documents, and review bid files for compliance before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files may contain commercial, pricing, or personal information and are uploaded to the BaiLian Biaoshu cloud service for processing.

Mitigation: Confirm user consent before upload and use the skill only for files the user explicitly provides for tender interpretation, bid generation, or compliance review.

Risk: The App Key grants access to the user's BaiLian Biaoshu account and credit balance if exposed.

Mitigation: Store the App Key only in the local config file, do not ask the user to paste it into chat, and do not forward URLs that contain App Key or bind_key parameters.

Risk: Bid-document generation consumes account credits and long-running jobs may continue after a local tool timeout.

Mitigation: Review credit balance before generation, use idempotent or continuation flows for long jobs, and avoid resubmitting generation requests when an existing job is still running.

Risk: Changing the API base URL could send sensitive tender or bid files to an unintended service.

Mitigation: Use the documented production endpoint unless the user intentionally configures a trusted alternative.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-tender-reader)
- [Publisher Profile](https://clawhub.ai/user/chichihaixiaojian666)
- [Usage Guide](references/usage.md)
- [Open API Contract Reference](references/api.md)
- [BaiLian Biaoshu Platform](https://biaoshu.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured text, with generated local files such as HTML reports, Word reports, and DOCX bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a locally stored App Key; uploads user-selected tender or bid files to the BaiLian Biaoshu cloud service for processing.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
