## Description:

自动解读招标文件要点，生成排版后的投标文件 .docx，并对投标文件做合规自查；使用前需要 App Key，文件会上传至百炼®标书云端处理。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid teams use this skill to analyze local tender files, generate editable bid documents, and review bid submissions for compliance risks. It is intended for cases where the user explicitly provides tender or bid files and consents to cloud processing by the 百炼®标书 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files may contain sensitive business or personal data and are uploaded to the 百炼®标书 cloud service.

Mitigation: Confirm the user understands and agrees to cloud processing before uploading files.

Risk: The local App Key is an account credential and could be exposed through chat, logs, or parameterized links.

Mitigation: Keep the App Key out of chat, store it only in the local config file, and do not forward recharge or binding links that contain credential parameters.

Risk: Generating bid documents consumes account credits.

Mitigation: Precheck the account balance and make clear that document generation is the credit-consuming step.

Risk: Changing the API base URL could send files or credentials to an unintended service.

Mitigation: Leave ZCM_BASE at the default unless the user intentionally chooses another trusted endpoint.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-swift)
- [百炼®标书 Platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API Contract Reference](references/api.md)
- [Usage Guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, JSON task results, HTML/Word reports, and .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided local tender/bid files and a local App Key; generated bid documents consume account credits.]

## Skill Version(s):

1.0.13 (source: server release metadata); bundled client 2.2.1 (source: artifact/scripts/zcm.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
