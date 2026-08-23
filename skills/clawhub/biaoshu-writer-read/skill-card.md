## Description:

凭 App Key 调用百炼®标书服务，帮助投标团队解读中国招标文件、抽取分包、生成投标文件，并可对投标文件做合规审查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

投标团队、招采顾问和相关业务人员 use this skill to analyze mainland-China tender documents, generate editable bid documents, and review drafted bids for compliance risks before submission.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid files may contain commercial, pricing, or personal information and are uploaded to the 百炼®标书 service for processing.

Mitigation: Use only after the user understands and accepts the upload and retention behavior; avoid processing documents that policy does not allow to leave the local environment.

Risk: The App Key is a full-account credential for the service.

Mitigation: Keep the App Key in the local config file only, never paste it into chat, and reset it through the service if exposure is suspected.

Risk: Server security evidence reports that configuration can cause the App Key and uploaded documents to be sent to a non-official endpoint.

Mitigation: Before use, verify that config.json has no base field and that ZCM_BASE is unset or points only to the official HTTPS API.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-read)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage and operating guide](references/usage.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with generated HTML reports, Word reports, and DOCX bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include local report paths, risk summaries, bid-document files, and credential setup guidance; bid generation can consume account credits.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
