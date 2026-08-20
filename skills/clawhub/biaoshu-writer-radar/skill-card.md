## Description:

Uses a user-provided App Key to call the 百炼标书 service for Chinese tender document interpretation, bid document drafting, and compliance review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill when a user explicitly provides local Chinese tender or bid files and asks for bid interpretation, bid document generation, or pre-submission compliance review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files may contain confidential business, pricing, or personal information and are uploaded to the remote service for processing.

Mitigation: Confirm user consent before upload and avoid processing files the user is not authorized to send to the service.

Risk: Generated files and task results may be retained under the App Key account after processing.

Mitigation: Tell users that uploaded files and generated outputs are retained by the service account and direct them to manage historical data in the official service.

Risk: The App Key is a full account credential stored in a local config file.

Mitigation: Keep the App Key out of chat, store it only in the local config file with restrictive permissions, and remove config.json when access is no longer needed.

Risk: Optional endpoint overrides can redirect API traffic away from the stated official service.

Mitigation: Use the official service endpoint and avoid ZCM_BASE or login --base unless the alternate destination is fully trusted.

Risk: Bid drafting and compliance outputs can affect commercial submissions and may contain incomplete or incorrect recommendations.

Mitigation: Have qualified staff review generated bid documents, risk findings, and retained待填项 before submission.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-radar)
- [百炼标书 Service](https://biaoshu.zhiliaobiaoxun.com/)
- [API Contract Reference](artifact/references/api.md)
- [Usage Runbook](artifact/references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance plus generated HTML reports, Word reports, and .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated files are written locally under biaoshu-bailian-files or a configured output path; service results may also be retained by the remote account.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
