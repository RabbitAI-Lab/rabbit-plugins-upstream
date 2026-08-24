## Description:

从招标解读直达成标的编制工具。它读懂招标文件的评分与废标要求后，一键生成成品投标文件(.docx)、编排投标应答，并完成合规审查。当用户明确提供招标/投标文件并要求解读、生成或合规审查时使用；仅咨询一般性招投标问题、未提供文件时不必调用本 SKILL。文件经百炼®标书云端处理、消耗账户积分，使用前请确认用户知悉。需 App Key（官网注册赠积分）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill for mainland-China tender workflows: interpreting tender files, generating editable bid documents, and reviewing bid documents for compliance risks. It is intended for users who provide local tender or bid files and accept cloud processing by the 百炼®标书 service.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid files can contain confidential pricing, commercial, or personal information and are uploaded to the 百炼®标书 service for processing.

Mitigation: Install and use the skill only after confirming that users accept this upload and retention behavior; avoid using it for files that cannot be sent to the stated service.

Risk: The security verdict notes that network scope is looser than the skill's single-target claim when sensitive files and an App Key are involved.

Mitigation: Review the skill before installation and confirm ZCM_BASE or config base settings are not pointed at an unexpected host before running tasks.

Risk: The App Key grants account access and may be exposed if pasted into chat or forwarded through credential-bearing links.

Mitigation: Keep the App Key out of chat, store it only in the local config file, avoid forwarding links that contain key parameters, and remove config.json with logout when it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-studio)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼®标书开放 API 契约参考](references/api.md)
- [执行细节（操作手册）](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Chinese user-facing text plus generated HTML, Word, and .docx files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces tender interpretation summaries, bid document files, compliance findings, and absolute output paths; requires a locally configured App Key.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
