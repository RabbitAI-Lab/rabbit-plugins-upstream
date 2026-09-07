## Description:

Helps users process tender and bid documents by uploading selected files to the 百炼标书 cloud service for tender interpretation, bid document generation, compliance review, and bid similarity checking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid teams use this skill to interpret tender requirements, generate editable bid documents, review submitted bid files for compliance and similarity risks, and produce supporting report artifacts before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, or personal information and are sent to the 百炼标书 cloud service.

Mitigation: Confirm the user is allowed to upload the selected documents before processing and disclose that the named cloud service handles the files.

Risk: The skill requires an API key that grants access to the provider account.

Mitigation: Keep the API key out of chat, store it only in the local configuration file, and avoid sharing links or messages that expose credentials.

Risk: Uploaded files and generated results may remain available in the provider account history for a limited period.

Mitigation: Use the provider account to review and manage stored server-side history and avoid uploading files that the user is not authorized to process.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-review-pro)
- [API Contract Reference](artifact/references/api.md)
- [Usage Guide](artifact/references/usage.md)
- [Knowledge Fields Reference](artifact/references/knowledge-fields.md)
- [百炼标书 Service](https://biaoshu.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with generated JSON, HTML, Word, and .docx file artifacts when tasks complete]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include absolute local file paths, short-term download links for generated bid documents, and Chinese procurement labels in report artifacts.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
