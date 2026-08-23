## Description:

投标文件一键生成工具，使用百炼标书开放 API 解读招标文件、生成 .docx 投标文件，并对投标文件进行合规自查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bidding teams use this skill for mainland-China tender workflows: interpreting tender files, generating editable bid documents, and reviewing bid submissions for compliance risks. It is intended for cases where the user explicitly provides local tender or bid files and consents to cloud processing.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid files may contain confidential commercial, pricing, or personal information and are uploaded to a cloud service for processing.

Mitigation: Confirm user consent before upload and avoid using the skill for materials that cannot be sent to the 百炼标书 service.

Risk: The App Key grants account access and may be exposed if pasted into chat or forwarded in account links.

Mitigation: Have the user store the App Key only in the local skill config.json file and do not repeat keys or key-bearing links in conversation.

Risk: Configurable API base settings can redirect sensitive uploads away from the expected official service.

Mitigation: Before processing files, confirm ZCM_BASE and any stored base override are unset or point to https://biaoshu.zhiliaobiaoxun.com/api/open/v1.

Risk: Generated bid documents and compliance reports may include incomplete, incorrect, or placeholder content.

Mitigation: Require human review of generated documents,待填项 placeholders, and compliance findings before submission.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-lite)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage reference](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Chinese text responses plus generated .docx bid documents and HTML or Word reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated artifacts are written to biaoshu-bailian-files/ or a configured output directory; App Key credentials are stored locally in skill config.json.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
