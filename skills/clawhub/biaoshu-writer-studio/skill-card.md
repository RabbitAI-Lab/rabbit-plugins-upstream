## Description:

智能标书编制 helps users interpret tender documents, generate editable bid documents, and review bid files for compliance using the 百炼®标书 cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid teams use this skill to analyze tender requirements, draft bid documents, and check bid submissions for compliance risks. It is intended for workflows where the user explicitly provides local tender or bid files and consents to cloud processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files can contain commercial, pricing, or personal information and are uploaded to the disclosed cloud service for processing.

Mitigation: Confirm the user understands and agrees before upload, and process only files the user explicitly provides.

Risk: The App Key is an account credential and may expose account access if pasted into chat or shared through credential-bearing links.

Mitigation: Keep the App Key out of chat, store it only in the local config file as instructed, and never forward links containing App Key or bind_key parameters.

Risk: Generated bid documents and compliance findings may include incomplete fields, partial review status, or content that requires domain judgment before submission.

Mitigation: Have a qualified reviewer check generated documents, unresolved placeholders, risk findings, and partial-review status before relying on the output.

Risk: Uploaded files and generated results are retained under the App Key account on the service for a limited period.

Mitigation: Notify users about service-side retention and direct them to manage historical data through the platform when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-studio)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [Open API contract](artifact/references/api.md)
- [Operation guide](artifact/references/usage.md)
- [Knowledge base fields](artifact/references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Configuration, Guidance]

**Output Format:** [Text or Markdown responses plus generated HTML, Word, and .docx files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include interpretation summaries, compliance findings, generated bid documents, report file paths, progress notices, and account balance notices.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
