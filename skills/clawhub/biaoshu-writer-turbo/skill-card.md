## Description:

标书自动撰写工具通过 App Key 接入百炼®标书开放 API，帮助用户解读招标文件、生成技术标与商务标 .docx 成品，并审查投标文件的合规风险。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid teams use this skill to work with tender and bid documents: extracting tender requirements, producing editable bid documents, and reviewing bids for compliance issues before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain business or personal information and are uploaded to the disclosed cloud service for processing.

Mitigation: Confirm user consent before upload and use the skill only for documents the user is permitted to send to the service.

Risk: The App Key is a full account credential stored locally in config.json.

Mitigation: Keep the App Key out of chat, restrict local file permissions, and delete config.json or use logout when the credential should no longer be stored.

Risk: Bid generation consumes credits from the App Key account.

Mitigation: Check balance and user intent before generation, and distinguish balance preflight from actual credit-consuming generation.

Risk: Changing ZCM_BASE or related configuration can redirect where files and credentials are used.

Mitigation: Verify any configured base URL or output override before running tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-turbo)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [Usage guide](references/usage.md)
- [API contract reference](references/api.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance plus generated HTML reports, Word reports, and .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include structured tender interpretation, compliance findings, absolute local file paths, and generated bid or report files.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
