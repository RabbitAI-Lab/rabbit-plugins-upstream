## Description:

链企投标文件生成 uses the 百炼 bid-writing API to help agents interpret tender documents, draft technical and commercial bid documents, generate .docx deliverables, and review bid compliance when the user provides local tender or bid files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business proposal teams use this skill to process tender documents, generate editable bid documents, and check submitted bid files for disqualification or compliance risks. It is intended for cases where the user explicitly provides local tender or bid files and understands that processing is performed by the 百炼 cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files may contain business, pricing, and personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Confirm user consent before upload and avoid using the skill for documents that are not approved for third-party cloud processing.

Risk: The App Key is a full account credential if exposed in chat, logs, or copied links.

Mitigation: Keep the App Key out of chat, store it only in the local config file, and do not share URLs or messages that contain credential parameters.

Risk: Bid generation can consume account points, and long-running generation jobs may continue after the local client stops waiting.

Mitigation: Confirm the user wants to generate the bid document before submission, check account balance, and resume existing jobs instead of resubmitting duplicate generation requests.

Risk: Generated results may remain available on the cloud service for a limited period.

Mitigation: Treat generated reports and documents as retained service data and manage or remove them through the service account when retention is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-ace)
- [百炼标书 service](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage and operation guide](references/usage.md)
- [Knowledge fields reference](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown responses with generated HTML reports and .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include absolute local file paths for generated reports or bid documents; cloud processing may also leave task results available through the service account for a limited period.]

## Skill Version(s):

1.0.14 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
