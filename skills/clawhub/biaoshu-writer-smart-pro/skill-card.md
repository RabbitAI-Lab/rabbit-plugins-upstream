## Description:

凭 App Key 调用百炼®标书开放 API，完成招标文件智能解读、分包抽取、成品投标文件生成和可选合规审查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

Bidding and proposal teams use this skill to turn local tender documents into structured tender analysis, generated bid documents, and optional compliance review reports through the 百炼®标书 service. It is intended for users who can provide local tender or bid files and approve upload to the vendor service before processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to the 百炼®标书 service for processing.

Mitigation: Confirm user consent before upload and clearly disclose that uploaded files and generated results may remain in the vendor account for about 7 days.

Risk: The App Key is a full account credential stored locally for API access.

Mitigation: Keep the App Key out of chat, store it only in the local config file, and instruct the user to reset it through the vendor service if exposure is suspected.

Risk: Generated bid documents and compliance findings may be incomplete or require professional review before submission.

Mitigation: Have the bidding team review generated documents, risk findings, and required manual checks before relying on them for a live tender.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-smart-pro)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/)
- [API reference](references/api.md)
- [Usage guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with generated local files such as HTML reports, Word reports, and .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated bid documents and reports are written to local output paths; processing uses the user's App Key and may require account balance.]

## Skill Version(s):

1.0.6 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
