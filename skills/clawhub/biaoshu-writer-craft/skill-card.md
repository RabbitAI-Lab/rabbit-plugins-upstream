## Description:

为中国大陆招投标场景解读招标文件、生成投标文件 .docx，并审查废标与合规风险。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding teams and proposal writers use this skill to process local Chinese tender and bid documents, generate editable bid-document deliverables, and review compliance risks before submission.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill handles confidential tender or bid files and account credentials.

Mitigation: Review before installing, use only when comfortable uploading files to the named service, confirm user consent before upload, and keep the App Key out of chat.

Risk: The API destination override is broader than the single-domain disclosure.

Mitigation: Avoid setting ZCM_BASE or any custom base URL unless the endpoint is intentionally trusted.

Risk: Account links or logs can expose credential-bearing App Key or bind_key values.

Mitigation: Use the local config.json credential flow and do not forward URLs that contain App Key or bind_key parameters.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-craft)
- [百炼®标书 Platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API Contract Reference](references/api.md)
- [Usage Guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [User-facing text plus local HTML reports, Word .docx files, and JSON-backed result summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated artifacts and report labels are primarily Simplified Chinese; outputs may include local absolute file paths.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
