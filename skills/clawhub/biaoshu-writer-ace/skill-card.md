## Description:

链企投标文件生成 helps agents interpret tender documents, draft bid documents, and review bid files for compliance by using the 百炼标书 service with a user-provided App Key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid-writing teams use this skill to turn local tender and bid files into structured tender analysis, editable bid documents, and compliance review reports. It is intended for cases where the user has provided the relevant files and understands that processing is performed by the 百炼标书 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files may contain commercial or personal information and are uploaded to the 百炼标书 service for processing.

Mitigation: Confirm the user understands and accepts the upload before processing, and use only files the user explicitly provides.

Risk: The App Key is a full account credential and could be exposed through chat, logs, screenshots, or links carrying credential parameters.

Mitigation: Keep the App Key out of chat, store it only in the local config.json file, avoid forwarding credential-bearing links, and rotate the key if exposure is suspected.

Risk: Generated bid documents and compliance findings may be incomplete or incorrect for a specific procurement.

Mitigation: Review generated documents and findings against the original tender requirements before using them for a bid submission.

Risk: Bid generation consumes account points, and repeated submissions can create duplicate costs.

Mitigation: Check balance before generation, avoid resubmitting long-running jobs, and resume or fetch existing job results when available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-ace)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [Usage guide](references/usage.md)
- [API contract reference](references/api.md)
- [百炼标书 service](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼标书 open API base](https://biaoshu.zhiliaobiaoxun.com/api/open/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Text guidance, local HTML and Word reports, and generated .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports and bid documents are written locally; bid generation uses account points and should be reviewed before submission.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
