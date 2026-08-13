## Description:

A mainland-China bidding assistant that uses the 百炼标书 API to interpret tender documents, generate business bid documents, and review bid compliance when users provide local tender or bid files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement teams use this skill to analyze Chinese tender documents, generate editable business bid files, and produce compliance review reports for submitted bid documents. It is intended for mainland-China bidding workflows and Chinese-language procurement artifacts.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid documents can contain confidential commercial, pricing, or personal information and are uploaded to a third-party cloud API for processing.

Mitigation: Confirm user consent before upload, use only intended local files, and review the 百炼标书 data retention expectations before processing sensitive procurement materials.

Risk: The local config.json contains an App Key that controls the user's 百炼标书 account and credits.

Mitigation: Keep config.json private with local file permissions, never paste the App Key into chat, and reset the key through the provider if exposure is suspected.

Risk: Bid generation consumes account credits, while submission endpoints also require a positive balance before work can start.

Mitigation: Check account balance before starting work and make the credit impact clear before generating bid documents.

Risk: Long-running generation jobs may continue server-side even if a local tool call times out, creating a duplicate-charge risk if resubmitted.

Mitigation: Track job IDs, resume progress or result retrieval for an existing job, and use idempotency keys for network retries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-master-business)
- [百炼标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance plus generated local files such as HTML reports, Word reports, and .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are primarily Simplified Chinese and may include absolute local file paths for generated artifacts.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
