## Description:

上传招标或投标文件后，帮助代理完成招标解读、投标文件生成、标书审查和 2-3 份投标文件相似风险检查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding teams use this skill to analyze tender requirements, draft editable bid documents, review submission risks, and compare bid files for similarity before submission.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Tender and bid files may contain sensitive commercial, pricing, and personal information and are uploaded to the 百炼®标书 cloud service.

Mitigation: Confirm the user is comfortable with cloud processing before installation or first use, and upload only files the user is authorized to process.

Risk: The API key is a full account credential.

Mitigation: Have the user store the key locally and never paste, repeat, or expose it in chat, logs, screenshots, or links.

Risk: Tender filenames and job or project IDs may be cached locally under ~/.zcm unless configured otherwise.

Mitigation: Use the documented storage configuration to place local metadata in an approved directory when stricter data handling is required.

Risk: The progress monitor can create excessive API traffic.

Mitigation: Use a slower explicit polling interval and limit concurrent runs until the default polling behavior is fixed.

Risk: Bid similarity output could be mistaken for a legal determination.

Mitigation: Treat similarity findings as internal pre-submission review signals and require human review for legal or compliance conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-lite)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)
- [API contract](references/api.md)
- [Usage guide](references/usage.md)
- [Knowledge base field guide](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, JSON]

**Output Format:** [Markdown guidance with generated .docx bid documents, HTML/Word reports, and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided API key; generated documents and task results may be retained by the cloud service for about 7 days.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
